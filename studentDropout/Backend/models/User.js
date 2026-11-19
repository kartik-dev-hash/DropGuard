import mongoose from "mongoose";

const userSchema = new mongoose.Schema(
  {
    email: {
      type: String,
      required: true,
      unique: true,
      lowercase: true,
      trim: true,
    },

    password: {
      type: String,
      required: true,
    },

    fullName: {
      type: String,
      required: true,
      trim: true,
    },

    role: {
      type: String,
      enum: ["platformAdmin", "counselor", "student", "hr", "employee"],
      required: true,
    },

    studentCode: {
      type: String,
      unique: true,
      sparse: true,
      uppercase: true,
    },

    employeeCode: {
      type: String,
      unique: true,
      sparse: true,
      uppercase: true,
    },

    institutionCode: {
      type: String,
      uppercase: true,
      trim: true,
    },

    companyCode: {
      type: String,
      uppercase: true,
      trim: true,
    },

    phoneNumber: {
      type: String,
      default: "",
      trim: true,
    },

    // Academic enhancement fields for students
    course: {
      type: String,
      default: "",
      trim: true,
    },

    yearOfStudy: {
      type: String,
      enum: ["", "1st", "2nd", "3rd", "4th", "1st Year", "2nd Year", "3rd Year", "4th Year"],
      default: "",
    },

    department: {
      type: String,
      default: "",
      trim: true,
    },

    assignedCounselor: {
      type: String,
      default: "Academic Counselor",
      trim: true,
    },

    assignedCounselorId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
    },

    assignedHR: {
      type: String,
      default: "Academic Counselor",
      trim: true,
    },
  },
  {
    timestamps: true,
  },
);

// Synchronize academic fields and aliases before validation
userSchema.pre("validate", function () {
  // Sync institutionCode <-> companyCode
  if (this.institutionCode && !this.companyCode) {
    this.companyCode = this.institutionCode;
  } else if (this.companyCode && !this.institutionCode) {
    this.institutionCode = this.companyCode;
  }

  // Sync studentCode <-> employeeCode
  if (this.studentCode && !this.employeeCode) {
    this.employeeCode = this.studentCode;
  } else if (this.employeeCode && !this.studentCode) {
    this.studentCode = this.employeeCode;
  }

  // Normalize roles: counselor <-> hr, student <-> employee
  if (this.role === "counselor" && !this.role) {
    this.role = "counselor";
  }

  // Sync assignedCounselor <-> assignedHR
  if (this.assignedCounselor && !this.assignedHR) {
    this.assignedHR = this.assignedCounselor;
  } else if (this.assignedHR && !this.assignedCounselor) {
    this.assignedCounselor = this.assignedHR;
  }
});

export default mongoose.model("User", userSchema);
