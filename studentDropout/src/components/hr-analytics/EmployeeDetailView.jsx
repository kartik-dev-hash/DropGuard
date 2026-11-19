import React, { useState } from "react";
import { RatingStars } from "../common/RatingStars";
import { StatusBadge } from "../common/Badge";
import { RetentionActionCenter } from "./RetentionActionCenter";
import {
  ArrowLeft,
  Users,
  Clock,
  ShieldAlert,
  Mail,
  Building,
  User,
  Sparkles,
} from "lucide-react";

export const EmployeeDetailView = ({
  employee,
  feedback,
  initialTab = "overview",
  backLabel = "Back to Student Directory",
  onBack,
  onRefresh,
}) => {
  const [activeTab, setActiveTab] = useState(initialTab);

  if (!employee) return null;

  const engagement = feedback?.academicEngagement ?? feedback?.jobSatisfaction ?? 0;
  const support = feedback?.supportSatisfaction ?? feedback?.workEnvironment ?? 0;
  const stress = feedback?.stressManagement ?? feedback?.workLifeBalance ?? 0;
  const belong = feedback?.belongingness ?? feedback?.growth ?? 0;

  const avgRating = feedback
    ? ((engagement + support + stress + belong) / 4).toFixed(1)
    : null;

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Top Navigation & Breadcrumb */}
      <div className="flex items-center justify-between">
        <button
          type="button"
          onClick={onBack}
          className="px-4 py-2 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 rounded-xl text-xs font-semibold flex items-center gap-2 shadow-2xs transition-all cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>{backLabel}</span>
        </button>

        <span className="font-mono text-xs font-bold text-slate-600 bg-slate-100 px-3 py-1 rounded-full border border-slate-200">
          Student ID: {employee.studentCode || employee.employeeCode || employee._id}
        </span>
      </div>

      {/* Main Profile Header Card */}
      <div className="p-6 bg-white rounded-3xl border border-slate-200 shadow-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div className="flex items-center gap-4">
          <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-indigo-500 to-purple-600 text-white font-extrabold text-2xl flex items-center justify-center shadow-md">
            {employee.fullName?.charAt(0)?.toUpperCase()}
          </div>
          <div>
            <div className="flex items-center gap-2.5 flex-wrap">
              <h2 className="text-xl font-bold text-slate-900">{employee.fullName}</h2>
              <span className="font-mono text-xs font-bold text-indigo-700 bg-indigo-50 px-2.5 py-0.5 rounded-lg border border-indigo-200">
                {employee.studentCode || employee.employeeCode || "N/A"}
              </span>
              <span className="text-xs text-slate-500 font-medium">({employee.role || "student"})</span>
            </div>
            <div className="flex flex-wrap items-center gap-3 text-xs text-slate-500 mt-2">
              <span className="flex items-center gap-1.5">
                <Mail className="w-3.5 h-3.5 text-slate-400" />
                {employee.email}
              </span>
              <span className="flex items-center gap-1.5">
                <Building className="w-3.5 h-3.5 text-slate-400" />
                Institution: <strong className="text-slate-700 uppercase">{employee.institutionCode || employee.companyCode}</strong>
              </span>
              {(employee.course || employee.yearOfStudy) && (
                <span className="bg-indigo-50 text-indigo-700 px-2.5 py-0.5 rounded-md font-semibold text-[11px] border border-indigo-100">
                  {employee.course || "General"} · {employee.yearOfStudy || "Year 1"}
                </span>
              )}
              {employee.department && (
                <span className="bg-slate-100 text-slate-700 px-2.5 py-0.5 rounded-md font-medium text-[11px] border border-slate-200">
                  Dept: {employee.department}
                </span>
              )}
            </div>
          </div>
        </div>

        {/* Tab Navigation Buttons */}
        <div className="flex items-center gap-2 p-1 bg-slate-100 rounded-2xl border border-slate-200/80">
          <button
            type="button"
            onClick={() => setActiveTab("overview")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
              activeTab === "overview"
                ? "bg-white text-indigo-700 shadow-sm"
                : "text-slate-600 hover:text-slate-900"
            }`}
          >
            Wellbeing & Profile
          </button>

          <button
            type="button"
            onClick={() => setActiveTab("retention")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 cursor-pointer ${
              activeTab === "retention"
                ? "bg-indigo-600 text-white shadow-sm"
                : "text-slate-600 hover:text-slate-900"
            }`}
          >
            <ShieldAlert className="w-3.5 h-3.5" />
            <span>Academic Support Center</span>
          </button>
        </div>
      </div>

      {/* Tab 1: Overview, Ratings & Feedback */}
      {activeTab === "overview" && (
        <div className="space-y-6">
          {/* ML Dropout Risk Banner */}
          {(() => {
            const ml = employee.mlPrediction;
            if (!ml?.isAvailable) {
              return (
                <div className="p-5 bg-slate-50 rounded-2xl border border-slate-200 flex items-center justify-between gap-4">
                  <div className="flex items-center gap-3.5">
                    <span className="w-3 h-3 rounded-full bg-slate-400 flex-shrink-0" />
                    <div>
                      <p className="text-sm font-bold text-slate-700">ML Dropout Risk: Not Evaluated</p>
                      <p className="text-xs text-slate-500 mt-0.5">
                        Run Analytics Refresh on the Dropout Analytics dashboard to generate supervised risk predictions.
                      </p>
                    </div>
                  </div>
                  <span className="text-xs font-mono bg-slate-200 text-slate-600 px-3 py-1 rounded-full font-bold">
                    UNRANKED
                  </span>
                </div>
              );
            }
            const isHigh = ml.outcome === "Yes";
            const prob = ml.probability != null ? `${(ml.probability * 100).toFixed(1)}%` : "—";
            const label = isHigh ? "High Risk" : ml.probability >= 0.35 ? "Watch / Medium Risk" : "On Track / Low Risk";
            const colors = isHigh
              ? "bg-rose-50 border-rose-200 text-rose-800"
              : ml.probability >= 0.35
              ? "bg-amber-50 border-amber-200 text-amber-800"
              : "bg-emerald-50 border-emerald-200 text-emerald-800";
            const dotColor = isHigh ? "bg-rose-500" : ml.probability >= 0.35 ? "bg-amber-500" : "bg-emerald-500";
            return (
              <div className={`p-5 rounded-2xl border flex items-center justify-between gap-4 ${colors}`}>
                <div className="flex items-center gap-3.5">
                  <span className={`w-3 h-3 rounded-full flex-shrink-0 ${dotColor} ${isHigh ? "animate-pulse" : ""}`} />
                  <div>
                    <p className="text-sm font-bold">ML Dropout Risk Assessment: {label}</p>
                    <p className="text-xs opacity-75 mt-0.5">
                      Model v{ml.modelVersion || "1.0.0"} · Calculated Probability: <strong>{prob}</strong> · This is a statistical estimate based on academic wellbeing sentiment.
                    </p>
                  </div>
                </div>
                <div className="text-right">
                  <span className="text-2xl font-extrabold">{prob}</span>
                  <span className="block text-[10px] opacity-75 uppercase font-bold tracking-wider">Dropout Prob.</span>
                </div>
              </div>
            );
          })()}

          {/* Feedback Section */}
          {!feedback ? (
            <div className="p-10 bg-white rounded-3xl border border-slate-200 text-center space-y-3 shadow-xs">
              <Clock className="w-10 h-10 text-amber-500 mx-auto" />
              <h4 className="text-base font-bold text-slate-800">Wellbeing Survey Not Submitted Yet</h4>
              <p className="text-xs text-slate-500 max-w-md mx-auto">
                This student has not completed their academic wellbeing survey for the current academic period.
              </p>
            </div>
          ) : (
            <div className="space-y-6">
              {/* Submitted Ratings Grid */}
              <div className="p-6 bg-white rounded-3xl border border-slate-200 space-y-5 shadow-xs">
                <div className="flex items-center justify-between pb-3 border-b border-slate-100 flex-wrap gap-2">
                  <div>
                    <h3 className="text-base font-bold text-slate-900">Academic Dimension Ratings</h3>
                    <p className="text-xs text-slate-500">Student ratings on a 1 to 5 scale</p>
                  </div>
                  <div className="flex items-center gap-2.5">
                    {avgRating && (
                      <span className="font-extrabold text-xs text-indigo-700 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-200">
                        ★ {avgRating} / 5.0 Overall
                      </span>
                    )}
                    <StatusBadge type="submitted" label="Verified Survey" />
                  </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                  <div className="p-4 bg-slate-50/80 rounded-2xl border border-slate-100 space-y-1.5">
                    <span className="text-xs font-semibold text-slate-500 block">Academic Engagement</span>
                    <RatingStars value={engagement} disabled />
                  </div>

                  <div className="p-4 bg-slate-50/80 rounded-2xl border border-slate-100 space-y-1.5">
                    <span className="text-xs font-semibold text-slate-500 block">Support Satisfaction</span>
                    <RatingStars value={support} disabled />
                  </div>

                  <div className="p-4 bg-slate-50/80 rounded-2xl border border-slate-100 space-y-1.5">
                    <span className="text-xs font-semibold text-slate-500 block">Stress Management</span>
                    <RatingStars value={stress} disabled />
                  </div>

                  <div className="p-4 bg-slate-50/80 rounded-2xl border border-slate-100 space-y-1.5">
                    <span className="text-xs font-semibold text-slate-500 block">Sense of Belonging</span>
                    <RatingStars value={belong} disabled />
                  </div>
                </div>
              </div>

              {/* Qualitative Written Responses */}
              <div className="p-6 bg-white rounded-3xl border border-slate-200 space-y-5 shadow-xs">
                <div>
                  <h3 className="text-base font-bold text-slate-900">Qualitative Statements & Comments</h3>
                  <p className="text-xs text-slate-500">Detailed subjective responses provided by the student</p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                  <div className="p-4 bg-slate-50/80 rounded-2xl border border-slate-100 space-y-1">
                    <strong className="block text-slate-800 font-bold">Counselor & Academic Support Sentiment</strong>
                    <p className="text-slate-600 leading-relaxed">{feedback.counselorFeedback || feedback.manager || "No response provided."}</p>
                  </div>

                  <div className="p-4 bg-slate-50/80 rounded-2xl border border-slate-100 space-y-1">
                    <strong className="block text-slate-800 font-bold">What the Student Liked Most</strong>
                    <p className="text-slate-600 leading-relaxed">{feedback.likedMost || "No response provided."}</p>
                  </div>

                  <div className="p-4 bg-slate-50/80 rounded-2xl border border-slate-100 space-y-1">
                    <strong className="block text-slate-800 font-bold">Suggested Academic Improvements</strong>
                    <p className="text-slate-600 leading-relaxed">{feedback.improvement || "No response provided."}</p>
                  </div>

                  <div className="p-4 bg-slate-50/80 rounded-2xl border border-slate-100 space-y-1">
                    <strong className="block text-slate-800 font-bold">Additional Comments & Observations</strong>
                    <p className="text-slate-600 leading-relaxed">{feedback.additionalComments || feedback.comments || "No additional comments."}</p>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Tab 2: Retention Action Center */}
      {activeTab === "retention" && (
        <RetentionActionCenter
          employee={employee}
          feedback={feedback}
          mlPrediction={employee.mlPrediction}
          onActionUpdated={onRefresh}
        />
      )}
    </div>
  );
};

export const StudentDetailView = EmployeeDetailView;
