import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../../api/client";
import { useAuth } from "../../context/AuthContext";
import { StatCard, Card } from "../../components/common/Card";
import { StatusBadge, DropoutRiskBadge } from "../../components/common/Badge";
import { LoadingSpinner } from "../../components/common/LoadingSpinner";
import { Modal } from "../../components/common/Modal";
import { Toast } from "../../components/common/Toast";
import { sendWelcomeEmail } from "../../utils/emailService";
import {
  GraduationCap,
  Users,
  CheckCircle2,
  Clock,
  AlertTriangle,
  UserPlus,
  ShieldPlus,
  ArrowRight,
  School,
  Mail,
  Lock,
  User,
  MailCheck,
  Send,
  BookOpen,
  Search,
  Sparkles,
} from "lucide-react";

export const CounselorDashboard = () => {
  const { user } = useAuth();
  const [data, setData] = useState({
    employees: [],
    students: [],
    submittedCount: 0,
    pendingFeedbacks: 0,
    feedbacks: [],
    companyCode: "",
    institutionCode: "",
    academicPeriod: "Semester 1 – 2026",
  });
  const [loading, setLoading] = useState(true);

  // Form Modals
  const [activeModal, setActiveModal] = useState(null); // 'student' | 'counselor' | null
  const [modalLoading, setModalLoading] = useState(false);
  const [toast, setToast] = useState(null);

  // Student Form State
  const [studentForm, setStudentForm] = useState({
    fullName: "",
    email: "",
    password: "",
    course: "",
    yearOfStudy: "1st",
    department: "",
    assignedCounselor: user?.fullName || "Academic Counselor",
  });

  // Counselor Form State
  const [counselorForm, setCounselorForm] = useState({
    fullName: "",
    email: "",
    password: "",
  });

  const [reminderStatus, setReminderStatus] = useState(null);
  const [triggeringReminder, setTriggeringReminder] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");

  const fetchStudentsData = async () => {
    try {
      const response = await api.get("/hr/employees");
      setData(response.data);
    } catch (err) {
      console.error("Error fetching students data:", err);
    } finally {
      setLoading(false);
    }
  };

  const fetchReminderStatus = async () => {
    try {
      const response = await api.get("/api/hr/reminders/status");
      setReminderStatus(response.data);
    } catch (err) {
      console.warn("Notice: Reminder status endpoint:", err.message);
    }
  };

  useEffect(() => {
    fetchStudentsData();
    fetchReminderStatus();
  }, []);

  const handleStudentInputChange = (e) => {
    const { name, value } = e.target;
    setStudentForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleCounselorInputChange = (e) => {
    const { name, value } = e.target;
    setCounselorForm((prev) => ({ ...prev, [name]: value }));
  };

  // Enroll Student (POST /Save)
  const handleEnrollStudent = async (e) => {
    e.preventDefault();
    setModalLoading(true);
    setToast(null);

    try {
      const response = await api.post("/Save", {
        fullName: studentForm.fullName.trim(),
        email: studentForm.email.trim(),
        password: studentForm.password,
        course: studentForm.course.trim(),
        yearOfStudy: studentForm.yearOfStudy,
        department: studentForm.department.trim(),
        assignedCounselor: studentForm.assignedCounselor.trim() || user?.fullName || "Academic Counselor",
      });

      // Send Welcome Email if email service configured
      try {
        await sendWelcomeEmail({
          to_email: studentForm.email.trim(),
          to_name: studentForm.fullName.trim(),
          password: studentForm.password,
        });
      } catch (e) {
        console.warn("Email service notice:", e);
      }

      setToast({ type: "success", text: `Student ${studentForm.fullName} enrolled successfully!` });
      setActiveModal(null);
      setStudentForm({
        fullName: "",
        email: "",
        password: "",
        course: "",
        yearOfStudy: "1st",
        department: "",
        assignedCounselor: user?.fullName || "Academic Counselor",
      });
      fetchStudentsData();
    } catch (err) {
      console.error("Enroll Student Error:", err);
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to enroll student.",
      });
    } finally {
      setModalLoading(false);
    }
  };

  // Add Counselor (POST /hr/create)
  const handleCreateCounselor = async (e) => {
    e.preventDefault();
    setModalLoading(true);
    setToast(null);

    try {
      await api.post("/hr/create", {
        fullName: counselorForm.fullName.trim(),
        email: counselorForm.email.trim(),
        password: counselorForm.password,
      });

      try {
        await sendWelcomeEmail({
          to_email: counselorForm.email.trim(),
          to_name: counselorForm.fullName.trim(),
          password: counselorForm.password,
        });
      } catch (e) {
        console.warn("Email service notice:", e);
      }

      setToast({ type: "success", text: `Counselor ${counselorForm.fullName} registered successfully!` });
      setActiveModal(null);
      setCounselorForm({ fullName: "", email: "", password: "" });
      fetchStudentsData();
    } catch (err) {
      console.error("Create Counselor Error:", err);
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to register counselor account.",
      });
    } finally {
      setModalLoading(false);
    }
  };

  const handleTriggerInvitations = async () => {
    setTriggeringReminder(true);
    try {
      const response = await api.post("/api/hr/reminders/send-invitations");
      const resData = response.data?.result;
      setToast({
        type: "success",
        text: `Invitations sent to ${resData?.sent || 0} students (${resData?.skippedAlreadySubmitted || 0} already submitted, ${resData?.skippedAlreadyNotified || 0} already notified).`,
      });
      fetchStudentsData();
      fetchReminderStatus();
    } catch (err) {
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to trigger check-in invitations.",
      });
    } finally {
      setTriggeringReminder(false);
    }
  };

  const handleTriggerReminders = async () => {
    setTriggeringReminder(true);
    try {
      const response = await api.post("/api/hr/reminders/send-reminders");
      const resData = response.data?.result;
      setToast({
        type: "success",
        text: `Reminders sent to ${resData?.sent || 0} pending students (${resData?.skippedAlreadySubmitted || 0} already submitted, ${resData?.skippedAlreadyReminded || 0} already reminded).`,
      });
      fetchStudentsData();
      fetchReminderStatus();
    } catch (err) {
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to trigger reminders.",
      });
    } finally {
      setTriggeringReminder(false);
    }
  };

  if (loading) {
    return <LoadingSpinner label="Loading Counselor Dashboard Analytics..." />;
  }

  const studentList = data.students || data.employees || [];
  const totalStudents = studentList.length;
  const submittedCount = data.submittedCount || 0;
  const pendingCount = data.pendingFeedbacks || 0;
  const completionPct = totalStudents
    ? Math.round((submittedCount / totalStudents) * 100)
    : 0;

  // Filter students by search query
  const filteredStudents = studentList.filter((stu) => {
    if (!searchQuery) return true;
    const q = searchQuery.toLowerCase().trim();
    return (
      stu.fullName?.toLowerCase().includes(q) ||
      stu.email?.toLowerCase().includes(q) ||
      (stu.studentCode || stu.employeeCode || "").toLowerCase().includes(q) ||
      stu.course?.toLowerCase().includes(q)
    );
  });

  // Calculate high risk from feedback scores
  const highRiskCount = (data.feedbacks || []).filter((f) => {
    const ae =
      typeof f.academicEngagement === "number"
        ? f.academicEngagement
        : f.jobSatisfaction;
    const ss =
      typeof f.supportSatisfaction === "number"
        ? f.supportSatisfaction
        : f.workEnvironment;
    const sm =
      typeof f.stressManagement === "number"
        ? f.stressManagement
        : f.workLifeBalance;
    const bl =
      typeof f.belongingness === "number" ? f.belongingness : f.growth;
    const scores = [ae, ss, sm, bl].filter((s) => typeof s === "number");
    const avg =
      scores.length ? scores.reduce((a, b) => a + b, 0) / scores.length : null;
    return avg !== null && avg <= 2.5;
  }).length;

  return (
    <div className="space-y-6">
      {toast && (
        <Toast
          type={toast.type}
          message={toast.text}
          onClose={() => setToast(null)}
        />
      )}

      {/* Hero Welcome Bar */}
      <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 rounded-3xl p-6 sm:p-8 text-white shadow-xl shadow-slate-900/15 relative overflow-hidden border border-slate-800">
        <div className="relative z-10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 mb-2 flex-wrap">
              <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-indigo-200 text-xs font-semibold border border-white/10">
                <School className="w-3.5 h-3.5 text-indigo-300" /> Institution:{" "}
                <strong className="uppercase text-white tracking-wider">
                  {data.institutionCode ||
                    data.companyCode ||
                    user?.companyCode ||
                    "APEX-2026"}
                </strong>
              </span>
              <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-400/20 text-amber-200 text-xs font-bold border border-amber-400/30">
                <Clock className="w-3.5 h-3.5 text-amber-300" />{" "}
                {data.academicPeriod || "Semester 1 – 2026"}
              </span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight text-white">
              Academic Retention & Wellbeing
            </h2>
            <p className="text-slate-300 text-xs sm:text-sm mt-1">
              Welcome back,{" "}
              <strong className="text-white">
                {user?.fullName || "Counselor"}
              </strong>
              . Monitor student dropout indicators, academic wellbeing & support.
            </p>
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={() => {
                setStudentForm({
                  fullName: "",
                  email: "",
                  password: "",
                  course: "",
                  yearOfStudy: "1st Year",
                  department: "",
                  assignedCounselor: user?.fullName || "Academic Counselor",
                });
                setActiveModal("student");
              }}
              className="px-4 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-xl shadow-md shadow-emerald-600/25 transition-all flex items-center gap-2 cursor-pointer"
            >
              <UserPlus className="w-4 h-4" />
              <span>Enroll Student</span>
            </button>

            <button
              onClick={() => {
                setCounselorForm({ fullName: "", email: "", password: "" });
                setActiveModal("counselor");
              }}
              className="px-4 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-md shadow-indigo-600/25 transition-all flex items-center gap-2 cursor-pointer"
            >
              <ShieldPlus className="w-4 h-4" />
              <span>Add Counselor</span>
            </button>
          </div>
        </div>
      </div>

      {/* KPI Stat Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <StatCard
          title="Total Students"
          value={totalStudents}
          icon={Users}
          color="indigo"
          subtext="Enrolled in active cohorts"
          badgeText="Active"
        />

        <StatCard
          title="Survey Submitted"
          value={submittedCount}
          icon={CheckCircle2}
          color="emerald"
          subtext="Completed wellbeing check-ins"
          badgeText={`${completionPct}% Rate`}
        />

        <StatCard
          title="Pending Surveys"
          value={pendingCount}
          icon={Clock}
          color="amber"
          subtext="Check-ins awaiting response"
        />

        <StatCard
          title="Dropout Risk"
          value={highRiskCount}
          icon={AlertTriangle}
          color="rose"
          subtext="Identified by ML & survey indicators"
          badgeText={highRiskCount > 0 ? "Requires Review" : "Stable"}
        />
      </div>

      {/* Main Two-Column Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
        {/* Left Column: Recent Students (8 cols) */}
        <div className="lg:col-span-8 space-y-6">
          <Card
            title="Recent Students"
            subtitle={`Latest enrolled students in ${data.academicPeriod || "current term"}`}
            headerAction={
              <div className="flex items-center gap-3">
                <div className="relative">
                  <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
                  <input
                    type="text"
                    placeholder="Search enrolled..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="pl-8 pr-2.5 py-1 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-hidden focus:ring-2 focus:ring-indigo-500 w-36 sm:w-48 text-slate-800"
                  />
                </div>
                <Link
                  to="/hr/employees"
                  className="text-xs font-bold text-indigo-600 hover:text-indigo-700 flex items-center gap-1"
                >
                  View All <ArrowRight className="w-3.5 h-3.5" />
                </Link>
              </div>
            }
          >
            {filteredStudents.length === 0 ? (
              <div className="py-10 text-center text-slate-400">
                <Users className="w-8 h-8 mx-auto mb-2 text-slate-300" />
                <p className="text-xs font-medium">
                  {studentList.length === 0
                    ? "No students enrolled yet. Click 'Enroll Student' to get started."
                    : "No students matching your search."}
                </p>
              </div>
            ) : (
              <div className="divide-y divide-slate-100">
                {filteredStudents.slice(0, 8).map((stu) => {
                  const ml = stu.mlPrediction;
                  const mlAvailable = ml?.isAvailable;
                  // Prefer ML prediction; fall back to survey heuristic
                  const riskLevel = mlAvailable
                    ? (ml.outcome === "Yes"
                        ? "HIGH_RISK"
                        : ml.probability >= 0.35
                        ? "NEEDS_ATTENTION"
                        : "HEALTHY")
                    : stu.experimentalSurveyRisk?.level;
                  const mlProb = mlAvailable ? ml.probability : null;

                  return (
                    <div
                      key={stu._id}
                      className="py-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 hover:bg-slate-50/60 px-2 rounded-xl transition-colors"
                    >
                      <div className="flex items-center gap-3">
                        <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-indigo-600 to-slate-800 text-white font-bold text-xs flex items-center justify-center shadow-xs flex-shrink-0">
                          {stu.fullName?.charAt(0)?.toUpperCase() || "S"}
                        </div>
                        <div>
                          <div className="flex items-center gap-2">
                            <p className="text-xs sm:text-sm font-bold text-slate-800">
                              {stu.fullName}
                            </p>
                            <span className="font-mono text-[10px] font-bold text-indigo-700 bg-indigo-50 px-1.5 py-0.5 rounded border border-indigo-200/70">
                              {stu.studentCode || stu.employeeCode}
                            </span>
                          </div>
                          <div className="flex items-center gap-2 text-[11px] text-slate-400 mt-0.5">
                            <span>{stu.email}</span>
                            {stu.course && (
                              <>
                                <span>•</span>
                                <span className="text-indigo-600 font-medium">
                                  {stu.course}
                                </span>
                              </>
                            )}
                            {stu.yearOfStudy && (
                              <>
                                <span>•</span>
                                <span className="text-slate-500 font-medium">
                                  {stu.yearOfStudy}
                                </span>
                              </>
                            )}
                          </div>
                        </div>
                      </div>

                      <div className="flex items-center gap-2.5 self-end sm:self-center">
                        <DropoutRiskBadge
                          riskLevel={riskLevel}
                          probability={mlProb}
                        />
                        {stu.submitted ? (
                          <StatusBadge type="submitted" label="Survey Done" />
                        ) : (
                          <StatusBadge type="pending" label="Pending" />
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </Card>
        </div>

        {/* Right Column: Quick Actions & Outreach (4 cols) */}
        <div className="lg:col-span-4 space-y-5">
          {/* Counselor Operations Card */}
          <Card
            title="Counselor Operations"
            subtitle="Enrollment & advisor management shortcuts"
          >
            <div className="space-y-3">
              <button
                onClick={() => {
                  setStudentForm({
                    fullName: "",
                    email: "",
                    password: "",
                    course: "",
                    yearOfStudy: "1st Year",
                    department: "",
                    assignedCounselor: user?.fullName || "Academic Counselor",
                  });
                  setActiveModal("student");
                }}
                className="w-full flex items-center gap-3.5 p-3.5 rounded-xl bg-emerald-50/80 hover:bg-emerald-100/80 border border-emerald-200 text-left transition-all cursor-pointer group"
              >
                <div className="w-10 h-10 rounded-lg bg-emerald-600 text-white flex items-center justify-center flex-shrink-0 shadow-xs">
                  <UserPlus className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-xs font-bold text-emerald-950">
                    Enroll New Student
                  </h4>
                  <p className="text-[11px] text-emerald-700 mt-0.5">
                    Assign cohort, course & credentials
                  </p>
                </div>
              </button>

              <button
                onClick={() => {
                  setCounselorForm({ fullName: "", email: "", password: "" });
                  setActiveModal("counselor");
                }}
                className="w-full flex items-center gap-3.5 p-3.5 rounded-xl bg-indigo-50/80 hover:bg-indigo-100/80 border border-indigo-200 text-left transition-all cursor-pointer group"
              >
                <div className="w-10 h-10 rounded-lg bg-indigo-600 text-white flex items-center justify-center flex-shrink-0 shadow-xs">
                  <ShieldPlus className="w-5 h-5" />
                </div>
                <div>
                  <h4 className="text-xs font-bold text-indigo-950">
                    Add Counselor / Advisor
                  </h4>
                  <p className="text-[11px] text-indigo-700 mt-0.5">
                    Grant advisory workspace credentials
                  </p>
                </div>
              </button>
            </div>
          </Card>

          {/* Academic Period Check-in Reminders Control */}
          <Card
            title={`Check-in Cycle`}
            subtitle={data.academicPeriod || "Current Academic Term"}
          >
            <div className="space-y-3.5">
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 text-xs space-y-2">
                <div className="flex items-center justify-between">
                  <span className="text-slate-500 font-medium text-[11px]">
                    Period Completion
                  </span>
                  <span className="font-extrabold text-slate-800">
                    {submittedCount} / {totalStudents} ({completionPct}%)
                  </span>
                </div>
                <div className="w-full bg-slate-200 rounded-full h-2 overflow-hidden">
                  <div
                    className="bg-emerald-500 h-2 rounded-full transition-all duration-500"
                    style={{ width: `${completionPct}%` }}
                  />
                </div>
              </div>

              <div className="grid grid-cols-2 gap-2 text-xs">
                <button
                  onClick={handleTriggerInvitations}
                  disabled={triggeringReminder}
                  className="p-2.5 bg-indigo-50 hover:bg-indigo-100 border border-indigo-200 text-indigo-700 font-bold rounded-xl transition-all flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50 text-[11px]"
                  title="Dispatch initial survey invitation to eligible students"
                >
                  <Send className="w-3.5 h-3.5 text-indigo-600" />
                  <span>Send Invites</span>
                </button>

                <button
                  onClick={handleTriggerReminders}
                  disabled={triggeringReminder}
                  className="p-2.5 bg-amber-50 hover:bg-amber-100 border border-amber-200 text-amber-800 font-bold rounded-xl transition-all flex items-center justify-center gap-1.5 cursor-pointer disabled:opacity-50 text-[11px]"
                  title="Send follow-up reminder only to students who have not submitted"
                >
                  <MailCheck className="w-3.5 h-3.5 text-amber-600" />
                  <span>Send Reminders</span>
                </button>
              </div>

              <p className="text-[10px] text-slate-400 text-center">
                Automated monthly outreach: 1st of month (invitation) & 8th (follow-up).
              </p>
            </div>
          </Card>
        </div>
      </div>

      {/* Modal: Enroll Student */}
      <Modal
        isOpen={activeModal === "student"}
        onClose={() => setActiveModal(null)}
        title="Enroll New Student"
        subtitle="Create an academic account with course and cohort details"
        icon={UserPlus}
        maxWidth="max-w-md"
      >
        <form onSubmit={handleEnrollStudent} className="space-y-3.5">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Student Full Name</label>
            <div className="relative">
              <User className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                name="fullName"
                required
                placeholder="Alex Johnson"
                value={studentForm.fullName}
                onChange={handleStudentInputChange}
                className="w-full pl-9 pr-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Student Email Address</label>
            <div className="relative">
              <Mail className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="email"
                name="email"
                required
                placeholder="student@institution.edu"
                value={studentForm.email}
                onChange={handleStudentInputChange}
                className="w-full pl-9 pr-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 focus:bg-white"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">Course / Program</label>
              <input
                type="text"
                name="course"
                placeholder="B.Tech CS, B.Sc"
                value={studentForm.course}
                onChange={handleStudentInputChange}
                className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 focus:bg-white"
              />
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">Year of Study</label>
              <select
                name="yearOfStudy"
                value={studentForm.yearOfStudy}
                onChange={handleStudentInputChange}
                className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 focus:bg-white"
              >
                <option value="1st">1st Year</option>
                <option value="2nd">2nd Year</option>
                <option value="3rd">3rd Year</option>
                <option value="4th">4th Year</option>
              </select>
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Department</label>
            <input
              type="text"
              name="department"
              placeholder="Computer Science, Business, etc."
              value={studentForm.department}
              onChange={handleStudentInputChange}
              className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 focus:bg-white"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Assigned Counselor</label>
            <input
              type="text"
              name="assignedCounselor"
              placeholder="Advisor name"
              value={studentForm.assignedCounselor}
              onChange={handleStudentInputChange}
              className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 focus:bg-white"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Temporary Password</label>
            <div className="relative">
              <Lock className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="password"
                name="password"
                required
                placeholder="••••••••"
                value={studentForm.password}
                onChange={handleStudentInputChange}
                className="w-full pl-9 pr-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-600 focus:bg-white"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={modalLoading}
            className="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50 mt-3"
          >
            {modalLoading ? "Enrolling Student..." : "Enroll Student"}
          </button>
        </form>
      </Modal>

      {/* Modal: Add Counselor */}
      <Modal
        isOpen={activeModal === "counselor"}
        onClose={() => setActiveModal(null)}
        title="Add Academic Counselor"
        subtitle="Register another counselor or academic advisor with management access"
        icon={ShieldPlus}
        maxWidth="max-w-md"
      >
        <form onSubmit={handleCreateCounselor} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Full Name</label>
            <div className="relative">
              <User className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                name="fullName"
                required
                placeholder="Dr. Eleanor Vance"
                value={counselorForm.fullName}
                onChange={handleCounselorInputChange}
                className="w-full pl-9 pr-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Email Address</label>
            <div className="relative">
              <Mail className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="email"
                name="email"
                required
                placeholder="counselor@institution.edu"
                value={counselorForm.email}
                onChange={handleCounselorInputChange}
                className="w-full pl-9 pr-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Password</label>
            <div className="relative">
              <Lock className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="password"
                name="password"
                required
                placeholder="••••••••"
                value={counselorForm.password}
                onChange={handleCounselorInputChange}
                className="w-full pl-9 pr-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={modalLoading}
            className="w-full py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-md transition-all flex items-center justify-center gap-2 cursor-pointer disabled:opacity-50 mt-2"
          >
            {modalLoading ? "Registering Counselor..." : "Register Counselor Account"}
          </button>
        </form>
      </Modal>
    </div>
  );
};
