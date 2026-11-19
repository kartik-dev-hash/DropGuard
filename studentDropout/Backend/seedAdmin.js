import mongoose from "mongoose";
import bcrypt from "bcryptjs";
import dotenv from "dotenv";
import User from "./models/User.js";
import company from "./models/company.js";

dotenv.config();

const MONGO_URI =
  process.env.MONGO_URI || "mongodb://127.0.0.1:27017/studentDropout";

async function seedDatabase() {
  try {
    await mongoose.connect(MONGO_URI);
    console.log("✅ MongoDB Connected for seeding:", MONGO_URI);

    // Common password for all accounts as requested: 1234
    const DEFAULT_PASSWORD = "1234";
    const hashedPassword = await bcrypt.hash(DEFAULT_PASSWORD, 10);

    // 1. Seed or Update Platform Admin
    const adminEmail = "admin@platform.com";
    let admin = await User.findOne({ email: adminEmail });

    if (admin) {
      admin.password = hashedPassword;
      await admin.save();
      console.log(`ℹ️ Platform Admin updated with password '${DEFAULT_PASSWORD}':`, adminEmail);
    } else {
      admin = await User.create({
        email: adminEmail,
        password: hashedPassword,
        fullName: "System Platform Admin",
        role: "platformAdmin",
      });
      console.log(`🚀 Platform Admin created with password '${DEFAULT_PASSWORD}':`, admin.email);
    }

    // 2. Find or Create Institution: "Ram meghe"
    let ramMegheComp = await company.findOne({
      $or: [
        { companyName: /ram meghe/i },
        { institutionName: /ram meghe/i },
        { companyCode: "QSDPT5" },
      ],
    });

    const instCode = ramMegheComp ? ramMegheComp.companyCode : "QSDPT5";

    // 3. Seed / Update Academic Counselors under "Ram meghe"
    const counselors = [
      {
        email: "raghuwanshikartik881@gmail.com",
        fullName: "Kartik Raghuwanshi (Counselor)",
      },
      {
        email: "kartikraghuwanshi774@gmail.com",
        fullName: "Kartik N. Raghuwanshi (Advisor)",
      },
      {
        email: "counselor@demo.com",
        fullName: "Dr. Kalyani Deshmukh",
      },
    ];

    let primaryHRId = null;

    for (const c of counselors) {
      let counselor = await User.findOne({ email: c.email });
      if (counselor) {
        counselor.password = hashedPassword;
        counselor.role = "hr";
        counselor.companyCode = instCode;
        counselor.institutionCode = instCode;
        counselor.fullName = c.fullName;
        await counselor.save();
        console.log(`✅ Counselor updated with password '${DEFAULT_PASSWORD}': ${c.email}`);
      } else {
        counselor = await User.create({
          email: c.email,
          password: hashedPassword,
          fullName: c.fullName,
          role: "hr",
          companyCode: instCode,
          institutionCode: instCode,
        });
        console.log(`🚀 Counselor created with password '${DEFAULT_PASSWORD}': ${c.email}`);
      }
      if (!primaryHRId) primaryHRId = counselor._id;
    }

    // Ensure "Ram meghe" institution exists and is approved
    if (!ramMegheComp) {
      ramMegheComp = await company.create({
        companyName: "Ram meghe",
        institutionName: "Prof. Ram Meghe Institute of Technology & Research",
        industry: "Engineering & Technology",
        companyCode: instCode,
        institutionCode: instCode,
        status: "approved",
        primaryHR: primaryHRId,
        primaryCounselor: primaryHRId,
      });
      console.log(`🚀 Created Institution Workspace: 'Ram meghe' (Code: ${instCode})`);
    } else {
      ramMegheComp.status = "approved";
      ramMegheComp.primaryHR = primaryHRId;
      await ramMegheComp.save();
      console.log(`ℹ️ Verified Institution: ${ramMegheComp.companyName} (Code: ${ramMegheComp.companyCode})`);
    }

    // 4. Seed Students under "Ram meghe" with password: 1234
    const studentsToSeed = [
      {
        email: "raghuwanshikartik521@gmail.com",
        fullName: "Kartik Raghuwanshi",
        course: "B.Tech Computer Science & Engineering",
        yearOfStudy: "3rd Year",
        department: "Computer Science",
        studentCode: "STU-RM521",
        assignedCounselor: "Dr. Kalyani Deshmukh",
      },
      {
        email: "student1@rammeghe.edu",
        fullName: "Aarav Deshmukh",
        course: "B.Tech Information Technology",
        yearOfStudy: "2nd Year",
        department: "Information Technology",
        studentCode: "STU-RM001",
        assignedCounselor: "Dr. Kalyani Deshmukh",
      },
      {
        email: "student2@rammeghe.edu",
        fullName: "Pooja Sharma",
        course: "B.Tech Artificial Intelligence & Data Science",
        yearOfStudy: "1st Year",
        department: "Data Science",
        studentCode: "STU-RM002",
        assignedCounselor: "Kartik Raghuwanshi (Counselor)",
      },
      {
        email: "student3@rammeghe.edu",
        fullName: "Rohan Patel",
        course: "B.Tech Mechanical Engineering",
        yearOfStudy: "4th Year",
        department: "Mechanical Engineering",
        studentCode: "STU-RM003",
        assignedCounselor: "Dr. Kalyani Deshmukh",
      },
      {
        email: "student@demo.com",
        fullName: "Demo Student",
        course: "B.Tech Computer Science & Engineering",
        yearOfStudy: "2nd Year",
        department: "Computer Science",
        studentCode: "STU-RM004",
        assignedCounselor: "Dr. Kalyani Deshmukh",
      },
    ];

    for (const s of studentsToSeed) {
      let student = await User.findOne({ email: s.email });
      if (student) {
        student.password = hashedPassword;
        student.role = "student";
        student.companyCode = ramMegheComp.companyCode;
        student.institutionCode = ramMegheComp.companyCode;
        student.course = s.course;
        student.yearOfStudy = s.yearOfStudy;
        student.department = s.department;
        student.studentCode = s.studentCode;
        student.employeeCode = s.studentCode;
        student.assignedCounselor = s.assignedCounselor;
        await student.save();
        console.log(`✅ Student updated in '${ramMegheComp.companyName}' with password '${DEFAULT_PASSWORD}': ${s.email}`);
      } else {
        await User.create({
          email: s.email,
          password: hashedPassword,
          fullName: s.fullName,
          role: "student",
          companyCode: ramMegheComp.companyCode,
          institutionCode: ramMegheComp.companyCode,
          employeeCode: s.studentCode,
          studentCode: s.studentCode,
          course: s.course,
          yearOfStudy: s.yearOfStudy,
          department: s.department,
          assignedCounselor: s.assignedCounselor,
        });
        console.log(`🚀 Student created in '${ramMegheComp.companyName}' with password '${DEFAULT_PASSWORD}': ${s.email}`);
      }
    }

    // 5. Update any remaining users to have password 1234
    const remainingUsers = await User.find({ password: { $ne: hashedPassword } });
    for (const u of remainingUsers) {
      u.password = hashedPassword;
      await u.save();
      console.log(`🔑 Reset password to '${DEFAULT_PASSWORD}' for: ${u.email}`);
    }

    console.log("\n=======================================================");
    console.log("🎉 ALL ACCOUNTS SEEDED WITH PASSWORD: '1234' 🎉");
    console.log("Institution: Ram meghe (Code: " + ramMegheComp.companyCode + ")");
    console.log("=======================================================");
  } catch (error) {
    console.error("❌ Seeding Error:", error);
  } finally {
    await mongoose.disconnect();
    console.log("✅ Database Connection Closed");
  }
}

seedDatabase();
