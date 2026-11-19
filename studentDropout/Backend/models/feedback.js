import mongoose from "mongoose";

const attritionSchema = new mongoose.Schema({
  // Student reference (supports both studentId and legacy employeeId)
  studentId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
  },
  employeeId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
  },

  // Monthly feedback cycle period (e.g., "2026-10" or "Semester 1 – 2026")
  feedbackPeriod: {
    type: String,
    required: true,
    index: true,
    default: () => {
      const now = new Date();
      return `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}`;
    },
  },

  // New academic ratings (1–5 scale)
  academicEngagement: {
    type: Number,
  },
  supportSatisfaction: {
    type: Number,
  },
  stressManagement: {
    type: Number,
  },
  belongingness: {
    type: Number,
  },

  // Qualitative fields
  counselorFeedback: {
    type: String,
    default: "",
  },

  // Legacy field support for backward compatibility
  jobSatisfaction: {
    type: Number,
  },
  workEnvironment: {
    type: Number,
  },
  workLifeBalance: {
    type: Number,
  },
  growth: {
    type: Number,
  },
  manager: {
    type: String,
    default: "",
  },

  likedMost: {
    type: String,
    default: "",
  },

  improvement: {
    type: String,
    default: "",
  },

  comments: {
    type: String,
    default: "",
  },

  // ML result
  prediction: {
    type: String,
  },

  probability: {
    type: Number,
  },

  submittedAt: {
    type: Date,
    default: Date.now,
  },
});

// Synchronize new academic fields with legacy fields on save
attritionSchema.pre("validate", function () {
  // Sync studentId and employeeId
  if (this.studentId && !this.employeeId) this.employeeId = this.studentId;
  if (this.employeeId && !this.studentId) this.studentId = this.employeeId;

  // Sync academicEngagement <-> jobSatisfaction
  if (this.academicEngagement != null && this.jobSatisfaction == null) {
    this.jobSatisfaction = this.academicEngagement;
  } else if (this.jobSatisfaction != null && this.academicEngagement == null) {
    this.academicEngagement = this.jobSatisfaction;
  }

  // Sync supportSatisfaction <-> workEnvironment
  if (this.supportSatisfaction != null && this.workEnvironment == null) {
    this.workEnvironment = this.supportSatisfaction;
  } else if (this.workEnvironment != null && this.supportSatisfaction == null) {
    this.supportSatisfaction = this.workEnvironment;
  }

  // Sync stressManagement <-> workLifeBalance
  if (this.stressManagement != null && this.workLifeBalance == null) {
    this.workLifeBalance = this.stressManagement;
  } else if (this.workLifeBalance != null && this.stressManagement == null) {
    this.stressManagement = this.workLifeBalance;
  }

  // Sync belongingness <-> growth
  if (this.belongingness != null && this.growth == null) {
    this.growth = this.belongingness;
  } else if (this.growth != null && this.belongingness == null) {
    this.belongingness = this.growth;
  }

  // Sync counselorFeedback <-> manager
  if (this.counselorFeedback && !this.manager) {
    this.manager = this.counselorFeedback;
  } else if (this.manager && !this.counselorFeedback) {
    this.counselorFeedback = this.manager;
  }
});

attritionSchema.index({ employeeId: 1, feedbackPeriod: 1 }, { unique: true });
attritionSchema.index({ studentId: 1, feedbackPeriod: 1 });

export default mongoose.model("EmployeeFeedback", attritionSchema, "feedback");



