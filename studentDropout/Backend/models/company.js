import mongoose from "mongoose";

const companySchema = new mongoose.Schema(
  {
    institutionName: {
      type: String,
      trim: true,
    },

    companyName: {
      type: String,
      required: true,
      trim: true,
    },

    industry: {
      type: String,
      required: true,
      trim: true,
    },

    institutionCode: {
      type: String,
      uppercase: true,
      trim: true,
    },

    companyCode: {
      type: String,
      required: true,
      unique: true,
      uppercase: true,
    },

    primaryCounselor: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
    },

    primaryHR: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    status: {
      type: String,
      enum: ["pending", "approved", "rejected"],
      default: "pending",
    },
  },
  {
    timestamps: true,
  },
);

companySchema.pre("validate", function () {
  if (this.institutionName && !this.companyName) {
    this.companyName = this.institutionName;
  } else if (this.companyName && !this.institutionName) {
    this.institutionName = this.companyName;
  }

  if (this.institutionCode && !this.companyCode) {
    this.companyCode = this.institutionCode;
  } else if (this.companyCode && !this.institutionCode) {
    this.institutionCode = this.companyCode;
  }

  if (this.primaryCounselor && !this.primaryHR) {
    this.primaryHR = this.primaryCounselor;
  } else if (this.primaryHR && !this.primaryCounselor) {
    this.primaryCounselor = this.primaryHR;
  }
});

export default mongoose.model("company", companySchema);
