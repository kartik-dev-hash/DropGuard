import React from "react";

export const StatusBadge = ({ type, label }) => {
  const styles = {
    submitted: "bg-emerald-50 text-emerald-700 border-emerald-200",
    pending: "bg-amber-50 text-amber-700 border-amber-200",
    highRisk: "bg-rose-50 text-rose-700 border-rose-200",
    mediumRisk: "bg-orange-50 text-orange-700 border-orange-200",
    watch: "bg-amber-50 text-amber-700 border-amber-200",
    lowRisk: "bg-blue-50 text-blue-700 border-blue-200",
    healthy: "bg-emerald-50 text-emerald-700 border-emerald-200",
    onTrack: "bg-emerald-50 text-emerald-700 border-emerald-200",
    hr: "bg-indigo-50 text-indigo-700 border-indigo-200",
    counselor: "bg-indigo-50 text-indigo-700 border-indigo-200",
    employee: "bg-slate-100 text-slate-700 border-slate-200",
    student: "bg-slate-100 text-slate-700 border-slate-200",
    default: "bg-slate-50 text-slate-600 border-slate-200",
  };

  const badgeStyle = styles[type] || styles.default;

  return (
    <span
      className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold border ${badgeStyle} transition-colors`}
    >
      <span
        className={`w-1.5 h-1.5 rounded-full ${
          type === "submitted" || type === "healthy" || type === "onTrack"
            ? "bg-emerald-500 animate-pulse"
            : type === "pending" || type === "mediumRisk" || type === "watch"
            ? "bg-amber-500"
            : type === "highRisk"
            ? "bg-rose-500 animate-ping"
            : "bg-current"
        }`}
      />
      {label}
    </span>
  );
};

export const DropoutRiskBadge = ({ riskLevel, risk, probability }) => {
  const effectiveRisk = riskLevel || risk;
  const isHigh =
    effectiveRisk === "HIGH_RISK" ||
    effectiveRisk === "high" ||
    (probability != null && probability >= 0.5);
  const isWatch =
    effectiveRisk === "NEEDS_ATTENTION" ||
    effectiveRisk === "watch" ||
    (probability != null && probability >= 0.35 && probability < 0.5);
  const isNoFeedback =
    effectiveRisk === "NO_FEEDBACK" ||
    effectiveRisk === "no_survey" ||
    (effectiveRisk == null && probability == null);

  if (isHigh) {
    return (
      <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-rose-50 text-rose-700 border border-rose-200">
        <span className="text-xs leading-none">🔴</span>
        <span>High Risk</span>
      </span>
    );
  }

  if (isWatch) {
    return (
      <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-amber-50 text-amber-700 border border-amber-200">
        <span className="text-xs leading-none">🟡</span>
        <span>Watch</span>
      </span>
    );
  }

  if (isNoFeedback) {
    return (
      <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-slate-50 text-slate-500 border border-slate-200">
        <span className="text-xs leading-none">⚪</span>
        <span>No Survey</span>
      </span>
    );
  }

  return (
    <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
      <span className="text-xs leading-none">🟢</span>
      <span>On Track</span>
    </span>
  );
};
