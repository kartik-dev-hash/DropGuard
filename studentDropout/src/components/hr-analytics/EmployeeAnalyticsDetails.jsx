import React, { useEffect, useState } from "react";
import { getEmployeeAnalytics } from "../../services/analyticsService";
import {
  ArrowLeft,
  User,
  Mail,
  ShieldCheck,
  Calendar,
  MessageSquare,
  Sparkles,
  AlertTriangle,
  BrainCircuit,
} from "lucide-react";

export const EmployeeAnalyticsDetails = ({ employeeId, onBack }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDetails = async () => {
      try {
        setLoading(true);
        const result = await getEmployeeAnalytics(employeeId);
        setData(result);
      } catch (err) {
        console.error("Error fetching employee analytics details:", err);
        setError(err.response?.data?.message || "Failed to load individual employee analytics.");
      } finally {
        setLoading(false);
      }
    };

    if (employeeId) {
      fetchDetails();
    }
  }, [employeeId]);

  if (loading) {
    return (
      <div className="p-12 text-center bg-white rounded-2xl border border-slate-200">
        <div className="w-8 h-8 border-3 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto mb-3" />
        <p className="text-xs text-slate-500 font-medium">Loading individual student analytics...</p>
      </div>
    );
  }

  if (error || !data) {
    return (
      <div className="p-8 bg-white rounded-2xl border border-slate-200 text-center space-y-4">
        <p className="text-sm font-semibold text-rose-600">{error || "Student not found."}</p>
        <button
          onClick={onBack}
          className="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-xl"
        >
          Return to Overview
        </button>
      </div>
    );
  }

  const { employee, analytics, feedbackHistory, mlStatus } = data;
  const currentAvg = analytics?.currentAverages || {};
  const riskInfo = analytics?.experimentalSurveyRisk || {};

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Top Navigation & Header */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBack}
          className="px-3.5 py-2 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 rounded-xl text-xs font-semibold flex items-center gap-2 shadow-2xs transition-colors cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to All Students</span>
        </button>

        <span className="text-xs font-mono bg-slate-100 text-slate-600 px-3 py-1 rounded-full border border-slate-200">
          Student ID: {employee.studentCode || employee.employeeCode || employee._id}
        </span>
      </div>

      {/* Student Profile Header Card */}
      <div className="p-6 bg-white rounded-2xl border border-slate-200/80 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-6">
        <div className="flex items-center gap-4">
          <div className="w-14 h-14 rounded-2xl bg-gradient-to-tr from-indigo-600 to-purple-600 text-white font-bold text-xl flex items-center justify-center shadow-md">
            {employee.fullName?.charAt(0)?.toUpperCase()}
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-lg font-bold text-slate-900">{employee.fullName}</h2>
              <span className="font-mono text-xs font-semibold bg-slate-100 text-slate-700 px-2.5 py-0.5 rounded border border-slate-200">
                {employee.studentCode || employee.employeeCode || "N/A"}
              </span>
            </div>
            <div className="flex flex-wrap items-center gap-3 text-xs text-slate-500 mt-1">
              <span className="flex items-center gap-1">
                <Mail className="w-3.5 h-3.5" />
                {employee.email}
              </span>
              <span>•</span>
              <span className="flex items-center gap-1">
                <ShieldCheck className="w-3.5 h-3.5 text-indigo-500" />
                Institution: {employee.institutionCode || employee.companyCode}
              </span>
              {(employee.course || employee.yearOfStudy) && (
                <>
                  <span>•</span>
                  <span className="text-indigo-600 font-semibold">
                    {employee.course || "General"} · {employee.yearOfStudy || "Year 1"}
                  </span>
                </>
              )}
            </div>
          </div>
        </div>

        {/* Status Chip */}
        <div className="text-right">
          <span className="text-[11px] font-semibold text-slate-400 block uppercase tracking-wider">
            Survey Submissions
          </span>
          <span className="text-xl font-bold text-slate-800">
            {feedbackHistory.length} Recorded
          </span>
        </div>
      </div>

      {/* Ratings & Risk Assessment Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Card 1: Ratings Breakdown */}
        <div className="p-6 bg-white rounded-2xl border border-slate-200/80 shadow-xs space-y-4">
          <h3 className="text-sm font-bold text-slate-900 pb-3 border-b border-slate-100 flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-indigo-600" />
            <span>Latest Wellbeing Ratings Breakdown</span>
          </h3>

          <div className="space-y-3.5">
            {[
              { label: "Academic Engagement", val: currentAvg.academicEngagement ?? currentAvg.jobSatisfaction, color: "bg-indigo-500" },
              { label: "Support Satisfaction", val: currentAvg.supportSatisfaction ?? currentAvg.workEnvironment, color: "bg-emerald-500" },
              { label: "Stress Management", val: currentAvg.stressManagement ?? currentAvg.workLifeBalance, color: "bg-amber-500" },
              { label: "Sense of Belonging", val: currentAvg.belongingness ?? currentAvg.growth, color: "bg-purple-500" },
            ].map((item) => (
              <div key={item.label} className="space-y-1">
                <div className="flex justify-between text-xs font-semibold">
                  <span className="text-slate-600">{item.label}</span>
                  <span className="text-slate-800">★ {item.val || 0} / 5.0</span>
                </div>
                <div className="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden">
                  <div
                    className={`h-full rounded-full ${item.color}`}
                    style={{ width: `${((item.val || 0) / 5) * 100}%` }}
                  />
                </div>
              </div>
            ))}
          </div>

          <div className="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-bold">
            <span className="text-slate-700">Combined Average Score</span>
            <span className="text-base text-indigo-600">★ {currentAvg.overall || 0} / 5.0</span>
          </div>
        </div>

        {/* Card 2: ML Risk Prediction & Assessment */}
        <div className="p-6 bg-white rounded-2xl border border-slate-200/80 shadow-xs space-y-4">
          <h3 className="text-sm font-bold text-slate-900 pb-3 border-b border-slate-100 flex items-center gap-2">
            <BrainCircuit className="w-4 h-4 text-indigo-600" />
            <span>Dropout Risk Assessment</span>
          </h3>

          {/* PRIMARY: ML Prediction block — shown when model has run */}
          {analytics?.mlPrediction?.isAvailable ? (
            <div className={`p-4 rounded-xl border space-y-3 ${
              analytics.mlPrediction.outcome === "Yes"
                ? "bg-rose-50 border-rose-200"
                : analytics.mlPrediction.probability >= 0.35
                ? "bg-amber-50 border-amber-200"
                : "bg-emerald-50 border-emerald-200"
            }`}>
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className={`w-2.5 h-2.5 rounded-full flex-shrink-0 ${
                    analytics.mlPrediction.outcome === "Yes"
                      ? "bg-rose-500 animate-pulse"
                      : analytics.mlPrediction.probability >= 0.35
                      ? "bg-amber-500"
                      : "bg-emerald-500"
                  }`} />
                  <span className="text-xs font-bold text-slate-800">
                    ML Prediction: {
                      analytics.mlPrediction.outcome === "Yes"
                        ? "High Dropout Risk"
                        : analytics.mlPrediction.probability >= 0.35
                        ? "Moderate Risk – Monitor"
                        : "Low Risk – On Track"
                    }
                  </span>
                </div>
                <span className={`text-lg font-black ${
                  analytics.mlPrediction.outcome === "Yes"
                    ? "text-rose-600"
                    : analytics.mlPrediction.probability >= 0.35
                    ? "text-amber-600"
                    : "text-emerald-600"
                }`}>
                  {analytics.mlPrediction.probability != null
                    ? `${(analytics.mlPrediction.probability * 100).toFixed(1)}%`
                    : "—"}
                </span>
              </div>
              <div className="w-full bg-white/60 h-2.5 rounded-full overflow-hidden">
                <div
                  className={`h-full rounded-full transition-all ${
                    analytics.mlPrediction.outcome === "Yes"
                      ? "bg-rose-500"
                      : analytics.mlPrediction.probability >= 0.35
                      ? "bg-amber-500"
                      : "bg-emerald-500"
                  }`}
                  style={{ width: `${((analytics.mlPrediction.probability ?? 0) * 100).toFixed(1)}%` }}
                />
              </div>
              <p className="text-[10px] text-slate-500">
                Random Forest model v{analytics.mlPrediction.modelVersion || mlStatus?.modelVersion} · Trained on academic engagement, support satisfaction, stress management &amp; belongingness features.
              </p>
            </div>
          ) : (
            /* FALLBACK: Survey heuristic when ML hasn't run yet */
            <div className={`p-4 rounded-xl border space-y-2 ${
              riskInfo.level === "HIGH_RISK"
                ? "bg-rose-50 border-rose-200"
                : riskInfo.level === "NEEDS_ATTENTION"
                ? "bg-amber-50 border-amber-200"
                : riskInfo.level === "HEALTHY"
                ? "bg-slate-50 border-slate-200"
                : "bg-slate-50 border-slate-200"
            }`}>
              <div className="flex items-center justify-between">
                <span className="text-xs font-semibold text-slate-600">Survey-Based Indicator:</span>
                <span className={`px-2.5 py-0.5 rounded-full text-xs font-bold ${
                  riskInfo.level === "HIGH_RISK"
                    ? "bg-rose-100 text-rose-700"
                    : riskInfo.level === "NEEDS_ATTENTION"
                    ? "bg-amber-100 text-amber-700"
                    : riskInfo.level === "HEALTHY"
                    ? "bg-emerald-100 text-emerald-700"
                    : "bg-slate-200 text-slate-700"
                }`}>
                  {riskInfo.label || "No Feedback Yet"}
                </span>
              </div>
              <p className="text-[11px] text-slate-500 leading-relaxed">
                {mlStatus?.status === "TRAINED" && riskInfo.level && riskInfo.level !== "NO_FEEDBACK"
                  ? "ML model is trained. Click \"Refresh Analytics\" on the dashboard to generate a precise ML prediction for this student."
                  : riskInfo.level === "NO_FEEDBACK"
                  ? "No survey submitted yet. ML prediction will be generated once the student completes a survey."
                  : "Descriptive indicator based on survey satisfaction thresholds. Not a trained ML prediction."}
              </p>
            </div>
          )}

          {/* ML model status chip */}
          <div className="flex items-center gap-2 pt-1">
            <BrainCircuit className="w-3.5 h-3.5 text-indigo-500 flex-shrink-0" />
            <span className="text-[11px] text-slate-500">
              Random Forest Model:&nbsp;
              <span className={`font-semibold ${mlStatus?.status === "TRAINED" ? "text-emerald-600" : "text-slate-400"}`}>
                {mlStatus?.status === "TRAINED"
                  ? `Active (v${mlStatus.modelVersion})`
                  : "Not trained"}
              </span>
              {analytics?.mlPrediction?.isAvailable && (
                <span className="ml-2 text-emerald-600 font-semibold">✓ Prediction computed</span>
              )}
            </span>
          </div>
        </div>
      </div>

      {/* Historical Feedback Responses */}
      <div className="bg-white rounded-2xl border border-slate-200/80 shadow-xs p-6 space-y-4">
        <h3 className="text-sm font-bold text-slate-900 pb-3 border-b border-slate-100 flex items-center gap-2">
          <MessageSquare className="w-4 h-4 text-slate-600" />
          <span>Qualitative Survey Submissions ({feedbackHistory.length})</span>
        </h3>

        {feedbackHistory.length === 0 ? (
          <p className="text-xs text-slate-400 py-6 text-center">No survey responses recorded yet for this student.</p>
        ) : (
          <div className="space-y-4">
            {feedbackHistory.map((item, idx) => (
              <div key={item._id || idx} className="p-4 rounded-xl bg-slate-50 border border-slate-200/80 space-y-3">
                <div className="flex items-center justify-between text-xs text-slate-500 pb-2 border-b border-slate-200">
                  <span className="font-semibold text-slate-700">Submission #{idx + 1}</span>
                  <span className="flex items-center gap-1 font-mono">
                    <Calendar className="w-3.5 h-3.5" />
                    {new Date(item.submittedAt || item.createdAt).toLocaleDateString()}
                  </span>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
                  <div>
                    <span className="font-semibold text-slate-700 block">Counselor / Teacher Relationship:</span>
                    <p className="text-slate-600 mt-0.5">{item.counselorFeedback || item.manager || "N/A"}</p>
                  </div>
                  <div>
                    <span className="font-semibold text-slate-700 block">Liked Most:</span>
                    <p className="text-slate-600 mt-0.5">{item.likedMost || "N/A"}</p>
                  </div>
                  <div>
                    <span className="font-semibold text-slate-700 block">Areas for Academic Improvement:</span>
                    <p className="text-slate-600 mt-0.5">{item.improvement || "N/A"}</p>
                  </div>
                  <div>
                    <span className="font-semibold text-slate-700 block">Additional Comments:</span>
                    <p className="text-slate-600 mt-0.5">{item.additionalComments || item.comments || "N/A"}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export const StudentAnalyticsDetails = EmployeeAnalyticsDetails;
