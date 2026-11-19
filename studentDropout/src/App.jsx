import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider, useAuth } from "./context/AuthContext";
import { AppLayout } from "./components/layout/AppLayout";
import { CompanyManagement } from "./pages/admin/CompanyManagement";
import { UserAdminManagement } from "./pages/admin/UserAdminManagement";
import { PlatformAnalytics } from "./pages/admin/PlatformAnalytics";

// Auth Pages
import { Login } from "./pages/auth/Login";
import { RegisterCompany } from "./pages/auth/RegisterCompany";

// Student / Employee Pages
import { EmployeeDashboard } from "./pages/employee/EmployeeDashboard";
import { EmployeeProfile } from "./pages/employee/EmployeeProfile";
import { GiveFeedback } from "./pages/employee/GiveFeedback";
import { FeedbackHistory } from "./pages/employee/FeedbackHistory";
import { Resources } from "./pages/employee/Resources";
import { HelpSupport } from "./pages/employee/HelpSupport";
import { MeetingInvitations } from "./pages/employee/MeetingInvitations";

// Counselor / HR Pages
import { HRDashboard } from "./pages/hr/HRDashboard";
import { EmployeeDirectory } from "./pages/hr/EmployeeDirectory";
import { FeedbackExplorer } from "./pages/hr/FeedbackExplorer";
import { AttritionInsights } from "./pages/hr/AttritionInsights";
import { HRManagement } from "./pages/hr/HRManagement";
import { CompanyOverview } from "./pages/hr/CompanyOverview";
import { Settings } from "./pages/hr/Settings";
import { RetentionCases } from "./pages/hr/RetentionCases";

// Role-based route guard supporting both legacy (hr/employee) and academic (counselor/student) role names
const ProtectedRoute = ({ allowedRole, children }) => {
  const { isLoggedIn, role } = useAuth();

  if (!isLoggedIn) {
    return <Navigate to="/login" replace />;
  }

  const matchesRole = () => {
    if (!allowedRole) return true;
    if (allowedRole === "hr" || allowedRole === "counselor") {
      return role === "hr" || role === "counselor";
    }
    if (allowedRole === "employee" || allowedRole === "student") {
      return role === "employee" || role === "student";
    }
    return role === allowedRole;
  };

  if (!matchesRole()) {
    const isCounselor = role === "counselor" || role === "hr";
    const dest = role === "platformAdmin" ? "/admin/companies" : isCounselor ? "/hr/dashboard" : "/employee/dashboard";
    return <Navigate to={dest} replace />;
  }

  return children;
};

// Root index redirect based on role
const RootRedirect = () => {
  const { isLoggedIn, role } = useAuth();
  if (!isLoggedIn) {
    return <Navigate to="/login" replace />;
  }
  const isCounselor = role === "counselor" || role === "hr";
  return <Navigate to={role === "platformAdmin" ? "/admin/companies" : isCounselor ? "/hr/dashboard" : "/employee/dashboard"} replace />;
};

function AppRoutes() {
  return (
    <Routes>
      {/* Root Redirect */}
      <Route path="/" element={<RootRedirect />} />

      {/* Public Auth Routes */}
      <Route path="/login" element={<Login />} />
      <Route path="/register-company" element={<RegisterCompany />} />
      <Route path="/register-institution" element={<RegisterCompany />} />

      {/* Legacy Route Aliases for backward compatibility */}
      <Route path="/signIn" element={<Navigate to="/login" replace />} />
      <Route path="/signUp" element={<Navigate to="/login" replace />} />
      <Route path="/form" element={<Navigate to="/register-company" replace />} />
      <Route path="/HRHome" element={<Navigate to="/hr/dashboard" replace />} />
      <Route path="/feedback" element={<Navigate to="/employee/feedback" replace />} />
      <Route path="/HrPage" element={<Navigate to="/hr/dashboard" replace />} />
      <Route path="/empFeedback" element={<Navigate to="/hr/feedback" replace />} />

      {/* Protected Student / Employee Portal Routes */}
      <Route
        path="/employee"
        element={
          <ProtectedRoute allowedRole="student">
            <AppLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Navigate to="/employee/dashboard" replace />} />
        <Route path="dashboard" element={<EmployeeDashboard />} />
        <Route path="profile" element={<EmployeeProfile />} />
        <Route path="feedback" element={<GiveFeedback />} />
        <Route path="history" element={<FeedbackHistory />} />
        <Route path="resources" element={<Resources />} />
        <Route path="support" element={<HelpSupport />} />
        <Route path="meetings" element={<MeetingInvitations />} />
      </Route>

      {/* Student Route Alias */}
      <Route
        path="/student"
        element={
          <ProtectedRoute allowedRole="student">
            <AppLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Navigate to="/employee/dashboard" replace />} />
        <Route path="dashboard" element={<EmployeeDashboard />} />
        <Route path="profile" element={<EmployeeProfile />} />
        <Route path="survey" element={<GiveFeedback />} />
        <Route path="history" element={<FeedbackHistory />} />
        <Route path="resources" element={<Resources />} />
        <Route path="support" element={<HelpSupport />} />
        <Route path="sessions" element={<MeetingInvitations />} />
      </Route>

      {/* Protected Counselor / HR Portal Routes */}
      <Route
        path="/hr"
        element={
          <ProtectedRoute allowedRole="counselor">
            <AppLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Navigate to="/hr/dashboard" replace />} />
        <Route path="dashboard" element={<HRDashboard />} />
        <Route path="employees" element={<EmployeeDirectory />} />
        <Route path="feedback" element={<FeedbackExplorer />} />
        <Route path="attrition" element={<AttritionInsights />} />
        <Route path="management" element={<HRManagement />} />
        <Route path="company" element={<CompanyOverview />} />
        <Route path="settings" element={<Settings />} />
        <Route path="retention-cases" element={<RetentionCases />} />
      </Route>

      {/* Counselor Route Alias */}
      <Route
        path="/counselor"
        element={
          <ProtectedRoute allowedRole="counselor">
            <AppLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Navigate to="/hr/dashboard" replace />} />
        <Route path="dashboard" element={<HRDashboard />} />
        <Route path="students" element={<EmployeeDirectory />} />
        <Route path="surveys" element={<FeedbackExplorer />} />
        <Route path="dropout-insights" element={<AttritionInsights />} />
        <Route path="enrollment" element={<HRManagement />} />
        <Route path="institution" element={<CompanyOverview />} />
        <Route path="settings" element={<Settings />} />
        <Route path="support-sessions" element={<RetentionCases />} />
      </Route>

      {/* Platform Admin Routes */}
      <Route
        path="/admin"
        element={
          <ProtectedRoute allowedRole="platformAdmin">
            <AppLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Navigate to="/admin/companies" replace />} />
        <Route path="dashboard" element={<Navigate to="/admin/companies" replace />} />
        <Route path="companies" element={<CompanyManagement />} />
        <Route path="institutions" element={<CompanyManagement />} />
        <Route path="users" element={<UserAdminManagement />} />
        <Route path="analytics" element={<PlatformAnalytics />} />
      </Route>

      {/* Catch-all Fallback */}
      <Route path="*" element={<RootRedirect />} />
    </Routes>
  );
}

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <AppRoutes />
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
