import React from "react";
import { useLocation } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { Menu, Building, ShieldCheck, UserCheck, LogOut } from "lucide-react";

export const Navbar = ({ toggleMobileSidebar }) => {
  const { user, role, logout } = useAuth();
  const location = useLocation();

  const getPageMeta = (pathname) => {
    const titleMap = {
      "/employee/dashboard": { title: "Student Dashboard", subtitle: "Overview of your academic progress & wellbeing" },
      "/employee/profile": { title: "Student Profile", subtitle: "Manage your academic details and enrollments" },
      "/employee/feedback": { title: "Wellbeing Survey", subtitle: "Share your voice to help improve your academic experience" },
      "/employee/history": { title: "Survey History", subtitle: "Track your past academic wellbeing submissions" },
      "/employee/meetings": { title: "Academic Support Sessions", subtitle: "Schedule and view one-on-one counselor sessions" },
      "/employee/resources": { title: "Academic Resources", subtitle: "Student handbook, tutoring, wellness & growth materials" },
      "/employee/support": { title: "Help & Support", subtitle: "Connect with academic counselors or campus wellness" },
      "/hr/dashboard": { title: "Counselor Analytics Dashboard", subtitle: "Real-time dropout risk metrics & student retention overview" },
      "/hr/employees": { title: "Student Directory", subtitle: "Browse, filter, and review student academic records" },
      "/hr/feedback": { title: "Survey Responses Explorer", subtitle: "Review submitted student wellbeing surveys" },
      "/hr/attrition": { title: "Dropout Analytics", subtitle: "Predictive risk analysis & retention recommendations" },
      "/hr/retention-cases": { title: "Academic Support Sessions", subtitle: "Manage high-risk dropout cases and intervention sessions" },
      "/hr/company": { title: "Institution Overview", subtitle: "Academic institution profile and campus settings" },
      "/hr/management": { title: "Counselor Management", subtitle: "Enroll new students & counselor team members" },
      "/hr/settings": { title: "Portal Settings", subtitle: "Configure system preferences & notification rules" },
      "/admin/companies": { title: "Institution Management", subtitle: "Manage registered colleges, universities & schools" },
      "/admin/users": { title: "User & Counselor Management", subtitle: "Manage platform users, counselors, and students" },
      "/admin/analytics": { title: "Platform Analytics", subtitle: "Cross-institution retention statistics & platform telemetry" },
    };

    return titleMap[pathname] || { title: "DropGuard Portal", subtitle: "Student Dropout Prediction & Academic Retention System" };
  };

  const meta = getPageMeta(location.pathname);

  return (
    <header className="sticky top-0 z-30 bg-white/80 backdrop-blur-md border-b border-slate-200/80 px-4 sm:px-8 py-3.5 transition-all">
      <div className="flex items-center justify-between gap-4">
        {/* Left Side: Mobile Menu + Page Info */}
        <div className="flex items-center gap-3.5">
          <button
            onClick={toggleMobileSidebar}
            className="p-2 rounded-xl text-slate-600 hover:bg-slate-100 lg:hidden transition-colors"
            aria-label="Open sidebar"
          >
            <Menu className="w-5 h-5" />
          </button>
          <div>
            <h1 className="text-base sm:text-lg font-bold text-slate-900 tracking-tight">
              {meta.title}
            </h1>
            <p className="text-xs text-slate-500 hidden sm:block">
              {meta.subtitle}
            </p>
          </div>
        </div>

        {/* Right Side: Institution Badge + User Profile & Logout */}
        <div className="flex items-center gap-3">
          {/* Institution Code Badge */}
          {(user?.institutionCode || user?.companyCode) && (
            <div className="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-slate-100 text-slate-700 text-xs font-semibold border border-slate-200">
              <Building className="w-3.5 h-3.5 text-indigo-600" />
              <span>Institution: <strong className="text-indigo-700 uppercase">{user.institutionCode || user.companyCode}</strong></span>
            </div>
          )}

          {/* User Details */}
          <div className="flex items-center gap-3 pl-3 border-l border-slate-200">
            <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-indigo-600 to-purple-600 text-white flex items-center justify-center font-bold text-sm shadow-sm">
              {user?.fullName?.charAt(0) || "U"}
            </div>
            <div className="hidden sm:block text-left">
              <p className="text-xs font-bold text-slate-800 leading-tight">
                {user?.fullName || "User"}
              </p>
              <div className="flex items-center gap-1 mt-0.5">
                {role === "hr" || role === "counselor" ? (
                  <span className="inline-flex items-center gap-1 text-[10px] font-bold text-indigo-600 bg-indigo-50 px-1.5 py-0.5 rounded border border-indigo-100">
                    <ShieldCheck className="w-2.5 h-2.5" /> Counselor
                  </span>
                ) : role === "platformAdmin" ? (
                  <span className="inline-flex items-center gap-1 text-[10px] font-bold text-amber-600 bg-amber-50 px-1.5 py-0.5 rounded border border-amber-100">
                    <ShieldCheck className="w-2.5 h-2.5" /> Platform Admin
                  </span>
                ) : (
                  <span className="inline-flex items-center gap-1 text-[10px] font-bold text-slate-600 bg-slate-100 px-1.5 py-0.5 rounded border border-slate-200">
                    <UserCheck className="w-2.5 h-2.5" /> Student
                  </span>
                )}
              </div>
            </div>

            <button
              onClick={logout}
              className="p-2 text-slate-400 hover:text-rose-600 hover:bg-rose-50 rounded-xl transition-colors ml-1"
              title="Logout"
            >
              <LogOut className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};
