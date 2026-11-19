import React, { useEffect, useState } from "react";
import api from "../../api/client";
import { Card } from "../../components/common/Card";
import { StatusBadge } from "../../components/common/Badge";
import { LoadingSpinner } from "../../components/common/LoadingSpinner";
import { EmptyState } from "../../components/common/EmptyState";
import { History, CheckCircle2, ShieldCheck } from "lucide-react";

export const FeedbackHistory = () => {
  const [statusData, setStatusData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await api.get("/predict/status");
        setStatusData(response.data);
      } catch (err) {
        console.error("Error fetching survey status history:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchStatus();
  }, []);

  if (loading) {
    return <LoadingSpinner label="Loading survey history..." />;
  }

  const isSubmitted = statusData?.submitted || false;

  return (
    <div className="max-w-4xl space-y-6">
      <div>
        <h2 className="text-xl font-bold text-slate-900">Academic Wellbeing Survey History</h2>
        <p className="text-xs text-slate-500">Track your past academic wellbeing survey submissions</p>
      </div>

      {!isSubmitted ? (
        <EmptyState
          icon={History}
          title="No Survey Submissions Logged"
          description="You have not submitted an academic wellbeing survey yet. Once submitted, your survey status log will appear here."
        />
      ) : (
        <Card>
          <div className="space-y-4">
            <div className="p-5 bg-slate-50 rounded-2xl border border-slate-100 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-2xl bg-emerald-100 text-emerald-600 flex items-center justify-center flex-shrink-0">
                  <CheckCircle2 className="w-6 h-6" />
                </div>
                <div>
                  <h4 className="text-base font-bold text-slate-800">Academic Wellbeing Check-in</h4>
                  <p className="text-xs text-slate-500 mt-0.5">{statusData?.message || "Submitted successfully"}</p>
                </div>
              </div>

              <StatusBadge type="submitted" label="Recorded" />
            </div>

            <div className="p-4 bg-indigo-50/50 rounded-2xl border border-indigo-100/70 text-xs text-indigo-900 flex items-center gap-2">
              <ShieldCheck className="w-4 h-4 text-indigo-600 flex-shrink-0" />
              <span>Your responses are securely reviewed by academic counselors to provide timely academic guidance, mentoring, and wellbeing support.</span>
            </div>
          </div>
        </Card>
      )}
    </div>
  );
};

export const SurveyHistory = FeedbackHistory;
