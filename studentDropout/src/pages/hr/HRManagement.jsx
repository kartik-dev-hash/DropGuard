import React, { useState } from "react";
import { Link } from "react-router-dom";
import api from "../../api/client";
import { useAuth } from "../../context/AuthContext";
import { Card } from "../../components/common/Card";
import { Toast } from "../../components/common/Toast";
import { sendWelcomeEmail } from "../../utils/emailService";
import {
  UserPlus,
  ShieldPlus,
  User,
  Mail,
  Lock,
  ArrowRight,
  GraduationCap,
  BookOpen,
  Building,
  School,
  CheckCircle2,
  Users,
  ShieldCheck,
  Sparkles,
} from "lucide-react";

export const HRManagement = () => {
  const { user } = useAuth();
  const [activeTab, setActiveTab] = useState("student"); // 'student' | 'counselor'
  const [loading, setLoading] = useState(false);
  const [toast, setToast] = useState(null);

  const [formFields, setFormFields] = useState({
    fullName: "",
    email: "",
    password: "",
    course: "",
    yearOfStudy: "1st Year",
    department: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormFields((prev) => ({ ...prev, [name]: value }));
  };

  const handleCreateStudent = async (e) => {
    e.preventDefault();
    setLoading(true);
    setToast(null);

    try {
      const response = await api.post("/Save", {
        fullName: formFields.fullName.trim(),
        email: formFields.email.trim(),
        password: formFields.password,
        course: formFields.course.trim(),
        yearOfStudy: formFields.yearOfStudy,
        department: formFields.department.trim(),
        assignedCounselor: user?.fullName || "Academic Counselor",
      });

      // Send email
      try {
        await sendWelcomeEmail({
          to_email: formFields.email.trim(),
          to_name: formFields.fullName.trim(),
          password: formFields.password,
        });
      } catch (err) {
        console.warn("Email service warning:", err);
      }

      const assignedCode =
        response.data.student?.studentCode ||
        response.data.employee?.employeeCode ||
        "STU-Generated";

      setToast({
        type: "success",
        text: `Student ${formFields.fullName} enrolled successfully with Student ID: ${assignedCode}!`,
      });

      setFormFields({
        fullName: "",
        email: "",
        password: "",
        course: "",
        yearOfStudy: "1st Year",
        department: "",
      });
    } catch (err) {
      console.error("Enroll Student error:", err);
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to enroll student.",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleCreateCounselor = async (e) => {
    e.preventDefault();
    setLoading(true);
    setToast(null);

    try {
      await api.post("/hr/create", {
        fullName: formFields.fullName.trim(),
        email: formFields.email.trim(),
        password: formFields.password,
      });

      try {
        await sendWelcomeEmail({
          to_email: formFields.email.trim(),
          to_name: formFields.fullName.trim(),
          password: formFields.password,
        });
      } catch (err) {
        console.warn("Email service warning:", err);
      }

      setToast({
        type: "success",
        text: `Academic Counselor ${formFields.fullName} registered successfully!`,
      });

      setFormFields({
        fullName: "",
        email: "",
        password: "",
        course: "",
        yearOfStudy: "1st Year",
        department: "",
      });
    } catch (err) {
      console.error("Create Counselor error:", err);
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to create counselor account.",
      });
    } finally {
      setLoading(false);
    }
  };

  const currentInstCode =
    user?.institutionCode || user?.companyCode || "APEX-2026";

  return (
    <div className="space-y-6">
      {/* Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 pb-2 border-b border-slate-200/80">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-indigo-50 text-indigo-700 border border-indigo-200/70">
              <School className="w-3.5 h-3.5 text-indigo-600" />
              Institution: {currentInstCode}
            </span>
            <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200/70">
              <Sparkles className="w-3 h-3 text-emerald-600" />
              Active System
            </span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
            Enrollment & Counselor Access
          </h1>
          <p className="text-xs sm:text-sm text-slate-500 mt-0.5">
            Register new students under academic cohorts or grant advisor workspace credentials.
          </p>
        </div>

        <Link
          to="/hr/employees"
          className="inline-flex items-center gap-2 px-4 py-2 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 font-semibold text-xs rounded-xl transition-all shadow-xs self-start sm:self-auto cursor-pointer"
        >
          <Users className="w-4 h-4 text-indigo-600" />
          <span>View Student Directory</span>
        </Link>
      </div>

      {toast && (
        <Toast
          type={toast.type}
          message={toast.text}
          onClose={() => setToast(null)}
        />
      )}

      {/* Main Dual-Panel Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* Left Column: Context, Guidelines & Institution Info (5 cols) */}
        <div className="lg:col-span-5 space-y-5">
          {/* Institution Summary Card */}
          <div className="bg-gradient-to-br from-indigo-900 via-slate-900 to-indigo-950 rounded-2xl p-6 text-white shadow-lg border border-indigo-800/40 relative overflow-hidden">
            <div className="relative z-10 space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-[11px] font-bold uppercase tracking-wider text-indigo-300">
                  Academic Scope
                </span>
                <span className="px-2 py-0.5 rounded-md bg-white/10 text-white text-[10px] font-mono font-bold">
                  {currentInstCode}
                </span>
              </div>

              <div>
                <h3 className="text-lg font-bold text-white">
                  {user?.institutionName || "Apex Institute of Technology"}
                </h3>
                <p className="text-xs text-indigo-200/80 mt-0.5">
                  Authorized counselor: <strong className="text-white">{user?.fullName || "Academic Counselor"}</strong>
                </p>
              </div>

              <div className="pt-2 border-t border-indigo-700/50 grid grid-cols-2 gap-3 text-xs">
                <div>
                  <span className="text-indigo-300/80 text-[11px] block">Security Protocol</span>
                  <span className="font-semibold text-white flex items-center gap-1 mt-0.5">
                    <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
                    Role-Based
                  </span>
                </div>
                <div>
                  <span className="text-indigo-300/80 text-[11px] block">Survey Engine</span>
                  <span className="font-semibold text-white flex items-center gap-1 mt-0.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-indigo-300" />
                    Active Term
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Quick Onboarding Protocol Card */}
          <div className="bg-white rounded-2xl p-5 border border-slate-200/80 shadow-xs space-y-3">
            <h3 className="text-xs font-bold uppercase tracking-wider text-slate-700 flex items-center gap-2">
              <GraduationCap className="w-4 h-4 text-emerald-600" />
              Enrollment Automated Workflow
            </h3>

            <div className="space-y-3 text-xs text-slate-600">
              <div className="flex items-start gap-2.5">
                <div className="w-5 h-5 rounded-full bg-emerald-100 text-emerald-800 font-bold flex items-center justify-center flex-shrink-0 text-[11px] mt-0.5">
                  1
                </div>
                <div>
                  <strong className="text-slate-800">Auto-Generated Student Code</strong>
                  <p className="text-[11px] text-slate-500">Every student is automatically assigned a unique <code className="text-emerald-700 font-mono">STU-XXXXXX</code> identifier.</p>
                </div>
              </div>

              <div className="flex items-start gap-2.5">
                <div className="w-5 h-5 rounded-full bg-indigo-100 text-indigo-800 font-bold flex items-center justify-center flex-shrink-0 text-[11px] mt-0.5">
                  2
                </div>
                <div>
                  <strong className="text-slate-800">Advisor Association</strong>
                  <p className="text-[11px] text-slate-500">Automatically linked to the active Counselor account for retention tracking & 1-on-1 session scheduling.</p>
                </div>
              </div>

              <div className="flex items-start gap-2.5">
                <div className="w-5 h-5 rounded-full bg-amber-100 text-amber-800 font-bold flex items-center justify-center flex-shrink-0 text-[11px] mt-0.5">
                  3
                </div>
                <div>
                  <strong className="text-slate-800">Survey Readiness</strong>
                  <p className="text-[11px] text-slate-500">Enrolled students become immediately eligible to complete academic wellbeing surveys.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Right Column: Enrollment Console Form (7 cols) */}
        <div className="lg:col-span-7">
          <div className="bg-white rounded-2xl border border-slate-200/80 shadow-xs overflow-hidden">
            {/* Tab Selection Header */}
            <div className="p-4 sm:p-5 border-b border-slate-100 bg-slate-50/70 flex items-center gap-2 sm:gap-3">
              <button
                type="button"
                onClick={() => {
                  setActiveTab("student");
                  setToast(null);
                }}
                className={`flex-1 flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-bold text-xs transition-all cursor-pointer ${
                  activeTab === "student"
                    ? "bg-emerald-600 text-white shadow-md shadow-emerald-600/25 ring-2 ring-emerald-600/20"
                    : "bg-white text-slate-600 border border-slate-200 hover:bg-slate-100/80"
                }`}
              >
                <GraduationCap className="w-4 h-4" />
                <span>Enroll Student</span>
              </button>

              <button
                type="button"
                onClick={() => {
                  setActiveTab("counselor");
                  setToast(null);
                }}
                className={`flex-1 flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-bold text-xs transition-all cursor-pointer ${
                  activeTab === "counselor"
                    ? "bg-indigo-600 text-white shadow-md shadow-indigo-600/25 ring-2 ring-indigo-600/20"
                    : "bg-white text-slate-600 border border-slate-200 hover:bg-slate-100/80"
                }`}
              >
                <ShieldPlus className="w-4 h-4" />
                <span>Add Counselor</span>
              </button>
            </div>

            {/* Form Body */}
            <div className="p-6 sm:p-8">
              <div className="mb-6">
                <h3 className="text-lg font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
                  {activeTab === "student" ? (
                    <>
                      <UserPlus className="w-5 h-5 text-emerald-600" />
                      Enroll New Student Account
                    </>
                  ) : (
                    <>
                      <ShieldPlus className="w-5 h-5 text-indigo-600" />
                      Register New Academic Counselor
                    </>
                  )}
                </h3>
                <p className="text-xs text-slate-500 mt-1">
                  {activeTab === "student"
                    ? "Create new student account with course enrollment and counselor tracking."
                    : "Grant administrative privileges to a team counselor or academic advisor."}
                </p>
              </div>

              <form
                onSubmit={
                  activeTab === "student"
                    ? handleCreateStudent
                    : handleCreateCounselor
                }
                className="space-y-4"
              >
                <div>
                  <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                    Full Name
                  </label>
                  <div className="relative">
                    <User className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
                    <input
                      type="text"
                      name="fullName"
                      required
                      placeholder={
                        activeTab === "student"
                          ? "e.g. Kartik Raghuwanshi"
                          : "e.g. Dr. Kalyani Deshmukh"
                      }
                      value={formFields.fullName}
                      onChange={handleChange}
                      className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 placeholder-slate-400 focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white transition-all"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                    Email Address (Login Username)
                  </label>
                  <div className="relative">
                    <Mail className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
                    <input
                      type="email"
                      name="email"
                      required
                      placeholder={
                        activeTab === "student"
                          ? "student@institution.edu"
                          : "counselor@institution.edu"
                      }
                      value={formFields.email}
                      onChange={handleChange}
                      className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 placeholder-slate-400 focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white transition-all"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                    Temporary / Initial Password
                  </label>
                  <div className="relative">
                    <Lock className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
                    <input
                      type="password"
                      name="password"
                      required
                      placeholder="••••••••"
                      value={formFields.password}
                      onChange={handleChange}
                      className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 placeholder-slate-400 focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white transition-all"
                    />
                  </div>
                </div>

                {activeTab === "student" && (
                  <>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                          Course / Program
                        </label>
                        <div className="relative">
                          <BookOpen className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
                          <input
                            type="text"
                            name="course"
                            placeholder="e.g. B.Tech Computer Engineering"
                            value={formFields.course}
                            onChange={handleChange}
                            className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 placeholder-slate-400 focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white transition-all"
                          />
                        </div>
                      </div>

                      <div>
                        <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                          Year of Study
                        </label>
                        <select
                          name="yearOfStudy"
                          value={formFields.yearOfStudy}
                          onChange={handleChange}
                          className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white transition-all"
                        >
                          <option value="1st Year">1st Year</option>
                          <option value="2nd Year">2nd Year</option>
                          <option value="3rd Year">3rd Year</option>
                          <option value="4th Year">4th Year</option>
                          <option value="Postgraduate">Postgraduate</option>
                        </select>
                      </div>
                    </div>

                    <div>
                      <label className="block text-xs font-semibold text-slate-700 mb-1.5">
                        Department / Faculty
                      </label>
                      <div className="relative">
                        <Building className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
                        <input
                          type="text"
                          name="department"
                          placeholder="e.g. Department of Computer Science & Engineering"
                          value={formFields.department}
                          onChange={handleChange}
                          className="w-full pl-10 pr-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 placeholder-slate-400 focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white transition-all"
                        />
                      </div>
                    </div>
                  </>
                )}

                <div className="pt-2">
                  <button
                    type="submit"
                    disabled={loading}
                    className={`w-full py-3 px-4 font-bold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50 text-white ${
                      activeTab === "student"
                        ? "bg-emerald-600 hover:bg-emerald-700 shadow-emerald-600/20"
                        : "bg-indigo-600 hover:bg-indigo-700 shadow-indigo-600/20"
                    }`}
                  >
                    {loading ? (
                      <span className="animate-pulse">
                        Processing Registration...
                      </span>
                    ) : (
                      <>
                        <span>
                          {activeTab === "student"
                            ? "Enroll Student Account"
                            : "Register Counselor Account"}
                        </span>
                        <ArrowRight className="w-4 h-4" />
                      </>
                    )}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export const CounselorManagement = HRManagement;
