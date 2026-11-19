import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import api from "../../api/client";
import { Card } from "../../components/common/Card";
import { StatusBadge } from "../../components/common/Badge";
import { LoadingSpinner } from "../../components/common/LoadingSpinner";
import {
  Sparkles,
  MessageSquarePlus,
  User,
  History,
  BookOpen,
  CheckCircle2,
  Clock,
  Building,
  ShieldCheck,
  ArrowRight,
  HeartHandshake,
} from "lucide-react";

export const EmployeeDashboard = () => {
  const { user } = useAuth();
  const [statusData, setStatusData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await api.get("/predict/status");
        setStatusData(response.data);
      } catch (err) {
        console.error("Error fetching status:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchStatus();
  }, []);

  if (loading) {
    return <LoadingSpinner label="Loading your portal dashboard..." />;
  }

  const isSubmitted = statusData?.submitted || false;
  const academicPeriod = statusData?.academicPeriod || "Semester 1 – 2026";

  return (
    <div className="space-y-6">
      {/* Hero Welcome Banner */}
      <div className="bg-gradient-to-br from-indigo-600 via-purple-600 to-slate-900 rounded-3xl p-6 sm:p-8 text-white shadow-xl shadow-indigo-900/20 relative overflow-hidden">
        <div className="absolute top-0 right-0 -mt-10 -mr-10 w-72 h-72 bg-white/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          <div className="space-y-2">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/10 backdrop-blur-md text-indigo-200 text-xs font-semibold border border-white/10">
              <Sparkles className="w-3.5 h-3.5 text-amber-300" /> Student Portal Hub
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
              Welcome back, {user?.fullName || "Student"}! 👋
            </h2>
            <p className="text-indigo-100/90 text-xs sm:text-sm max-w-xl leading-relaxed">
              Your honest feedback plays a crucial role in shaping course curriculum, advising support, and student academic success.
            </p>
          </div>

          {/* Student Badge Quick Tag */}
          <div className="bg-white/10 backdrop-blur-md p-4 rounded-2xl border border-white/20 text-xs font-medium space-y-1.5 min-w-[200px]">
            <div className="flex items-center justify-between text-indigo-200">
              <span>Student ID:</span>
              <strong className="text-white font-mono uppercase">{user?.studentCode || user?.employeeCode || "STU-N/A"}</strong>
            </div>
            <div className="flex items-center justify-between text-indigo-200">
              <span>Institution Code:</span>
              <strong className="text-white font-mono uppercase">{user?.institutionCode || user?.companyCode || "N/A"}</strong>
            </div>
            {user?.course && (
              <div className="flex items-center justify-between text-indigo-200 pt-1 border-t border-white/10">
                <span>Program:</span>
                <strong className="text-amber-300">{user.course} ({user.yearOfStudy || "1st"} Yr)</strong>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Main Grid Section */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Left Column: Survey Status Card (Spans 2 cols on desktop) */}
        <div className="md:col-span-2 space-y-6">
          <Card className="relative overflow-hidden border-indigo-100">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-xs font-bold uppercase tracking-wider text-indigo-600 block mb-1">
                  {academicPeriod} Check-in Status
                </span>
                <h3 className="text-xl font-bold text-slate-900">
                  {isSubmitted ? "Academic Survey Successfully Submitted" : "Your Wellbeing Check-in is Pending"}
                </h3>
              </div>

              {isSubmitted ? (
                <StatusBadge type="submitted" label="Completed" />
              ) : (
                <StatusBadge type="pending" label="Action Required" />
              )}
            </div>

            <p className="text-xs sm:text-sm text-slate-600 mt-3 leading-relaxed">
              {isSubmitted
                ? "Thank you for sharing your academic wellbeing experience! Your responses are securely processed to help counselors and faculty support your success."
                : "You have not submitted your academic wellbeing survey for this term yet. It takes less than 3 minutes to share your voice."}
            </p>

            <div className="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
              {isSubmitted ? (
                <div className="flex items-center gap-2 text-xs font-semibold text-emerald-600 bg-emerald-50 px-3.5 py-2 rounded-xl border border-emerald-100">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Response Logged & Confidential</span>
                </div>
              ) : (
                <Link
                  to="/employee/feedback"
                  className="inline-flex items-center gap-2 px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-md shadow-indigo-600/20 transition-all"
                >
                  <MessageSquarePlus className="w-4 h-4" />
                  <span>Submit Academic Survey</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </Link>
              )}
            </div>
          </Card>

          {/* Helpful Tips Card */}
          <Card title="Academic Success & Student Wellness" subtitle="Tips to navigate your degree and well-being">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="p-4 bg-slate-50 rounded-2xl border border-slate-100 space-y-1">
                <HeartHandshake className="w-5 h-5 text-indigo-600 mb-2" />
                <h4 className="text-xs font-bold text-slate-800">Counselor Advisory</h4>
                <p className="text-[11px] text-slate-500 leading-normal">
                  Regular check-ins with your assigned academic advisor help resolve coursework roadblocks early.
                </p>
              </div>

              <div className="p-4 bg-slate-50 rounded-2xl border border-slate-100 space-y-1">
                <BookOpen className="w-5 h-5 text-purple-600 mb-2" />
                <h4 className="text-xs font-bold text-slate-800">Learning Support</h4>
                <p className="text-[11px] text-slate-500 leading-normal">
                  Access campus tutoring, peer mentoring, and academic development workshops.
                </p>
              </div>
            </div>
          </Card>
        </div>

        {/* Right Column: Quick Navigation Shortcuts */}
        <div className="space-y-4">
          <Card title="Quick Actions">
            <div className="space-y-2.5">
              <Link
                to="/employee/feedback"
                className="flex items-center gap-3 p-3 rounded-xl bg-slate-50 hover:bg-indigo-50 border border-slate-200/80 hover:border-indigo-200 text-slate-700 hover:text-indigo-700 transition-all font-medium text-xs group"
              >
                <div className="w-8 h-8 rounded-lg bg-indigo-100 text-indigo-600 flex items-center justify-center flex-shrink-0">
                  <MessageSquarePlus className="w-4 h-4" />
                </div>
                <div className="flex-1">
                  <p className="font-semibold">Submit Academic Survey</p>
                  <p className="text-[10px] text-slate-500">Rate your academic experience</p>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-indigo-600 group-hover:translate-x-0.5 transition-all" />
              </Link>

              <Link
                to="/employee/profile"
                className="flex items-center gap-3 p-3 rounded-xl bg-slate-50 hover:bg-indigo-50 border border-slate-200/80 hover:border-indigo-200 text-slate-700 hover:text-indigo-700 transition-all font-medium text-xs group"
              >
                <div className="w-8 h-8 rounded-lg bg-purple-100 text-purple-600 flex items-center justify-center flex-shrink-0">
                  <User className="w-4 h-4" />
                </div>
                <div className="flex-1">
                  <p className="font-semibold">My Student Profile</p>
                  <p className="text-[10px] text-slate-500">Check course & counselor info</p>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-indigo-600 group-hover:translate-x-0.5 transition-all" />
              </Link>

              <Link
                to="/employee/history"
                className="flex items-center gap-3 p-3 rounded-xl bg-slate-50 hover:bg-indigo-50 border border-slate-200/80 hover:border-indigo-200 text-slate-700 hover:text-indigo-700 transition-all font-medium text-xs group"
              >
                <div className="w-8 h-8 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center flex-shrink-0">
                  <History className="w-4 h-4" />
                </div>
                <div className="flex-1">
                  <p className="font-semibold">Survey History</p>
                  <p className="text-[10px] text-slate-500">Review past term submissions</p>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-indigo-600 group-hover:translate-x-0.5 transition-all" />
              </Link>

              <Link
                to="/employee/resources"
                className="flex items-center gap-3 p-3 rounded-xl bg-slate-50 hover:bg-indigo-50 border border-slate-200/80 hover:border-indigo-200 text-slate-700 hover:text-indigo-700 transition-all font-medium text-xs group"
              >
                <div className="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-600 flex items-center justify-center flex-shrink-0">
                  <BookOpen className="w-4 h-4" />
                </div>
                <div className="flex-1">
                  <p className="font-semibold">Campus Resources</p>
                  <p className="text-[10px] text-slate-500">Guides, tutoring & wellness</p>
                </div>
                <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-indigo-600 group-hover:translate-x-0.5 transition-all" />
              </Link>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
};
