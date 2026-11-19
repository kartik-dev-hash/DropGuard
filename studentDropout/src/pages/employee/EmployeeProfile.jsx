import React, { useState } from "react";
import { useAuth } from "../../context/AuthContext";
import api from "../../api/client";
import { Card } from "../../components/common/Card";
import { StatusBadge } from "../../components/common/Badge";
import { Modal } from "../../components/common/Modal";
import { Toast } from "../../components/common/Toast";
import {
  GraduationCap,
  User,
  Mail,
  Hash,
  School,
  ShieldCheck,
  CheckCircle2,
  BookOpen,
  Calendar,
  Layers,
  Phone,
  UserCheck,
  Edit3,
} from "lucide-react";

export const EmployeeProfile = () => {
  const { user, updateUser } = useAuth();
  const [isEditing, setIsEditing] = useState(false);
  const [loading, setLoading] = useState(false);
  const [toast, setToast] = useState(null);

  const [formData, setFormData] = useState({
    course: user?.course || "",
    yearOfStudy: user?.yearOfStudy || "1st",
    department: user?.department || "",
    phoneNumber: user?.phoneNumber || "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSaveProfile = async (e) => {
    e.preventDefault();
    setLoading(true);
    setToast(null);

    try {
      const res = await api.put("/student/profile", formData);
      if (res.data?.user) {
        updateUser(res.data.user);
      }
      setToast({ type: "success", text: "Student academic profile updated successfully! ✅" });
      setIsEditing(false);
    } catch (err) {
      setToast({
        type: "error",
        text: err.response?.data?.message || "Failed to update profile.",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl space-y-6">
      {toast && <Toast type={toast.type} message={toast.text} onClose={() => setToast(null)} />}

      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-bold text-slate-900">Student Academic Profile</h2>
          <p className="text-xs text-slate-500">Your registered enrollment details, cohort and counselor assignment</p>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={() => {
              setFormData({
                course: user?.course || "",
                yearOfStudy: user?.yearOfStudy || "1st",
                department: user?.department || "",
                phoneNumber: user?.phoneNumber || "",
              });
              setIsEditing(true);
            }}
            className="px-3.5 py-1.5 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs font-bold rounded-xl border border-indigo-200 transition-all flex items-center gap-1.5 cursor-pointer"
          >
            <Edit3 className="w-3.5 h-3.5" />
            <span>Update Academics</span>
          </button>
          <StatusBadge type="student" label="Enrolled Student" />
        </div>
      </div>

      <Card>
        {/* Top Profile Summary Header */}
        <div className="flex flex-col sm:flex-row items-center gap-6 pb-6 border-b border-slate-100">
          <div className="w-20 h-20 rounded-2xl bg-gradient-to-tr from-indigo-600 to-purple-600 text-white flex items-center justify-center font-extrabold text-2xl shadow-lg shadow-indigo-600/30">
            {user?.fullName?.charAt(0) || "S"}
          </div>

          <div className="space-y-1 text-center sm:text-left">
            <h3 className="text-2xl font-extrabold text-slate-900">{user?.fullName || "Student Name"}</h3>
            <p className="text-xs font-medium text-slate-500">{user?.email}</p>
            <div className="flex items-center justify-center sm:justify-start gap-2 pt-1 flex-wrap">
              <span className="inline-flex items-center gap-1 text-[11px] font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded-full border border-indigo-100">
                <ShieldCheck className="w-3 h-3" /> Student
              </span>
              {(user?.studentCode || user?.employeeCode) && (
                <span className="inline-flex items-center gap-1 text-[11px] font-bold text-slate-700 bg-slate-100 px-2.5 py-0.5 rounded-full border border-slate-200 font-mono">
                  ID: {user?.studentCode || user?.employeeCode}
                </span>
              )}
              {user?.course && (
                <span className="inline-flex items-center gap-1 text-[11px] font-bold text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-100">
                  <BookOpen className="w-3 h-3" /> {user.course}
                </span>
              )}
            </div>
          </div>
        </div>

        {/* Profile Details Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 pt-6">
          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-indigo-100 text-indigo-600">
              <User className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Full Name</span>
              <span className="text-sm font-bold text-slate-800">{user?.fullName || "N/A"}</span>
            </div>
          </div>

          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-purple-100 text-purple-600">
              <Mail className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Email Address</span>
              <span className="text-sm font-bold text-slate-800">{user?.email || "N/A"}</span>
            </div>
          </div>

          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-amber-100 text-amber-600">
              <Hash className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Student ID</span>
              <span className="text-sm font-mono font-bold text-slate-800">{user?.studentCode || user?.employeeCode || "N/A"}</span>
            </div>
          </div>

          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-emerald-100 text-emerald-600">
              <School className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Institution Code</span>
              <span className="text-sm font-mono font-bold text-slate-800 uppercase">{user?.institutionCode || user?.companyCode || "N/A"}</span>
            </div>
          </div>

          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-blue-100 text-blue-600">
              <BookOpen className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Course / Degree</span>
              <span className="text-sm font-bold text-slate-800">{user?.course || "General Curriculum"}</span>
            </div>
          </div>

          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-teal-100 text-teal-600">
              <Calendar className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Year of Study</span>
              <span className="text-sm font-bold text-slate-800">{user?.yearOfStudy ? `${user.yearOfStudy} Year` : "1st Year"}</span>
            </div>
          </div>

          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-violet-100 text-violet-600">
              <Layers className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Department</span>
              <span className="text-sm font-bold text-slate-800">{user?.department || "Academic Division"}</span>
            </div>
          </div>

          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-rose-100 text-rose-600">
              <UserCheck className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Assigned Counselor</span>
              <span className="text-sm font-bold text-slate-800">{user?.assignedCounselor || user?.assignedHR || "Academic Counselor"}</span>
            </div>
          </div>

          <div className="p-4 bg-slate-50/70 rounded-2xl border border-slate-100 flex items-start gap-3.5">
            <div className="p-2.5 rounded-xl bg-orange-100 text-orange-600">
              <Phone className="w-5 h-5" />
            </div>
            <div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Contact Phone</span>
              <span className="text-sm font-bold text-slate-800">{user?.phoneNumber || "Not provided"}</span>
            </div>
          </div>
        </div>

        {/* Verification Footer */}
        <div className="mt-8 pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
          <div className="flex items-center gap-1.5 text-emerald-600 font-semibold">
            <CheckCircle2 className="w-4 h-4" />
            <span>Verified Student Record</span>
          </div>
          <span>Account ID: {user?.id || user?._id || "N/A"}</span>
        </div>
      </Card>

      {/* Modal: Edit Student Academics */}
      <Modal
        isOpen={isEditing}
        onClose={() => setIsEditing(false)}
        title="Update Academic Profile"
        subtitle="Manage your course, cohort year and contact number"
        icon={BookOpen}
        maxWidth="max-w-md"
      >
        <form onSubmit={handleSaveProfile} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Course / Program</label>
            <input
              type="text"
              name="course"
              required
              placeholder="e.g. B.Tech Computer Science"
              value={formData.course}
              onChange={handleChange}
              className="w-full px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Year of Study</label>
            <select
              name="yearOfStudy"
              value={formData.yearOfStudy}
              onChange={handleChange}
              className="w-full px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white"
            >
              <option value="1st">1st Year</option>
              <option value="2nd">2nd Year</option>
              <option value="3rd">3rd Year</option>
              <option value="4th">4th Year</option>
            </select>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Department</label>
            <input
              type="text"
              name="department"
              placeholder="e.g. School of Engineering"
              value={formData.department}
              onChange={handleChange}
              className="w-full px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">Phone Number (WhatsApp Outreach)</label>
            <input
              type="tel"
              name="phoneNumber"
              placeholder="+91 9876543210"
              value={formData.phoneNumber}
              onChange={handleChange}
              className="w-full px-3.5 py-2.5 bg-slate-50 border border-slate-200 rounded-xl text-xs sm:text-sm font-medium text-slate-800 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:bg-white"
            />
          </div>

          <div className="flex items-center justify-end gap-2 pt-2">
            <button
              type="button"
              onClick={() => setIsEditing(false)}
              className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs rounded-xl transition cursor-pointer"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="px-5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-md transition cursor-pointer disabled:opacity-50"
            >
              {loading ? "Saving..." : "Save Changes"}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export const StudentProfile = EmployeeProfile;
