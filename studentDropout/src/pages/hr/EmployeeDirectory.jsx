import React, { useEffect, useState } from "react";
import api from "../../api/client";
import { DataTable } from "../../components/common/DataTable";
import { StatusBadge, DropoutRiskBadge } from "../../components/common/Badge";
import { LoadingSpinner } from "../../components/common/LoadingSpinner";
import { RatingStars } from "../../components/common/RatingStars";
import { Users, Eye, RefreshCw, Clock, ShieldAlert, GraduationCap } from "lucide-react";
import { EmployeeDetailView } from "../../components/hr-analytics/EmployeeDetailView";

export const EmployeeDirectory = () => {
  const [employees, setEmployees] = useState([]);
  const [feedbacks, setFeedbacks] = useState([]);
  const [loading, setLoading] = useState(true);

  // Selected Employee Modal
  const [selectedEmp, setSelectedEmp] = useState(null);
  const [selectedEmpFeedback, setSelectedEmpFeedback] = useState(null);
  const [modalTab, setModalTab] = useState("overview"); // 'overview' | 'retention'

  const fetchEmployees = async () => {
    setLoading(true);
    try {
      const response = await api.get("/hr/employees");
      setEmployees(response.data.employees || []);
      setFeedbacks(response.data.feedbacks || []);
    } catch (err) {
      console.error("Error fetching employees:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  const handleViewEmployee = (emp) => {
    setSelectedEmp(emp);
    setModalTab("overview");
    const foundFeed = feedbacks.find(
      (f) => f.studentId === emp._id || f.employeeId === emp._id || f.studentId?._id === emp._id || f.employeeId?._id === emp._id,
    );
    setSelectedEmpFeedback(foundFeed || null);
  };

  const handleOpenRetention = (emp) => {
    setSelectedEmp(emp);
    setModalTab("retention");
    const foundFeed = feedbacks.find(
      (f) => f.studentId === emp._id || f.employeeId === emp._id || f.studentId?._id === emp._id || f.employeeId?._id === emp._id,
    );
    setSelectedEmpFeedback(foundFeed || null);
  };

  const columns = [
    {
      header: "Student Name",
      cell: (row) => (
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-500 text-white font-bold text-xs flex items-center justify-center shadow-xs">
            {row.fullName?.charAt(0)?.toUpperCase()}
          </div>
          <div>
            <p className="font-bold text-slate-800">{row.fullName}</p>
            <p className="text-[11px] text-slate-400 capitalize">{row.role || "student"}</p>
          </div>
        </div>
      ),
    },
    {
      header: "Email",
      accessor: "email",
    },
    {
      header: "Student ID",
      cell: (row) => (
        <span className="font-mono text-xs font-bold text-slate-700 bg-slate-100 px-2.5 py-1 rounded border border-slate-200">
          {row.studentCode || row.employeeCode || "N/A"}
        </span>
      ),
    },
    {
      header: "Program / Cohort",
      cell: (row) => (
        <div className="text-xs">
          <p className="font-semibold text-slate-800">{row.course || "General Studies"}</p>
          <p className="text-[11px] text-slate-500">{row.yearOfStudy || "Year 1"} {row.department ? `· ${row.department}` : ""}</p>
        </div>
      ),
    },
    {
      header: "Institution",
      cell: (row) => (
        <span className="font-mono text-xs font-bold text-slate-700 uppercase">
          {row.institutionCode || row.companyCode || "N/A"}
        </span>
      ),
    },
    {
      header: "Survey Status",
      cell: (row) =>
        row.submitted ? (
          <StatusBadge type="submitted" label="Submitted" />
        ) : (
          <StatusBadge type="pending" label="Pending" />
        ),
    },
    {
      header: "Dropout Risk",
      cell: (row) => (
        <DropoutRiskBadge
          risk={
            !row.mlPrediction?.isAvailable
              ? "no_survey"
              : row.mlPrediction.outcome === "Yes"
              ? "high"
              : (row.mlPrediction.probability ?? 0) >= 0.35
              ? "watch"
              : "onTrack"
          }
          probability={row.mlPrediction?.probability}
        />
      ),
    },
    {
      header: "Action",
      align: "center",
      cell: (row) => (
        <div className="flex items-center justify-center gap-1.5">
          <button
            onClick={() => handleViewEmployee(row)}
            className="p-1.5 text-indigo-600 hover:text-indigo-800 hover:bg-indigo-50 rounded-xl transition-colors font-medium text-xs flex items-center gap-1 cursor-pointer"
            title="View Details"
          >
            <Eye className="w-4 h-4" />
            <span>Profile</span>
          </button>

          <button
            onClick={() => handleOpenRetention(row)}
            className="p-1.5 text-amber-700 hover:text-amber-900 hover:bg-amber-50 rounded-xl transition-colors font-semibold text-xs flex items-center gap-1 cursor-pointer"
            title="Open Academic Support Center"
          >
            <ShieldAlert className="w-4 h-4 text-amber-600" />
            <span>Support</span>
          </button>
        </div>
      ),
    },
  ];

  if (loading) {
    return <LoadingSpinner label="Loading student directory..." />;
  }

  // When a student is selected, render full-page details view
  if (selectedEmp) {
    return (
      <EmployeeDetailView
        employee={selectedEmp}
        feedback={selectedEmpFeedback}
        initialTab={modalTab}
        onBack={() => {
          setSelectedEmp(null);
          setSelectedEmpFeedback(null);
        }}
        onRefresh={fetchEmployees}
      />
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-bold text-slate-900">
            Student Directory
          </h2>
          <p className="text-xs text-slate-500">
            Manage and inspect enrolled students, academic courses, and retention indicators
          </p>
        </div>

        <button
          onClick={fetchEmployees}
          className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold text-xs rounded-xl transition-all flex items-center gap-2 cursor-pointer"
        >
          <RefreshCw className="w-3.5 h-3.5" />
          <span>Refresh Data</span>
        </button>
      </div>

      <DataTable
        columns={columns}
        data={employees}
        searchPlaceholder="Search by student name, ID, course, institution..."
        searchFields={["fullName", "email", "studentCode", "employeeCode", "course", "department", "institutionCode", "companyCode"]}
        filterOptions={[
          { label: "Survey Submitted", value: "SUBMITTED" },
          { label: "Survey Pending", value: "PENDING" },
        ]}
        onFilterChange={(row, filterVal) => {
          if (filterVal === "SUBMITTED") return row.submitted;
          if (filterVal === "PENDING") return !row.submitted;
          return true;
        }}
        emptyTitle="No students found"
        emptyDescription="No student records match your search query."
      />
    </div>
  );
};

export const StudentDirectory = EmployeeDirectory;
