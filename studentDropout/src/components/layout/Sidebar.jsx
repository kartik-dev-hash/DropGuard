import React from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { LogoMark } from "../common/Logo";
import {
  LayoutDashboard,
  User,
  MessageSquarePlus,
  History,
  BookOpen,
  HelpCircle,
  Users,
  MessageSquareText,
  TrendingUp,
  Building2,
  Settings,
  LogOut,
  ShieldCheck,
  ChevronLeft,
  ChevronRight,
  BarChart3,
  UserCog,
  Bot,
  CalendarClock,
} from "lucide-react";

export const Sidebar = ({ isOpen, toggleSidebar, isMobileOpen, closeMobile }) => {
  const { user, role, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const studentNavItems = [
    { label: "Dashboard", path: "/employee/dashboard", icon: LayoutDashboard },
    { label: "Student Profile", path: "/employee/profile", icon: User },
    { label: "Wellbeing Survey", path: "/employee/feedback", icon: MessageSquarePlus },
    { label: "Survey History", path: "/employee/history", icon: History },
    { label: "Support Sessions", path: "/employee/meetings", icon: CalendarClock },
    { label: "Academic Resources", path: "/employee/resources", icon: BookOpen },
    { label: "Help & Support", path: "/employee/support", icon: HelpCircle },
  ];

  const counselorNavItems = [
    { label: "Dashboard", path: "/hr/dashboard", icon: LayoutDashboard },
    { label: "Students", path: "/hr/employees", icon: Users },
    { label: "Survey Responses", path: "/hr/feedback", icon: MessageSquareText },
    { label: "Dropout Analytics", path: "/hr/attrition", icon: TrendingUp },
    { label: "Academic Support", path: "/hr/retention-cases", icon: Bot },
    { label: "Institution", path: "/hr/company", icon: Building2 },
    { label: "Settings", path: "/hr/settings", icon: Settings },
  ];

  const adminNavItems = [
    { label: "Institution Management", path: "/admin/companies", icon: Building2 },
    { label: "User & Counselor Management", path: "/admin/users", icon: UserCog },
    { label: "Platform Analytics", path: "/admin/analytics", icon: BarChart3 },
  ];

  const navItems =
    role === "hr" || role === "counselor"
      ? counselorNavItems
      : role === "platformAdmin"
      ? adminNavItems
      : studentNavItems;

  return (
    <>
      {/* Mobile Backdrop Overlay */}
      {isMobileOpen && (
        <div
          className="fixed inset-0 z-40 bg-slate-900/60 backdrop-blur-xs lg:hidden"
          onClick={closeMobile}
        />
      )}

      {/* Sidebar Container */}
      <aside
        className={`fixed top-0 left-0 z-50 h-screen bg-slate-900 text-slate-300 flex flex-col transition-all duration-300 border-r border-slate-800 ${
          isOpen ? "w-64" : "w-20"
        } ${
          isMobileOpen
            ? "translate-x-0"
            : "-translate-x-full lg:translate-x-0"
        }`}
      >
        {/* Header Logo Section */}
        <div className="h-18 px-5 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-3 overflow-hidden">
            <LogoMark className="w-10 h-10 drop-shadow-md" />
            {isOpen && (
              <div className="flex flex-col overflow-hidden leading-tight">
                <span className="font-extrabold text-sm text-white tracking-tight truncate">
                  Drop<span className="text-indigo-400">Guard</span>
                </span>
                <span className="text-[10px] font-semibold text-indigo-300 uppercase tracking-wider flex items-center gap-1 truncate mt-0.5">
                  <ShieldCheck className="w-3 h-3 text-indigo-400 flex-shrink-0" />
                  {role === "platformAdmin"
                    ? "Platform Admin"
                    : role === "hr" || role === "counselor"
                    ? "Counselor Portal"
                    : "Student Portal"}
                </span>
              </div>
            )}
          </div>

          <button
            onClick={toggleSidebar}
            className="hidden lg:flex p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
            title={isOpen ? "Collapse Sidebar" : "Expand Sidebar"}
          >
            {isOpen ? <ChevronLeft className="w-5 h-5" /> : <ChevronRight className="w-5 h-5" />}
          </button>
        </div>

        {/* User Card info inside sidebar */}
        {isOpen && user && (
          <div className="mx-3 mt-4 p-3.5 bg-slate-800/60 rounded-2xl border border-slate-800 flex items-center gap-3">
            <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-500 flex items-center justify-center text-white font-bold text-xs uppercase flex-shrink-0">
              {user.fullName?.charAt(0) || "U"}
            </div>
            <div className="overflow-hidden flex-1">
              <p className="text-xs font-semibold text-white truncate">{user.fullName}</p>
              <p className="text-[11px] text-slate-400 truncate">{user.email}</p>
            </div>
          </div>
        )}

        {/* Navigation Items */}
        <nav className="flex-1 p-3 space-y-1.5 overflow-y-auto mt-2">
          {isOpen && (
            <span className="px-3 py-1 text-[10px] font-bold text-slate-500 uppercase tracking-wider block">
              Main Menu
            </span>
          )}

          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <NavLink
                key={item.path}
                to={item.path}
                onClick={closeMobile}
                className={({ isActive }) =>
                  `flex items-center gap-3.5 px-3.5 py-3 rounded-xl font-medium text-sm transition-all duration-200 ${
                    isActive
                      ? "bg-indigo-600 text-white font-semibold shadow-md shadow-indigo-900/40"
                      : "text-slate-400 hover:bg-slate-800/80 hover:text-white"
                  }`
                }
                title={!isOpen ? item.label : undefined}
              >
                <Icon className="w-5 h-5 flex-shrink-0" />
                {isOpen && <span className="truncate">{item.label}</span>}
              </NavLink>
            );
          })}
        </nav>

        {/* Logout Button */}
        <div className="p-3 border-t border-slate-800">
          <button
            onClick={handleLogout}
            className="w-full flex items-center gap-3.5 px-3.5 py-3 rounded-xl text-slate-400 hover:bg-rose-500/10 hover:text-rose-400 font-medium text-sm transition-all"
            title={!isOpen ? "Logout" : undefined}
          >
            <LogOut className="w-5 h-5 flex-shrink-0" />
            {isOpen && <span>Logout</span>}
          </button>
        </div>
      </aside>
    </>
  );
};
