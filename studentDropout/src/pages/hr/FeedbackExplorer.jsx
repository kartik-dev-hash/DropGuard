import React, { useEffect, useState } from "react";
import api from "../../api/client";
import { DataTable } from "../../components/common/DataTable";
import { RatingStars } from "../../components/common/RatingStars";
import { LoadingSpinner } from "../../components/common/LoadingSpinner";
import { Eye } from "lucide-react";
import { EmployeeDetailView } from "../../components/hr-analytics/EmployeeDetailView";
import { DropoutRiskBadge } from "../../components/common/Badge";

export const FeedbackExplorer = () => {
  const [employees, setEmployees] = useState([]);
  const [feedbacks, setFeedbacks] = useState([]);
  const [loading, setLoading] = useState(true);

  const [selectedItem, setSelectedItem] = useState(null); // { emp, feed }

  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await api.get("/hr/employees");
      setEmployees(response.data.employees || []);
      setFeedbacks(response.data.feedbacks || []);
    } catch (err) {
      console.error("Error fetching survey list:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  // Merge submitted feedbacks with student details
  const feedbackList = feedbacks.map((feed) => {
    const studentRefId = feed.studentId?._id || feed.studentId || feed.employeeId?._id || feed.employeeId;
    const emp = employees.find((e) => e._id === studentRefId);

    const academicEngagement = feed.academicEngagement ?? feed.jobSatisfaction ?? 0;
    const supportSatisfaction = feed.supportSatisfaction ?? feed.workEnvironment ?? 0;
    const stressManagement = feed.stressManagement ?? feed.workLifeBalance ?? 0;
    const belongingness = feed.belongingness ?? feed.growth ?? 0;

    const avgRating = (
      (academicEngagement + supportSatisfaction + stressManagement + belongingness) / 4
    ).toFixed(1);

    return {
      ...feed,
      student: emp,
      studentName: emp?.fullName || "Student",
      studentEmail: emp?.email || "",
      studentCode: emp?.studentCode || emp?.employeeCode || "N/A",
      course: emp?.course || "",
      yearOfStudy: emp?.yearOfStudy || "",
      mlPrediction: emp?.mlPrediction,
      academicEngagement,
      supportSatisfaction,
      stressManagement,
      belongingness,
      avgRating,
    };
  });

  const columns = [
    {
      header: "Student",
      cell: (row) => (
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-indigo-500 to-purple-500 text-white font-bold text-xs flex items-center justify-center">
            {row.studentName?.charAt(0)?.toUpperCase()}
          </div>
          <div>
            <p className="font-bold text-slate-800">{row.studentName}</p>
            <p className="text-[11px] text-slate-400">{row.studentEmail}</p>
            {row.course && (
              <p className="text-[10px] text-indigo-600 font-medium">
                {row.course} {row.yearOfStudy ? `• ${row.yearOfStudy}` : ""}
              </p>
            )}
          </div>
        </div>
      ),
    },
    {
      header: "Student ID",
      cell: (row) => (
        <span className="font-mono text-xs font-bold text-slate-700 bg-slate-100 px-2.5 py-1 rounded border border-slate-200">
          {row.studentCode}
        </span>
      ),
    },
    {
      header: "Engagement",
      cell: (row) => <RatingStars value={row.academicEngagement} size="sm" showLabel={false} disabled />,
    },
    {
      header: "Support",
      cell: (row) => <RatingStars value={row.supportSatisfaction} size="sm" showLabel={false} disabled />,
    },
    {
      header: "Stress Mgmt",
      cell: (row) => <RatingStars value={row.stressManagement} size="sm" showLabel={false} disabled />,
    },
    {
      header: "Belonging",
      cell: (row) => <RatingStars value={row.belongingness} size="sm" showLabel={false} disabled />,
    },
    {
      header: "Average Score",
      cell: (row) => (
        <span className="font-extrabold text-xs text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-full border border-indigo-100">
          ★ {row.avgRating} / 5
        </span>
      ),
    },
    {
      header: "Dropout Risk",
      cell: (row) => {
        const ml = row.mlPrediction;
        if (!ml?.isAvailable) {
          return <DropoutRiskBadge risk="no_survey" />;
        }
        const isHigh = ml.outcome === "Yes" || ml.probability >= 0.6;
        if (isHigh) {
          return <DropoutRiskBadge risk="high" probability={ml.probability} />;
        }
        const prob = ml.probability ?? 0;
        if (prob >= 0.35) {
          return <DropoutRiskBadge risk="watch" probability={ml.probability} />;
        }
        return <DropoutRiskBadge risk="onTrack" probability={ml.probability} />;
      },
    },
    {
      header: "Action",
      align: "center",
      cell: (row) => (
        <button
          onClick={() => setSelectedItem(row)}
          className="p-2 text-indigo-600 hover:text-indigo-800 hover:bg-indigo-50 rounded-xl transition-colors font-medium text-xs flex items-center gap-1 mx-auto cursor-pointer"
        >
          <Eye className="w-4 h-4" />
          <span>View Response</span>
        </button>
      ),
    },
  ];

  if (loading) {
    return <LoadingSpinner label="Loading survey explorer..." />;
  }

  // When a survey response is selected, render full-page details view
  if (selectedItem) {
    const studentObj = selectedItem.student || {
      _id: selectedItem.studentId?._id || selectedItem.studentId || selectedItem.employeeId?._id || selectedItem.employeeId,
      fullName: selectedItem.studentName,
      email: selectedItem.studentEmail,
      studentCode: selectedItem.studentCode,
      employeeCode: selectedItem.studentCode,
      course: selectedItem.course,
      yearOfStudy: selectedItem.yearOfStudy,
      mlPrediction: selectedItem.mlPrediction,
      institutionCode: selectedItem.institutionCode || selectedItem.companyCode,
      companyCode: selectedItem.companyCode,
      role: "Student",
    };

    return (
      <EmployeeDetailView
        employee={studentObj}
        feedback={selectedItem}
        initialTab="overview"
        backLabel="Back to Survey Explorer"
        onBack={() => setSelectedItem(null)}
        onRefresh={fetchData}
      />
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900">Student Survey Explorer</h2>
        <p className="text-xs text-slate-500">Review academic wellbeing ratings and written survey responses</p>
      </div>

      <DataTable
        columns={columns}
        data={feedbackList}
        searchPlaceholder="Search surveys by student name, ID, or course..."
        searchFields={["studentName", "studentEmail", "studentCode", "course", "counselorFeedback", "manager"]}
        emptyTitle="No Survey Submissions Found"
        emptyDescription="None of your enrolled students have submitted an academic wellbeing survey yet."
      />
    </div>
  );
};

export const SurveyExplorer = FeedbackExplorer;
