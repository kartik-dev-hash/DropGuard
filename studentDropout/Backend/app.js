import express from "express";
import User from "./models/User.js";
import mongoose from "mongoose";
import cors from "cors";
import cookieParser from "cookie-parser";
import jwt from "jsonwebtoken";
import bcrypt from "bcryptjs";
import EmployeeFeedback from "./models/feedback.js";
import EmployeeAnalytics from "./models/EmployeeAnalytics.js";
import company from "./models/company.js";
import dotenv from "dotenv";
import path from "path";
import { fileURLToPath } from "url";
import analyticsRoutes from "./routes/analyticsRoutes.js";
import { initializeFeedbackScheduler } from "./services/reminderScheduler.js";
import { refreshCompanyAnalytics } from "./services/analyticsService.js";
import { trainModel, getModelStatus } from "./services/mlService.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.join(__dirname, ".env") });
dotenv.config();

const JWT_SECRET = process.env.JWT_SECRET || "8fK29xPq7Lm4Vn8Rs2Yw6Za1Tc5Hd9Ju3Xe7Bg4Nk1";

mongoose
  .connect(process.env.MONGO_URI || "mongodb://127.0.0.1:27017/studentDropout")
  .then(async () => {
    console.log("✅ MongoDB Connected");
    // Auto-refresh analytics on startup so ML predictions are populated
    try {
      const { refreshCompanyAnalytics } = await import("./services/analyticsService.js");
      const { getModelStatus, trainModel } = await import("./services/mlService.js");
      const mlStatus = await getModelStatus();
      // If model not trained yet, auto-train from CSV
      if (!mlStatus.isReadyForInference) {
        const csvPath = path.join(__dirname, "ml", "data", "WA_Fn-UseC_-HR-Employee-Attrition.csv");
        console.log("🤖 Auto-training ML model from dataset...");
        await trainModel(csvPath, "1.0.0", true);
        console.log("✅ ML model auto-trained successfully.");
      }
      // Refresh analytics for all companies that have feedback
      const companies = await company.find({ status: "approved" }).lean();
      for (const comp of companies) {
        await refreshCompanyAnalytics(comp.companyCode).catch(() => {});
      }
      console.log("✅ Analytics auto-refreshed with ML predictions on startup.");
    } catch (e) {
      console.log("⚠️  Auto-refresh analytics failed (non-fatal):", e.message);
    }
  })
  .catch((err) => console.log("❌ MongoDB Error:", err));

const app = express();
app.use(express.json());
app.use(
  cors({
    origin: (origin, callback) => {
      // Allow requests with no origin (mobile apps, curl, Postman)
      // or from localhost / local network IPs / Vercel deployments
      const isAllowed =
        !origin ||
        /^https?:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(origin) ||
        /^https?:\/\/(10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+)(:\d+)?$/.test(origin) ||
        /\.vercel\.app$/.test(origin) ||
        /\.onrender\.com$/.test(origin) ||
        (process.env.ALLOWED_ORIGIN && origin === process.env.ALLOWED_ORIGIN);
      callback(isAllowed ? null : new Error("CORS blocked"), isAllowed);
    },
    credentials: true,
    methods: ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allowedHeaders: ["Content-Type", "Authorization"],
  }),
);
app.use("/uploads", express.static("uploads"));
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

// Server health test endpoint
app.get("/test", (req, res) => {
  res.json({
    message: "Server is running!",
    dbStatus:
      mongoose.connection.readyState === 1 ? "Connected" : "Not connected",
  });
});

// ============================================================================
// AUTHENTICATION & AUTHORIZATION MIDDLEWARE
// ============================================================================

// Simple Authentication Middleware: verifies JWT token from Authorization header
function isLogedIn(req, res, next) {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader) {
      return res.status(401).json({
        message: "Token not provided",
      });
    }

    const token = authHeader.split(" ")[1];
    const decoded = jwt.verify(token, JWT_SECRET);

    req.user = decoded; // { userId, email, role, companyCode }
    next();
  } catch (error) {
    return res.status(401).json({
      message: "Invalid or expired token",
    });
  }
}

// Simple Role Authorization Middleware: verifies user role in MongoDB
function requireRole(requiredRole) {
  return async function (req, res, next) {
    try {
      const user = await User.findById(req.user.userId);

      if (!user) {
        return res.status(401).json({
          message: "User session expired or user no longer exists. Please log in again.",
        });
      }

      const roleMatches =
        user.role === "platformAdmin" ||
        user.role === requiredRole ||
        (requiredRole === "hr" && (user.role === "counselor" || user.role === "hr")) ||
        (requiredRole === "counselor" && (user.role === "counselor" || user.role === "hr")) ||
        (requiredRole === "employee" && (user.role === "student" || user.role === "employee")) ||
        (requiredRole === "student" && (user.role === "student" || user.role === "employee"));

      if (!roleMatches) {
        return res.status(403).json({
          message: `Access denied. Requires ${requiredRole} role.`,
        });
      }

      req.currentUser = user; // Attach verified database user object
      next();
    } catch (error) {
      return res.status(500).json({
        message: error.message,
      });
    }
  };
}

// Current User Verification Endpoint
app.get("/api/auth/me", isLogedIn, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId).select("-password");
    if (!user) {
      return res.status(401).json({
        message: "User session expired or user no longer exists. Please log in again.",
      });
    }
    return res.status(200).json({
      user: {
        id: user._id,
        email: user.email,
        fullName: user.fullName,
        role: user.role,
        companyCode: user.companyCode,
        institutionCode: user.institutionCode || user.companyCode,
      },
    });
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
});
app.get("/auth/verify", isLogedIn, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId).select("-password");
    if (!user) {
      return res.status(401).json({
        message: "User session expired or user no longer exists. Please log in again.",
      });
    }
    return res.status(200).json({ valid: true, user });
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
});

// ============================================================================
// PUBLIC AUTH ROUTE
// ============================================================================

// LOGIN API (platformAdmin, counselor/hr, student/employee)
app.post("/login", async function (req, res) {
  try {
    const email = req.body.email.toLowerCase().trim();
    const user = await User.findOne({ email });

    if (!user) {
      return res.status(401).json({ message: "User session expired or user no longer exists. Please log in again." });
    }

    const isPasswordValid = await bcrypt.compare(
      req.body.password,
      user.password,
    );

    if (!isPasswordValid) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    // Verify institution approval
    if (["hr", "employee", "counselor", "student"].includes(user.role)) {
      let comp = await company.findOne({
        $or: [
          { companyCode: user.companyCode },
          { institutionCode: user.companyCode },
        ],
      });
      if (!comp) {
        // Auto-heal missing institution record if company collection was wiped
        const instCode = user.companyCode || user.institutionCode || "APEX-2026";
        comp = await company.create({
          companyName: "Apex Institute of Technology",
          institutionName: "Apex Institute of Technology",
          industry: "Higher Education",
          companyCode: instCode,
          institutionCode: instCode,
          status: "approved",
          primaryHR: user._id,
        });
        if (!user.companyCode) {
          user.companyCode = instCode;
          user.institutionCode = instCode;
          await user.save();
        }
      }
      if (comp.status === "pending") {
        return res.status(403).json({
          message:
            "Your institution registration is pending Platform Admin approval.",
        });
      }
      if (comp.status === "rejected") {
        return res.status(403).json({
          message:
            "Your institution registration has been rejected by the Platform Admin.",
        });
      }
    }

    // Sign JWT using JWT_SECRET from environment
    const token = jwt.sign(
      {
        userId: user._id,
        email: user.email,
        role: user.role,
        companyCode: user.companyCode,
        institutionCode: user.institutionCode || user.companyCode,
      },
      JWT_SECRET,
    );

    return res.status(200).json({
      message: "Login successful",
      token,
      user: {
        id: user._id,
        email: user.email,
        fullName: user.fullName,
        role: user.role,
        companyCode: user.companyCode,
        institutionCode: user.institutionCode || user.companyCode,
        employeeCode: user.employeeCode,
        studentCode: user.studentCode || user.employeeCode,
        course: user.course || "",
        yearOfStudy: user.yearOfStudy || "",
        department: user.department || "",
        assignedCounselor: user.assignedCounselor || user.assignedHR || "",
        phoneNumber: user.phoneNumber || "",
      },
    });
  } catch (error) {
    console.error("Login error:", error);
    res.status(500).json({ message: error.message });
  }
});

// ============================================================================
// PLATFORM ADMIN ROUTES
// ============================================================================

// Create & Approve Company + Primary HR (Platform Admin only)
app.post(
  "/admin/companies",
  isLogedIn,
  requireRole("platformAdmin"),
  async function (req, res) {
    const { companyName, industry, adminName, adminEmail, password } = req.body;

    try {
      const existingComp = await company.findOne({
        companyName: companyName.trim(),
      });
      if (existingComp) {
        return res
          .status(400)
          .json({ message: "Company is already registered" });
      }

      const existingUser = await User.findOne({
        email: adminEmail.toLowerCase().trim(),
      });
      if (existingUser) {
        return res
          .status(400)
          .json({ message: "HR Admin email already exists" });
      }

      const hashedPassword = await bcrypt.hash(password, 10);
      const finalCompanyCode = Math.random()
        .toString(36)
        .substring(2, 8)
        .toUpperCase();

      // 1. Create Primary HR user
      const hrUser = await User.create({
        email: adminEmail.toLowerCase().trim(),
        password: hashedPassword,
        fullName: adminName.trim(),
        role: "hr",
        companyCode: finalCompanyCode,
      });

      // 2. Create Company
      const companyInfo = await company.create({
        companyName: companyName.trim(),
        industry: industry.trim(),
        primaryHR: hrUser._id,
        companyCode: finalCompanyCode,
      });

      res.status(201).json({
        message: "Company and Primary HR registered successfully",
        companyInfo,
        hr: {
          id: hrUser._id,
          fullName: hrUser.fullName,
          email: hrUser.email,
          role: hrUser.role,
          companyCode: hrUser.companyCode,
        },
      });
    } catch (error) {
      console.error("Admin company creation error:", error);
      res.status(500).json({ message: error.message });
    }
  },
);

// List Pending Companies (Platform Admin only)
app.get(
  "/admin/pending-companies",
  isLogedIn,
  requireRole("platformAdmin"),
  async function (req, res) {
    try {
      const pending = await company
        .find({ status: "pending" })
        .populate("primaryHR", "-password")
        .lean();
      res.status(200).json({ companies: pending });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },
);

// List ALL Companies with any status (Platform Admin only)
app.get(
  "/admin/all-companies",
  isLogedIn,
  requireRole("platformAdmin"),
  async function (req, res) {
    try {
      const all = await company
        .find({})
        .populate("primaryHR", "-password")
        .sort({ createdAt: -1 })
        .lean();

      // Aggregate user counts per company
      const userCounts = await User.aggregate([
        {
          $group: {
            _id: "$companyCode",
            totalEmployees: {
              $sum: { $cond: [{ $eq: ["$role", "employee"] }, 1, 0] },
            },
            totalHRs: {
              $sum: { $cond: [{ $eq: ["$role", "hr"] }, 1, 0] },
            },
          },
        },
      ]);

      const countMap = {};
      userCounts.forEach((c) => {
        if (c._id) {
          countMap[c._id.toUpperCase()] = c;
        }
      });

      const companiesWithCounts = all.map((c) => {
        const stats = c.companyCode
          ? countMap[c.companyCode.toUpperCase()]
          : null;
        return {
          ...c,
          employeeCount: stats ? stats.totalEmployees : 0,
          hrCount: stats ? stats.totalHRs : 0,
        };
      });

      res.status(200).json({ companies: companiesWithCounts });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },
);

// Approve a pending company (Platform Admin only)
app.put(
  "/admin/approve-company/:id",
  isLogedIn,
  requireRole("platformAdmin"),
  async function (req, res) {
    try {
      const comp = await company.findById(req.params.id);
      if (!comp) return res.status(404).json({ message: "Company not found" });
      if (comp.status === "approved")
        return res.status(400).json({ message: "Company already approved" });
      comp.status = "approved";
      await comp.save();
      res.status(200).json({ message: "Company approved successfully" });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },
);

// Reject a pending company (Platform Admin only)
app.put(
  "/admin/reject-company/:id",
  isLogedIn,
  requireRole("platformAdmin"),
  async function (req, res) {
    try {
      const comp = await company.findById(req.params.id);
      if (!comp) return res.status(404).json({ message: "Company not found" });
      if (comp.status === "rejected")
        return res.status(400).json({ message: "Company already rejected" });
      comp.status = "rejected";
      await comp.save();
      res.status(200).json({ message: "Company rejected successfully" });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },
);

// Legacy Company Registration Endpoint (kept for compatibility)
app.post("/form", async function (req, res) {
  const { companyName, industry, adminName, adminEmail, password } = req.body;

  try {
    const find = await company.findOne({ companyName: companyName.trim() });

    if (find) {
      return res
        .status(400)
        .json({ message: "Your Company is Already Registered" });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const finalCompanyCode = Math.random()
      .toString(36)
      .substring(2, 8)
      .toUpperCase();

    const user = await User.create({
      email: adminEmail.toLowerCase().trim(),
      password: hashedPassword,
      fullName: adminName.trim(),
      role: "hr",
      companyCode: finalCompanyCode,
    });

    const companyInfo = await company.create({
      companyName: companyName.trim(),
      industry: industry.trim(),
      primaryHR: user._id,
      companyCode: finalCompanyCode,
    });

    res.status(201).json({
      message: "Registered",
      companyInfo: companyInfo,
      hr: {
        id: user._id,
        fullName: user.fullName,
        email: user.email,
        role: user.role,
        companyCode: user.companyCode,
      },
    });
  } catch (error) {
    console.log("Registering Error:", error);
    res.status(500).json({ message: error.message });
  }
});

// ============================================================================
// HR ROUTES
// ============================================================================

// Mount HR / Counselor Analytics and Machine Learning API endpoints
app.use("/api/hr", isLogedIn, requireRole("hr"), analyticsRoutes);
app.use("/hr/analytics", isLogedIn, requireRole("hr"), analyticsRoutes);
app.use("/api/counselor", isLogedIn, requireRole("hr"), analyticsRoutes);
app.use("/counselor/analytics", isLogedIn, requireRole("hr"), analyticsRoutes);

// Get Students & Feedbacks for Logged-In Counselor's / HR's Institution Only
const getStudentsHandler = async (req, res) => {
  try {
    const hr = req.currentUser;

    // Fetch students belonging strictly to Counselor's institution/companyCode (or all if platform admin)
    const filter = { role: { $in: ["student", "employee"] } };
    if (hr.companyCode) {
      filter.companyCode = hr.companyCode;
    }

    const employees = await User.find(filter)
      .select("-password")
      .lean();

    const employeeIds = employees.map((e) => e._id);

    const now = new Date();
    const currentPeriod = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}`;
    const academicPeriod = process.env.ACADEMIC_PERIOD || "Semester 1 – 2026";

    const predictions = await EmployeeFeedback.find({
      employeeId: { $in: employeeIds },
      $or: [
        { feedbackPeriod: currentPeriod },
        { feedbackPeriod: academicPeriod },
        { feedbackPeriod: { $exists: false } },
      ],
    })
      .select("employeeId feedbackPeriod")
      .lean();

    const submittedSet = new Set(
      predictions.map((p) => p.employeeId.toString()),
    );

    // Fetch EmployeeAnalytics to get ML prediction per student
    const analyticsFilter = { employeeId: { $in: employeeIds } };
    if (hr.companyCode) {
      analyticsFilter.companyCode = hr.companyCode.toUpperCase();
    }
    const analyticsRecords = await EmployeeAnalytics.find(analyticsFilter)
      .select("employeeId mlPrediction experimentalSurveyRisk currentAverages")
      .lean();

    const analyticsMap = {};
    analyticsRecords.forEach((a) => {
      analyticsMap[a.employeeId.toString()] = {
        mlPrediction: a.mlPrediction,
        experimentalSurveyRisk: a.experimentalSurveyRisk,
        currentAverages: a.currentAverages,
      };
    });

    const employeesWithStatus = employees.map((emp) => ({
      ...emp,
      studentCode: emp.studentCode || emp.employeeCode,
      institutionCode: emp.institutionCode || emp.companyCode,
      assignedCounselor: emp.assignedCounselor || emp.assignedHR || "Academic Counselor",
      submitted: submittedSet.has(emp._id.toString()),
      mlPrediction: analyticsMap[emp._id.toString()]?.mlPrediction || {
        isAvailable: false,
      },
      experimentalSurveyRisk: analyticsMap[emp._id.toString()]
        ?.experimentalSurveyRisk || { level: "NO_FEEDBACK", label: "No Survey Submitted" },
      currentAverages: analyticsMap[emp._id.toString()]?.currentAverages,
    }));

    const submittedCount = submittedSet.size;

    const feedbacks = await EmployeeFeedback.find({
      employeeId: { $in: employeeIds },
    });

    const activeCode = hr.companyCode || (employeesWithStatus[0]?.companyCode) || "APEX-2026";

    res.status(200).json({
      companyCode: activeCode,
      institutionCode: hr.institutionCode || activeCode,
      currentPeriod,
      academicPeriod,
      employees: employeesWithStatus,
      students: employeesWithStatus,
      submittedCount,
      pendingFeedbacks: employees.length - submittedCount,
      feedbacks,
    });
  } catch (error) {
    console.log("Get students error:", error);
    res.status(500).json({ message: error.message });
  }
};

app.get("/hr/employees", isLogedIn, requireRole("hr"), getStudentsHandler);
app.get("/counselor/students", isLogedIn, requireRole("hr"), getStudentsHandler);

// Helper to resolve company code safely even after DB wipe
async function resolveCompanyCode(user, requestedCode) {
  if (requestedCode) return requestedCode.toUpperCase();
  if (user?.companyCode) return user.companyCode.toUpperCase();
  if (user?.institutionCode) return user.institutionCode.toUpperCase();

  // Find existing approved institution or create default
  let comp = await company.findOne({ status: "approved" });
  if (!comp) comp = await company.findOne({});
  if (!comp) {
    comp = await company.create({
      companyName: "Apex Institute of Technology",
      institutionName: "Apex Institute of Technology",
      industry: "Higher Education",
      companyCode: "APEX-2026",
      institutionCode: "APEX-2026",
      status: "approved",
      primaryHR: user?._id || new mongoose.Types.ObjectId(),
    });
  }
  return comp.companyCode;
}

// Create Co-HR Admin for Logged-In HR's Company Only
app.post("/hr/create", isLogedIn, requireRole("hr"), async function (req, res) {
  const { email, password, fullName, companyCode } = req.body;

  try {
    const hr = req.currentUser;

    const existingUser = await User.findOne({
      email: email.toLowerCase().trim(),
    });

    if (existingUser) {
      return res.status(400).json({ message: "User already exists with this email" });
    }

    const targetCode = await resolveCompanyCode(hr, companyCode);
    const hashedPassword = await bcrypt.hash(password, 10);

    const user = await User.create({
      email: email.toLowerCase().trim(),
      password: hashedPassword,
      fullName: fullName.trim(),
      role: "hr",
      companyCode: targetCode,
      institutionCode: targetCode,
    });

    res.status(201).json({
      message: "Academic Counselor registered successfully",
      hr: {
        id: user._id,
        fullName: user.fullName,
        email: user.email,
        role: user.role,
        companyCode: user.companyCode,
      },
      counselor: {
        id: user._id,
        fullName: user.fullName,
        email: user.email,
        role: user.role,
        companyCode: user.companyCode,
      },
    });
  } catch (error) {
    console.error("HR creation error:", error);
    res.status(500).json({ message: error.message });
  }
});

// Enroll Student / Create Employee for Logged-In Counselor's / HR's Institution
const enrollStudentHandler = async function (req, res) {
  const { email, password, fullName, course, yearOfStudy, department, assignedCounselor, companyCode } = req.body;

  try {
    const hr = req.currentUser;

    const existingUser = await User.findOne({
      email: email.toLowerCase().trim(),
    });

    if (existingUser) {
      return res.status(400).json({ message: "User already exists with this email" });
    }

    const targetCode = await resolveCompanyCode(hr, companyCode);
    const hashedPassword = await bcrypt.hash(password, 10);
    const codeSuffix = Math.random().toString(36).substring(2, 8).toUpperCase();
    const studentCode = "STU-" + codeSuffix;

    const user = await User.create({
      email: email.toLowerCase().trim(),
      password: hashedPassword,
      fullName: fullName.trim(),
      role: "student",
      companyCode: targetCode,
      institutionCode: targetCode,
      employeeCode: studentCode,
      studentCode: studentCode,
      course: course?.trim() || "",
      yearOfStudy: yearOfStudy || "1st Year",
      department: department?.trim() || "",
      assignedCounselor: assignedCounselor?.trim() || hr?.fullName || "Academic Counselor",
      assignedCounselorId: hr?._id,
      assignedHR: assignedCounselor?.trim() || hr?.fullName || "Academic Counselor",
    });

    res.status(201).json({
      message: "Student enrolled successfully",
      student: {
        id: user._id,
        fullName: user.fullName,
        email: user.email,
        role: user.role,
        companyCode: user.companyCode,
        institutionCode: user.institutionCode,
        studentCode: user.studentCode,
        employeeCode: user.employeeCode,
        course: user.course,
        yearOfStudy: user.yearOfStudy,
        department: user.department,
        assignedCounselor: user.assignedCounselor,
      },
      employee: {
        id: user._id,
        fullName: user.fullName,
        email: user.email,
        role: user.role,
        companyCode: user.companyCode,
        employeeCode: user.employeeCode,
      },
    });
  } catch (error) {
    console.error("Error creating student:", error);
    res.status(500).json({ message: error.message });
  }
};

app.post("/Save", isLogedIn, requireRole("hr"), enrollStudentHandler);
app.post("/counselor/students/save", isLogedIn, requireRole("hr"), enrollStudentHandler);

// ============================================================================
// STUDENT & EMPLOYEE ROUTES
// ============================================================================

// Check Student Feedback Status for current academic cycle
app.get("/predict/status", isLogedIn, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId);

    if (!user) {
      return res.status(401).json({ message: "User session expired or user no longer exists. Please log in again." });
    }

    const now = new Date();
    const currentPeriod = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}`;
    const academicPeriod = process.env.ACADEMIC_PERIOD || "Semester 1 – 2026";

    const existingPrediction = await EmployeeFeedback.findOne({
      $and: [
        { $or: [{ employeeId: req.user.userId }, { studentId: req.user.userId }] },
        {
          $or: [
            { feedbackPeriod: currentPeriod },
            { feedbackPeriod: academicPeriod },
          ],
        },
      ],
    });

    return res.json({
      user: {
        id: user._id,
        fullName: user.fullName,
        email: user.email,
        role: user.role,
        companyCode: user.companyCode,
        institutionCode: user.institutionCode || user.companyCode,
        employeeCode: user.employeeCode,
        studentCode: user.studentCode || user.employeeCode,
        course: user.course || "",
        yearOfStudy: user.yearOfStudy || "",
        department: user.department || "",
        assignedCounselor: user.assignedCounselor || user.assignedHR || "Academic Counselor",
        phoneNumber: user.phoneNumber || "",
      },
      currentPeriod,
      academicPeriod,
      submitted: !!existingPrediction,
      message: existingPrediction
        ? "You have already submitted your academic wellbeing survey 😇"
        : "You have not submitted the academic survey for this term yet",
    });
  } catch (error) {
    console.log("Status error:", error);
    res.status(500).json({ message: error.message });
  }
});

// Update Student Profile
app.put("/student/profile", isLogedIn, async (req, res) => {
  try {
    const { course, yearOfStudy, department, phoneNumber } = req.body;
    const user = await User.findById(req.user.userId);
    if (!user) {
      return res.status(401).json({ message: "User session expired or user no longer exists. Please log in again." });
    }

    if (course !== undefined) user.course = course;
    if (yearOfStudy !== undefined) user.yearOfStudy = yearOfStudy;
    if (department !== undefined) user.department = department;
    if (phoneNumber !== undefined) user.phoneNumber = phoneNumber;

    await user.save();

    res.json({
      message: "Student profile updated successfully",
      user: {
        id: user._id,
        fullName: user.fullName,
        email: user.email,
        role: user.role,
        companyCode: user.companyCode,
        institutionCode: user.institutionCode || user.companyCode,
        studentCode: user.studentCode || user.employeeCode,
        course: user.course,
        yearOfStudy: user.yearOfStudy,
        department: user.department,
        assignedCounselor: user.assignedCounselor || user.assignedHR || "",
        phoneNumber: user.phoneNumber,
      },
    });
  } catch (error) {
    res.status(500).json({ message: error.message });
  }
});

// Submit Academic Survey (Student/Employee role, 1 submission per cycle)
app.post(
  "/predict",
  isLogedIn,
  requireRole("employee"),
  async function (req, res) {
    try {
      const { feedbacks } = req.body;
      const user = req.currentUser;

      const now = new Date();
      const currentPeriod = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}`;
      const academicPeriod = process.env.ACADEMIC_PERIOD || currentPeriod;

      const existingPrediction = await EmployeeFeedback.findOne({
        $and: [
          { $or: [{ employeeId: user._id }, { studentId: user._id }] },
          { $or: [{ feedbackPeriod: currentPeriod }, { feedbackPeriod: academicPeriod }] },
        ],
      });

      if (existingPrediction) {
        return res.status(400).json({
          message: "You have already submitted your survey for this term",
        });
      }

      const ae = feedbacks.academicEngagement != null ? feedbacks.academicEngagement : feedbacks.jobSatisfaction;
      const ss = feedbacks.supportSatisfaction != null ? feedbacks.supportSatisfaction : feedbacks.workEnvironment;
      const sm = feedbacks.stressManagement != null ? feedbacks.stressManagement : feedbacks.workLifeBalance;
      const bl = feedbacks.belongingness != null ? feedbacks.belongingness : feedbacks.growth;
      const cf = feedbacks.counselorFeedback || feedbacks.manager || "";

      await EmployeeFeedback.create({
        studentId: user._id,
        employeeId: user._id,
        feedbackPeriod: currentPeriod,
        academicEngagement: ae,
        supportSatisfaction: ss,
        stressManagement: sm,
        belongingness: bl,
        counselorFeedback: cf,
        // Backward compatibility
        jobSatisfaction: ae,
        workEnvironment: ss,
        workLifeBalance: sm,
        growth: bl,
        manager: cf,
        likedMost: feedbacks.likedMost || "",
        improvement: feedbacks.improvement || "",
        comments: feedbacks.comments || "",
      });

      // Auto-refresh analytics so ML prediction is immediately available
      const companyCode = user.companyCode || user.institutionCode;
      if (companyCode) {
        const { refreshCompanyAnalytics } = await import("./services/analyticsService.js");
        refreshCompanyAnalytics(companyCode).catch(() => {});
      }

      res.json({
        message: "Academic Wellbeing Survey Submitted Successfully",
      });
    } catch (error) {
      console.log("Survey submission error:", error);
      res.status(500).json({ message: error.message });
    }
  },
);

// ============================================================================
// PLATFORM ADMIN — ADDITIONAL ROUTES
// ============================================================================

// List ALL Users across platform (Platform Admin only)
app.get(
  "/admin/users",
  isLogedIn,
  requireRole("platformAdmin"),
  async function (req, res) {
    try {
      const users = await User.find({})
        .select("-password")
        .sort({ createdAt: -1 })
        .lean();
      res.status(200).json({ users });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },
);

// Platform-wide aggregate statistics (Platform Admin only)
app.get(
  "/admin/platform-stats",
  isLogedIn,
  requireRole("platformAdmin"),
  async function (req, res) {
    try {
      const [
        totalCompanies,
        approvedCompanies,
        pendingCompanies,
        rejectedCompanies,
        totalUsers,
        totalHRs,
        totalEmployees,
        totalAdmins,
      ] = await Promise.all([
        company.countDocuments({}),
        company.countDocuments({ status: "approved" }),
        company.countDocuments({ status: "pending" }),
        company.countDocuments({ status: "rejected" }),
        User.countDocuments({}),
        User.countDocuments({ role: "hr" }),
        User.countDocuments({ role: "employee" }),
        User.countDocuments({ role: "platformAdmin" }),
      ]);

      // Recent 6 months company registrations for trend
      const sixMonthsAgo = new Date();
      sixMonthsAgo.setMonth(sixMonthsAgo.getMonth() - 5);
      sixMonthsAgo.setDate(1);
      sixMonthsAgo.setHours(0, 0, 0, 0);

      const monthlyCompanies = await company.aggregate([
        { $match: { createdAt: { $gte: sixMonthsAgo } } },
        {
          $group: {
            _id: {
              year: { $year: "$createdAt" },
              month: { $month: "$createdAt" },
            },
            count: { $sum: 1 },
          },
        },
        { $sort: { "_id.year": 1, "_id.month": 1 } },
      ]);

      const monthlyUsers = await User.aggregate([
        {
          $match: {
            createdAt: { $gte: sixMonthsAgo },
            role: { $ne: "platformAdmin" },
          },
        },
        {
          $group: {
            _id: {
              year: { $year: "$createdAt" },
              month: { $month: "$createdAt" },
            },
            count: { $sum: 1 },
          },
        },
        { $sort: { "_id.year": 1, "_id.month": 1 } },
      ]);

      res.status(200).json({
        companies: {
          total: totalCompanies,
          approved: approvedCompanies,
          pending: pendingCompanies,
          rejected: rejectedCompanies,
        },
        users: {
          total: totalUsers,
          hr: totalHRs,
          employee: totalEmployees,
          admin: totalAdmins,
        },
        trends: { monthlyCompanies, monthlyUsers },
      });
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  },
);

// Toggle user active/inactive status (Platform Admin only) — by setting a flag if needed
// For now: toggle companyCode blank to effectively disable or restore
// This is kept minimal per RBAC constraints — no password changes allowed

// ============================================================================
// EMPLOYEE – IN-APP MEETING INVITATION ENDPOINTS
// ============================================================================

// GET /api/employee/invitations/my
// Employee retrieves their own pending or active meeting invitation.
app.get(
  "/api/employee/invitations/my",
  isLogedIn,
  requireRole("employee"),
  async (req, res) => {
    try {
      const RetentionAction = (await import("./models/RetentionAction.js"))
        .default;

      const invitation = await RetentionAction.findOne({
        employeeId: req.currentUser._id,
        meetingDate: { $ne: "" },
      })
        .select(
          "status invitationStatus meetingDate meetingTime meetingLocation meetingLink " +
            "assignedHR notes employeeNote autoScheduled autoScheduledAt " +
            "invitationRespondedAt riskSnapshot exceptionReason inExceptionQueue",
        )
        .sort({ updatedAt: -1 })
        .lean();

      if (!invitation) {
        return res
          .status(200)
          .json({ invitation: null, message: "No meeting invitation found." });
      }

      // Strip confidential risk scores from employee view
      const safeInvitation = {
        ...invitation,
        riskSnapshot: undefined, // never expose ML scores to employees
      };

      res.status(200).json({ invitation: safeInvitation });
    } catch (error) {
      console.error("Error fetching employee invitation:", error);
      res.status(500).json({ message: error.message });
    }
  },
);

// POST & PATCH /api/employee/invitations/respond
// Employee accepts, declines, or requests rescheduling.
const handleInvitationResponse = async (req, res) => {
  try {
    const { response, note, preferredDate, preferredTime } = req.body;

    if (!["Accepted", "Declined", "RescheduleRequested"].includes(response)) {
      return res.status(400).json({
        message:
          "Invalid response. Must be 'Accepted', 'Declined', or 'RescheduleRequested'.",
      });
    }

    const RetentionAction = (await import("./models/RetentionAction.js"))
      .default;

    const invitation = await RetentionAction.findOne({
      employeeId: req.currentUser._id,
      invitationStatus: { $in: ["Pending", "RescheduleRequested"] },
    });

    if (!invitation) {
      return res
        .status(404)
        .json({ message: "No pending invitation found to respond to." });
    }

    const updateFields = {
      invitationStatus: response,
      invitationRespondedAt: new Date(),
      employeeNote: note || "",
    };

    if (response === "Accepted") {
      updateFields.status = "In Progress";
    } else if (response === "Declined") {
      updateFields.status = "Cancelled";
      updateFields.meetingDate = "";
      updateFields.meetingTime = "";
      updateFields.meetingLink = "";
    } else if (response === "RescheduleRequested") {
      // Employee preference stored; HR must confirm
      updateFields.notes = `Employee requested reschedule${preferredDate ? ` to ${preferredDate}` : ""}${preferredTime ? ` at ${preferredTime}` : ""}. Note: ${note || "none"}.`;
    }

    const historyEntry = {
      contactMethod: "Other",
      contactedAt: new Date(),
      contactedBy: req.currentUser.fullName || "Employee",
      status: response.toUpperCase(),
      note: note || `Employee responded: ${response}`,
    };

    await RetentionAction.findByIdAndUpdate(invitation._id, {
      $set: updateFields,
      $push: { contactHistory: historyEntry },
    });

    res.status(200).json({
      message: `Response recorded: ${response}`,
      invitationStatus: response,
    });
  } catch (error) {
    console.error("Error recording invitation response:", error);
    res.status(500).json({ message: error.message });
  }
};

app.patch(
  "/api/employee/invitations/respond",
  isLogedIn,
  requireRole("employee"),
  handleInvitationResponse,
);
app.post(
  "/api/employee/invitations/respond",
  isLogedIn,
  requireRole("employee"),
  handleInvitationResponse,
);

// ============================================================================
// SERVER LISTEN
// ============================================================================

const PORT = process.env.PORT || 5000;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`🚀 Server running on port ${PORT}`);
  console.log(`🔗 Test: http://localhost:${PORT}`);
  initializeFeedbackScheduler();
});
