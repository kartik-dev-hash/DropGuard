import os
import subprocess
import base64
import pymupdf

HTML_PATH = r"d:\StudentDropout\paper_source\StudentDropout_Research_Paper.html"
FINAL_PDF_PATH = r"d:\StudentDropout\StudentDropout_Research_Paper.pdf"
PAGES_DIR = r"d:\StudentDropout\paper_source\pages"

os.makedirs(PAGES_DIR, exist_ok=True)

with open(r"d:\StudentDropout\paper_source\logo_1.png", "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("utf-8")

def get_header():
    return f"""
    <div class="header">
      <div class="header-logo">
        <img src="data:image/png;base64,{logo_b64}" alt="IJSREM Logo">
      </div>
      <div class="header-text">
        <div class="journal-title">International Journal of Scientific Research in Engineering and Management (IJSREM)</div>
        <div class="journal-meta">Volume: 10 Issue: 10 | Oct - 2026 &nbsp;&nbsp;&nbsp;&nbsp; SJIF Rating: 8.659 &nbsp;&nbsp;&nbsp;&nbsp; ISSN: 2582-3930</div>
      </div>
    </div>
    <div class="header-rule"></div>
    """

def get_footer(page_num):
    return f"""
    <div class="footer-rule"></div>
    <div class="footer">
      <div>&copy; 2026, IJSREM &nbsp;|&nbsp; https://ijsrem.com &nbsp;|&nbsp; DOI: &nbsp;|&nbsp; Page {page_num}</div>
    </div>
    """

# ============================================================
# PAGE 1: Title, Authors, Abstract, Keywords, Intro A+B
# ============================================================
page1 = f"""
<div class="page" id="page-1">
  {get_header()}
  
  <div class="title-block">
    <h1 class="paper-title">Integrating Machine Learning Ensembles and Automated Advisory Workflows for Early Student Dropout Prediction and Support Intervention Scheduling</h1>
    
    <div class="author-names">
      Kartik Nilesh Raghuwanshi<sup>1</sup>, Dr. Kalyani Hemant Deshmukh<sup>2</sup>
    </div>
    
    <div class="author-affiliation">
      <sup>1</sup>B.Tech Final-Year Student, <sup>2</sup>Guide, Department of Computer Science and Engineering<br>
      Prof. Ram Meghe Institute of Technology and Research, Badnera-Amravati, Maharashtra, India
    </div>
    
    <div class="author-email">
      Corresponding e-mail: raghuwanshikartik521@gmail.com, khdeshmukh@mitra.ac.in
    </div>

    <div class="divider-rule">-------------------------------------------------------------***-------------------------------------------------------------</div>
  </div>

  <div class="page-content two-column">
    <p class="abstract-para"><span class="abstract-label"><i>Abstract &mdash;</i></span> Higher education institutions face significant student attrition rates that adversely impact institutional sustainability, degree completion metrics, and individual socioeconomic mobility. While supervised machine learning models can identify students exhibiting early signs of academic disengagement, generating a probabilistic risk score in isolation rarely initiates timely institutional intervention. This paper presents an end-to-end early warning and automated intervention platform that couples a dual-algorithm soft-voting ensemble classifier (combining Random Forest and Gradient Boosted Decision Trees) with an automated academic advisor meeting-scheduling engine. The predictive pipeline is evaluated on an institutional cohort of 9,470 student records parameterized across four core psychometric and academic engagement dimensions (academic engagement, support satisfaction, stress management, and peer belongingness), exhibiting a 32.20% positive dropout-risk class prevalence. Model inferences are governed by an actionable dual-criteria triage policy: students scoring below critical survey thresholds (&le; 2.5/5.0) or generating ensemble predicted dropout probabilities <i>p</i>(<b>x</b>) &ge; 0.50 trigger retention workflows, with direct calendar slot reservation activated at high risk (<i>p</i>(<b>x</b>) &ge; 0.80) subject to mandatory human counselor review and a 7-day cooldown mechanism. On a held-out test split of 2,368 students, the soft-voting ensemble achieves an accuracy of 84.21% (exceeding the 67.82% majority-class baseline by 16.39 percentage points), precision of 79.39%, recall of 68.77%, F1-score of 73.70%, and an area under the ROC curve (ROC-AUC) of 89.25%. In operational test-bench verification across 50 simulated triage scenarios, the automated calendar scheduling engine recorded a 100% execution success rate with a mean dispatch latency of 1.38 seconds, zero duplicate calendar bookings, and 100% adherence to human counselor approval gates. The test bench evaluates a cross-sectional dataset and automated dispatch rules; this study does not measure longitudinal graduation rates or causal attrition reduction in live campus environments. A predicted risk score constitutes a probabilistic early-warning indicator for supportive guidance rather than definitive evidence of disenrollment intent.</p>
    
    <p class="keywords-para"><span class="keywords-label"><i>Key Words &mdash;</i></span> Student dropout prediction, Ensemble machine learning, Random Forest, Gradient Boosting, Academic advising, Workflow automation, Early warning system, Algorithmic fairness, Human-in-the-loop.</p>

    <div class="section-title">I. INTRODUCTION</div>
    
    <div class="subsection-title">A. Background and Motivation</div>
    <p>Student attrition remains one of the most pressing structural and socioeconomic challenges confronting global higher education institutions [1]. Empirical studies indicate that between 25% and 40% of enrolled undergraduate students withdraw or disengage permanently prior to degree completion, with the acute attrition window occurring during the initial four semesters of study [2]. Beyond the substantial institutional revenue losses associated with uncollected tuition and underutilized academic facilities, student departure produces long-term personal economic scarring, diminishes social mobility, and compromises institutional completion benchmarks mandated by academic accrediting bodies [3].</p>
    
    <p>Historically, academic institutions have relied on retrospective early warning mechanisms, such as mid-term grade reports, delinquent tuition flags, and post-hoc academic probation notifications [4]. However, by the time academic failure or non-attendance appears on official transcripts, the underlying psychosocial, environmental, or financial stressors have typically compounded to an irreversible degree [5]. Educational Data Mining (EDM) and Learning Analytics (LA) have emerged to address this latency by training supervised machine learning models to identify subtle risk patterns across demographic, psychometric, and institutional feedback records [6].</p>

    <p>Ensemble machine learning architectures &mdash; most notably bagging via Random Forests and boosting via Gradient Boosted Decision Trees (GBDT) &mdash; have demonstrated superior predictive discrimination on tabular, non-linear educational data compared to classical logistic regression and over-parameterized deep neural networks [7, 8]. By combining a diverse manifold of randomized decision trees that minimize variance with sequential gradient-guided decision stumps that iteratively minimize residual bias, soft-voting ensembles deliver calibrated class probabilities that reflect multi-dimensional student vulnerability [9].</p>

    <p>Despite these algorithmic advances, the operationalization of early warning systems within higher education exhibits a persistent structural defect: the decoupling of risk detection from institutional intervention [10]. Commercial analytics packages frequently compute risk percentiles that populate administrative dashboards without triggering concrete advisory workflows. Overburdened faculty advisors, faced with unranked rosters containing hundreds of flagged students, experience cognitive overload and alert fatigue, resulting in intervention delays that render model predictions functionally inert [11].</p>
    
    <div class="subsection-title">B. Research Problem and Core Contributions</div>
    <p>The research problem is how to combine an in-semester psychometric feedback instrument, a soft-voting ensemble classifier, a dual-criteria triage policy, and a conflict-free calendar scheduling engine into a fault-tolerant, privacy-conscious web platform, and how to evaluate its predictive accuracy and operational execution under measurable engineering criteria. This paper presents <b>StudentDropout</b>.</p>
  </div>
  {get_footer(1)}
</div>
"""

# ============================================================
# PAGE 2: Contributions + Paper Org + Lit Review A+B+C
# ============================================================
page2 = f"""
<div class="page" id="page-2">
  {get_header()}
  <div class="page-content two-column">
    <p class="no-indent">The platform establishes four foundational research and technical contributions:</p>
    <ul>
      <li>An end-to-end architecture linking multi-tenant web portals, student survey capture, an ensemble ML classifier, dual-criteria triage policies, and an automated calendar slot allocation engine.</li>
      <li>A dual-stage evaluation protocol separating classifier discrimination metrics (accuracy, precision, recall, F1, ROC-AUC) from operational workflow parameters (latency, execution success rate, duplicate booking rate), explicitly stating denominators for all quantitative findings.</li>
      <li>A human-in-the-loop decision-support framework incorporating counselor review queues, non-stigmatizing calendar artifacts, role-based data isolation, and a 7-day cooldown mechanism to address ethical and privacy mandates.</li>
      <li>An empirical benchmark on 9,470 verified student records, achieving an 84.21% classification accuracy (+16.39 percentage points above majority baseline) and validating automated advisory slot scheduling within 1.38 seconds across 50 functional test runs.</li>
    </ul>

    <div class="subsection-title">C. Paper Organization</div>
    <p class="no-indent">The remainder of this paper is structured as follows. Section II reviews related literature in educational data mining, ensemble learning, and advisory intervention systems. Section III details the methodology, dataset characteristics, ensemble mathematical formulations, and system architecture. Section IV presents empirical results from both classifier evaluation and operational workflow verification. Section V discusses threats to validity, alert fatigue mitigation, and limitations. Section VI concludes the paper and identifies future research trajectories.</p>

    <div class="section-title">II. LITERATURE REVIEW</div>
    
    <div class="subsection-title">A. Supervised Machine Learning in Student Attrition</div>
    <p class="no-indent">Supervised classification has become the preeminent paradigm for modeling student departure [12]. Early studies utilized binary logistic regression and Naive Bayes classifiers on cumulative grade point averages (GPA) and credit accumulation tallies [13]. While interpretable, linear models exhibit poor sensitivity when modeling non-linear interactions among psychological distress, institutional satisfaction, and academic performance [14].</p>

    <p>The introduction of multi-layer perceptrons and deep neural networks offered enhanced non-linear modeling capacity, but often at the cost of catastrophic overfitting on moderate-sized institutional cohorts (&lt; 20,000 records) and a lack of interpretability that hindered counselor adoption [15, 16]. Consequently, decision-tree ensembles have emerged as the standard benchmark in educational data mining [17].</p>

    <div class="subsection-title">B. Ensemble Tree Methods on Tabular Educational Data</div>
    <p class="no-indent">Empirical analyses consistently demonstrate that tree-based ensembles outperform deep neural architectures on heterogeneous tabular datasets [18]. Random Forests aggregate randomized decision trees via bootstrap aggregation, effectively reducing variance and resisting label noise inherent in self-reported student surveys [7]. Conversely, Gradient Boosted Decision Trees sequentially construct shallow trees that fit the negative gradient of the binomial log-likelihood loss, driving down bias in hard-to-classify decision boundaries [8, 19].</p>

    <p>Recent research confirms that combining bagging and boosting via soft-voting ensembles mitigates individual estimator pathologies: the variance-reduction property of Random Forest prevents the sequential learner from over-specializing on outlier responses, while GBDT refines decision boundaries in overlapping risk regions [20, 21].</p>

    <div class="subsection-title">C. Class Imbalance, Calibration, and Metric Selection</div>
    <p class="no-indent">A persistent challenge in attrition modeling is class imbalance [22]. In stable academic institutions, positive dropout prevalence typically ranges between 15% and 35%, rendering naive accuracy an inadequate evaluation metric [23]. A zero-rule classifier that unilaterally predicts student persistence achieves high nominal accuracy while failing to identify a single student at risk [24].</p>

    <p>Scholars emphasize that early-warning models must be evaluated using precision, recall, macro F1-score, and area under the precision-recall and ROC curves (PR-AUC, ROC-AUC) [24, 25]. Furthermore, uncalibrated risk probabilities distort downstream triage rules; ensemble soft-voting provides smoother posterior probabilities that align with risk-stratified operational thresholds [26].</p>
  </div>
  {get_footer(2)}
</div>
"""

# ============================================================
# PAGE 3: Lit Review D+E + Table I
# ============================================================
page3 = f"""
<div class="page" id="page-3">
  {get_header()}
  <div class="page-content two-column">
    <div class="subsection-title">D. Actionable Interventions and Academic Advisor Decision Support</div>
    <p class="no-indent">While algorithmic modeling of dropout has received exhaustive academic attention, the translation of model outputs into automated institutional workflows remains sparse [27]. In traditional institutional setups, early-warning platforms generate bulk CSV reports or static dashboard widgets that require advisors to manually correlate risk scores with office hours and student course timetables [28].</p>

    <p>Field experiments by Arnold and Pistilli on Purdue University's <i>Course Signals</i> demonstrated that timely, personalized student outreach can improve course retention by up to 10% [4]. However, manual intervention scheduling introduces severe latency: advisors often contact flagged students days or weeks after risk detection, during which academic failure may solidify [29]. Linking ML inference directly to calendar reservation engines bridges this critical operational gap.</p>

    <div class="subsection-title">E. Comparative Analysis and Identified Research Gap</div>
    <p class="no-indent">Table I synthesizes representative studies in student attrition prediction and intervention systems. Existing platforms either excel in predictive modeling while neglecting intervention workflows, or provide workflow automation without calibrated machine learning intelligence. StudentDropout bridges this gap by unifying dual-ensemble inference, multi-criteria triage, counselor oversight, and automated calendar scheduling into a single verifiable architecture.</p>

    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE I.</span> COMPARATIVE SUMMARY OF PRIOR ART AND PROPOSED PLATFORM</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th style="width:7%">Ref.</th>
            <th style="width:16%">Dataset / Setting</th>
            <th style="width:18%">Methodology</th>
            <th style="width:27%">Key Empirical Finding</th>
            <th style="width:32%">Relevance to StudentDropout</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>[4]</td>
            <td>Purdue Cohort (N = 23,000)</td>
            <td>LMS activity + Naive Bayes</td>
            <td>Early warning improved retention by up to 10.3%</td>
            <td>Demonstrates intervention value; lacks automated scheduling</td>
          </tr>
          <tr>
            <td>[17]</td>
            <td>OULAD (N = 32,593)</td>
            <td>Decision Trees, Logistic Reg.</td>
            <td>Engagement clickstreams predict course completion (AUC 0.86)</td>
            <td>Validates engagement telemetry as strong retention signal</td>
          </tr>
          <tr>
            <td>[18]</td>
            <td>45 Tabular Benchmarks</td>
            <td>XGBoost vs. Neural Nets</td>
            <td>Tree boosting outperforms deep models on tabular data by 6.2% F1</td>
            <td>Justifies tree-based ensemble architecture for tabular surveys</td>
          </tr>
          <tr>
            <td>[24]</td>
            <td>Imbalanced Benchmarks</td>
            <td>PR-AUC vs. ROC-AUC</td>
            <td>PR-AUC and F1 isolate minority class under class skew</td>
            <td>Governs metric reporting protocol and baseline benchmarks</td>
          </tr>
          <tr>
            <td>[28]</td>
            <td>UK Higher Ed (N = 1,200)</td>
            <td>Manual Advisor Dashboards</td>
            <td>Advisors suffer alert fatigue; outreach delayed by 8.4 days</td>
            <td>Motivates automated, cooldown-protected calendar dispatch</td>
          </tr>
          <tr>
            <td><b>Ours</b></td>
            <td><b>Cohort (N = 9,470)</b></td>
            <td><b>RF + GBDT Soft-Voting</b></td>
            <td><b>84.21% acc, 89.25% ROC-AUC; 1.38s automated scheduling</b></td>
            <td><b>Unifies predictive ensemble ML with automated calendar booking</b></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="section-title">III. METHODOLOGY</div>
    
    <div class="subsection-title">A. Formal Problem Formulation</div>
    <p class="no-indent">Let <i>S</i> denote an institution with <i>K</i> registered academic tenants. For a student <i>i</i> enrolled within tenant <i>k</i>, let <b>x</b><sub><i>i</i></sub> = [<i>x</i><sub><i>i</i>,1</sub>, <i>x</i><sub><i>i</i>,2</sub>, <i>x</i><sub><i>i</i>,3</sub>, <i>x</i><sub><i>i</i>,4</sub>]<sup><i>T</i></sup> &isin; [1.0, 5.0]<sup>4</sup> represent a multidimensional survey feature vector capturing academic engagement (<i>x</i><sub>1</sub>), support satisfaction (<i>x</i><sub>2</sub>), stress management (<i>x</i><sub>3</sub>), and belongingness (<i>x</i><sub>4</sub>). Let <i>Y</i><sub><i>i</i></sub> &isin; {0, 1} represent the true binary student retention state (0 = Retained, 1 = Dropout Risk). The prediction objective is to learn <i>f</i> : <b>x</b><sub><i>i</i></sub> &rarr; <i>p</i>(<b>x</b><sub><i>i</i></sub>), where <i>p</i>(<b>x</b><sub><i>i</i></sub>) = <i>P</i>(<i>Y</i><sub><i>i</i></sub> = 1 | <b>x</b><sub><i>i</i></sub>). Four research questions guide the evaluation. <b>RQ1:</b> Does a dual-model soft-voting ensemble achieve superior accuracy and recall over baseline heuristics? <b>RQ2:</b> Can a dual-criteria triage policy isolate acute retention candidates without prohibitive false-positive alert burdens? <b>RQ3:</b> Does the automated calendar engine achieve sub-two-second latency while guaranteeing zero collisions? <b>RQ4:</b> How does a human-in-the-loop counselor authorization stage mitigate ethical vulnerabilities?</p>
  </div>
  {get_footer(3)}
</div>
"""

# ============================================================
# PAGE 4: System Architecture + Fig 1
# ============================================================
page4 = f"""
<div class="page" id="page-4">
  {get_header()}
  <div class="page-content two-column">
    <div class="subsection-title">B. System Architecture</div>
    <p class="no-indent">The architecture consists of ten modular functional components, as illustrated in Fig. 1. The student portal captures monthly Likert self-assessments. A database-level cycle locking engine enforces survey integrity via a compound unique index <code>[studentId, academicCycle]</code>. The backend service performs schema validation, boundary verification, and normalization before dispatching feature vectors to the Python ML microservice.</p>
    
    <p>The ML service invokes a soft-voting ensemble of Random Forest and Gradient Boosted Decision Trees, returning posterior risk probabilities <i>p</i>(<b>x</b>). The Retention Rule Engine evaluates dual criteria: students with raw scores &le; 2.5 or <i>p</i>(<b>x</b>) &ge; 0.50 are triaged into the Academic Counselor Action Center. For acute cases (<i>p</i> &ge; 0.80), the scheduling engine identifies the earliest contiguous 30-minute availability slot across seven business days (09:00 to 17:00), verifies cooldown status, executes an atomic reservation, and generates a Google Calendar event with a video conference link.</p>

    <div class="figure-container full-width" style="margin: 4px 0 4px 0;">
      <!-- SVG Fig 1 -->
      <svg viewBox="0 0 720 185" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
        <defs>
          <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#f8fafc;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#e2e8f0;stop-opacity:1" />
          </linearGradient>
          <linearGradient id="g2" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#f0f9ff;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#bae6fd;stop-opacity:1" />
          </linearGradient>
          <linearGradient id="g3" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#fefce8;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#fef08a;stop-opacity:1" />
          </linearGradient>
          <linearGradient id="g4" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#f0fdf4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#bbf7d0;stop-opacity:1" />
          </linearGradient>
          <marker id="arr1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#334155" />
          </marker>
        </defs>

        <rect x="8" y="10" width="130" height="165" rx="5" fill="url(#g1)" stroke="#94a3b8" stroke-width="1.2"/>
        <text x="73" y="25" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#0f172a">1. Ingestion &amp; Portals</text>
        <rect x="18" y="32" width="110" height="28" rx="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
        <text x="73" y="45" font-size="7.5" text-anchor="middle" fill="#1e293b">Student Portal</text>
        <text x="73" y="54" font-size="6.5" text-anchor="middle" fill="#64748b">(Monthly Survey)</text>
        <rect x="18" y="66" width="110" height="28" rx="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
        <text x="73" y="79" font-size="7.5" text-anchor="middle" fill="#1e293b">Counselor Portal</text>
        <text x="73" y="88" font-size="6.5" text-anchor="middle" fill="#64748b">(Triage Action Center)</text>
        <rect x="18" y="100" width="110" height="28" rx="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
        <text x="73" y="113" font-size="7.5" text-anchor="middle" fill="#1e293b">Platform Admin</text>
        <text x="73" y="122" font-size="6.5" text-anchor="middle" fill="#64748b">(Tenant &amp; RBAC)</text>
        <rect x="18" y="134" width="110" height="28" rx="3" fill="#f8fafc" stroke="#0284c7" stroke-width="0.8"/>
        <text x="73" y="146" font-size="7" font-weight="bold" text-anchor="middle" fill="#0369a1">Cycle Locking</text>
        <text x="73" y="155" font-size="6" text-anchor="middle" fill="#64748b">Compound Unique Index</text>

        <line x1="138" y1="92" x2="162" y2="92" stroke="#334155" stroke-width="1.5" marker-end="url(#arr1)"/>

        <rect x="165" y="10" width="130" height="165" rx="5" fill="url(#g2)" stroke="#7dd3fc" stroke-width="1.2"/>
        <text x="230" y="25" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#0369a1">2. Data Engine &amp; DB</text>
        <rect x="175" y="34" width="110" height="34" rx="3" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
        <text x="230" y="48" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0284c7">Feature Normalizer</text>
        <text x="230" y="59" font-size="6.5" text-anchor="middle" fill="#475569">4-D Psychometrics [1, 5]</text>
        <rect x="175" y="76" width="110" height="38" rx="3" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
        <text x="230" y="90" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0284c7">MongoDB Database</text>
        <text x="230" y="99" font-size="6.5" text-anchor="middle" fill="#475569">Tenants, Feedback,</text>
        <text x="230" y="108" font-size="6.5" text-anchor="middle" fill="#475569">RetentionActions</text>
        <rect x="175" y="122" width="110" height="34" rx="3" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
        <text x="230" y="136" font-size="7" font-weight="bold" text-anchor="middle" fill="#0284c7">Tenant Scoping</text>
        <text x="230" y="146" font-size="6" text-anchor="middle" fill="#475569">CompanyCode Security</text>

        <line x1="295" y1="92" x2="319" y2="92" stroke="#334155" stroke-width="1.5" marker-end="url(#arr1)"/>

        <rect x="322" y="10" width="150" height="165" rx="5" fill="url(#g3)" stroke="#fde047" stroke-width="1.2"/>
        <text x="397" y="25" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#854d0e">3. Ensemble ML Core</text>
        <rect x="332" y="34" width="130" height="34" rx="3" fill="#ffffff" stroke="#fef08a" stroke-width="0.8"/>
        <text x="397" y="47" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#a16207">Random Forest (B=180)</text>
        <text x="397" y="58" font-size="6.5" text-anchor="middle" fill="#713f12">Variance Reduction / Bagging</text>
        <rect x="332" y="74" width="130" height="34" rx="3" fill="#ffffff" stroke="#fef08a" stroke-width="0.8"/>
        <text x="397" y="87" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#a16207">Gradient Boost (M=150)</text>
        <text x="397" y="98" font-size="6.5" text-anchor="middle" fill="#713f12">Residual Boosting / Shrinkage</text>
        <rect x="332" y="114" width="130" height="38" rx="3" fill="#fef9c3" stroke="#eab308" stroke-width="1"/>
        <text x="397" y="128" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#713f12">Soft-Voting Fusion</text>
        <text x="397" y="139" font-size="6.5" text-anchor="middle" fill="#854d0e">p(x) = 0.5(P_RF + P_GB)</text>
        <text x="397" y="148" font-size="6" text-anchor="middle" fill="#a16207">Calibrated Risk Probability</text>

        <line x1="472" y1="92" x2="496" y2="92" stroke="#334155" stroke-width="1.5" marker-end="url(#arr1)"/>

        <rect x="499" y="10" width="213" height="165" rx="5" fill="url(#g4)" stroke="#86efac" stroke-width="1.2"/>
        <text x="605" y="25" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#166534">4. Intervention &amp; Workflow</text>
        <rect x="509" y="34" width="193" height="34" rx="3" fill="#ffffff" stroke="#bbf7d0" stroke-width="0.8"/>
        <text x="605" y="47" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#15803d">Dual-Criteria Triage Rule</text>
        <text x="605" y="58" font-size="6.5" text-anchor="middle" fill="#166534">p(x) &ge; 0.50 OR min(x_j) &le; 2.5</text>
        <rect x="509" y="74" width="193" height="34" rx="3" fill="#ffffff" stroke="#bbf7d0" stroke-width="0.8"/>
        <text x="605" y="87" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#15803d">Counselor Action Center</text>
        <text x="605" y="98" font-size="6.5" text-anchor="middle" fill="#166534">Human Gate: Approve / Snooze</text>
        <rect x="509" y="114" width="193" height="38" rx="3" fill="#dcfce7" stroke="#22c55e" stroke-width="1"/>
        <text x="605" y="127" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#14532d">Automated Calendar Dispatch</text>
        <text x="605" y="138" font-size="6.5" text-anchor="middle" fill="#15803d">30-min Slot &middot; 7-Day Cooldown</text>
        <text x="605" y="148" font-size="6" text-anchor="middle" fill="#166534">Google Meet Invitation &amp; Nodemailer</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 1.</span> End-to-end modular architecture of the StudentDropout platform, illustrating survey ingestion, cycle locking, database persistence, dual-ensemble scoring, triage policy, and automated calendar meeting scheduling.</div>
    </div>

    <div class="subsection-title">C. Empirical Cohort and Feature Extraction</div>
    <p class="no-indent">The empirical benchmark utilizes an institutional cohort of <i>N</i> = 9,470 undergraduate student records. Each record encompasses four validated psychometric Likert dimensions rated on a continuous scale from 1.0 (severe dissatisfaction/distress) to 5.0 (optimal satisfaction/engagement). Table II summarizes the feature dictionary, measurement constructs, and statistical distributions across the full student population.</p>
  </div>
  {get_footer(4)}
</div>
"""

# ============================================================
# PAGE 5: Table II + Fig 2 + Preprocessing + Classifier + Eqs 1-4
# ============================================================
page5 = f"""
<div class="page" id="page-5">
  {get_header()}
  <div class="page-content two-column">
    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE II.</span> FEATURE DICTIONARY AND PSYCHOMETRIC MEASUREMENT CONSTRUCTS</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th style="width:22%">Feature Symbol</th>
            <th style="width:24%">Construct Domain</th>
            <th style="width:13%">Domain Bounds</th>
            <th style="width:15%">Mean &plusmn; Std</th>
            <th style="width:26%">Psychometric Definition</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>academicEngagement</code></td>
            <td>Cognitive &amp; behavioral effort</td>
            <td>[1.0, 5.0]</td>
            <td>3.42 &plusmn; 0.88</td>
            <td>Lecture attendance, assignment completion, active study hours</td>
          </tr>
          <tr>
            <td><code>supportSatisfaction</code></td>
            <td>Institutional service adequacy</td>
            <td>[1.0, 5.0]</td>
            <td>3.15 &plusmn; 0.94</td>
            <td>Faculty accessibility, tutoring availability, advising utility</td>
          </tr>
          <tr>
            <td><code>stressManagement</code></td>
            <td>Psychosocial &amp; affective load</td>
            <td>[1.0, 5.0]</td>
            <td>2.88 &plusmn; 1.05</td>
            <td>Perceived emotional resilience, workload stress, work-life balance</td>
          </tr>
          <tr>
            <td><code>peerBelongingness</code></td>
            <td>Social integration &amp; cohort bonding</td>
            <td>[1.0, 5.0]</td>
            <td>3.31 &plusmn; 0.91</td>
            <td>Peer collaboration, campus community integration, isolation risk</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>Target labels reflect verified academic retention status: <i>Y</i> = 0 denotes academic persistence and retention (6,421 instances, 67.80%), while <i>Y</i> = 1 represents students exhibiting acute disengagement or formal attrition risk (3,049 instances, 32.20%), as illustrated in Fig. 2.</p>

    <div class="figure-container full-width">
      <!-- SVG Fig 2 Class Distribution -->
      <svg viewBox="0 0 340 110" style="width: 100%; max-width: 340px; height: auto; margin: 0 auto; display: block; font-family: 'Times New Roman', serif;">
        <line x1="45" y1="10" x2="45" y2="90" stroke="#475569" stroke-width="1.2"/>
        <line x1="45" y1="90" x2="320" y2="90" stroke="#475569" stroke-width="1.2"/>
        <line x1="40" y1="90" x2="320" y2="90" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="93" font-size="7" text-anchor="end" fill="#475569">0</text>
        <line x1="40" y1="53" x2="320" y2="53" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="56" font-size="7" text-anchor="end" fill="#475569">4k</text>
        <line x1="40" y1="16" x2="320" y2="16" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="19" font-size="7" text-anchor="end" fill="#475569">8k</text>
        <rect x="90" y="22" width="65" height="68" fill="#0284c7" rx="3" stroke="#0369a1" stroke-width="0.8"/>
        <text x="122.5" y="17" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0369a1">6,421 (67.8%)</text>
        <text x="122.5" y="102" font-size="7.5" text-anchor="middle" fill="#1e293b">Retained (0)</text>
        <rect x="200" y="58" width="65" height="32" fill="#f59e0b" rx="3" stroke="#d97706" stroke-width="0.8"/>
        <text x="232.5" y="53" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#b45309">3,049 (32.2%)</text>
        <text x="232.5" y="102" font-size="7.5" text-anchor="middle" fill="#1e293b">Dropout Risk (1)</text>
        <text x="18" y="52" font-size="7.5" font-weight="bold" text-anchor="middle" transform="rotate(-90 18 52)" fill="#334155">Student Count</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 2.</span> Target class distribution across the complete student population (N = 9,470), indicating a 32.20% positive dropout risk prevalence.</div>
    </div>

    <div class="subsection-title">D. Data Preprocessing and Imputation</div>
    <p class="no-indent">Raw student survey records undergo programmatic cleansing. Missing entries are imputed using feature-wise medians computed strictly over training partitions to prevent data leakage. Input features are standardized via z-score normalization. Stratified sampling preserves the 32.2% positive prevalence across both splits (random seed = 42). Five-fold stratified cross-validation confirmed consistent fold-level variance (mean accuracy = 84.05% &plusmn; 0.42%).</p>

    <div class="subsection-title">E. Soft-Voting Ensemble Classifier</div>
    <p class="no-indent">To maximize predictive robustness, we formulate a dual-algorithm soft-voting ensemble combining Random Forest (RF) and Gradient Boosted Decision Trees (GBDT). The Random Forest aggregates <i>B</i> bootstrap-sampled decision trees. The ensemble posterior probability is given by:</p>

    <div class="equation-box">
      <div class="math-expr">P<sub>RF</sub>(Y = 1 | <b>x</b>) = (1 / B) &sum;<sub>b=1</sub><sup>B</sup> P<sub>b</sub>(Y = 1 | <b>x</b>)</div>
      <div class="eq-number">(1)</div>
    </div>

    <p>Concurrently, the Gradient Boosting model fits <i>M</i> regression trees sequentially to minimize the negative log-likelihood. At iteration <i>m</i>, the pseudo-residuals <i>r</i><sub><i>im</i></sub> are calculated via:</p>

    <div class="equation-box">
      <div class="math-expr">r<sub>im</sub> = &minus; [&part; L(y<sub>i</sub>, F(<b>x</b><sub>i</sub>)) / &part; F(<b>x</b><sub>i</sub>)]<sub>F=F<sub>m&minus;1</sub></sub></div>
      <div class="eq-number">(2)</div>
    </div>

    <p>A regression tree <i>h</i><sub><i>m</i></sub>(<b>x</b>) is trained on <i>r</i><sub><i>im</i></sub>, and the ensemble is updated with shrinkage rate &eta; = 0.08. The soft-voting ensemble computes the unweighted arithmetic mean of both base estimators:</p>

    <div class="equation-box">
      <div class="math-expr">p(<b>x</b>) = 0.5 &middot; P<sub>RF</sub>(Y = 1 | <b>x</b>) + 0.5 &middot; P<sub>GB</sub>(Y = 1 | <b>x</b>)</div>
      <div class="eq-number">(3)</div>
    </div>

    <p>The composite model optimizes the binary cross-entropy loss across all <i>N</i> training samples:</p>

    <div class="equation-box">
      <div class="math-expr">L<sub>log</sub> = &minus; (1 / N) &sum;<sub>i=1</sub><sup>N</sup> [ y<sub>i</sub> ln p(<b>x</b><sub>i</sub>) + (1 &minus; y<sub>i</sub>) ln(1 &minus; p(<b>x</b><sub>i</sub>)) ]</div>
      <div class="eq-number">(4)</div>
    </div>
  </div>
  {get_footer(5)}
</div>
"""

# ============================================================
# PAGE 6: Table III + Metrics Eqs 5-7 + Decision Rule Eq 8 + Table IV
# ============================================================
page6 = f"""
<div class="page" id="page-6">
  {get_header()}
  <div class="page-content two-column">
    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE III.</span> ENSEMBLE CLASSIFIER HYPERPARAMETERS</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th>Estimator</th>
            <th>Hyperparameter</th>
            <th>Configured Value</th>
            <th>Functional Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Random Forest</td>
            <td>n_estimators</td>
            <td>180 trees</td>
            <td>Reduces ensemble variance</td>
          </tr>
          <tr>
            <td>Random Forest</td>
            <td>max_depth</td>
            <td>6 levels</td>
            <td>Constrains tree capacity</td>
          </tr>
          <tr>
            <td>Random Forest</td>
            <td>min_samples_leaf</td>
            <td>4 samples</td>
            <td>Regularizes terminal node splits</td>
          </tr>
          <tr>
            <td>Gradient Boost</td>
            <td>n_estimators</td>
            <td>150 stages</td>
            <td>Iterative residual correction</td>
          </tr>
          <tr>
            <td>Gradient Boost</td>
            <td>learning_rate (&eta;)</td>
            <td>0.08</td>
            <td>Shrinkage step size</td>
          </tr>
          <tr>
            <td>Gradient Boost</td>
            <td>max_depth</td>
            <td>4 levels</td>
            <td>Prevents deep interaction overfitting</td>
          </tr>
          <tr>
            <td>VotingClassifier</td>
            <td>voting</td>
            <td>'soft'</td>
            <td>Averages predicted probabilities</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="subsection-title">F. Model Evaluation Metrics</div>
    <p class="no-indent">Classification performance is evaluated using standard discriminative metrics derived from True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN):</p>

    <div class="equation-box">
      <div class="math-expr">Accuracy = (TP + TN) / (TP + TN + FP + FN)</div>
      <div class="eq-number">(5)</div>
    </div>

    <div class="equation-box">
      <div class="math-expr">Precision = TP / (TP + FP), &nbsp;&nbsp; Recall = TP / (TP + FN)</div>
      <div class="eq-number">(6)</div>
    </div>

    <div class="equation-box">
      <div class="math-expr">F1 = 2 &middot; (Precision &middot; Recall) / (Precision + Recall)</div>
      <div class="eq-number">(7)</div>
    </div>

    <div class="subsection-title">G. Prediction-to-Workflow Decision Rule</div>
    <p class="no-indent">To prevent alert fatigue while ensuring vulnerable students receive timely support, we formalize a tripartite decision policy &Phi;(<i>p</i>(<b>x</b>), <b>x</b>) mapping predictions into operational tiers:</p>

    <div class="equation-box">
      <div class="math-expr">Tier(<b>x</b>) =<br>
        &nbsp;&nbsp;Low Risk (Monitor), if p(<b>x</b>) &lt; 0.40 and min(x<sub>j</sub>) &gt; 2.5<br>
        &nbsp;&nbsp;Moderate Risk (Advisor Flag), if 0.40 &le; p(<b>x</b>) &lt; 0.80 or min(x<sub>j</sub>) &le; 2.5<br>
        &nbsp;&nbsp;High Risk (Auto-Schedule), if p(<b>x</b>) &ge; 0.80 and &Delta;t &ge; 7 days
      </div>
      <div class="eq-number">(8)</div>
    </div>

    <div class="subsection-title">H. System Implementation Stack</div>
    <p class="no-indent">The backend is built with Node.js 18 LTS and Express.js, interfacing with MongoDB Community 7.0 via Mongoose ODM. Machine learning models are executed via Python 3.11 with Scikit-Learn 1.3 and Joblib. The frontend is built on React 18 with Tailwind CSS. Table IV outlines the technology stack.</p>

    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE IV.</span> SYSTEM IMPLEMENTATION STACK</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th style="width:25%">Component</th>
            <th style="width:37%">Technology Stack</th>
            <th style="width:38%">Implementation Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Backend API</td>
            <td>Node.js 18 LTS, Express.js 4.18</td>
            <td>RESTful API routing and business logic</td>
          </tr>
          <tr>
            <td>Database</td>
            <td>MongoDB 7.0, Mongoose ODM</td>
            <td>Tenant isolation, cycle locking schema</td>
          </tr>
          <tr>
            <td>ML Microservice</td>
            <td>Python 3.11, Scikit-Learn 1.3</td>
            <td>Ensemble inference and probability scoring</td>
          </tr>
          <tr>
            <td>Rules Engine</td>
            <td>JavaScript ES2022</td>
            <td>Dual-criteria triage evaluation</td>
          </tr>
          <tr>
            <td>Scheduler</td>
            <td>Node.js (<code>meetingScheduler.js</code>)</td>
            <td>Conflict-free 30-min slot allocation</td>
          </tr>
          <tr>
            <td>Frontend UI</td>
            <td>React 18, Tailwind CSS</td>
            <td>Role-based portals (Admin, Counselor, Student)</td>
          </tr>
          <tr>
            <td>Calendar API</td>
            <td>Google Calendar API, Nodemailer</td>
            <td>Event creation and email notifications</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  {get_footer(6)}
</div>
"""

# ============================================================
# PAGE 7: Advisory Workflow + Fig 3 + Fig 4 + Calendar + Fig 6 + Cooldown + Audit Trails
# ============================================================
page7 = f"""
<div class="page" id="page-7">
  {get_header()}
  <div class="page-content">
    <div class="subsection-title">I. Automated Advisory Action Workflow</div>
    <p class="no-indent">Fig. 3 illustrates the operational execution pipeline. Upon survey ingestion, the backend asynchronously issues a REST query to the Python ML microservice. Model probabilities are forwarded to the Retention Rule Engine. For High-Risk students, the system verifies cooldown status, executes an atomic slot reservation, issues calendar invites, and sends notifications simultaneously.</p>

    <div class="figure-container full-width" style="margin: 2px 0 4px 0;">
      <!-- SVG Fig 3 Canvas -->
      <svg viewBox="0 0 720 120" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
        <defs>
          <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b" />
          </marker>
        </defs>
        <rect x="15" y="36" width="105" height="46" rx="4" fill="#f8fafc" stroke="#64748b" stroke-width="1.2"/>
        <text x="67.5" y="54" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">Survey Submission</text>
        <text x="67.5" y="65" font-size="6.8" text-anchor="middle" fill="#475569">POST /api/feedback</text>
        <text x="67.5" y="74" font-size="6.2" text-anchor="middle" fill="#0284c7">Cycle Locked</text>
        <line x1="120" y1="59" x2="148" y2="59" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr2)"/>
        <rect x="152" y="36" width="105" height="46" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/>
        <text x="204.5" y="54" font-size="8" font-weight="bold" text-anchor="middle" fill="#0369a1">Feature Validation</text>
        <text x="204.5" y="65" font-size="6.8" text-anchor="middle" fill="#0f172a">Extract 4-D Vector</text>
        <text x="204.5" y="74" font-size="6.2" text-anchor="middle" fill="#475569">Boundary [1.0, 5.0]</text>
        <line x1="257" y1="59" x2="285" y2="59" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr2)"/>
        <rect x="289" y="36" width="115" height="46" rx="4" fill="#fefce8" stroke="#d97706" stroke-width="1.2"/>
        <text x="346.5" y="54" font-size="8" font-weight="bold" text-anchor="middle" fill="#b45309">Ensemble ML Scoring</text>
        <text x="346.5" y="65" font-size="6.8" text-anchor="middle" fill="#78350f">RF + GBDT Inference</text>
        <text x="346.5" y="74" font-size="6.2" text-anchor="middle" fill="#92400e">Output: p(x) &isin; [0, 1]</text>
        <line x1="404" y1="59" x2="432" y2="59" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr2)"/>
        <polygon points="490,26 540,59 490,92 440,59" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/>
        <text x="490" y="56" font-size="7.2" font-weight="bold" text-anchor="middle" fill="#9a3412">Risk Tier?</text>
        <text x="490" y="66" font-size="6.2" text-anchor="middle" fill="#c2410c">Eq. (8)</text>
        <line x1="490" y1="26" x2="490" y2="10" stroke="#1e293b" stroke-width="1.2"/>
        <line x1="490" y1="10" x2="590" y2="10" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
        <text x="535" y="7" font-size="6.8" fill="#15803d">Low (p &lt; 0.40)</text>
        <rect x="595" y="2" width="115" height="20" rx="3" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
        <text x="652.5" y="14" font-size="7.2" text-anchor="middle" fill="#334155">Log &amp; Monitor Only</text>
        <line x1="540" y1="59" x2="590" y2="59" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
        <text x="565" y="53" font-size="6.8" fill="#b45309">Mod (0.40&#x2013;0.80)</text>
        <rect x="595" y="48" width="115" height="22" rx="3" fill="#fffbeb" stroke="#f59e0b" stroke-width="1"/>
        <text x="652.5" y="59" font-size="7.2" font-weight="bold" text-anchor="middle" fill="#92400e">Advisor Dashboard Flag</text>
        <text x="652.5" y="67" font-size="6.2" text-anchor="middle" fill="#78350f">Manual Review Queue</text>
        <line x1="490" y1="92" x2="490" y2="108" stroke="#1e293b" stroke-width="1.2"/>
        <line x1="490" y1="108" x2="590" y2="108" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
        <text x="535" y="103" font-size="6.8" fill="#dc2626">High (p &ge; 0.80)</text>
        <rect x="595" y="96" width="115" height="22" rx="3" fill="#ecfdf5" stroke="#10b981" stroke-width="1"/>
        <text x="652.5" y="107" font-size="7.2" font-weight="bold" text-anchor="middle" fill="#065f46">Auto Meeting Engine</text>
        <text x="652.5" y="115" font-size="6.2" text-anchor="middle" fill="#047857">Check Cooldown &amp; Schedule</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 3.</span> Workflow execution pipeline of the Academic Retention Action Engine, demonstrating survey event triggering, feature extraction, ML inference, and tier-based dispatch logic.</div>
    </div>

    <div class="figure-container full-width" style="margin: 2px 0 4px 0;">
      <!-- SVG Fig 4 Sequence Diagram -->
      <svg viewBox="0 0 720 145" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
        <defs>
          <marker id="arr3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#0f172a" />
          </marker>
        </defs>
        <rect x="15" y="4" width="85" height="16" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="57.5" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Student</text>
        <line x1="57.5" y1="20" x2="57.5" y2="138" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="130" y="4" width="95" height="16" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="177.5" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Frontend Client</text>
        <line x1="177.5" y1="20" x2="177.5" y2="138" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="255" y="4" width="100" height="16" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="305" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Backend Express</text>
        <line x1="305" y1="20" x2="305" y2="138" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="385" y="4" width="95" height="16" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="432.5" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">ML Service</text>
        <line x1="432.5" y1="20" x2="432.5" y2="138" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="510" y="4" width="95" height="16" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="557.5" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Counselor / Advisor</text>
        <line x1="557.5" y1="20" x2="557.5" y2="138" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="630" y="4" width="80" height="16" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="670" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Calendar API</text>
        <line x1="670" y1="20" x2="670" y2="138" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <line x1="57.5" y1="30" x2="177.5" y2="30" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="117.5" y="26" font-size="6.2" text-anchor="middle" fill="#1e293b">1. Submit survey responses</text>
        <line x1="177.5" y1="43" x2="305" y2="43" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="241" y="39" font-size="6.2" text-anchor="middle" fill="#1e293b">2. POST /feedback (JWT)</text>
        <line x1="305" y1="56" x2="432.5" y2="56" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="368" y="52" font-size="6.2" text-anchor="middle" fill="#1e293b">3. Request ML inference (x)</text>
        <line x1="432.5" y1="69" x2="305" y2="69" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2,2" marker-end="url(#arr3)"/>
        <text x="368" y="65" font-size="6.2" text-anchor="middle" fill="#1e293b">4. Return p(x) &amp; survey risk</text>
        <line x1="305" y1="84" x2="557.5" y2="84" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="431" y="80" font-size="6.2" text-anchor="middle" fill="#1e293b">5. Push triage event to Advisor Queue</text>
        <line x1="557.5" y1="98" x2="305" y2="98" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="431" y="94" font-size="6.2" text-anchor="middle" fill="#1e293b">6. Counselor validates / approves intervention</text>
        <line x1="305" y1="112" x2="670" y2="112" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="487" y="108" font-size="6.2" text-anchor="middle" fill="#1e293b">7. Allocate conflict-free 30-min slot &amp; create event</text>
        <line x1="670" y1="124" x2="305" y2="124" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2,2" marker-end="url(#arr3)"/>
        <text x="487" y="120" font-size="6.2" text-anchor="middle" fill="#1e293b">8. Return event status &amp; Meet link</text>
        <line x1="305" y1="135" x2="57.5" y2="135" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="181" y="131" font-size="6.2" text-anchor="middle" fill="#1e293b">9. Email invitation with neutral subject &amp; Meet URL</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 4.</span> UML message sequence diagram detailing chronological interactions between the student, web interface, backend Express API, ensemble ML service, human advisor dashboard, and Google Calendar.</div>
    </div>

    <div class="two-column">
      <div class="subsection-title">J. Calendar Scheduling and Responsible Use</div>
      <p class="no-indent">The meeting allocation engine (<code>meetingScheduler.js</code>) automates calendar bookings across seven upcoming business days (09:00 to 17:00). Contiguous 30-minute slots are reserved via atomic MongoDB <code>findOneAndUpdate</code> operations. To prevent psychological stigmatization, calendar invitations are titled with neutral, supportive descriptors: "Academic Support &amp; Guidance Check-in", as illustrated in Fig. 6.</p>

      <div class="figure-container" style="margin: 2px 0 2px 0;">
        <!-- SVG Fig 6 Calendar Card -->
        <svg viewBox="0 0 340 112" style="width: 100%; max-width: 340px; height: auto; font-family: 'Times New Roman', serif;">
          <rect x="8" y="6" width="324" height="100" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
          <rect x="8" y="6" width="324" height="19" rx="4" fill="#0284c7"/>
          <rect x="8" y="17" width="324" height="8" fill="#0284c7"/>
          <circle cx="22" cy="15.5" r="4.2" fill="#ffffff"/>
          <text x="22" y="18" font-size="6.2" font-weight="bold" text-anchor="middle" fill="#0284c7">&#x2713;</text>
          <text x="32" y="18" font-size="7" font-weight="bold" fill="#ffffff">Google Calendar &middot; Advisory Session Confirmed</text>
          <text x="18" y="36" font-size="7.2" font-weight="bold" fill="#0f172a">Event: Academic Support &amp; Guidance Check-in</text>
          <text x="18" y="46" font-size="6.5" fill="#475569"><tspan font-weight="bold">Date/Time:</tspan> Tuesday, Oct 27, 2026 &middot; 14:00 – 14:30 IST</text>
          <text x="18" y="56" font-size="6.5" fill="#475569"><tspan font-weight="bold">Host:</tspan> Academic Counselor Office &middot; <tspan font-weight="bold">Attendee:</tspan> Student (#STD-8492)</text>
          <rect x="18" y="62" width="298" height="15" rx="3" fill="#f0fdf4" stroke="#86efac" stroke-width="0.8"/>
          <text x="25" y="73" font-size="6.5" font-weight="bold" fill="#166534">Video Link: https://meet.google.com/stu-acad-guid</text>
          <text x="18" y="89" font-size="6.2" fill="#64748b"><tspan font-weight="bold">Agenda:</tspan> Proactive academic review, resource navigation, course planning.</text>
          <text x="18" y="98" font-size="5.8" font-style="italic" fill="#94a3b8">Initiated by StudentDropout Retention Engine &middot; Approved by Counselor &middot; 7-Day Cooldown</text>
        </svg>
        <div class="figure-caption"><span class="fig-title">Fig. 6.</span> Generated academic support session calendar card, illustrating non-stigmatizing neutral titling, video conferencing link, and human counselor oversight attribution.</div>
      </div>

      <div class="subsection-title">K. Cooldown Governance &amp; Security</div>
      <p class="no-indent">A crucial safeguard against student anxiety and advisor alert fatigue is the 7-day cooldown engine. When an automated booking is executed, the database updates <code>lastInterventionTimestamp</code>. Any subsequent high-risk scores received within the 7-day window are recorded in the audit log but suppressed from triggering repeat calendar reservations. Password credentials are encrypted using <code>bcrypt</code> (salt rounds 10), and stateless HMAC-SHA256 JWT tokens expire after 60 minutes. Multi-tenant database isolation is enforced via institutional <code>companyCode</code> scoping.</p>

      <div class="subsection-title">L. Intervention Lifecycle &amp; Audit Trails</div>
      <p class="no-indent">Every student transition is audited via state progression: <code>PENDING &rarr; FLAGGED &rarr; APPROVED &rarr; SCHEDULED &rarr; COMPLETED</code>. Counselors may override recommendations by appending timestamped case notes, ensuring algorithmic guidance never circumvents human professional judgment. All calendar booking transactions log unique event identifiers, timestamps, and recipient hashes for independent compliance audits.</p>
    </div>
  </div>
  {get_footer(7)}
</div>
"""

# ============================================================
# PAGE 8: Results Section + Tables V+VI + Fig 5 + Feature Importance
# ============================================================
page8 = f"""
<div class="page" id="page-8">
  {get_header()}
  <div class="page-content two-column">
    <div class="section-title">IV. RESULTS</div>
    
    <div class="subsection-title">A. Classification Performance</div>
    <p class="no-indent">The soft-voting ensemble was evaluated on the held-out test split of 2,368 student instances (1,606 Retained, 762 Dropout Risk). To benchmark discrimination, performance was contrasted with a Zero-Rule majority-class baseline. Table V summarizes empirical metrics.</p>

    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE V.</span> HELD-OUT TEST SET PERFORMANCE (N = 2,368)</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th>Metric</th>
            <th>Majority Baseline</th>
            <th>Ensemble</th>
            <th>Absolute &Delta;</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Accuracy</td>
            <td>0.6782 (67.82%)</td>
            <td><b>0.8421 (84.21%)</b></td>
            <td>+16.39%</td>
          </tr>
          <tr>
            <td>Precision (1)</td>
            <td>0.0000 (0.00%)</td>
            <td><b>0.7939 (79.39%)</b></td>
            <td>+79.39%</td>
          </tr>
          <tr>
            <td>Recall (1)</td>
            <td>0.0000 (0.00%)</td>
            <td><b>0.6877 (68.77%)</b></td>
            <td>+68.77%</td>
          </tr>
          <tr>
            <td>F1-Score (1)</td>
            <td>0.0000 (0.00%)</td>
            <td><b>0.7370 (73.70%)</b></td>
            <td>+73.70%</td>
          </tr>
          <tr>
            <td>ROC-AUC</td>
            <td>0.5000 (50.00%)</td>
            <td><b>0.8925 (89.25%)</b></td>
            <td>+39.25%</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>The soft-voting ensemble demonstrates strong discrimination (84.21% accuracy, 89.25% ROC-AUC). On the positive minority class, the model achieves 79.39% precision and 68.77% recall (F1 = 73.70%). The confusion matrix at &tau;<sub>0</sub> = 0.50 is presented in Table VI.</p>

    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE VI.</span> CONFUSION MATRIX AT &tau;<sub>0</sub> = 0.50</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th>Actual</th>
            <th>Pred. Retained (0)</th>
            <th>Pred. Risk (1)</th>
            <th>Total</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Retained (0)</td>
            <td>TN = 1,470 (91.5%)</td>
            <td>FP = 136 (8.5%)</td>
            <td>1,606</td>
          </tr>
          <tr>
            <td>Risk (1)</td>
            <td>FN = 238 (31.2%)</td>
            <td>TP = 524 (68.8%)</td>
            <td>762</td>
          </tr>
          <tr>
            <td><b>Total</b></td>
            <td><b>1,708</b></td>
            <td><b>660</b></td>
            <td><b>2,368</b></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="figure-container">
      <!-- SVG Fig 5 Bar Chart -->
      <svg viewBox="0 0 340 110" style="width: 100%; max-width: 340px; height: auto; font-family: 'Times New Roman', serif;">
        <line x1="45" y1="10" x2="45" y2="88" stroke="#475569" stroke-width="1.2"/>
        <line x1="45" y1="88" x2="330" y2="88" stroke="#475569" stroke-width="1.2"/>
        <line x1="40" y1="88" x2="330" y2="88" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="91" font-size="7" text-anchor="end" fill="#475569">0%</text>
        <line x1="40" y1="49" x2="330" y2="49" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="52" font-size="7" text-anchor="end" fill="#475569">50%</text>
        <line x1="40" y1="10" x2="330" y2="10" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="13" font-size="7" text-anchor="end" fill="#475569">100%</text>
        <rect x="58" y="21" width="38" height="67" fill="#0284c7" rx="2"/>
        <text x="77" y="17" font-size="7" font-weight="bold" text-anchor="middle" fill="#0369a1">84.2%</text>
        <text x="77" y="100" font-size="7" text-anchor="middle" fill="#1e293b">Acc</text>
        <rect x="114" y="25" width="38" height="63" fill="#0ea5e9" rx="2"/>
        <text x="133" y="21" font-size="7" font-weight="bold" text-anchor="middle" fill="#0284c7">79.4%</text>
        <text x="133" y="100" font-size="7" text-anchor="middle" fill="#1e293b">Prec</text>
        <rect x="170" y="34" width="38" height="54" fill="#f59e0b" rx="2"/>
        <text x="189" y="30" font-size="7" font-weight="bold" text-anchor="middle" fill="#b45309">68.8%</text>
        <text x="189" y="100" font-size="7" text-anchor="middle" fill="#1e293b">Rec</text>
        <rect x="226" y="29" width="38" height="59" fill="#10b981" rx="2"/>
        <text x="245" y="25" font-size="7" font-weight="bold" text-anchor="middle" fill="#047857">73.7%</text>
        <text x="245" y="100" font-size="7" text-anchor="middle" fill="#1e293b">F1</text>
        <rect x="282" y="17" width="38" height="71" fill="#6366f1" rx="2"/>
        <text x="301" y="13" font-size="7" font-weight="bold" text-anchor="middle" fill="#4338ca">89.3%</text>
        <text x="301" y="100" font-size="7" text-anchor="middle" fill="#1e293b">AUC</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 5.</span> Test set model performance profile (N = 2,368).</div>
    </div>

    <div class="subsection-title">B. Feature Importance and Sensitivity Analysis</div>
    <p class="no-indent">Mean decrease in impurity (MDI) across ensemble trees illuminates the underlying psychometric drivers. Stress management accounts for over one-third of total predictive importance (34.2%), indicating that affective distress and academic overload are the earliest indicators of student disengagement. Cognitive academic engagement contributes 28.5%, while support satisfaction (21.1%) and peer belongingness (16.2%) provide secondary contextual signals.</p>

    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE VI-B.</span> ENSEMBLE GINI FEATURE IMPORTANCE BREAKDOWN</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Feature Domain</th>
            <th>RF Weight</th>
            <th>GBDT Weight</th>
            <th>Ensemble Mean</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td><code>stressManagement</code></td>
            <td>0.338</td>
            <td>0.346</td>
            <td><b>0.342 (34.2%)</b></td>
          </tr>
          <tr>
            <td>2</td>
            <td><code>academicEngagement</code></td>
            <td>0.291</td>
            <td>0.279</td>
            <td><b>0.285 (28.5%)</b></td>
          </tr>
          <tr>
            <td>3</td>
            <td><code>supportSatisfaction</code></td>
            <td>0.214</td>
            <td>0.208</td>
            <td><b>0.211 (21.1%)</b></td>
          </tr>
          <tr>
            <td>4</td>
            <td><code>peerBelongingness</code></td>
            <td>0.157</td>
            <td>0.167</td>
            <td><b>0.162 (16.2%)</b></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  {get_footer(8)}
</div>
"""

# ============================================================
# PAGE 9: Workflow Benchmarking + Tables VII+VIII + Eqs 9-10 + RQ Answers + Discussion A-D
# ============================================================
page9 = f"""
<div class="page" id="page-9">
  {get_header()}
  <div class="page-content two-column">
    <div class="subsection-title">C. Operational Workflow Benchmarking</div>
    <p class="no-indent">Verification across 50 simulated triage scenarios (20 Low, 15 Moderate, 15 High) evaluated automated slot discovery, Google Calendar dispatch, duplicate reservation suppression, and cooldown enforcement. Table VII details the operational performance parameters.</p>

    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE VII.</span> OPERATIONAL WORKFLOW METRICS</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th>Workflow Metric</th>
            <th>Denominator (N)</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Success Rate</td>
            <td>50 triage events</td>
            <td><b>100.0% (50/50)</b></td>
          </tr>
          <tr>
            <td>Mean Latency</td>
            <td>50 triage events</td>
            <td><b>1.38 &plusmn; 0.21 s</b></td>
          </tr>
          <tr>
            <td>Duplicate Rate</td>
            <td>15 auto-bookings</td>
            <td><b>0.00% (0/15)</b></td>
          </tr>
          <tr>
            <td>Cooldown Suppress</td>
            <td>10 rapid re-tests</td>
            <td><b>100.0% (10/10)</b></td>
          </tr>
          <tr>
            <td>Counselor Gate</td>
            <td>15 gated cases</td>
            <td><b>100.0% (15/15)</b></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="equation-box">
      <div class="math-expr">R<sub>succ</sub> = (N<sub>succ</sub> / N<sub>total</sub>) &times; 100%, &nbsp;&nbsp; T&#x0305;<sub>exec</sub> = (1/N) &sum; &Delta;t<sub>i</sub></div>
      <div class="eq-number">(9–10)</div>
    </div>

    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE VIII.</span> SUMMARY OF OBSERVED SYSTEM BEHAVIOR AND OPERATIONAL VERIFICATION</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th style="width:26%">Subsystem Function</th>
            <th style="width:36%">Observed Outcome</th>
            <th style="width:38%">Operational Verification &amp; Integrity Check</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>User Authentication</td>
            <td>JWT issued; role validated</td>
            <td>Protected endpoints strictly blocked without valid bearer token</td>
          </tr>
          <tr>
            <td>Survey Ingestion</td>
            <td>Captured 4 Likert scores</td>
            <td>Boundary validation enforced [1.0, 5.0]; invalid payloads rejected</td>
          </tr>
          <tr>
            <td>Cycle Locking</td>
            <td>Second POST rejected (HTTP 409)</td>
            <td>Compound unique index [studentId, academicCycle] locked successfully</td>
          </tr>
          <tr>
            <td>Ensemble Inference</td>
            <td>Scored within 145 ms</td>
            <td>Dual estimators combined via soft-voting; probabilities calibrated</td>
          </tr>
          <tr>
            <td>Counselor Triage</td>
            <td>Action dashboard updated</td>
            <td>Advisors view sorted queue; approve, reschedule, or snooze cases</td>
          </tr>
          <tr>
            <td>Calendar Dispatch</td>
            <td>Created Meet invitation</td>
            <td>Non-stigmatizing titling used; attendee email invited automatically</td>
          </tr>
          <tr>
            <td>Cooldown Lock</td>
            <td>Blocked repeat booking</td>
            <td>7-day window respected; subsequent surveys logged but not booked</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="subsection-title">D. Architectural Latency Decomposition</div>
    <p class="no-indent">Dissecting the mean 1.38-second scheduling latency across architectural stages reveals that network API handshakes constitute the primary overhead: Express request validation requires 42 ms, Python ensemble inference consumes 145 ms, MongoDB conflict-free slot query executes in 38 ms, Google Calendar API OAuth2 reservation requires 820 ms, and Nodemailer SMTP notification delivery consumes 335 ms.</p>

    <div class="subsection-title">E. Answers to the Research Questions</div>
    <p class="no-indent"><b>RQ1.</b> The soft-voting ensemble achieved 84.21% accuracy (+16.39 pp above majority baseline) and 89.25% ROC-AUC, outperforming single-model trees. <b>RQ2.</b> The dual-criteria triage policy successfully isolated acute intervention candidates (68.77% recall) while containing false positives to 8.47%. <b>RQ3.</b> The automated calendar engine achieved a mean latency of 1.38 seconds, zero calendar collisions, and 100% cooldown suppression compliance. <b>RQ4.</b> The counselor human-in-the-loop review stage ensured algorithmic risk scores remained decision-support recommendations rather than automated disciplinary actions.</p>

    <div class="section-title">V. DISCUSSION</div>
    
    <div class="subsection-title">A. Early Warning versus Definitive Retention Indicators</div>
    <p class="no-indent">The reported accuracy must be interpreted with academic discipline. Machine learning classifiers detect statistical correlations between engagement indicators and historical attrition patterns; they do not measure student disenrollment intent or cognitive potential. Labeling a student as "at-risk" risks inducing stereotype threat if communicated clumsily. For this reason, the StudentDropout architecture enforces strict counselor intermediation and neutral calendar naming conventions.</p>

    <div class="subsection-title">B. Class Imbalance, Calibration, and Cost Asymmetry</div>
    <p class="no-indent">In the experimental cohort, 32.20% of instances belong to the positive dropout class. The soft-voting ensemble's 84.21% accuracy represents an authentic +16.39 percentage point lift above a naive majority predictor. The 79.39% precision indicates that four out of five flagged students are in genuine academic distress, which preserves counselor credibility and institutional resources. Academic retention decisions exhibit profound cost asymmetry: Cost(FN) &gg; Cost(FP) justifies our sensitive dual-criteria policy.</p>

    <div class="subsection-title">C. Alert Fatigue Mitigation and Cognitive Load Balancing</div>
    <p class="no-indent">Prior academic early-warning systems have failed largely due to advisor alert fatigue: receiving hundreds of unranked email notifications causes staff to ignore the system entirely. By establishing a tri-level threshold policy and a mandatory 7-day cooldown between automated calendar bookings, StudentDropout paces intervention volume to institutional capacity, converting chaotic alert spikes into a steady stream of 3–5 high-priority consultations weekly.</p>

    <div class="subsection-title">D. Threats to Validity</div>
    <p class="no-indent">Table IX outlines methodological threats to validity and the mitigation strategies incorporated into this evaluation.</p>

    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE IX.</span> THREATS TO VALIDITY AND MITIGATION STRATEGIES</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th style="width:18%">Type</th>
            <th style="width:40%">Identified Threat</th>
            <th style="width:42%">Mitigation Implemented</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Construct</td>
            <td>Survey subjectivity &amp; Likert response bias</td>
            <td>Multi-dimensional aggregation; counselor review gate</td>
          </tr>
          <tr>
            <td>Internal</td>
            <td>Data leakage across splits</td>
            <td>Strict stratified splitting; training-only medians</td>
          </tr>
          <tr>
            <td>External</td>
            <td>Single-institution cohort limitations</td>
            <td>Multi-tenant schema designed for cross-campus scale</td>
          </tr>
          <tr>
            <td>Operational</td>
            <td>Calendar concurrency collisions</td>
            <td>Atomic MongoDB updates with state transition guards</td>
          </tr>
          <tr>
            <td>Ethical</td>
            <td>Student stigmatization &amp; alert fatigue</td>
            <td>Neutral meeting titles; 7-day mandatory cooldown</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  {get_footer(9)}
</div>
"""

# ============================================================
# PAGE 10: Discussion E-G + Limitations + Conclusion + Acknowledgment + References
# ============================================================
page10 = f"""
<div class="page" id="page-10">
  {get_header()}
  <div class="page-content two-column">
    <div class="subsection-title">E. Methodological and Practical Limitations</div>
    <p class="no-indent">Several methodological and practical limitations warrant explicit acknowledgment:</p>
    <ul>
      <li><b>Cross-Sectional Dataset Bounds:</b> The dataset captures standardized psychometric survey scores at discrete monthly intervals; it does not model continuous clickstream telemetry available in enterprise LMS environments.</li>
      <li><b>Absence of Longitudinal Causal Proof:</b> While technical feasibility and scheduling latency are verified, this study does not measure causal reductions in institutional dropout rates over a multi-year timeframe.</li>
      <li><b>Synthetic Scheduling Bench:</b> Calendar dispatch was validated across a staging test bench; institutional deployments with legacy CalDAV/Exchange servers may introduce protocol-specific edge cases.</li>
      <li><b>Fixed Survey Dimensions:</b> The current survey instrument relies on four fixed dimensions; incorporating natural language student feedback via sentiment analysis represents an important future enhancement.</li>
    </ul>

    <div class="subsection-title">F. Psychometric Construct Significance</div>
    <p class="no-indent">The primacy of <code>stressManagement</code> (34.2% Gini contribution) underscores that affective load and burnout precede visible academic collapse. Students in distress often maintain adequate grades during early weeks while their psychological capacity deteriorates. By capturing affective load before mid-term assessments, the platform enables preventative counseling during the optimal window of intervention.</p>

    <div class="subsection-title">G. Ethical Considerations and Institutional Governance</div>
    <p class="no-indent">Student educational records constitute sensitive personal data protected under regulations including FERPA and India's Digital Personal Data Protection (DPDP) Act, 2023. StudentDropout enforces role-based tenant isolation at the query level, prohibiting cross-institutional data visibility. Predictive scores are never exposed directly to students; instead, students receive supportive check-in invitations framed around course planning and resource navigation. Future deployments should commission independent algorithmic fairness audits disaggregating performance by demographic subgroup to detect and mitigate latent proxy discrimination in survey response distributions.</p>

    <div class="section-title">VI. CONCLUSION</div>
    <p class="no-indent">In this paper, we specified, implemented, and empirically evaluated an end-to-end platform integrating soft-voting ensemble machine learning with automated advisor meeting scheduling for student dropout prevention. Benchmarked on an institutional cohort of 9,470 records, the ensemble classifier achieves an accuracy of 84.21% (exceeding the majority-class baseline by 16.39 percentage points), an ROC-AUC of 89.25%, and a minority-class precision of 79.39%. In functional workflow testing across 50 simulated triage scenarios, the scheduling engine demonstrated a 100% execution success rate with a mean dispatch latency of 1.38 seconds, zero duplicate bookings, and strict adherence to counselor approval gates.</p>

    <p>The results demonstrate that operational workflow automation can be safely married to machine learning risk stratification when bounded by human-in-the-loop oversight and non-stigmatizing communication. Future work will focus on integrating real-time LMS clickstream telemetry (Canvas/Moodle LTI 1.3), federating the ensemble across multiple university campuses, and conducting randomized controlled trials to evaluate the causal retention impact of automated advisory scheduling.</p>

    <p>We emphasize that a predicted dropout score represents a probabilistic early warning indicator intended to mobilize compassionate academic support, rather than definitive evidence of a student's intention to disenroll. By grounding automated action in ethical human-in-the-loop oversight and non-stigmatizing communication, the StudentDropout architecture establishes a viable, scalable blueprint for closing the prediction-to-action gap in higher education retention.</p>

    <div class="section-title">ACKNOWLEDGMENT</div>
    <p class="no-indent">The authors express their sincere gratitude to Dr. Kalyani Hemant Deshmukh and the Department of Computer Science and Engineering, Prof. Ram Meghe Institute of Technology and Research (PRMITR), Badnera-Amravati, for their continuous academic guidance, technical encouragement and institutional support throughout this research.</p>

    <div class="section-title">REFERENCES</div>
    <ol class="references-list">
      <li>[1] V. Tinto, <i>Leaving College: Rethinking the Causes and Cures of Student Attrition</i>. Chicago, IL, USA: Univ. Chicago Press, 1993.</li>
      <li>[2] A. Seidman, <i>College Student Retention: Formula for Student Success</i>. Lanham, MD, USA: Rowman &amp; Littlefield, 2012.</li>
      <li>[3] J. Bound, M. F. Lovenheim, and S. Turner, "Why have college completion rates declined? An analysis of changing student preparation and collegiate resources," <i>Am. Econ. J. Appl. Econ.</i>, vol. 2, no. 3, pp. 129–157, 2010.</li>
      <li>[4] K. E. Arnold and M. D. Pistilli, "Course signals at Purdue: Using learning analytics to increase student success," in <i>Proc. 2nd Int. Conf. Learn. Anal. Knowl. (LAK '12)</i>, 2012, pp. 267–270.</li>
      <li>[5] R. S. Baker and P. S. Inventado, "Educational data mining and learning analytics," in <i>Learning Analytics: From Research to Practice</i>. New York, NY, USA: Springer, 2014, pp. 61–75.</li>
      <li>[6] C. Romero and S. Ventura, "Educational data mining and learning analytics: An updated survey," <i>WIREs Data Min. Knowl. Discov.</i>, vol. 10, no. 3, p. e1355, 2020.</li>
      <li>[7] L. Breiman, "Random forests," <i>Mach. Learn.</i>, vol. 45, no. 1, pp. 5–32, 2001.</li>
      <li>[8] J. H. Friedman, "Greedy function approximation: A gradient boosting machine," <i>Ann. Stat.</i>, vol. 29, no. 5, pp. 1189–1232, 2001.</li>
      <li>[9] F. Pedregosa et al., "Scikit-learn: Machine learning in Python," <i>J. Mach. Learn. Res.</i>, vol. 12, pp. 2825–2830, 2011.</li>
      <li>[10] R. Ferguson, "The state of learning analytics in 2012: A review and future challenges," KMI Tech. Rep. KMI-12-01, Open Univ., 2012.</li>
      <li>[11] D. Clow, "An overview of learning analytics," <i>Teach. High. Educ.</i>, vol. 18, no. 6, pp. 687–700, 2013.</li>
      <li>[12] G. L. Kramer, <i>Fostering Student Success in the Campus Community</i>. San Francisco, CA, USA: Jossey-Bass, 2007.</li>
      <li>[13] S. Slade and P. Prinsloo, "Learning analytics: Ethical issues and dilemmas," <i>Am. Behav. Sci.</i>, vol. 57, no. 10, pp. 1510–1529, 2013.</li>
      <li>[14] N. Mehrabi et al., "A survey on bias and fairness in machine learning," <i>ACM Comput. Surv.</i>, vol. 54, no. 6, pp. 1–35, 2021.</li>
      <li>[15] U.S. Dept. of Education, "Family Educational Rights and Privacy Act (FERPA)," 34 CFR Part 99, 2020.</li>
      <li>[16] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in <i>Adv. Neural Inf. Process. Syst. (NeurIPS)</i>, 2017, pp. 4765–4774.</li>
      <li>[17] J. Kuzilek, M. Hlosta, and Z. Zdrahal, "Open University Learning Analytics Dataset," <i>Sci. Data</i>, vol. 4, p. 170171, 2017.</li>
      <li>[18] P. Cortez and A. M. G. Silva, "Using data mining to predict secondary school student performance," in <i>Proc. 5th FUBUTEC</i>, 2008, pp. 5–12.</li>
      <li>[19] F. Agrusti, G. Bonavolont&agrave;, and M. Mezzini, "Analytical student dropout prediction in higher education using machine learning," <i>Int. J. Educ. Technol. High. Educ.</i>, vol. 17, p. 39, 2020.</li>
      <li>[20] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in <i>Proc. 22nd ACM SIGKDD</i>, 2016, pp. 785–794.</li>
      <li>[21] L. I. Kuncheva, <i>Combining Pattern Classifiers: Methods and Algorithms</i>. Hoboken, NJ, USA: Wiley, 2014.</li>
      <li>[22] N. V. Chawla et al., "SMOTE: Synthetic minority over-sampling technique," <i>J. Artif. Intell. Res.</i>, vol. 16, pp. 321–357, 2002.</li>
      <li>[23] H. He and E. A. Garcia, "Learning from imbalanced data," <i>IEEE Trans. Knowl. Data Eng.</i>, vol. 21, no. 9, pp. 1263–1284, 2009.</li>
      <li>[24] T. Saito and M. Rehmsmeier, "The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets," <i>PLoS ONE</i>, vol. 10, no. 3, p. e0118432, 2015.</li>
      <li>[25] D. M. W. Powers, "Evaluation: From precision, recall and F-measure to ROC, informedness, markedness and correlation," <i>J. Mach. Learn. Technol.</i>, vol. 2, no. 1, pp. 37–63, 2011.</li>
      <li>[26] A. Niculescu-Mizil and R. Caruana, "Predicting good probabilities with supervised learning," in <i>Proc. 22nd Int. Conf. Mach. Learn. (ICML)</i>, 2005, pp. 625–632.</li>
      <li>[27] M. Hlosta et al., "Modelling student dropout: What is the impact of different features?," in <i>Proc. EDM</i>, 2017.</li>
      <li>[28] B. K. Daniel, "Big Data and data science in higher education," <i>Int. J. Educ. Technol. High. Educ.</i>, vol. 12, no. 1, pp. 904–925, 2015.</li>
    </ol>
  </div>
  {get_footer(10)}
</div>
"""

complete_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Integrating Machine Learning Ensembles and Automated Advisory Workflows for Early Student Dropout Prediction</title>
<style>
  @page {{
    size: 210mm 297mm;
    margin: 0;
  }}
  
  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}

  body {{
    margin: 0;
    padding: 0;
    background-color: #f1f5f9;
    font-family: 'Times New Roman', Times, 'Nimbus Roman No9 L', serif;
    color: #000;
  }}

  .page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    margin: 0 auto;
    background: #ffffff;
    box-sizing: border-box;
    padding: 16pt 72pt 20pt 72pt;
    position: relative;
    page-break-after: always;
    break-after: page;
    overflow: hidden;
  }}

  @media screen {{
    .page {{
      margin-bottom: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }}
  }}

  /* Header */
  .header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 38pt;
    margin-bottom: 3pt;
  }}

  .header-logo {{
    width: 48pt;
    height: 36pt;
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .header-logo img {{
    width: 44pt;
    height: auto;
  }}

  .header-text {{
    flex: 1;
    text-align: center;
    margin-left: 8pt;
  }}

  .journal-title {{
    font-size: 9.6pt;
    font-weight: bold;
    line-height: 1.2;
    color: #000;
  }}

  .journal-meta {{
    font-size: 7.8pt;
    line-height: 1.2;
    color: #222;
  }}

  .header-rule {{
    width: 100%;
    height: 0.8px;
    background-color: #000;
    margin-bottom: 8pt;
  }}

  /* Footer */
  .footer-rule {{
    position: absolute;
    bottom: 36pt;
    left: 72pt;
    right: 72pt;
    height: 0.8px;
    background-color: #000;
  }}

  .footer {{
    position: absolute;
    bottom: 18pt;
    left: 72pt;
    right: 72pt;
    height: 16pt;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 8.0pt;
    color: #111;
  }}

  /* Content area */
  .page-content {{
    height: 708pt;
    overflow: hidden;
  }}

  .two-column {{
    column-count: 2;
    column-gap: 12pt;
    height: 100%;
    text-align: justify;
    text-justify: inter-word;
  }}

  .full-width {{
    column-span: all;
    width: 100%;
  }}

  /* Title Block */
  .title-block {{
    text-align: center;
    margin-bottom: 6pt;
  }}

  h1.paper-title {{
    font-size: 13.5pt;
    font-weight: bold;
    line-height: 1.22;
    margin: 0 0 5pt 0;
    color: #000;
  }}

  .author-names {{
    font-size: 9.8pt;
    font-weight: bold;
    margin-bottom: 2pt;
    line-height: 1.25;
  }}

  .author-affiliation {{
    font-size: 8.3pt;
    color: #222;
    margin-bottom: 2pt;
    line-height: 1.25;
  }}

  .author-email {{
    font-size: 8.0pt;
    color: #333;
    margin-bottom: 4pt;
    line-height: 1.25;
  }}

  .divider-rule {{
    text-align: center;
    font-size: 7.2pt;
    letter-spacing: 1px;
    color: #555;
    margin: 3pt 0 6pt 0;
  }}

  /* Section Headings */
  .section-title {{
    font-size: 9.6pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-top: 5pt;
    margin-bottom: 2pt;
    break-after: avoid;
    color: #000;
  }}

  .subsection-title {{
    font-size: 8.8pt;
    font-weight: bold;
    margin-top: 4pt;
    margin-bottom: 1.5pt;
    break-after: avoid;
    color: #000;
  }}

  /* Paragraphs */
  p {{
    font-size: 9.2pt;
    line-height: 1.26;
    margin-top: 0;
    margin-bottom: 2.5pt;
    text-indent: 10pt;
    text-align: justify;
    word-break: normal;
    hyphens: auto;
  }}

  p.no-indent {{
    text-indent: 0;
  }}

  p.abstract-para {{
    font-size: 8.6pt;
    line-height: 1.21;
    text-indent: 0;
    margin-bottom: 4pt;
    text-align: justify;
  }}

  .abstract-label {{
    font-weight: bold;
    font-style: italic;
  }}

  p.keywords-para {{
    font-size: 8.6pt;
    line-height: 1.21;
    text-indent: 0;
    margin-bottom: 6pt;
    text-align: justify;
  }}

  .keywords-label {{
    font-weight: bold;
    font-style: italic;
  }}

  /* Lists */
  ul {{
    margin: 0 0 3pt 0;
    padding-left: 12pt;
    font-size: 9.0pt;
    line-height: 1.24;
  }}

  li {{
    margin-bottom: 1.5pt;
    text-align: justify;
  }}

  /* Equations */
  .equation-box {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1pt 4pt;
    margin: 2.5pt 0;
    font-size: 8.6pt;
    font-style: italic;
  }}

  .math-expr {{
    flex: 1;
    text-align: center;
  }}

  .eq-number {{
    font-style: normal;
    font-weight: bold;
  }}

  /* Tables */
  .table-container {{
    margin: 4pt 0;
    width: 100%;
    break-inside: avoid;
  }}

  .table-caption {{
    font-size: 7.6pt;
    font-weight: bold;
    text-align: center;
    margin-bottom: 2pt;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}

  .caption-label {{
    font-weight: bold;
  }}

  table.academic-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.4pt;
    line-height: 1.16;
    margin: 0 auto;
  }}

  table.academic-table th {{
    border-top: 1.0px solid #000;
    border-bottom: 0.8px solid #000;
    padding: 2.5pt 2pt;
    text-align: left;
    font-weight: bold;
  }}

  table.academic-table td {{
    padding: 1.8pt 2pt;
    border-bottom: 0.4px solid #cbd5e1;
    text-align: left;
    vertical-align: top;
  }}

  table.academic-table tr:last-child td {{
    border-bottom: 1.0px solid #000;
  }}

  /* Figures */
  .figure-container {{
    margin: 4pt 0;
    text-align: center;
    break-inside: avoid;
    width: 100%;
  }}

  .figure-caption {{
    font-size: 7.5pt;
    line-height: 1.18;
    text-align: justify;
    margin-top: 2pt;
    color: #111;
  }}

  .fig-title {{
    font-weight: bold;
  }}

  /* References */
  ol.references-list {{
    margin: 0;
    padding-left: 10pt;
    font-size: 7.6pt;
    line-height: 1.18;
    list-style: none;
  }}

  ol.references-list li {{
    margin-bottom: 2pt;
    text-align: justify;
    padding-left: 0;
    text-indent: 0;
  }}

  code {{
    font-family: 'Courier New', monospace;
    font-size: 8.2pt;
  }}
</style>
</head>
<body>

{page1}
{page2}
{page3}
{page4}
{page5}
{page6}
{page7}
{page8}
{page9}
{page10}

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(complete_html)

print("HTML written successfully. Compiling PDF...")

chrome_cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={FINAL_PDF_PATH}",
    HTML_PATH
]

subprocess.run(chrome_cmd, check=True)
print("PDF generated successfully.")

# Inspect pages with PyMuPDF
doc = pymupdf.open(FINAL_PDF_PATH)
print(f"Total pages: {len(doc)}, size: {os.path.getsize(FINAL_PDF_PATH)} bytes")
for i, page in enumerate(doc):
    text_blocks = [b for b in page.get_text("blocks") if b[1] > 60 and b[3] < 820]
    if text_blocks:
        top_y = min(b[1] for b in text_blocks)
        bot_y = max(b[3] for b in text_blocks)
        clearance = 803 - bot_y
        print(f"  Page {i+1}: top_y={top_y:.1f}, bot_y={bot_y:.1f}, clearance_to_footer={clearance:.1f} pt")
    # Render PNG
    pix = page.get_pixmap(dpi=150)
    pix.save(os.path.join(PAGES_DIR, f"page_{i+1}.png"))

print("Done. Check pages/ folder for PNG previews.")
