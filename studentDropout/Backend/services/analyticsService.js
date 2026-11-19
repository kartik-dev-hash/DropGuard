import User from "../models/User.js";
import EmployeeFeedback from "../models/feedback.js";
import CompanyAnalytics from "../models/CompanyAnalytics.js";
import EmployeeAnalytics from "../models/EmployeeAnalytics.js";
import { getModelStatus, predictOutcome } from "./mlService.js";

/**
 * Calculate distribution frequencies for rating values (1 to 5)
 */
function calculateDistribution(scores) {
  const dist = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };
  scores.forEach((s) => {
    if (typeof s === "number" && s >= 1 && s <= 5) {
      const rounded = Math.round(s);
      dist[rounded] = (dist[rounded] || 0) + 1;
    }
  });
  return dist;
}

/**
 * Generate or refresh company-level and employee-level analytics
 * Strictly scoped by companyCode to prevent cross-company data leakage
 */
export async function refreshCompanyAnalytics(companyCode) {
  const sanitizedCompanyCode = companyCode.toUpperCase().trim();

  // 1. Fetch authorized company/institution students
  const employees = await User.find({
    companyCode: sanitizedCompanyCode,
    role: { $in: ["employee", "student"] },
  })
    .select("_id fullName email employeeCode studentCode companyCode institutionCode course yearOfStudy department assignedCounselor assignedHR")
    .lean();

  const totalEmployeesInCompany = employees.length;
  const employeeIds = employees.map((e) => e._id);

  // 2. Fetch feedback submissions for these students only
  const feedbacks = await EmployeeFeedback.find({
    employeeId: { $in: employeeIds },
  }).lean();

  const totalFeedbackSubmissions = feedbacks.length;

  // Track unique students represented in feedback
  const uniqueEmployeeSet = new Set(
    feedbacks.map((f) => f.employeeId.toString()),
  );
  const uniqueEmployeesRepresented = uniqueEmployeeSet.size;

  // 3. Compute institution aggregate ratings
  const aeScores = [];
  const ssScores = [];
  const smScores = [];
  const blScores = [];

  const counselorDist = {};
  const improvementThemesMap = {};
  let totalCommentsCount = 0;

  feedbacks.forEach((f) => {
    const ae = typeof f.academicEngagement === "number" ? f.academicEngagement : f.jobSatisfaction;
    const ss = typeof f.supportSatisfaction === "number" ? f.supportSatisfaction : f.workEnvironment;
    const sm = typeof f.stressManagement === "number" ? f.stressManagement : f.workLifeBalance;
    const bl = typeof f.belongingness === "number" ? f.belongingness : f.growth;
    const cf = f.counselorFeedback || f.manager;

    if (typeof ae === "number") aeScores.push(ae);
    if (typeof ss === "number") ssScores.push(ss);
    if (typeof sm === "number") smScores.push(sm);
    if (typeof bl === "number") blScores.push(bl);

    if (cf && typeof cf === "string") {
      const cleanCf = cf.trim();
      counselorDist[cleanCf] = (counselorDist[cleanCf] || 0) + 1;
    }

    // Inspect improvement text
    if (f.improvement && typeof f.improvement === "string") {
      const cleanImp = f.improvement.trim().toLowerCase();
      if (cleanImp && cleanImp !== "none" && cleanImp !== "no") {
        totalCommentsCount++;
        improvementThemesMap[cleanImp] =
          (improvementThemesMap[cleanImp] || 0) + 1;
      }
    }
  });

  const topImprovementThemes = Object.entries(improvementThemesMap)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([theme, count]) => ({ theme, count }));

  const avg = (arr) =>
    arr.length
      ? Number((arr.reduce((a, b) => a + b, 0) / arr.length).toFixed(2))
      : 0;

  const averages = {
    academicEngagement: avg(aeScores),
    supportSatisfaction: avg(ssScores),
    stressManagement: avg(smScores),
    belongingness: avg(blScores),
    // Backward-compatible keys
    jobSatisfaction: avg(aeScores),
    workEnvironment: avg(ssScores),
    workLifeBalance: avg(smScores),
    growth: avg(blScores),
    overall: avg([...aeScores, ...ssScores, ...smScores, ...blScores]),
  };

  // Aggregate actual feedback submissions by calendar date for time-series charts
  const dateMap = {};
  feedbacks.forEach((f) => {
    const rawDate = f.submittedAt || f.createdAt;
    if (rawDate) {
      const d = new Date(rawDate);
      const dateStr = d.toISOString().split("T")[0]; // YYYY-MM-DD
      if (!dateMap[dateStr]) {
        dateMap[dateStr] = {
          date: dateStr,
          timestamp: d,
          ae: [],
          ss: [],
          sm: [],
          bl: [],
        };
      }
      const ae = typeof f.academicEngagement === "number" ? f.academicEngagement : f.jobSatisfaction;
      const ss = typeof f.supportSatisfaction === "number" ? f.supportSatisfaction : f.workEnvironment;
      const sm = typeof f.stressManagement === "number" ? f.stressManagement : f.workLifeBalance;
      const bl = typeof f.belongingness === "number" ? f.belongingness : f.growth;

      if (typeof ae === "number") dateMap[dateStr].ae.push(ae);
      if (typeof ss === "number") dateMap[dateStr].ss.push(ss);
      if (typeof sm === "number") dateMap[dateStr].sm.push(sm);
      if (typeof bl === "number") dateMap[dateStr].bl.push(bl);
    }
  });

  const timelineTrends = Object.values(dateMap)
    .sort((a, b) => new Date(a.date) - new Date(b.date))
    .map((item) => {
      const allScores = [...item.ae, ...item.ss, ...item.sm, ...item.bl];
      return {
        date: item.date,
        timestamp: item.timestamp,
        count: item.ae.length,
        avgAcademicEngagement: avg(item.ae),
        avgSupportSatisfaction: avg(item.ss),
        avgStressManagement: avg(item.sm),
        avgBelongingness: avg(item.bl),
        // Backward-compatible keys
        avgJobSatisfaction: avg(item.ae),
        avgWorkEnvironment: avg(item.ss),
        avgWorkLifeBalance: avg(item.sm),
        avgGrowth: avg(item.bl),
        avgOverall: avg(allScores),
      };
    });

  const distributions = {
    academicEngagement: calculateDistribution(aeScores),
    supportSatisfaction: calculateDistribution(ssScores),
    stressManagement: calculateDistribution(smScores),
    belongingness: calculateDistribution(blScores),
    counselorFeedback: counselorDist,
    // Backward-compatible keys
    jobSatisfaction: calculateDistribution(aeScores),
    workEnvironment: calculateDistribution(ssScores),
    workLifeBalance: calculateDistribution(smScores),
    growth: calculateDistribution(blScores),
    manager: counselorDist,
  };

  // 4. Check ML Model status and compute per-employee analytics
  const mlStatus = await getModelStatus();

  let highRiskCount = 0;
  let needsAttentionCount = 0;
  let healthyCount = 0;
  let unsubmittedCount = 0;

  for (const emp of employees) {
    const empFeedbacks = feedbacks.filter(
      (f) => f.employeeId.toString() === emp._id.toString(),
    );

    if (empFeedbacks.length === 0) {
      unsubmittedCount++;
      await EmployeeAnalytics.findOneAndUpdate(
        { employeeId: emp._id, companyCode: sanitizedCompanyCode },
        {
          employeeId: emp._id,
          companyCode: sanitizedCompanyCode,
          generatedAt: new Date(),
          totalSubmissions: 0,
          latestSubmissionDate: null,
          currentAverages: {
            jobSatisfaction: 0,
            workEnvironment: 0,
            workLifeBalance: 0,
            growth: 0,
            overall: 0,
          },
          experimentalSurveyRisk: {
            level: "NO_FEEDBACK",
            label: "Pending Survey Response",
            score: null,
            disclaimer: "No feedback submitted yet.",
          },
          mlPrediction: { isAvailable: false },
        },
        { upsert: true, returnDocument: "after" },
      );
      continue;
    }

    const latest = empFeedbacks[empFeedbacks.length - 1];
    const aeVal = typeof latest.academicEngagement === "number" ? latest.academicEngagement : latest.jobSatisfaction;
    const ssVal = typeof latest.supportSatisfaction === "number" ? latest.supportSatisfaction : latest.workEnvironment;
    const smVal = typeof latest.stressManagement === "number" ? latest.stressManagement : latest.workLifeBalance;
    const blVal = typeof latest.belongingness === "number" ? latest.belongingness : latest.growth;

    const scores = [aeVal, ssVal, smVal, blVal].filter((s) => typeof s === "number");
    const empAvg = scores.length
      ? Number((scores.reduce((a, b) => a + b, 0) / scores.length).toFixed(2))
      : 0;

    let riskLevel = "HEALTHY";
    let riskLabel = "On Track";

    if (empAvg <= 2.5) {
      riskLevel = "HIGH_RISK";
      riskLabel = "High Dropout Risk";
      highRiskCount++;
    } else if (empAvg <= 3.5) {
      riskLevel = "NEEDS_ATTENTION";
      riskLabel = "Needs Academic Support";
      needsAttentionCount++;
    } else {
      healthyCount++;
    }

    // Run ML model inference if trained
    let empMlPrediction = {
      isAvailable: false,
      outcome: null,
      probability: null,
    };

    if (
      mlStatus.isReadyForInference &&
      typeof aeVal === "number"
    ) {
      try {
        const inf = await predictOutcome({
          academicEngagement: Math.min(4, Math.max(1, Math.round(aeVal))),
          supportSatisfaction: Math.min(4, Math.max(1, Math.round(ssVal || 3))),
          stressManagement: Math.min(4, Math.max(1, Math.round(smVal || 3))),
          belongingness: Math.min(4, Math.max(1, Math.round(blVal || 3))),
        });
        if (inf && inf.isAvailable) {
          empMlPrediction = {
            isAvailable: true,
            outcome: inf.outcome,
            probability: inf.probability,
            modelVersion: inf.modelVersion,
            predictionTimestamp: new Date(),
          };
        }
      } catch (infErr) {
        // Fall back gracefully if inference fails
      }
    }

    await EmployeeAnalytics.findOneAndUpdate(
      { employeeId: emp._id, companyCode: sanitizedCompanyCode },
      {
        employeeId: emp._id,
        companyCode: sanitizedCompanyCode,
        generatedAt: new Date(),
        totalSubmissions: empFeedbacks.length,
        latestSubmissionDate:
          latest.submittedAt || latest.createdAt || new Date(),
        currentAverages: {
          academicEngagement: aeVal || 0,
          supportSatisfaction: ssVal || 0,
          stressManagement: smVal || 0,
          belongingness: blVal || 0,
          jobSatisfaction: aeVal || 0,
          workEnvironment: ssVal || 0,
          workLifeBalance: smVal || 0,
          growth: blVal || 0,
          overall: empAvg,
        },
        experimentalSurveyRisk: {
          level: riskLevel,
          label: riskLabel,
          score: empAvg,
          disclaimer:
            "Descriptive indicator based on survey satisfaction thresholds. Not a trained ML prediction.",
        },
        mlPrediction: empMlPrediction,
      },
      { upsert: true, returnDocument: "after" },
    );
  }

  // 6. Save CompanyAnalytics snapshot in MongoDB (upsert — one document per company, no duplicates)
  const companySnapshot = await CompanyAnalytics.findOneAndUpdate(
    { companyCode: sanitizedCompanyCode },
    {
      companyCode: sanitizedCompanyCode,
      generatedAt: new Date(),
      totalEmployeesInCompany,
      totalFeedbackSubmissions,
      uniqueEmployeesRepresented,
      averages,
      distributions,
      timelineTrends,
      textInsights: {
        totalCommentsAnalyzed: totalCommentsCount,
        topImprovementThemes,
      },
      experimentalRiskSummary: {
        highRiskCount,
        needsAttentionCount,
        healthyCount,
        unsubmittedCount,
      },
      modelVersionUsed: mlStatus.modelVersion || "none",
      mlModelStatus: mlStatus.status,
    },
    { upsert: true, returnDocument: "after" },
  );

  return companySnapshot;
}

/**
 * Retrieve latest stored company analytics or generate if none exists
 */
export async function getCompanyAnalyticsOverview(companyCode) {
  const sanitizedCompanyCode = companyCode.toUpperCase().trim();

  let latestSnapshot = await CompanyAnalytics.findOne({
    companyCode: sanitizedCompanyCode,
  })
    .sort({ generatedAt: -1 })
    .lean();

  if (!latestSnapshot) {
    latestSnapshot = await refreshCompanyAnalytics(sanitizedCompanyCode);
  }

  const mlStatus = await getModelStatus();

  return {
    ...latestSnapshot,
    mlStatus,
  };
}

/**
 * Retrieve individual employee analytics details
 */
export async function getEmployeeAnalyticsDetails(employeeId, companyCode) {
  const sanitizedCompanyCode = companyCode.toUpperCase().trim();

  // Verify student belongs to authorized institution
  const emp = await User.findOne({
    _id: employeeId,
    companyCode: sanitizedCompanyCode,
    role: { $in: ["student", "employee"] },
  })
    .select("_id fullName email employeeCode studentCode companyCode institutionCode course yearOfStudy department assignedCounselor assignedHR createdAt")
    .lean();

  if (!emp) {
    return null;
  }

  // Fetch feedback history for this employee
  const feedbackHistory = await EmployeeFeedback.find({ employeeId: emp._id })
    .sort({ submittedAt: 1 })
    .lean();

  // Get or calculate employee analytics snapshot
  let employeeAnalytics = await EmployeeAnalytics.findOne({
    employeeId: emp._id,
    companyCode: sanitizedCompanyCode,
  }).lean();

  if (!employeeAnalytics) {
    await refreshCompanyAnalytics(sanitizedCompanyCode);
    employeeAnalytics = await EmployeeAnalytics.findOne({
      employeeId: emp._id,
      companyCode: sanitizedCompanyCode,
    }).lean();
  }

  const mlStatus = await getModelStatus();

  return {
    employee: emp,
    analytics: employeeAnalytics,
    feedbackHistory,
    mlStatus,
  };
}
