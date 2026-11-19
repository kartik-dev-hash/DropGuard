import React, { useEffect, useState } from "react";
import api from "../api/client";
import { useAuth } from "../context/AuthContext";

const STATUS_BADGE = {
  pending: "bg-yellow-100 text-yellow-800",
  approved: "bg-green-100 text-green-800",
  rejected: "bg-red-100 text-red-800",
};

export const PlatformAdmin = () => {
  const { token } = useAuth();
  const [companies, setCompanies] = useState([]);
  const [loading, setLoading] = useState(false);
  const [actionLoading, setActionLoading] = useState({});
  const [error, setError] = useState("");
  const [filter, setFilter] = useState("all"); // all | pending | approved | rejected

  const fetchAll = async () => {
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
    if (token) fetchAll();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);

  const handleAction = async (id, action) => {
    setActionLoading((prev) => ({ ...prev, [id]: true }));
    try {
      await api.put(`/admin/${action}-company/${id}`);
      await fetchAll();
    } catch (e) {
      alert(e.response?.data?.message || `Failed to ${action} institution`);
    } finally {
      setActionLoading((prev) => ({ ...prev, [id]: false }));
    }
  };

  const filtered = companies.filter((c) =>
    filter === "all" ? true : c.status === filter
  );

  const counts = {
    all: companies.length,
    pending: companies.filter((c) => c.status === "pending").length,
    approved: companies.filter((c) => c.status === "approved").length,
    rejected: companies.filter((c) => c.status === "rejected").length,
  };

  return (
    <div className="min-h-screen bg-slate-50 p-6">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-slate-800">Platform Admin Dashboard</h1>
        <p className="text-slate-500 mt-1">
          Review institution registration requests and manage workspace access.
        </p>
      </div>

      {/* Stat Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8">
        {[
          { label: "Total Institutions", key: "all", color: "bg-slate-100 text-slate-700" },
          { label: "Pending", key: "pending", color: "bg-yellow-50 text-yellow-700 border border-yellow-200" },
          { label: "Approved", key: "approved", color: "bg-green-50 text-green-700 border border-green-200" },
          { label: "Rejected", key: "rejected", color: "bg-red-50 text-red-700 border border-red-200" },
        ].map(({ label, key, color }) => (
          <button
            key={key}
            onClick={() => setFilter(key)}
            className={`rounded-xl p-4 text-left transition-all shadow-sm hover:shadow-md cursor-pointer ${color} ${
              filter === key ? "ring-2 ring-indigo-500 shadow-md" : ""
            }`}
          >
            <p className="text-sm font-medium">{label}</p>
            <p className="text-3xl font-bold mt-1">{counts[key]}</p>
          </button>
        ))}
      </div>

      {/* Error */}
      {error && (
        <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg mb-6">
          {error}
        </div>
      )}

      {/* Table */}
      <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
        <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between">
          <h2 className="font-semibold text-slate-700">
            {filter === "all" ? "All Institutions" : `${filter.charAt(0).toUpperCase() + filter.slice(1)} Institutions`}
          </h2>
          <button
            onClick={fetchAll}
            className="text-sm text-indigo-600 hover:text-indigo-800 font-medium cursor-pointer"
          >
            ↻ Refresh
          </button>
        </div>

        {loading ? (
          <div className="p-10 text-center text-slate-500">Loading institutions...</div>
        ) : filtered.length === 0 ? (
          <div className="p-10 text-center text-slate-400">
            No {filter === "all" ? "" : filter} institutions found.
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead className="bg-slate-50 text-slate-600 uppercase text-xs tracking-wider">
                <tr>
                  <th className="px-6 py-3 text-left">Institution Name</th>
                  <th className="px-6 py-3 text-left">Category</th>
                  <th className="px-6 py-3 text-left">Institution Code</th>
                  <th className="px-6 py-3 text-left">Lead Counselor</th>
                  <th className="px-6 py-3 text-left">Counselor Email</th>
                  <th className="px-6 py-3 text-left">Status</th>
                  <th className="px-6 py-3 text-left">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {filtered.map((c) => {
                  const instName = c.institutionName || c.companyName;
                  const instCode = c.institutionCode || c.companyCode;
                  const counselor = c.primaryCounselor || c.primaryHR;
                  return (
                    <tr key={c._id} className="hover:bg-slate-50 transition-colors">
                      <td className="px-6 py-4 font-medium text-slate-800">{instName}</td>
                      <td className="px-6 py-4 text-slate-600">{c.industry || "Academic"}</td>
                      <td className="px-6 py-4">
                        <span className="font-mono bg-slate-100 px-2 py-1 rounded text-xs font-bold text-slate-700">
                          {instCode}
                        </span>
                      </td>
                      <td className="px-6 py-4 text-slate-600">{counselor?.fullName || "N/A"}</td>
                      <td className="px-6 py-4 text-slate-600">{counselor?.email || "N/A"}</td>
                      <td className="px-6 py-4">
                        <span
                          className={`px-3 py-1 rounded-full text-xs font-semibold capitalize ${
                            STATUS_BADGE[c.status] || "bg-gray-100 text-gray-600"
                          }`}
                        >
                          {c.status}
                        </span>
                      </td>
                      <td className="px-6 py-4">
                        {c.status === "pending" && (
                          <div className="flex gap-2">
                            <button
                              disabled={actionLoading[c._id]}
                              onClick={() => handleAction(c._id, "approve")}
                              className="px-3 py-1 bg-green-600 text-white text-xs rounded-lg hover:bg-green-700 disabled:opacity-50 font-medium transition-colors cursor-pointer"
                            >
                              {actionLoading[c._id] ? "..." : "Approve"}
                            </button>
                            <button
                              disabled={actionLoading[c._id]}
                              onClick={() => handleAction(c._id, "reject")}
                              className="px-3 py-1 bg-red-600 text-white text-xs rounded-lg hover:bg-red-700 disabled:opacity-50 font-medium transition-colors cursor-pointer"
                            >
                              {actionLoading[c._id] ? "..." : "Reject"}
                            </button>
                          </div>
                        )}
                        {c.status === "approved" && (
                          <button
                            disabled={actionLoading[c._id]}
                            onClick={() => handleAction(c._id, "reject")}
                            className="px-3 py-1 bg-red-100 text-red-700 text-xs rounded-lg hover:bg-red-200 disabled:opacity-50 font-medium transition-colors cursor-pointer"
                          >
                            {actionLoading[c._id] ? "..." : "Revoke"}
                          </button>
                        )}
                        {c.status === "rejected" && (
                          <button
                            disabled={actionLoading[c._id]}
                            onClick={() => handleAction(c._id, "approve")}
                            className="px-3 py-1 bg-green-100 text-green-700 text-xs rounded-lg hover:bg-green-200 disabled:opacity-50 font-medium transition-colors cursor-pointer"
                          >
                            {actionLoading[c._id] ? "..." : "Re-approve"}
                          </button>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};
