import React, { useEffect, useState } from "react";
import api from "../../api/client";
import { useAuth } from "../../context/AuthContext";
import { Modal } from "../../components/common/Modal";
import { Toast } from "../../components/common/Toast";
import {
  UserCog,
  Search,
  Filter,
  RefreshCw,
  Users,
  ShieldCheck,
  UserCheck,
  Building2,
  Mail,
  Phone,
  Calendar,
  Eye,
  X,
  BadgeCheck,
  Shield,
  GraduationCap,
  BookOpen,
  UserPlus,
  ShieldPlus,
  Lock,
  Building,
} from "lucide-react";

const ROLE_BADGE = {
  platformAdmin: "bg-purple-50 text-purple-700 border-purple-200",
  hr: "bg-indigo-50 text-indigo-700 border-indigo-200",
  counselor: "bg-indigo-50 text-indigo-700 border-indigo-200",
  employee: "bg-emerald-50 text-emerald-700 border-emerald-200",
  student: "bg-emerald-50 text-emerald-700 border-emerald-200",
};

const ROLE_LABEL = {
  platformAdmin: "Platform Admin",
  hr: "Academic Counselor",
  counselor: "Academic Counselor",
  employee: "Student",
  student: "Student",
};

export const UserAdminManagement = () => {
  const { token, user: loggedInUser } = useAuth();
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [roleFilter, setRoleFilter] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedUser, setSelectedUser] = useState(null);

  const [activeModal, setActiveModal] = useState(null); // 'student' | 'counselor' | null
  const [modalLoading, setModalLoading] = useState(false);
  const [toast, setToast] = useState(null);

  const [studentForm, setStudentForm] = useState({
    fullName: "",
    email: "",
    password: "",
    course: "",
    yearOfStudy: "1st Year",
    department: "",
    companyCode: "APEX-2026",
  });

  const [counselorForm, setCounselorForm] = useState({
    fullName: "",
    email: "",
    password: "",
    companyCode: "APEX-2026",
  });

  const handleEnrollStudent = async (e) => {
    e.preventDefault();
    setModalLoading(true);
    setToast(null);

    try {
      const res = await api.post("/Save", {
        fullName: studentForm.fullName.trim(),
        email: studentForm.email.trim(),
        password: studentForm.password,
        course: studentForm.course.trim(),
        yearOfStudy: studentForm.yearOfStudy,
        department: studentForm.department.trim(),
        companyCode: studentForm.companyCode.trim(),
      });

      const assignedCode =
        res.data.student?.studentCode || res.data.employee?.employeeCode || "STU-ID";
      setToast({
        type: "success",
        text: `Student ${studentForm.fullName} enrolled successfully with ID: ${assignedCode}!`,
      });
      setActiveModal(null);
      setStudentForm({
        fullName: "",
        email: "",
        password: "",
        course: "",
        yearOfStudy: "1st Year",
        department: "",
        companyCode: "APEX-2026",
      });
      fetchUsers();
    } catch (err) {
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to enroll student.",
      });
    } finally {
      setModalLoading(false);
    }
  };

  const handleCreateCounselor = async (e) => {
    e.preventDefault();
    setModalLoading(true);
    setToast(null);

    try {
      await api.post("/hr/create", {
        fullName: counselorForm.fullName.trim(),
        email: counselorForm.email.trim(),
        password: counselorForm.password,
        companyCode: counselorForm.companyCode.trim(),
      });

      setToast({
        type: "success",
        text: `Academic Counselor ${counselorForm.fullName} registered successfully!`,
      });
      setActiveModal(null);
      setCounselorForm({
        fullName: "",
        email: "",
        password: "",
        companyCode: "APEX-2026",
      });
      fetchUsers();
    } catch (err) {
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to add counselor.",
      });
    } finally {
      setModalLoading(false);
    }
  };

  const fetchUsers = async () => {
    setLoading(true);
    setError("");
    try {
      const res = await api.get("/admin/users");
      setUsers(res.data.users || []);
    } catch (e) {
      setError(e.response?.data?.message || "Failed to load users");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (token) fetchUsers();
  }, [token]);

  const filtered = users.filter((u) => {
    let matchesRole = true;
    if (roleFilter === "counselor") {
      matchesRole = u.role === "counselor" || u.role === "hr";
    } else if (roleFilter === "student") {
      matchesRole = u.role === "student" || u.role === "employee";
    } else if (roleFilter !== "all") {
      matchesRole = u.role === roleFilter;
    }

    const query = searchQuery.toLowerCase().trim();
    const instCode = (u.institutionCode || u.companyCode || "").toLowerCase();
    const stuCode = (u.studentCode || u.employeeCode || "").toLowerCase();
    const matchesSearch =
      !query ||
      u.fullName?.toLowerCase().includes(query) ||
      u.email?.toLowerCase().includes(query) ||
      instCode.includes(query) ||
      stuCode.includes(query) ||
      u.course?.toLowerCase().includes(query);

    return matchesRole && matchesSearch;
  });

  const counts = {
    all: users.length,
    platformAdmin: users.filter((u) => u.role === "platformAdmin").length,
    counselor: users.filter((u) => u.role === "counselor" || u.role === "hr").length,
    student: users.filter((u) => u.role === "student" || u.role === "employee").length,
  };

  return (
    <div className="space-y-6">
      {toast && (
        <Toast
          type={toast.type}
          message={toast.text}
          onClose={() => setToast(null)}
        />
      )}

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-bold text-slate-800 tracking-tight flex items-center gap-2.5">
            <UserCog className="w-8 h-8 text-indigo-600" />
            User & Counselor Management
          </h1>
          <p className="text-slate-500 text-sm mt-1">
            Browse all user accounts across institutions with role-based access verification.
          </p>
        </div>

        <div className="flex items-center gap-2 flex-wrap">
          <button
            onClick={() => setActiveModal("student")}
            className="inline-flex items-center gap-1.5 px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-xl shadow-xs transition-all cursor-pointer"
          >
            <UserPlus className="w-4 h-4" />
            <span>Enroll Student</span>
          </button>

          <button
            onClick={() => setActiveModal("counselor")}
            className="inline-flex items-center gap-1.5 px-3.5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-xs transition-all cursor-pointer"
          >
            <ShieldPlus className="w-4 h-4" />
            <span>Add Counselor</span>
          </button>

          <button
            onClick={fetchUsers}
            disabled={loading}
            className="inline-flex items-center gap-2 px-3.5 py-2 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 font-medium text-xs rounded-xl transition-all shadow-xs disabled:opacity-50 cursor-pointer"
          >
            <RefreshCw
              className={`w-3.5 h-3.5 ${
                loading ? "animate-spin text-indigo-600" : ""
              }`}
            />
            <span>Refresh</span>
          </button>
        </div>
      </div>

      {/* Role Breakdown Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        {[
          { label: "All Users", key: "all", count: counts.all, color: "text-slate-700 bg-slate-50 border-slate-200" },
          { label: "Platform Admins", key: "platformAdmin", count: counts.platformAdmin, color: "text-purple-700 bg-purple-50/50 border-purple-200" },
          { label: "Counselors", key: "counselor", count: counts.counselor, color: "text-indigo-700 bg-indigo-50/50 border-indigo-200" },
          { label: "Students", key: "student", count: counts.student, color: "text-emerald-700 bg-emerald-50/50 border-emerald-200" },
        ].map((item) => (
          <button
            key={item.key}
            onClick={() => setRoleFilter(item.key)}
            className={`p-4 rounded-2xl border text-left transition-all cursor-pointer ${item.color} ${
              roleFilter === item.key
                ? "ring-2 ring-indigo-500 shadow-sm"
                : "hover:border-slate-300"
            }`}
          >
            <p className="text-xs font-semibold uppercase tracking-wider opacity-80">{item.label}</p>
            <p className="text-2xl sm:text-3xl font-extrabold mt-1">{item.count}</p>
          </button>
        ))}
      </div>

      {error && (
        <div className="p-4 bg-rose-50 border border-rose-200 text-rose-700 rounded-xl text-sm">
          {error}
        </div>
      )}

      {/* Search and Filter */}
      <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="relative w-full sm:w-80">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search by name, email, institution code..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-800 placeholder-slate-400 focus:outline-hidden focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all"
          />
        </div>

        <div className="flex items-center gap-2 w-full sm:w-auto">
          <Filter className="w-4 h-4 text-slate-400" />
          <span className="text-xs font-medium text-slate-500 mr-1">Role:</span>
          {[
            { key: "all", label: "All" },
            { key: "platformAdmin", label: "Platform Admin" },
            { key: "counselor", label: "Counselor" },
            { key: "student", label: "Student" },
          ].map((r) => (
            <button
              key={r.key}
              onClick={() => setRoleFilter(r.key)}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all cursor-pointer ${
                roleFilter === r.key
                  ? "bg-indigo-600 text-white shadow-xs"
                  : "bg-slate-100 text-slate-600 hover:bg-slate-200"
              }`}
            >
              {r.label}
            </button>
          ))}
        </div>
      </div>

      {/* Users Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        {loading ? (
          <div className="p-12 text-center text-slate-400">
            <RefreshCw className="w-6 h-6 animate-spin mx-auto mb-2 text-indigo-500" />
            Loading platform users...
          </div>
        ) : filtered.length === 0 ? (
          <div className="p-12 text-center text-slate-400">
            <Users className="w-10 h-10 mx-auto mb-2 text-slate-300" />
            No users found matching current criteria.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="bg-slate-50/80 text-slate-500 text-xs font-semibold uppercase tracking-wider border-b border-slate-100">
                <tr>
                  <th className="px-6 py-3.5">User</th>
                  <th className="px-6 py-3.5">Role</th>
                  <th className="px-6 py-3.5">Institution Code</th>
                  <th className="px-6 py-3.5">ID / Code</th>
                  <th className="px-6 py-3.5">Joined Date</th>
                  <th className="px-6 py-3.5 text-right">Action</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {filtered.map((u) => {
                  const isCurrent = loggedInUser && loggedInUser.id === u._id;
                  const instCode = u.institutionCode || u.companyCode;
                  const userCode = u.studentCode || u.employeeCode;
                  const isStudent = u.role === "student" || u.role === "employee";
                  const isCounselor = u.role === "counselor" || u.role === "hr";

                  return (
                    <tr key={u._id} className="hover:bg-slate-50/80 transition-colors">
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-3">
                          <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-slate-200 to-slate-300 flex items-center justify-center font-bold text-xs text-slate-700 uppercase flex-shrink-0">
                            {u.fullName?.charAt(0) || "U"}
                          </div>
                          <div>
                            <div className="font-semibold text-slate-800 flex items-center gap-1.5">
                              {u.fullName}
                              {isCurrent && (
                                <span className="text-[10px] bg-indigo-100 text-indigo-700 font-bold px-1.5 py-0.5 rounded-sm">
                                  You
                                </span>
                              )}
                            </div>
                            <div className="text-xs text-slate-400 flex items-center gap-1 mt-0.5">
                              <Mail className="w-3 h-3" />
                              {u.email}
                            </div>
                            {u.course && (
                              <div className="text-[11px] text-slate-500 flex items-center gap-1 mt-0.5">
                                <BookOpen className="w-3 h-3 text-indigo-500" />
                                {u.course} {u.yearOfStudy ? `• ${u.yearOfStudy}` : ""}
                              </div>
                            )}
                          </div>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <span
                          className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold border ${
                            ROLE_BADGE[u.role] || "bg-slate-100 text-slate-700 border-slate-200"
                          }`}
                        >
                          {u.role === "platformAdmin" && <Shield className="w-3 h-3" />}
                          {isCounselor && <ShieldCheck className="w-3 h-3" />}
                          {isStudent && <GraduationCap className="w-3 h-3" />}
                          {ROLE_LABEL[u.role] || u.role}
                        </span>
                      </td>
                      <td className="px-6 py-4">
                        {instCode ? (
                          <span className="font-mono bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md text-xs font-bold border border-slate-200">
                            {instCode}
                          </span>
                        ) : (
                          <span className="text-slate-400 text-xs italic">System Wide</span>
                        )}
                      </td>
                      <td className="px-6 py-4 text-xs font-mono text-slate-600">
                        {userCode || "—"}
                      </td>
                      <td className="px-6 py-4 text-slate-500 text-xs">
                        {u.createdAt
                          ? new Date(u.createdAt).toLocaleDateString("en-US", {
                              year: "numeric",
                              month: "short",
                              day: "numeric",
                            })
                          : "N/A"}
                      </td>
                      <td className="px-6 py-4 text-right">
                        <button
                          onClick={() => setSelectedUser(u)}
                          className="px-2.5 py-1.5 text-indigo-600 hover:bg-indigo-50 rounded-lg text-xs font-medium inline-flex items-center gap-1 transition-colors cursor-pointer"
                        >
                          <Eye className="w-3.5 h-3.5" />
                          Details
                        </button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* User Details Modal */}
      <Modal
        isOpen={Boolean(selectedUser)}
        onClose={() => setSelectedUser(null)}
        title="Account Information"
        subtitle={selectedUser ? `${selectedUser.fullName} (${selectedUser.email})` : ""}
        icon={UserCog}
        maxWidth="max-w-md"
      >
        {selectedUser && (
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 rounded-2xl bg-indigo-100 text-indigo-600 flex items-center justify-center font-bold text-lg uppercase flex-shrink-0">
                {selectedUser.fullName?.charAt(0) || "U"}
              </div>
              <div>
                <h4 className="font-bold text-slate-800 text-base">{selectedUser.fullName}</h4>
                <p className="text-xs text-slate-500">{selectedUser.email}</p>
              </div>
            </div>

            <div className="space-y-3 pt-2">
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                <span className="text-xs font-medium text-slate-500">Platform Role</span>
                <span
                  className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold border ${
                    ROLE_BADGE[selectedUser.role] || "bg-slate-100 text-slate-700 border-slate-200"
                  }`}
                >
                  {ROLE_LABEL[selectedUser.role] || selectedUser.role}
                </span>
              </div>

              <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                <span className="text-xs font-medium text-slate-500">Institution Code</span>
                <span className="font-mono font-bold text-xs text-slate-800">
                  {selectedUser.institutionCode || selectedUser.companyCode || "Platform Root"}
                </span>
              </div>

              {(selectedUser.studentCode || selectedUser.employeeCode) && (
                <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                  <span className="text-xs font-medium text-slate-500">ID Code</span>
                  <span className="font-mono font-bold text-xs text-slate-800">
                    {selectedUser.studentCode || selectedUser.employeeCode}
                  </span>
                </div>
              )}

              {selectedUser.course && (
                <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                  <span className="text-xs font-medium text-slate-500">Course & Year</span>
                  <span className="text-xs font-bold text-slate-800">
                    {selectedUser.course} ({selectedUser.yearOfStudy || "N/A"})
                  </span>
                </div>
              )}

              {selectedUser.department && (
                <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                  <span className="text-xs font-medium text-slate-500">Department</span>
                  <span className="text-xs font-medium text-slate-800">
                    {selectedUser.department}
                  </span>
                </div>
              )}

              {selectedUser.assignedCounselor && (
                <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                  <span className="text-xs font-medium text-slate-500">Assigned Counselor</span>
                  <span className="text-xs font-medium text-slate-800">
                    {selectedUser.assignedCounselor}
                  </span>
                </div>
              )}

              {selectedUser.phoneNumber && (
                <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                  <span className="text-xs font-medium text-slate-500">Phone Number</span>
                  <span className="text-xs font-medium text-slate-800">
                    {selectedUser.phoneNumber}
                  </span>
                </div>
              )}

              <div className="p-3 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-between">
                <span className="text-xs font-medium text-slate-500">Registered At</span>
                <span className="text-xs font-medium text-slate-800">
                  {selectedUser.createdAt
                    ? new Date(selectedUser.createdAt).toLocaleString()
                    : "N/A"}
                </span>
              </div>
            </div>

            <div className="flex justify-end pt-3 border-t border-slate-100">
              <button
                type="button"
                onClick={() => setSelectedUser(null)}
                className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-sm font-medium transition-colors cursor-pointer"
              >
                Close
              </button>
            </div>
          </div>
        )}
      </Modal>

      {/* Modal: Enroll Student */}
      <Modal
        isOpen={activeModal === "student"}
        onClose={() => setActiveModal(null)}
        title="Enroll New Student (Platform Admin)"
        subtitle="Provision student account and register under institution"
        icon={UserPlus}
      >
        <form onSubmit={handleEnrollStudent} className="space-y-3.5">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Full Name
            </label>
            <div className="relative">
              <Users className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                required
                placeholder="Student Full Name"
                value={studentForm.fullName}
                onChange={(e) =>
                  setStudentForm((p) => ({ ...p, fullName: e.target.value }))
                }
                className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Email Address
            </label>
            <div className="relative">
              <Mail className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="email"
                required
                placeholder="student@institution.edu"
                value={studentForm.email}
                onChange={(e) =>
                  setStudentForm((p) => ({ ...p, email: e.target.value }))
                }
                className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Password
            </label>
            <div className="relative">
              <Lock className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="password"
                required
                placeholder="••••••••"
                value={studentForm.password}
                onChange={(e) =>
                  setStudentForm((p) => ({ ...p, password: e.target.value }))
                }
                className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div className="grid grid-cols-2 gap-3">
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Course
              </label>
              <input
                type="text"
                placeholder="e.g. Computer Engineering"
                value={studentForm.course}
                onChange={(e) =>
                  setStudentForm((p) => ({ ...p, course: e.target.value }))
                }
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-700 mb-1">
                Year of Study
              </label>
              <select
                value={studentForm.yearOfStudy}
                onChange={(e) =>
                  setStudentForm((p) => ({ ...p, yearOfStudy: e.target.value }))
                }
                className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              >
                <option value="1st Year">1st Year</option>
                <option value="2nd Year">2nd Year</option>
                <option value="3rd Year">3rd Year</option>
                <option value="4th Year">4th Year</option>
              </select>
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Institution Code
            </label>
            <input
              type="text"
              placeholder="e.g. APEX-2026"
              value={studentForm.companyCode}
              onChange={(e) =>
                setStudentForm((p) => ({ ...p, companyCode: e.target.value }))
              }
              className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl font-mono uppercase focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
            />
          </div>

          <div className="flex justify-end gap-2 pt-3">
            <button
              type="button"
              onClick={() => setActiveModal(null)}
              className="px-4 py-2 border border-slate-200 text-slate-600 rounded-xl text-xs font-medium hover:bg-slate-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={modalLoading}
              className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold transition-all disabled:opacity-50"
            >
              {modalLoading ? "Enrolling..." : "Enroll Student"}
            </button>
          </div>
        </form>
      </Modal>

      {/* Modal: Add Counselor */}
      <Modal
        isOpen={activeModal === "counselor"}
        onClose={() => setActiveModal(null)}
        title="Add Academic Counselor (Platform Admin)"
        subtitle="Grant counselor advisory privileges"
        icon={ShieldPlus}
      >
        <form onSubmit={handleCreateCounselor} className="space-y-3.5">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Full Name
            </label>
            <div className="relative">
              <Users className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                required
                placeholder="Counselor Full Name"
                value={counselorForm.fullName}
                onChange={(e) =>
                  setCounselorForm((p) => ({ ...p, fullName: e.target.value }))
                }
                className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Email Address
            </label>
            <div className="relative">
              <Mail className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="email"
                required
                placeholder="counselor@institution.edu"
                value={counselorForm.email}
                onChange={(e) =>
                  setCounselorForm((p) => ({ ...p, email: e.target.value }))
                }
                className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Password
            </label>
            <div className="relative">
              <Lock className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="password"
                required
                placeholder="••••••••"
                value={counselorForm.password}
                onChange={(e) =>
                  setCounselorForm((p) => ({ ...p, password: e.target.value }))
                }
                className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Institution Code
            </label>
            <input
              type="text"
              placeholder="e.g. APEX-2026"
              value={counselorForm.companyCode}
              onChange={(e) =>
                setCounselorForm((p) => ({ ...p, companyCode: e.target.value }))
              }
              className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl font-mono uppercase focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
            />
          </div>

          <div className="flex justify-end gap-2 pt-3">
            <button
              type="button"
              onClick={() => setActiveModal(null)}
              className="px-4 py-2 border border-slate-200 text-slate-600 rounded-xl text-xs font-medium hover:bg-slate-50"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={modalLoading}
              className="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold transition-all disabled:opacity-50"
            >
              {modalLoading ? "Creating..." : "Add Counselor"}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
};
