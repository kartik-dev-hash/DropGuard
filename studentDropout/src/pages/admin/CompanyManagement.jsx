import React, { useEffect, useState } from "react";
import api from "../../api/client";
import { useAuth } from "../../context/AuthContext";
import { Modal } from "../../components/common/Modal";
import {
  Building2,
  Search,
  Filter,
  RefreshCw,
  Users,
  ShieldCheck,
  Calendar,
  Mail,
  Briefcase,
  CheckCircle2,
  XCircle,
  Clock,
  Eye,
  X,
  Building,
  Plus,
  Lock,
  User,
} from "lucide-react";

const STATUS_BADGE = {
  pending: "bg-amber-50 text-amber-700 border-amber-200",
  approved: "bg-emerald-50 text-emerald-700 border-emerald-200",
  rejected: "bg-rose-50 text-rose-700 border-rose-200",
};

export const CompanyManagement = () => {
  const { token } = useAuth();
  const [companies, setCompanies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [actionLoading, setActionLoading] = useState({});
  const [error, setError] = useState("");
  const [filter, setFilter] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedCompany, setSelectedCompany] = useState(null);
  const [isCreateOpen, setIsCreateOpen] = useState(false);
  const [createLoading, setCreateLoading] = useState(false);
  const [createForm, setCreateForm] = useState({
    companyName: "",
    industry: "Higher Education",
    adminName: "",
    adminEmail: "",
    password: "",
  });

  const handleCreateCompany = async (e) => {
    e.preventDefault();
    setCreateLoading(true);
    try {
      await api.post("/admin/companies", {
        companyName: createForm.companyName.trim(),
        industry: createForm.industry.trim() || "Higher Education",
        adminName: createForm.adminName.trim(),
        adminEmail: createForm.adminEmail.trim(),
        password: createForm.password,
      });
      setIsCreateOpen(false);
      setCreateForm({
        companyName: "",
        industry: "Higher Education",
        adminName: "",
        adminEmail: "",
        password: "",
      });
      await fetchCompanies();
    } catch (err) {
      alert(err.response?.data?.message || "Failed to register institution");
    } finally {
      setCreateLoading(false);
    }
  };

  const fetchCompanies = async () => {
    setLoading(true);
    setError("");
    try {
      const res = await api.get("/admin/all-companies");
      setCompanies(res.data.companies || []);
    } catch (e) {
      setError(e.response?.data?.message || "Failed to load institutions");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (token) fetchCompanies();
  }, [token]);

  const handleAction = async (id, action) => {
    setActionLoading((prev) => ({ ...prev, [id]: true }));
    try {
      await api.put(`/admin/${action}-company/${id}`);
      await fetchCompanies();
      if (selectedCompany && selectedCompany._id === id) {
        setSelectedCompany((prev) => ({
          ...prev,
          status: action === "approve" ? "approved" : "rejected",
        }));
      }
    } catch (e) {
      alert(e.response?.data?.message || `Failed to ${action} institution`);
    } finally {
      setActionLoading((prev) => ({ ...prev, [id]: false }));
    }
  };

  const filtered = companies.filter((c) => {
    const matchesFilter = filter === "all" ? true : c.status === filter;
    const query = searchQuery.toLowerCase().trim();
    const name = (c.institutionName || c.companyName || "").toLowerCase();
    const code = (c.institutionCode || c.companyCode || "").toLowerCase();
    const industry = (c.industry || "").toLowerCase();
    const counselorName = (c.primaryCounselor?.fullName || c.primaryHR?.fullName || "").toLowerCase();
    const counselorEmail = (c.primaryCounselor?.email || c.primaryHR?.email || "").toLowerCase();

    const matchesSearch =
      !query ||
      name.includes(query) ||
      code.includes(query) ||
      industry.includes(query) ||
      counselorName.includes(query) ||
      counselorEmail.includes(query);

    return matchesFilter && matchesSearch;
  });

  const counts = {
    all: companies.length,
    pending: companies.filter((c) => c.status === "pending").length,
    approved: companies.filter((c) => c.status === "approved").length,
    rejected: companies.filter((c) => c.status === "rejected").length,
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-bold text-slate-800 tracking-tight flex items-center gap-2.5">
            <Building2 className="w-8 h-8 text-indigo-600" />
            Institution Management
          </h1>
          <p className="text-slate-500 text-sm mt-1">
            Review registered institutions, manage onboarding approval, and track student footprint.
          </p>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={() => setIsCreateOpen(true)}
            className="inline-flex items-center gap-1.5 px-3.5 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs rounded-xl shadow-xs transition-all cursor-pointer"
          >
            <Plus className="w-4 h-4" />
            <span>Register Institution</span>
          </button>

          <button
            onClick={fetchCompanies}
            disabled={loading}
            className="inline-flex items-center gap-2 px-3.5 py-2 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 font-medium text-xs rounded-xl transition-all shadow-xs disabled:opacity-50 cursor-pointer"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${loading ? "animate-spin text-indigo-600" : ""}`} />
            <span>Refresh</span>
          </button>
        </div>
      </div>

      {/* Metric Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        {[
          { label: "All Institutions", key: "all", count: counts.all, color: "text-slate-700 bg-slate-50 border-slate-200" },
          { label: "Pending Approval", key: "pending", count: counts.pending, color: "text-amber-700 bg-amber-50/50 border-amber-200" },
          { label: "Active & Approved", key: "approved", count: counts.approved, color: "text-emerald-700 bg-emerald-50/50 border-emerald-200" },
          { label: "Rejected / Suspended", key: "rejected", count: counts.rejected, color: "text-rose-700 bg-rose-50/50 border-rose-200" },
        ].map((item) => (
          <button
            key={item.key}
            onClick={() => setFilter(item.key)}
            className={`p-4 rounded-2xl border text-left transition-all cursor-pointer ${item.color} ${
              filter === item.key
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

      {/* Filter and Search Bar */}
      <div className="bg-white p-4 rounded-2xl border border-slate-200 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="relative w-full sm:w-80">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search by institution, code, counselor..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-800 placeholder-slate-400 focus:outline-hidden focus:ring-2 focus:ring-indigo-500 focus:bg-white transition-all"
          />
        </div>

        <div className="flex items-center gap-2 w-full sm:w-auto">
          <Filter className="w-4 h-4 text-slate-400" />
          <span className="text-xs font-medium text-slate-500 mr-1">Status:</span>
          {["all", "pending", "approved", "rejected"].map((st) => (
            <button
              key={st}
              onClick={() => setFilter(st)}
              className={`px-3 py-1.5 rounded-lg text-xs font-medium capitalize transition-all cursor-pointer ${
                filter === st
                  ? "bg-indigo-600 text-white shadow-xs"
                  : "bg-slate-100 text-slate-600 hover:bg-slate-200"
              }`}
            >
              {st}
            </button>
          ))}
        </div>
      </div>

      {/* Institutions Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-xs overflow-hidden">
        {loading ? (
          <div className="p-12 text-center text-slate-400">
            <RefreshCw className="w-6 h-6 animate-spin mx-auto mb-2 text-indigo-500" />
            Loading registered institutions...
          </div>
        ) : filtered.length === 0 ? (
          <div className="p-12 text-center text-slate-400">
            <Building className="w-10 h-10 mx-auto mb-2 text-slate-300" />
            No institutions found matching current filters.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="bg-slate-50/80 text-slate-500 text-xs font-semibold uppercase tracking-wider border-b border-slate-100">
                <tr>
                  <th className="px-6 py-3.5">Institution Name</th>
                  <th className="px-6 py-3.5">Category</th>
                  <th className="px-6 py-3.5">Institution Code</th>
                  <th className="px-6 py-3.5">Registered Date</th>
                  <th className="px-6 py-3.5">Students</th>
                  <th className="px-6 py-3.5">Status</th>
                  <th className="px-6 py-3.5 text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {filtered.map((comp) => {
                  const instName = comp.institutionName || comp.companyName;
                  const instCode = comp.institutionCode || comp.companyCode;
                  const counselor = comp.primaryCounselor || comp.primaryHR;
                  const count = comp.studentCount ?? comp.employeeCount ?? 0;

                  return (
                    <tr key={comp._id} className="hover:bg-slate-50/80 transition-colors">
                      <td className="px-6 py-4">
                        <div className="font-semibold text-slate-800">{instName}</div>
                        <div className="text-xs text-slate-400 flex items-center gap-1 mt-0.5">
                          <Mail className="w-3 h-3" />
                          {counselor?.email || "No counselor assigned"}
                        </div>
                      </td>
                      <td className="px-6 py-4 text-slate-600 font-medium">
                        {comp.industry || "Academic Institution"}
                      </td>
                      <td className="px-6 py-4">
                        <span className="font-mono bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md text-xs font-bold border border-slate-200">
                          {instCode}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-slate-500 text-xs">
                        {comp.createdAt
                          ? new Date(comp.createdAt).toLocaleDateString("en-US", {
                              year: "numeric",
                              month: "short",
                              day: "numeric",
                            })
                          : "N/A"}
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex items-center gap-1.5 text-slate-700 font-medium">
                          <Users className="w-4 h-4 text-indigo-500" />
                          <span>{count}</span>
                        </div>
                      </td>
                      <td className="px-6 py-4">
                        <span
                          className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold border capitalize ${
                            STATUS_BADGE[comp.status] || "bg-slate-100 text-slate-600 border-slate-200"
                          }`}
                        >
                          {comp.status === "approved" && <CheckCircle2 className="w-3 h-3" />}
                          {comp.status === "pending" && <Clock className="w-3 h-3" />}
                          {comp.status === "rejected" && <XCircle className="w-3 h-3" />}
                          {comp.status}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-right">
                        <div className="flex items-center justify-end gap-2">
                          <button
                            onClick={() => setSelectedCompany(comp)}
                            className="px-2.5 py-1.5 text-indigo-600 hover:bg-indigo-50 rounded-lg text-xs font-medium flex items-center gap-1 transition-colors cursor-pointer"
                            title="View Details"
                          >
                            <Eye className="w-3.5 h-3.5" />
                            Details
                          </button>

                          {comp.status === "pending" && (
                            <>
                              <button
                                disabled={actionLoading[comp._id]}
                                onClick={() => handleAction(comp._id, "approve")}
                                className="px-3 py-1.5 bg-emerald-600 text-white hover:bg-emerald-700 rounded-lg text-xs font-medium transition-colors disabled:opacity-50 cursor-pointer"
                              >
                                {actionLoading[comp._id] ? "..." : "Approve"}
                              </button>
                              <button
                                disabled={actionLoading[comp._id]}
                                onClick={() => handleAction(comp._id, "reject")}
                                className="px-3 py-1.5 bg-rose-600 text-white hover:bg-rose-700 rounded-lg text-xs font-medium transition-colors disabled:opacity-50 cursor-pointer"
                              >
                                {actionLoading[comp._id] ? "..." : "Reject"}
                              </button>
                            </>
                          )}

                          {comp.status === "approved" && (
                            <button
                              disabled={actionLoading[comp._id]}
                              onClick={() => handleAction(comp._id, "reject")}
                              className="px-2.5 py-1.5 text-rose-600 hover:bg-rose-50 border border-rose-200 rounded-lg text-xs font-medium transition-colors disabled:opacity-50 cursor-pointer"
                            >
                              {actionLoading[comp._id] ? "..." : "Revoke Access"}
                            </button>
                          )}

                          {comp.status === "rejected" && (
                            <button
                              disabled={actionLoading[comp._id]}
                              onClick={() => handleAction(comp._id, "approve")}
                              className="px-2.5 py-1.5 text-emerald-600 hover:bg-emerald-50 border border-emerald-200 rounded-lg text-xs font-medium transition-colors disabled:opacity-50 cursor-pointer"
                            >
                              {actionLoading[comp._id] ? "..." : "Re-approve"}
                            </button>
                          )}
                        </div>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Institution Details Modal */}
      <Modal
        isOpen={Boolean(selectedCompany)}
        onClose={() => setSelectedCompany(null)}
        title="Institution Details"
        subtitle={selectedCompany ? `${selectedCompany.institutionName || selectedCompany.companyName} (${selectedCompany.industry || "Academic"})` : ""}
        icon={Building2}
        maxWidth="max-w-lg"
      >
        {selectedCompany && (
          <div className="space-y-4">
            <div className="flex items-start justify-between">
              <div>
                <h4 className="text-xl font-bold text-slate-800">{selectedCompany.institutionName || selectedCompany.companyName}</h4>
                <p className="text-sm text-slate-500">{selectedCompany.industry || "Academic Institution"}</p>
              </div>
              <span
                className={`inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-semibold border capitalize ${
                  STATUS_BADGE[selectedCompany.status] || "bg-slate-100 text-slate-600 border-slate-200"
                }`}
              >
                {selectedCompany.status}
              </span>
            </div>

            <div className="grid grid-cols-2 gap-3 pt-2">
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-100">
                <span className="text-[11px] font-medium text-slate-400 block uppercase">Institution Code</span>
                <span className="font-mono font-bold text-sm text-slate-800">{selectedCompany.institutionCode || selectedCompany.companyCode}</span>
              </div>
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-100">
                <span className="text-[11px] font-medium text-slate-400 block uppercase">Total Students</span>
                <span className="font-bold text-sm text-slate-800">{selectedCompany.studentCount ?? selectedCompany.employeeCount ?? 0}</span>
              </div>
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-100">
                <span className="text-[11px] font-medium text-slate-400 block uppercase">Registered On</span>
                <span className="font-medium text-sm text-slate-700">
                  {selectedCompany.createdAt
                    ? new Date(selectedCompany.createdAt).toLocaleDateString()
                    : "N/A"}
                </span>
              </div>
              <div className="p-3 bg-slate-50 rounded-xl border border-slate-100">
                <span className="text-[11px] font-medium text-slate-400 block uppercase">Counselors</span>
                <span className="font-bold text-sm text-slate-800">{selectedCompany.counselorCount ?? selectedCompany.hrCount ?? 1}</span>
              </div>
            </div>

            <div className="pt-2 border-t border-slate-100 space-y-2">
              <h5 className="text-xs font-semibold text-slate-500 uppercase tracking-wider">
                Lead Academic Counselor
              </h5>
              <div className="p-3 bg-indigo-50/50 rounded-xl border border-indigo-100 flex items-center justify-between">
                <div>
                  <p className="text-sm font-bold text-slate-800">
                    {selectedCompany.primaryCounselor?.fullName || selectedCompany.primaryHR?.fullName || "Not Assigned"}
                  </p>
                  <p className="text-xs text-slate-500">
                    {selectedCompany.primaryCounselor?.email || selectedCompany.primaryHR?.email || "No email"}
                  </p>
                </div>
                <ShieldCheck className="w-5 h-5 text-indigo-500" />
              </div>
            </div>

            <div className="flex justify-end pt-3 border-t border-slate-100">
              <button
                type="button"
                onClick={() => setSelectedCompany(null)}
                className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-sm font-medium transition-colors cursor-pointer"
              >
                Close
              </button>
            </div>
          </div>
        )}
      </Modal>

      {/* Modal: Register Institution & Primary Counselor */}
      <Modal
        isOpen={isCreateOpen}
        onClose={() => setIsCreateOpen(false)}
        title="Register New Institution Workspace"
        subtitle="Provision approved institution and create lead academic counselor"
        icon={Building2}
      >
        <form onSubmit={handleCreateCompany} className="space-y-3.5">
          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Institution Name
            </label>
            <div className="relative">
              <Building className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
              <input
                type="text"
                required
                placeholder="e.g. Stanford Academy / Pune University"
                value={createForm.companyName}
                onChange={(e) =>
                  setCreateForm((p) => ({ ...p, companyName: e.target.value }))
                }
                className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-700 mb-1">
              Industry / Type
            </label>
            <input
              type="text"
              placeholder="Higher Education / University / High School"
              value={createForm.industry}
              onChange={(e) =>
                setCreateForm((p) => ({ ...p, industry: e.target.value }))
              }
              className="w-full px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
            />
          </div>

          <div className="pt-2 border-t border-slate-100">
            <h5 className="text-xs font-bold text-slate-800 mb-2">
              Primary Academic Counselor Account
            </h5>
            <div className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  Lead Counselor Name
                </label>
                <div className="relative">
                  <User className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                  <input
                    type="text"
                    required
                    placeholder="e.g. Dr. Kalyani Deshmukh"
                    value={createForm.adminName}
                    onChange={(e) =>
                      setCreateForm((p) => ({ ...p, adminName: e.target.value }))
                    }
                    className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  Counselor Email Address
                </label>
                <div className="relative">
                  <Mail className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                  <input
                    type="email"
                    required
                    placeholder="counselor@institution.edu"
                    value={createForm.adminEmail}
                    onChange={(e) =>
                      setCreateForm((p) => ({ ...p, adminEmail: e.target.value }))
                    }
                    className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold text-slate-700 mb-1">
                  Counselor Initial Password
                </label>
                <div className="relative">
                  <Lock className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
                  <input
                    type="password"
                    required
                    placeholder="••••••••"
                    value={createForm.password}
                    onChange={(e) =>
                      setCreateForm((p) => ({ ...p, password: e.target.value }))
                    }
                    className="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-xl focus:outline-hidden focus:ring-2 focus:ring-indigo-600 focus:bg-white"
                  />
                </div>
              </div>
            </div>
          </div>

          <div className="flex justify-end gap-2 pt-3">
            <button
              type="button"
              onClick={() => setIsCreateOpen(false)}
              className="px-4 py-2 border border-slate-200 text-slate-600 rounded-xl text-xs font-medium hover:bg-slate-50 cursor-pointer"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={createLoading}
              className="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold transition-all disabled:opacity-50 cursor-pointer"
            >
              {createLoading ? "Registering..." : "Create & Approve Workspace"}
            </button>
          </div>
        </form>
      </Modal>
    </div>
  );
};

export const InstitutionManagement = CompanyManagement;
