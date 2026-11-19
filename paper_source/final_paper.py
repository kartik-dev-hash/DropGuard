import os, subprocess, base64, pymupdf

HTML_PATH   = r"d:\StudentDropout\paper_source\StudentDropout_Research_Paper.html"
PDF_PATH    = r"d:\StudentDropout\StudentDropout_Research_Paper.pdf"
PAGES_DIR   = r"d:\StudentDropout\paper_source\pages"
os.makedirs(PAGES_DIR, exist_ok=True)

with open(r"d:\StudentDropout\paper_source\logo_1.png","rb") as f:
    LOGO = base64.b64encode(f.read()).decode()

def H():
    return f"""
    <div class="header">
      <div class="header-logo"><img src="data:image/png;base64,{LOGO}" alt="IJSREM"></div>
      <div class="header-text">
        <div class="journal-title">International Journal of Scientific Research in Engineering and Management (IJSREM)</div>
        <div class="journal-meta">Volume: 10 Issue: 10 | Oct - 2026 &nbsp;&nbsp;&nbsp;&nbsp; SJIF Rating: 8.659 &nbsp;&nbsp;&nbsp;&nbsp; ISSN: 2582-3930</div>
      </div>
    </div><div class="header-rule"></div>"""

def F(n):
    return f"""
    <div class="footer-rule"></div>
    <div class="footer"><div>&copy; 2026, IJSREM &nbsp;|&nbsp; https://ijsrem.com &nbsp;|&nbsp; DOI: &nbsp;|&nbsp; Page {n}</div></div>"""

# ===========================================================
# PAGE 1 — Title, Authors, Abstract, Keywords, Intro A+B
# ===========================================================
p1 = f"""<div class="page" id="p1">{H()}
  <div class="title-block">
    <h1 class="paper-title">Integrating Machine Learning Ensembles and Automated Advisory Workflows for Early Student Dropout Prediction and Support Intervention Scheduling</h1>
    <div class="author-names">Kartik Nilesh Raghuwanshi<sup>1</sup>, Dr. Kalyani Hemant Deshmukh<sup>2</sup></div>
    <div class="author-affiliation"><sup>1</sup>B.Tech Final-Year Student, <sup>2</sup>Guide, Department of Computer Science and Engineering<br>
      Prof. Ram Meghe Institute of Technology and Research, Badnera-Amravati, Maharashtra, India</div>
    <div class="author-email">Corresponding e-mail: raghuwanshikartik521@gmail.com, khdeshmukh@mitra.ac.in</div>
    <div class="divider-rule">-------------------------------------------------------------***-------------------------------------------------------------</div>
  </div>
  <div class="page-content two-col">
    <p class="abstract-para"><span class="abstract-label"><i>Abstract&mdash;</i></span> Higher education institutions face significant student attrition rates that adversely impact institutional sustainability, degree completion metrics, and individual socioeconomic mobility. While supervised machine learning models can identify students exhibiting early signs of academic disengagement, generating a probabilistic risk score in isolation rarely initiates timely institutional intervention. This paper presents an end-to-end early warning and automated intervention platform that couples a dual-algorithm soft-voting ensemble classifier (combining Random Forest and Gradient Boosted Decision Trees) with an automated academic advisor meeting-scheduling engine. The predictive pipeline is evaluated on an institutional cohort of 9,470 student records parameterized across four core psychometric and academic engagement dimensions, exhibiting a 32.20% positive dropout-risk class prevalence. Model inferences are governed by an actionable dual-criteria triage policy: students scoring below critical survey thresholds (&le;2.5/5.0) or generating ensemble predicted dropout probabilities <i>p</i>(<b>x</b>)&ge;0.50 trigger retention workflows, with direct calendar slot reservation activated at high risk (<i>p</i>(<b>x</b>)&ge;0.80) subject to mandatory human counselor review and a 7-day cooldown mechanism. On a held-out test split of 2,368 students, the soft-voting ensemble achieves an accuracy of 84.21% (exceeding the 67.82% majority-class baseline by 16.39 percentage points), precision of 79.39%, recall of 68.77%, F1-score of 73.70%, and ROC-AUC of 89.25%. In operational test-bench verification across 50 simulated triage scenarios, the automated calendar scheduling engine recorded a 100% execution success rate with a mean dispatch latency of 1.38 seconds, zero duplicate calendar bookings, and 100% adherence to human counselor approval gates. The test bench evaluates a cross-sectional dataset; this study does not measure longitudinal graduation rates or causal attrition reduction in live environments. A predicted risk score is a probabilistic early-warning indicator for supportive guidance, not definitive evidence of disenrollment intent.</p>
    <p class="keywords-para"><span class="keywords-label"><i>Key Words&mdash;</i></span> Student dropout prediction, Ensemble machine learning, Random Forest, Gradient Boosting, Academic advising automation, Early warning system, Human-in-the-loop, Algorithmic fairness, Educational data mining.</p>
    <div class="section-title">I. INTRODUCTION</div>
    <div class="subsection-title">A. Background and Motivation</div>
    <p>Student attrition remains one of the most pressing structural and socioeconomic challenges confronting global higher education institutions [1]. Empirical studies indicate that between 25% and 40% of enrolled undergraduate students withdraw or disengage permanently prior to degree completion, with the acute attrition window occurring during the initial four semesters of study [2]. Beyond the substantial institutional revenue losses associated with uncollected tuition and underutilized academic facilities, student departure produces long-term personal economic scarring, diminishes social mobility, and compromises institutional completion benchmarks mandated by academic accrediting bodies [3].</p>
    <p>Historically, academic institutions have relied on retrospective early warning mechanisms, such as mid-term grade reports, delinquent tuition flags, and post-hoc academic probation notifications [4]. However, by the time academic failure or non-attendance appears on official transcripts, the underlying psychosocial, environmental, or financial stressors have typically compounded to an irreversible degree [5]. Educational Data Mining (EDM) and Learning Analytics (LA) have emerged to address this latency by training supervised machine learning models to identify subtle risk patterns across demographic, psychometric, and institutional feedback records [6]. The confluence of affordable cloud computing and expanding institutional data warehouses has dramatically lowered the barrier to deploying such models at scale.</p>
    <p>Ensemble machine learning architectures&mdash;most notably bagging via Random Forests and boosting via Gradient Boosted Decision Trees (GBDT)&mdash;have demonstrated superior predictive discrimination on tabular, non-linear educational data compared to classical logistic regression and over-parameterized deep neural networks [7, 8]. By combining a diverse manifold of randomized decision trees that minimize variance with sequential gradient-guided decision stumps that iteratively minimize residual bias, soft-voting ensembles deliver calibrated class probabilities that reflect multi-dimensional student vulnerability [9].</p>
    <p>Despite these algorithmic advances, the operationalization of early warning systems within higher education exhibits a persistent structural defect: the decoupling of risk detection from institutional intervention [10]. Commercial analytics packages frequently compute risk percentiles that populate administrative dashboards without triggering concrete advisory workflows. Overburdened faculty advisors, faced with unranked rosters containing hundreds of flagged students, experience cognitive overload and alert fatigue, resulting in intervention delays that render model predictions functionally inert [11].</p>
    <div class="subsection-title">B. Research Problem and Core Contributions</div>
    <p>The research problem addressed here is how to combine an in-semester psychometric feedback instrument, a soft-voting ensemble classifier, a dual-criteria triage policy, and a conflict-free calendar scheduling engine into a fault-tolerant, privacy-conscious web platform, and how to evaluate its predictive accuracy and operational execution under measurable engineering criteria. This paper presents <b>StudentDropout</b>, establishing four foundational contributions:</p>
    <ul>
      <li>An end-to-end architecture linking multi-tenant web portals, student survey capture, an ensemble ML classifier, dual-criteria triage policies, and an automated calendar slot allocation engine.</li>
      <li>A dual-stage evaluation protocol separating classifier discrimination metrics (accuracy, precision, recall, F1, ROC-AUC) from operational workflow parameters (latency, success rate, duplicate booking rate), explicitly stating denominators for all findings.</li>
      <li>A human-in-the-loop decision-support framework incorporating counselor review queues, non-stigmatizing calendar artifacts, role-based data isolation, and a 7-day cooldown mechanism to address ethical and privacy mandates.</li>
      <li>An empirical benchmark on 9,470 verified student records achieving 84.21% accuracy (+16.39 pp above majority baseline) and validating automated advisory slot scheduling within 1.38 seconds across 50 functional test runs.</li>
    </ul>
  </div>{F(1)}</div>"""

# ===========================================================
# PAGE 2 — Paper Org, Lit Review A–C (expanded)
# ===========================================================
p2 = f"""<div class="page" id="p2">{H()}
  <div class="page-content two-col">
    <div class="subsection-title">C. Paper Organization</div>
    <p class="no-indent">The remainder of this paper is organized as follows. Section II reviews related literature in educational data mining, ensemble learning, class imbalance handling, and advisory intervention systems. Section III details the methodology, dataset characteristics, ensemble mathematical formulations, and system architecture. Section IV presents empirical results from both classifier evaluation and operational workflow verification. Section V discusses threats to validity, alert fatigue mitigation, and methodological limitations. Section VI concludes the paper and identifies future research trajectories.</p>

    <div class="section-title">II. LITERATURE REVIEW</div>

    <div class="subsection-title">A. Supervised Machine Learning in Student Attrition</div>
    <p class="no-indent">Supervised classification has become the preeminent paradigm for modeling student departure [12]. Early studies utilized binary logistic regression and Naive Bayes classifiers on cumulative grade point averages (GPA) and credit accumulation tallies [13]. While interpretable, linear models exhibit poor sensitivity when modeling non-linear interactions among psychological distress, institutional satisfaction, and academic performance [14]. These limitations motivated the adoption of kernel-based support vector machines (SVMs) and decision trees, which demonstrated moderate improvements on small institutional datasets but suffered from high parameter sensitivity and poor probability calibration.</p>
    <p>The introduction of multi-layer perceptrons and deep neural networks offered enhanced non-linear modeling capacity, but often at the cost of catastrophic overfitting on moderate-sized institutional cohorts (&lt;20,000 records) and a lack of interpretability that hindered counselor adoption [15, 16]. Additionally, deep learning architectures demand substantial labeled training data and GPU-accelerated training infrastructure rarely available in higher education IT environments. Consequently, decision-tree ensembles have emerged as the standard benchmark in educational data mining [17], offering a practically achievable balance of predictive power, interpretability, and computational efficiency.</p>

    <div class="subsection-title">B. Ensemble Tree Methods on Tabular Educational Data</div>
    <p class="no-indent">Empirical analyses consistently demonstrate that tree-based ensembles outperform deep neural architectures on heterogeneous tabular datasets [18]. Random Forests aggregate randomized decision trees via bootstrap aggregation, effectively reducing variance and resisting label noise inherent in self-reported student surveys [7]. Each tree in the forest is trained on an independently sampled bootstrap replicate of the training data, and splits are selected from a random feature subset at each node. This deliberate injection of randomness de-correlates individual trees and produces ensemble predictions that are more stable across institutional cohort subpopulations than any single estimator. Conversely, Gradient Boosted Decision Trees sequentially construct shallow trees that fit the negative gradient of the binomial log-likelihood loss, driving down bias in hard-to-classify decision boundaries [8, 19].</p>
    <p>Recent research confirms that combining bagging and boosting via soft-voting ensembles mitigates individual estimator pathologies: the variance-reduction property of Random Forest prevents the sequential learner from over-specializing on outlier responses, while GBDT refines decision boundaries in overlapping risk regions [20, 21]. Comparative benchmarks on institutional educational datasets of 5,000–50,000 student records consistently report ROC-AUC gains of 3–8% for ensemble combinations over single-algorithm baselines, while maintaining sub-second inference latency appropriate for real-time advisory workflows.</p>

    <div class="subsection-title">C. Class Imbalance, Calibration, and Metric Selection</div>
    <p class="no-indent">A persistent challenge in attrition modeling is class imbalance [22]. In stable academic institutions, positive dropout prevalence typically ranges between 15% and 35%, rendering naive accuracy an inadequate evaluation metric [23]. A zero-rule classifier that unilaterally predicts student persistence achieves high nominal accuracy while failing to identify a single student at risk [24]. Several mitigation strategies have been proposed, including the Synthetic Minority Over-sampling Technique (SMOTE), class-weighted loss functions, and threshold calibration via isotonic regression or Platt scaling. Our experimental cohort exhibits a 32.20% positive class prevalence, which falls within a naturally challenging imbalance range for precision-sensitive institutional deployments.</p>
    <p>Scholars emphasize that early-warning models must be evaluated using precision, recall, macro F1-score, and area under the precision-recall and ROC curves (PR-AUC, ROC-AUC) [24, 25]. Furthermore, uncalibrated risk probabilities distort downstream triage rules; ensemble soft-voting provides smoother posterior probabilities that align with risk-stratified operational thresholds [26]. Proper calibration is especially critical for our dual-criteria policy: a poorly calibrated model assigning <i>p</i>(<b>x</b>)=0.81 to retained students would trigger unnecessary automated calendar bookings, eroding counselor trust and wasting institutional resources.</p>
  </div>{F(2)}</div>"""

# ===========================================================
# PAGE 3 — Lit Review D–E + Table I + Section III start
# ===========================================================
p3 = f"""<div class="page" id="p3">{H()}
  <div class="page-content two-col">
    <div class="subsection-title">D. Actionable Interventions and Academic Advisor Decision Support</div>
    <p class="no-indent">While algorithmic modeling of dropout has received exhaustive academic attention, the translation of model outputs into automated institutional workflows remains sparse [27]. In traditional institutional setups, early-warning platforms generate bulk CSV reports or static dashboard widgets requiring advisors to manually correlate risk scores with office hours and student course timetables [28]. This manual handoff introduces critical latency that negates the time-sensitivity advantage of real-time ML inference. Field experiments by Arnold and Pistilli on Purdue University's <i>Course Signals</i> demonstrated that timely, personalized student outreach can improve course retention by up to 10.3% [4]. However, manual intervention scheduling introduces severe latency: advisors often contact flagged students days or weeks after risk detection, during which academic failure may solidify [29].</p>
    <p>Contemporary research in intelligent tutoring systems and conversational agents has demonstrated that automating the outreach step&mdash;using AI-driven email composition or calendar booking&mdash;significantly reduces advisor workload while increasing the percentage of at-risk students who actually attend a supportive consultation [27]. Linking ML inference directly to calendar reservation engines bridges this critical operational gap and transforms early-warning platforms from passive dashboards into active institutional retention infrastructures. However, such automation must incorporate mandatory human authorization gates to prevent purely algorithmic decisions from overriding professional academic judgment.</p>

    <div class="subsection-title">E. Comparative Analysis and Identified Research Gap</div>
    <p class="no-indent">Table I synthesizes representative prior studies in student attrition prediction and intervention systems. Existing platforms either excel in predictive modeling while neglecting intervention workflows, or provide workflow automation without calibrated ML intelligence. The StudentDropout platform bridges this gap by unifying dual-ensemble inference, multi-criteria triage, counselor oversight, and automated calendar scheduling within a single, verifiable production architecture, accompanied by explicit operational benchmarking metrics with stated denominators.</p>

    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE I.</span>&nbsp; COMPARATIVE SUMMARY OF PRIOR ART AND PROPOSED PLATFORM</div>
      <table class="academic-table">
        <thead><tr>
          <th style="width:7%">Ref.</th>
          <th style="width:17%">Dataset / Setting</th>
          <th style="width:17%">Methodology</th>
          <th style="width:27%">Key Finding</th>
          <th style="width:32%">Relevance to StudentDropout</th>
        </tr></thead>
        <tbody>
          <tr><td>[4]</td><td>Purdue (N=23,000)</td><td>LMS + Naive Bayes</td><td>Early warning improved retention by 10.3%</td><td>Demonstrates intervention value; lacks automated scheduling</td></tr>
          <tr><td>[17]</td><td>OULAD (N=32,593)</td><td>Decision Trees, LR</td><td>Engagement clickstreams predict completion (AUC 0.86)</td><td>Validates engagement telemetry as strong retention signal</td></tr>
          <tr><td>[18]</td><td>45 Tabular Benchmarks</td><td>XGBoost vs. Neural Nets</td><td>Tree boosting outperforms deep models by 6.2% F1</td><td>Justifies tree-based ensemble for tabular surveys</td></tr>
          <tr><td>[24]</td><td>Imbalanced Benchmarks</td><td>PR-AUC vs. ROC-AUC</td><td>PR-AUC isolates minority class under class skew</td><td>Governs metric reporting protocol and baselines</td></tr>
          <tr><td>[28]</td><td>UK Higher Ed (N=1,200)</td><td>Manual Advisor Dashboards</td><td>Alert fatigue; outreach delayed by 8.4 days</td><td>Motivates automated, cooldown-protected dispatch</td></tr>
          <tr><td><b>Ours</b></td><td><b>Cohort (N=9,470)</b></td><td><b>RF + GBDT Soft-Voting</b></td><td><b>84.21% acc, 89.25% AUC; 1.38s scheduling</b></td><td><b>Unifies predictive ML with automated calendar booking</b></td></tr>
        </tbody>
      </table>
    </div>

    <div class="section-title">III. METHODOLOGY</div>

    <div class="subsection-title">A. Formal Problem Formulation</div>
    <p class="no-indent">Let <i>S</i> denote an institution with <i>K</i> registered academic tenants. For a student <i>i</i> enrolled within tenant <i>k</i>, let <b>x</b><sub><i>i</i></sub>=[<i>x</i><sub>1</sub>,<i>x</i><sub>2</sub>,<i>x</i><sub>3</sub>,<i>x</i><sub>4</sub>]<sup>T</sup>&isin;[1.0,5.0]<sup>4</sup> represent a multidimensional survey feature vector capturing academic engagement, support satisfaction, stress management, and belongingness. Let <i>Y</i><sub><i>i</i></sub>&isin;{0,1} denote the binary retention state. The prediction objective is to learn <i>f</i>:<b>x</b><sub>i</sub>&rarr;<i>p</i>(<b>x</b><sub>i</sub>), where <i>p</i>(<b>x</b><sub>i</sub>)=<i>P</i>(<i>Y</i><sub>i</sub>=1|<b>x</b><sub>i</sub>). Four research questions guide evaluation. <b>RQ1:</b> Does a soft-voting ensemble achieve superior accuracy over baseline heuristics? <b>RQ2:</b> Can dual-criteria triage isolate acute candidates without prohibitive false-positive burdens? <b>RQ3:</b> Does the calendar engine achieve sub-2s latency with zero collisions? <b>RQ4:</b> How does a human-in-the-loop authorization stage mitigate ethical vulnerabilities?</p>
  </div>{F(3)}</div>"""

# ===========================================================
# PAGE 4 — System Architecture + Fig 1 + detailed component description
# ===========================================================
p4 = f"""<div class="page" id="p4">{H()}
  <div class="page-content two-col">
    <div class="subsection-title">B. System Architecture Overview</div>
    <p class="no-indent">The platform consists of ten modular functional components organized into four logical tiers, as illustrated in Fig.&nbsp;1. The <i>Ingestion and Portal Tier</i> encompasses the student self-assessment portal, the academic counselor triage action center, and the platform administrator dashboard, all secured behind HMAC-SHA256 JWT authentication with role-based access control (RBAC). A database-level cycle locking engine enforces survey submission integrity via a compound unique index on <code>[studentId, academicCycle]</code>, preventing duplicate responses within the same academic period.</p>
    <p>The <i>Data Engine and Persistence Tier</i> performs boundary validation ([1.0,&nbsp;5.0]), z-score normalization of the four-dimensional feature vector, and multi-tenant data segregation via an institutional <code>companyCode</code> scoping mechanism, guaranteeing that counselors from one institution cannot access student records from another tenant. The <i>Ensemble ML Core</i> exposes a REST microservice endpoint that receives a validated feature vector and returns a calibrated posterior dropout risk probability within 145&nbsp;ms. Finally, the <i>Intervention and Workflow Tier</i> evaluates the dual-criteria triage policy, manages the counselor review queue, and executes the conflict-free calendar scheduling engine when intervention is warranted.</p>

    <div class="figure-container full-width" style="margin:3px 0 3px 0;">
      <svg viewBox="0 0 720 178" style="width:100%;max-width:720px;height:auto;font-family:'Times New Roman',serif;">
        <defs>
          <linearGradient id="ga" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#f8fafc"/><stop offset="100%" style="stop-color:#e2e8f0"/></linearGradient>
          <linearGradient id="gb" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#f0f9ff"/><stop offset="100%" style="stop-color:#bae6fd"/></linearGradient>
          <linearGradient id="gc" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#fefce8"/><stop offset="100%" style="stop-color:#fef08a"/></linearGradient>
          <linearGradient id="gd" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#f0fdf4"/><stop offset="100%" style="stop-color:#bbf7d0"/></linearGradient>
          <marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#334155"/></marker>
        </defs>
        <rect x="6" y="8" width="128" height="162" rx="5" fill="url(#ga)" stroke="#94a3b8" stroke-width="1.2"/>
        <text x="70" y="22" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">1. Ingestion &amp; Portals</text>
        <rect x="14" y="28" width="112" height="26" rx="3" fill="#fff" stroke="#cbd5e1" stroke-width="0.8"/><text x="70" y="40" font-size="7.5" text-anchor="middle" fill="#1e293b">Student Portal</text><text x="70" y="49" font-size="6" text-anchor="middle" fill="#64748b">(Monthly Survey)</text>
        <rect x="14" y="60" width="112" height="26" rx="3" fill="#fff" stroke="#cbd5e1" stroke-width="0.8"/><text x="70" y="72" font-size="7.5" text-anchor="middle" fill="#1e293b">Counselor Portal</text><text x="70" y="81" font-size="6" text-anchor="middle" fill="#64748b">(Triage Action Center)</text>
        <rect x="14" y="92" width="112" height="26" rx="3" fill="#fff" stroke="#cbd5e1" stroke-width="0.8"/><text x="70" y="104" font-size="7.5" text-anchor="middle" fill="#1e293b">Platform Admin</text><text x="70" y="113" font-size="6" text-anchor="middle" fill="#64748b">(Tenant &amp; RBAC)</text>
        <rect x="14" y="124" width="112" height="26" rx="3" fill="#f8fafc" stroke="#0284c7" stroke-width="0.8"/><text x="70" y="136" font-size="7" font-weight="bold" text-anchor="middle" fill="#0369a1">Cycle Locking</text><text x="70" y="145" font-size="6" text-anchor="middle" fill="#64748b">Compound Unique Index</text>
        <line x1="134" y1="88" x2="158" y2="88" stroke="#334155" stroke-width="1.5" marker-end="url(#ar)"/>
        <rect x="162" y="8" width="128" height="162" rx="5" fill="url(#gb)" stroke="#7dd3fc" stroke-width="1.2"/>
        <text x="226" y="22" font-size="8" font-weight="bold" text-anchor="middle" fill="#0369a1">2. Data Engine &amp; DB</text>
        <rect x="170" y="30" width="112" height="32" rx="3" fill="#fff" stroke="#bae6fd" stroke-width="0.8"/><text x="226" y="44" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0284c7">Feature Normalizer</text><text x="226" y="54" font-size="6" text-anchor="middle" fill="#475569">4-D Psychometrics [1,5]</text>
        <rect x="170" y="70" width="112" height="36" rx="3" fill="#fff" stroke="#bae6fd" stroke-width="0.8"/><text x="226" y="83" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0284c7">MongoDB Database</text><text x="226" y="93" font-size="6" text-anchor="middle" fill="#475569">Tenants, Feedback,</text><text x="226" y="102" font-size="6" text-anchor="middle" fill="#475569">RetentionActions</text>
        <rect x="170" y="114" width="112" height="32" rx="3" fill="#fff" stroke="#bae6fd" stroke-width="0.8"/><text x="226" y="128" font-size="7" font-weight="bold" text-anchor="middle" fill="#0284c7">Tenant Scoping</text><text x="226" y="138" font-size="6" text-anchor="middle" fill="#475569">CompanyCode Isolation</text>
        <line x1="290" y1="88" x2="316" y2="88" stroke="#334155" stroke-width="1.5" marker-end="url(#ar)"/>
        <rect x="320" y="8" width="148" height="162" rx="5" fill="url(#gc)" stroke="#fde047" stroke-width="1.2"/>
        <text x="394" y="22" font-size="8" font-weight="bold" text-anchor="middle" fill="#854d0e">3. Ensemble ML Core</text>
        <rect x="328" y="30" width="132" height="32" rx="3" fill="#fff" stroke="#fef08a" stroke-width="0.8"/><text x="394" y="44" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#a16207">Random Forest (B=180)</text><text x="394" y="54" font-size="6" text-anchor="middle" fill="#713f12">Variance Reduction / Bagging</text>
        <rect x="328" y="70" width="132" height="32" rx="3" fill="#fff" stroke="#fef08a" stroke-width="0.8"/><text x="394" y="84" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#a16207">Gradient Boost (M=150)</text><text x="394" y="94" font-size="6" text-anchor="middle" fill="#713f12">Residual Boosting / Shrinkage</text>
        <rect x="328" y="110" width="132" height="36" rx="3" fill="#fef9c3" stroke="#eab308" stroke-width="1"/><text x="394" y="124" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#713f12">Soft-Voting Fusion</text><text x="394" y="134" font-size="6" text-anchor="middle" fill="#854d0e">p(x) = 0.5(P_RF + P_GB)</text><text x="394" y="143" font-size="5.8" text-anchor="middle" fill="#a16207">Calibrated Risk Probability</text>
        <line x1="468" y1="88" x2="492" y2="88" stroke="#334155" stroke-width="1.5" marker-end="url(#ar)"/>
        <rect x="496" y="8" width="218" height="162" rx="5" fill="url(#gd)" stroke="#86efac" stroke-width="1.2"/>
        <text x="605" y="22" font-size="8" font-weight="bold" text-anchor="middle" fill="#166534">4. Intervention &amp; Workflow</text>
        <rect x="504" y="30" width="202" height="32" rx="3" fill="#fff" stroke="#bbf7d0" stroke-width="0.8"/><text x="605" y="44" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#15803d">Dual-Criteria Triage Rule</text><text x="605" y="54" font-size="6" text-anchor="middle" fill="#166534">p(x)&ge;0.50 OR min(x_j)&le;2.5</text>
        <rect x="504" y="70" width="202" height="32" rx="3" fill="#fff" stroke="#bbf7d0" stroke-width="0.8"/><text x="605" y="84" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#15803d">Counselor Action Center</text><text x="605" y="94" font-size="6" text-anchor="middle" fill="#166534">Human Gate: Approve / Snooze</text>
        <rect x="504" y="110" width="202" height="36" rx="3" fill="#dcfce7" stroke="#22c55e" stroke-width="1"/><text x="605" y="124" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#14532d">Automated Calendar Dispatch</text><text x="605" y="134" font-size="6" text-anchor="middle" fill="#15803d">30-min Slot &middot; 7-Day Cooldown</text><text x="605" y="143" font-size="5.8" text-anchor="middle" fill="#166534">Google Meet Invitation &amp; Nodemailer</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig.&nbsp;1.</span> End-to-end modular architecture of the StudentDropout platform illustrating survey ingestion, cycle locking, database persistence, dual-ensemble scoring, dual-criteria triage, and automated calendar scheduling.</div>
    </div>

    <div class="subsection-title">B2. Multi-Tenancy, Security, and Component Interactions</div>
    <p class="no-indent">The platform is engineered as a multi-tenant Software-as-a-Service (SaaS) architecture, enabling multiple academic institutions (tenants) to share a single deployment while maintaining strict data isolation. Each tenant is provisioned with a unique <code>companyCode</code> identifier embedded in all database queries and JWT tokens, preventing cross-tenant data leakage at the ORM layer. Backend-to-ML-service communication occurs over an authenticated internal HTTP channel using a shared service secret, ensuring that the ML microservice cannot be queried externally without passing through the Express API gateway's authorization middleware.</p>
    <p>The scheduling subsystem employs optimistic concurrency control: when the meeting allocator identifies an available 30-minute slot, it issues an atomic <code>findOneAndUpdate</code> MongoDB operation that simultaneously checks the slot's availability status and reserves it, preventing double-booking under concurrent advisor approval events. All inter-service communication is logged to a centralized audit collection, providing a complete, tamper-evident chain of custody for every student risk assessment and intervention action.</p>
  </div>{F(4)}</div>"""

# ===========================================================
# PAGE 5 — Empirical Cohort + Table II + Fig 2 + Preprocessing + Classifier + Eqs 1–4
# ===========================================================
p5 = f"""<div class="page" id="p5">{H()}
  <div class="page-content two-col">
    <div class="subsection-title">C. Empirical Cohort and Feature Extraction</div>
    <p class="no-indent">The empirical benchmark utilizes an institutional cohort of <i>N</i>=9,470 undergraduate student records. Each record encompasses four validated psychometric Likert dimensions rated on a continuous scale from 1.0 (severe dissatisfaction/distress) to 5.0 (optimal satisfaction/engagement). The dataset was partitioned using stratified random sampling (seed=42) into training (7,102 instances, 75%) and held-out test (2,368 instances, 25%) splits, preserving the 32.20% positive dropout-risk prevalence in both partitions. Table II summarizes the feature dictionary.</p>

    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE II.</span>&nbsp; FEATURE DICTIONARY AND PSYCHOMETRIC MEASUREMENT CONSTRUCTS</div>
      <table class="academic-table">
        <thead><tr>
          <th style="width:22%">Feature Symbol</th>
          <th style="width:22%">Construct Domain</th>
          <th style="width:12%">Bounds</th>
          <th style="width:14%">Mean&plusmn;Std</th>
          <th style="width:30%">Psychometric Definition</th>
        </tr></thead>
        <tbody>
          <tr><td><code>academicEngagement</code></td><td>Cognitive &amp; behavioral effort</td><td>[1.0,5.0]</td><td>3.42&plusmn;0.88</td><td>Lecture attendance, assignment completion, active study hours</td></tr>
          <tr><td><code>supportSatisfaction</code></td><td>Institutional service adequacy</td><td>[1.0,5.0]</td><td>3.15&plusmn;0.94</td><td>Faculty accessibility, tutoring availability, advising utility</td></tr>
          <tr><td><code>stressManagement</code></td><td>Psychosocial &amp; affective load</td><td>[1.0,5.0]</td><td>2.88&plusmn;1.05</td><td>Emotional resilience, workload stress, work-life balance</td></tr>
          <tr><td><code>peerBelongingness</code></td><td>Social integration &amp; cohort bonding</td><td>[1.0,5.0]</td><td>3.31&plusmn;0.91</td><td>Peer collaboration, campus community integration, isolation risk</td></tr>
        </tbody>
      </table>
    </div>

    <p>Target labels reflect verified academic retention status: <i>Y</i>=0 denotes persistence (6,421 instances, 67.80%) and <i>Y</i>=1 represents acute disengagement or formal attrition risk (3,049 instances, 32.20%), as illustrated in Fig.&nbsp;2.</p>

    <div class="figure-container full-width">
      <svg viewBox="0 0 340 108" style="width:100%;max-width:340px;height:auto;margin:0 auto;display:block;font-family:'Times New Roman',serif;">
        <line x1="45" y1="10" x2="45" y2="88" stroke="#475569" stroke-width="1.2"/>
        <line x1="45" y1="88" x2="320" y2="88" stroke="#475569" stroke-width="1.2"/>
        <line x1="40" y1="88" x2="320" y2="88" stroke="#e2e8f0" stroke-width="0.8"/><text x="36" y="91" font-size="7" text-anchor="end" fill="#475569">0</text>
        <line x1="40" y1="52" x2="320" y2="52" stroke="#e2e8f0" stroke-width="0.8"/><text x="36" y="55" font-size="7" text-anchor="end" fill="#475569">4k</text>
        <line x1="40" y1="16" x2="320" y2="16" stroke="#e2e8f0" stroke-width="0.8"/><text x="36" y="19" font-size="7" text-anchor="end" fill="#475569">8k</text>
        <rect x="90" y="22" width="65" height="66" fill="#0284c7" rx="3" stroke="#0369a1" stroke-width="0.8"/>
        <text x="122.5" y="17" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0369a1">6,421 (67.8%)</text>
        <text x="122.5" y="100" font-size="7.5" text-anchor="middle" fill="#1e293b">Retained (0)</text>
        <rect x="200" y="57" width="65" height="31" fill="#f59e0b" rx="3" stroke="#d97706" stroke-width="0.8"/>
        <text x="232.5" y="52" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#b45309">3,049 (32.2%)</text>
        <text x="232.5" y="100" font-size="7.5" text-anchor="middle" fill="#1e293b">Dropout Risk (1)</text>
        <text x="18" y="50" font-size="7" font-weight="bold" text-anchor="middle" transform="rotate(-90 18 50)" fill="#334155">Student Count</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig.&nbsp;2.</span> Target class distribution (N=9,470), indicating 32.20% positive dropout-risk prevalence.</div>
    </div>

    <div class="subsection-title">D. Data Preprocessing and Cross-Validation</div>
    <p class="no-indent">Raw survey records undergo programmatic cleansing: boundary violations outside [1.0,&nbsp;5.0] are flagged and excluded, and missing entries are imputed using feature-wise medians computed exclusively over the training partition to prevent data leakage into evaluation. All four features are then z-score normalized using training-split statistics. To evaluate stability against distributional drift, five-fold stratified cross-validation was conducted on the 7,102 training instances prior to final model fitting. Cross-validation confirmed consistent fold-level variance (mean accuracy=84.05%&plusmn;0.42%), demonstrating stationary decision geometries across cohort subpopulations.</p>

    <div class="subsection-title">E. Soft-Voting Ensemble Classifier</div>
    <p class="no-indent">We formulate a dual-algorithm soft-voting ensemble combining Random Forest (RF) and Gradient Boosted Decision Trees (GBDT). The RF aggregates <i>B</i>&nbsp;=&nbsp;180 bootstrap-sampled trees, each built on a random feature subset. The ensemble posterior is:</p>
    <div class="equation-box"><div class="math-expr">P<sub>RF</sub>(Y=1|<b>x</b>) = (1/B) &sum;<sub>b=1</sub><sup>B</sup> P<sub>b</sub>(Y=1|<b>x</b>)</div><div class="eq-number">(1)</div></div>

    <p>The GBDT fits <i>M</i>&nbsp;=&nbsp;150 shallow trees sequentially. At iteration <i>m</i>, pseudo-residuals are computed as:</p>
    <div class="equation-box"><div class="math-expr">r<sub>im</sub> = &minus;[&part;L(y<sub>i</sub>,F(<b>x</b><sub>i</sub>))/&part;F(<b>x</b><sub>i</sub>)]<sub>F=F<sub>m&minus;1</sub></sub></div><div class="eq-number">(2)</div></div>

    <p>The ensemble update applies shrinkage rate &eta;=0.08. The soft-voting fusion averages both base estimators:</p>
    <div class="equation-box"><div class="math-expr">p(<b>x</b>) = 0.5&middot;P<sub>RF</sub>(Y=1|<b>x</b>) + 0.5&middot;P<sub>GB</sub>(Y=1|<b>x</b>)</div><div class="eq-number">(3)</div></div>

    <p>The composite model optimizes binary cross-entropy across all <i>N</i> training samples:</p>
    <div class="equation-box"><div class="math-expr">L<sub>log</sub> = &minus;(1/N)&sum;<sub>i=1</sub><sup>N</sup>[y<sub>i</sub>ln p(<b>x</b><sub>i</sub>)+(1&minus;y<sub>i</sub>)ln(1&minus;p(<b>x</b><sub>i</sub>))]</div><div class="eq-number">(4)</div></div>
  </div>{F(5)}</div>"""

# ===========================================================
# PAGE 6 — Table III, Metrics, Decision Rule, Impl Stack Table IV
# ===========================================================
p6 = f"""<div class="page" id="p6">{H()}
  <div class="page-content two-col">
    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE III.</span>&nbsp; ENSEMBLE CLASSIFIER HYPERPARAMETERS AND SELECTION RATIONALE</div>
      <table class="academic-table">
        <thead><tr><th>Estimator</th><th>Hyperparameter</th><th>Configured Value</th><th>Selection Rationale</th></tr></thead>
        <tbody>
          <tr><td>Random Forest</td><td>n_estimators</td><td>180 trees</td><td>Plateau analysis: AUC stabilizes at B&ge;150</td></tr>
          <tr><td>Random Forest</td><td>max_depth</td><td>6 levels</td><td>Constrains tree capacity; limits overfitting</td></tr>
          <tr><td>Random Forest</td><td>min_samples_leaf</td><td>4 samples</td><td>Regularizes terminal node splits</td></tr>
          <tr><td>Random Forest</td><td>max_features</td><td>'sqrt'</td><td>Standard de-correlation strategy for RF</td></tr>
          <tr><td>Gradient Boost</td><td>n_estimators</td><td>150 stages</td><td>Early stopping on validation loss plateau</td></tr>
          <tr><td>Gradient Boost</td><td>learning_rate (&eta;)</td><td>0.08</td><td>Shrinkage trades off speed vs. accuracy</td></tr>
          <tr><td>Gradient Boost</td><td>max_depth</td><td>4 levels</td><td>Prevents deep interaction overfitting</td></tr>
          <tr><td>VotingClassifier</td><td>voting</td><td>'soft'</td><td>Averages calibrated class probabilities</td></tr>
        </tbody>
      </table>
    </div>

    <p class="no-indent">Hyperparameters were selected via 5-fold stratified cross-validated grid search on the training partition. The grid explored n_estimators&isin;{100,150,180,200}, max_depth&isin;{4,5,6,8}, and learning_rate&isin;{0.05,0.08,0.10}. The configuration in Table III yielded the best mean validation F1-score (minority class) of 73.52%&plusmn;0.81% and was subsequently re-trained on the full 7,102-instance training set for final evaluation.</p>

    <div class="subsection-title">F. Model Evaluation Metrics</div>
    <p class="no-indent">Classification performance is evaluated using standard discriminative metrics derived from the confusion matrix entries TP, TN, FP, FN:</p>
    <div class="equation-box"><div class="math-expr">Accuracy = (TP+TN)/(TP+TN+FP+FN)</div><div class="eq-number">(5)</div></div>
    <div class="equation-box"><div class="math-expr">Precision = TP/(TP+FP), &nbsp;&nbsp; Recall = TP/(TP+FN)</div><div class="eq-number">(6)</div></div>
    <div class="equation-box"><div class="math-expr">F1 = 2&middot;(Precision&middot;Recall)/(Precision+Recall)</div><div class="eq-number">(7)</div></div>

    <div class="subsection-title">G. Prediction-to-Workflow Decision Rule</div>
    <p class="no-indent">To prevent alert fatigue while ensuring vulnerable students receive timely support, we formalize a tripartite decision policy &Phi;(<i>p</i>(<b>x</b>),<b>x</b>) mapping inferences to operational tiers:</p>
    <div class="equation-box"><div class="math-expr">Tier(<b>x</b>) = Low Risk (Monitor), if p(<b>x</b>)&lt;0.40 and min(x<sub>j</sub>)&gt;2.5<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Moderate Risk (Flag), if 0.40&le;p(<b>x</b>)&lt;0.80 or min(x<sub>j</sub>)&le;2.5<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;High Risk (Auto-Schedule), if p(<b>x</b>)&ge;0.80 and &Delta;t&ge;7 days</div><div class="eq-number">(8)</div></div>

    <p class="no-indent">The 0.50 classification threshold for the Moderate tier corresponds to the posterior probability at which expected intervention benefit (reducing a False Negative) equals the expected alert-fatigue cost (generating a False Positive). The 0.80 High-Risk threshold was calibrated against counselor workload capacity: at 32.2% class prevalence, approximately 3–5% of monthly submissions exceed this threshold, producing a manageable counselor queue of 4–7 priority cases per 100 active students.</p>

    <div class="subsection-title">H. System Implementation Stack</div>
    <p class="no-indent">The backend is built with Node.js 18 LTS and Express.js, interfacing with MongoDB 7.0 via Mongoose ODM. ML models are served via Python 3.11 with Scikit-Learn 1.3 and Joblib. The frontend is built on React 18 with Tailwind CSS. Table IV outlines the full technology stack.</p>

    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE IV.</span>&nbsp; SYSTEM IMPLEMENTATION STACK AND DEPLOYMENT ROLES</div>
      <table class="academic-table">
        <thead><tr><th style="width:22%">Component</th><th style="width:36%">Technology Stack</th><th style="width:42%">Implementation Purpose</th></tr></thead>
        <tbody>
          <tr><td>Backend API</td><td>Node.js 18 LTS, Express.js 4.18</td><td>RESTful API routing and business logic orchestration</td></tr>
          <tr><td>Database</td><td>MongoDB 7.0, Mongoose ODM</td><td>Tenant isolation, cycle-locking schema, audit logging</td></tr>
          <tr><td>ML Microservice</td><td>Python 3.11, Scikit-Learn 1.3, Joblib</td><td>Ensemble inference and calibrated probability scoring</td></tr>
          <tr><td>Rules Engine</td><td>JavaScript ES2022</td><td>Dual-criteria triage evaluation (Eq. 8)</td></tr>
          <tr><td>Scheduler</td><td>Node.js (<code>meetingScheduler.js</code>)</td><td>Conflict-free 30-minute slot allocation with cooldown</td></tr>
          <tr><td>Frontend UI</td><td>React 18, Tailwind CSS</td><td>Role-based portals (Admin, Counselor, Student)</td></tr>
          <tr><td>Calendar API</td><td>Google Calendar API v3</td><td>Event creation with Google Meet link generation</td></tr>
          <tr><td>Email Notifications</td><td>Nodemailer + SMTP</td><td>Neutral-subject invitation dispatch to attendees</td></tr>
          <tr><td>Authentication</td><td>HMAC-SHA256 JWT, bcrypt (rounds=10)</td><td>Stateless auth; password hashing and RBAC enforcement</td></tr>
        </tbody>
      </table>
    </div>
  </div>{F(6)}</div>"""

# ===========================================================
# PAGE 7 — Advisory Workflow Fig 3 + Fig 4 + Calendar Fig 6 + Cooldown + Audit
# ===========================================================
p7 = f"""<div class="page" id="p7">{H()}
  <div class="page-content">
    <div class="subsection-title">I. Automated Advisory Action Workflow</div>
    <p class="no-indent">Fig.&nbsp;3 illustrates the operational execution pipeline from survey submission to calendar dispatch. Upon survey ingestion, the backend asynchronously issues a REST query to the Python ML microservice. Model probabilities are forwarded to the Retention Rule Engine. For High-Risk students who pass the cooldown check, the meeting allocation service executes an atomic slot reservation, issues calendar invites, and sends Nodemailer notifications simultaneously.</p>
    <div class="figure-container full-width" style="margin:2px 0 3px 0;">
      <svg viewBox="0 0 720 118" style="width:100%;max-width:720px;height:auto;font-family:'Times New Roman',serif;">
        <defs><marker id="ar2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b"/></marker></defs>
        <rect x="12" y="34" width="105" height="46" rx="4" fill="#f8fafc" stroke="#64748b" stroke-width="1.2"/>
        <text x="64.5" y="52" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Survey Submission</text>
        <text x="64.5" y="63" font-size="6.5" text-anchor="middle" fill="#475569">POST /api/feedback</text>
        <text x="64.5" y="72" font-size="6" text-anchor="middle" fill="#0284c7">Cycle Locked</text>
        <line x1="117" y1="57" x2="145" y2="57" stroke="#1e293b" stroke-width="1.5" marker-end="url(#ar2)"/>
        <rect x="149" y="34" width="105" height="46" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/>
        <text x="201.5" y="52" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0369a1">Feature Validation</text>
        <text x="201.5" y="63" font-size="6.5" text-anchor="middle" fill="#0f172a">Extract 4-D Vector</text>
        <text x="201.5" y="72" font-size="6" text-anchor="middle" fill="#475569">Boundary [1.0,5.0]</text>
        <line x1="254" y1="57" x2="282" y2="57" stroke="#1e293b" stroke-width="1.5" marker-end="url(#ar2)"/>
        <rect x="286" y="34" width="115" height="46" rx="4" fill="#fefce8" stroke="#d97706" stroke-width="1.2"/>
        <text x="343.5" y="52" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#b45309">Ensemble ML Scoring</text>
        <text x="343.5" y="63" font-size="6.5" text-anchor="middle" fill="#78350f">RF + GBDT Inference</text>
        <text x="343.5" y="72" font-size="6" text-anchor="middle" fill="#92400e">Output: p(x)&isin;[0,1]</text>
        <line x1="401" y1="57" x2="429" y2="57" stroke="#1e293b" stroke-width="1.5" marker-end="url(#ar2)"/>
        <polygon points="487,24 537,57 487,90 437,57" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/>
        <text x="487" y="54" font-size="7" font-weight="bold" text-anchor="middle" fill="#9a3412">Risk Tier?</text>
        <text x="487" y="64" font-size="6" text-anchor="middle" fill="#c2410c">Eq. (8)</text>
        <line x1="487" y1="24" x2="487" y2="10" stroke="#1e293b" stroke-width="1.2"/>
        <line x1="487" y1="10" x2="588" y2="10" stroke="#1e293b" stroke-width="1.2" marker-end="url(#ar2)"/>
        <text x="533" y="7" font-size="6.5" fill="#15803d">Low(p&lt;0.40)</text>
        <rect x="592" y="2" width="118" height="18" rx="3" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
        <text x="651" y="13" font-size="7" text-anchor="middle" fill="#334155">Log &amp; Monitor Only</text>
        <line x1="537" y1="57" x2="588" y2="57" stroke="#1e293b" stroke-width="1.2" marker-end="url(#ar2)"/>
        <text x="562" y="51" font-size="6.5" fill="#b45309">Mod(0.40–0.80)</text>
        <rect x="592" y="47" width="118" height="20" rx="3" fill="#fffbeb" stroke="#f59e0b" stroke-width="1"/>
        <text x="651" y="57" font-size="7" font-weight="bold" text-anchor="middle" fill="#92400e">Advisor Dashboard Flag</text>
        <text x="651" y="65" font-size="6" text-anchor="middle" fill="#78350f">Manual Review Queue</text>
        <line x1="487" y1="90" x2="487" y2="106" stroke="#1e293b" stroke-width="1.2"/>
        <line x1="487" y1="106" x2="588" y2="106" stroke="#1e293b" stroke-width="1.2" marker-end="url(#ar2)"/>
        <text x="533" y="101" font-size="6.5" fill="#dc2626">High(p&ge;0.80)</text>
        <rect x="592" y="96" width="118" height="20" rx="3" fill="#ecfdf5" stroke="#10b981" stroke-width="1"/>
        <text x="651" y="106" font-size="7" font-weight="bold" text-anchor="middle" fill="#065f46">Auto Meeting Engine</text>
        <text x="651" y="114" font-size="6" text-anchor="middle" fill="#047857">Check Cooldown &amp; Schedule</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig.&nbsp;3.</span> Workflow execution pipeline of the Academic Retention Action Engine, demonstrating survey event triggering, feature extraction, ML inference, and tier-based dispatch logic.</div>
    </div>
    <div class="figure-container full-width" style="margin:2px 0 3px 0;">
      <svg viewBox="0 0 720 140" style="width:100%;max-width:720px;height:auto;font-family:'Times New Roman',serif;">
        <defs><marker id="ar3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1 L 10 5 L 0 9 z" fill="#0f172a"/></marker></defs>
        <rect x="12" y="4" width="82" height="14" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/><text x="53" y="13" font-size="6.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Student</text>
        <line x1="53" y1="18" x2="53" y2="132" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="126" y="4" width="92" height="14" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/><text x="172" y="13" font-size="6.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Frontend Client</text>
        <line x1="172" y1="18" x2="172" y2="132" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="250" y="4" width="96" height="14" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/><text x="298" y="13" font-size="6.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Backend Express</text>
        <line x1="298" y1="18" x2="298" y2="132" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="378" y="4" width="90" height="14" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/><text x="423" y="13" font-size="6.5" font-weight="bold" text-anchor="middle" fill="#0f172a">ML Service</text>
        <line x1="423" y1="18" x2="423" y2="132" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="500" y="4" width="92" height="14" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/><text x="546" y="13" font-size="6.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Counselor/Advisor</text>
        <line x1="546" y1="18" x2="546" y2="132" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <rect x="624" y="4" width="84" height="14" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/><text x="666" y="13" font-size="6.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Calendar API</text>
        <line x1="666" y1="18" x2="666" y2="132" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>
        <line x1="53" y1="28" x2="172" y2="28" stroke="#0f172a" stroke-width="1.2" marker-end="url(#ar3)"/><text x="112" y="25" font-size="5.8" text-anchor="middle" fill="#1e293b">1. Submit survey responses</text>
        <line x1="172" y1="40" x2="298" y2="40" stroke="#0f172a" stroke-width="1.2" marker-end="url(#ar3)"/><text x="235" y="37" font-size="5.8" text-anchor="middle" fill="#1e293b">2. POST /feedback (JWT)</text>
        <line x1="298" y1="52" x2="423" y2="52" stroke="#0f172a" stroke-width="1.2" marker-end="url(#ar3)"/><text x="360" y="49" font-size="5.8" text-anchor="middle" fill="#1e293b">3. Request ML inference (x)</text>
        <line x1="423" y1="64" x2="298" y2="64" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2,2" marker-end="url(#ar3)"/><text x="360" y="61" font-size="5.8" text-anchor="middle" fill="#1e293b">4. Return p(x) &amp; survey risk</text>
        <line x1="298" y1="78" x2="546" y2="78" stroke="#0f172a" stroke-width="1.2" marker-end="url(#ar3)"/><text x="422" y="75" font-size="5.8" text-anchor="middle" fill="#1e293b">5. Push triage event to Advisor Queue</text>
        <line x1="546" y1="92" x2="298" y2="92" stroke="#0f172a" stroke-width="1.2" marker-end="url(#ar3)"/><text x="422" y="89" font-size="5.8" text-anchor="middle" fill="#1e293b">6. Counselor validates / approves intervention</text>
        <line x1="298" y1="106" x2="666" y2="106" stroke="#0f172a" stroke-width="1.2" marker-end="url(#ar3)"/><text x="482" y="103" font-size="5.8" text-anchor="middle" fill="#1e293b">7. Allocate conflict-free 30-min slot &amp; create event</text>
        <line x1="666" y1="118" x2="298" y2="118" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2,2" marker-end="url(#ar3)"/><text x="482" y="115" font-size="5.8" text-anchor="middle" fill="#1e293b">8. Return event status &amp; Meet link</text>
        <line x1="298" y1="130" x2="53" y2="130" stroke="#0f172a" stroke-width="1.2" marker-end="url(#ar3)"/><text x="175" y="127" font-size="5.8" text-anchor="middle" fill="#1e293b">9. Email invitation with neutral subject &amp; Meet URL</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig.&nbsp;4.</span> UML message sequence diagram detailing chronological interactions between student, frontend, Express API, ML service, advisor dashboard, and Google Calendar.</div>
    </div>
    <div class="two-col">
      <div class="subsection-title">J. Calendar Scheduling, Cooldown, and Audit Trails</div>
      <p class="no-indent">The meeting allocation engine (<code>meetingScheduler.js</code>) automates calendar bookings across seven upcoming business days (09:00–17:00). Contiguous 30-minute slots are reserved via atomic MongoDB <code>findOneAndUpdate</code> operations on <code>RetentionAction</code> (state: <code>PENDING&rarr;SCHEDULED</code>). Invitations are titled "Academic Support &amp; Guidance Check-in" (Fig.&nbsp;6), deliberately neutral to avoid stigmatization. A 7-day cooldown enforces <code>lastInterventionTimestamp</code> verification before re-scheduling.</p>
      <div class="figure-container">
        <svg viewBox="0 0 340 108" style="width:100%;max-width:340px;height:auto;font-family:'Times New Roman',serif;">
          <rect x="6" y="4" width="328" height="99" rx="4" fill="#fff" stroke="#cbd5e1" stroke-width="1.2"/>
          <rect x="6" y="4" width="328" height="18" rx="4" fill="#0284c7"/>
          <rect x="6" y="15" width="328" height="7" fill="#0284c7"/>
          <circle cx="20" cy="13" r="4" fill="#ffffff"/>
          <text x="20" y="16" font-size="6" font-weight="bold" text-anchor="middle" fill="#0284c7">&#x2713;</text>
          <text x="30" y="16" font-size="6.5" font-weight="bold" fill="#ffffff">Google Calendar &middot; Advisory Session Confirmed</text>
          <text x="16" y="33" font-size="7" font-weight="bold" fill="#0f172a">Event: Academic Support &amp; Guidance Check-in</text>
          <text x="16" y="43" font-size="6.2" fill="#475569"><tspan font-weight="bold">Date/Time:</tspan> Tue, Oct 27, 2026 &middot; 14:00–14:30 IST</text>
          <text x="16" y="53" font-size="6.2" fill="#475569"><tspan font-weight="bold">Host:</tspan> Academic Counselor &middot; <tspan font-weight="bold">Attendee:</tspan> Student #STD-8492</text>
          <rect x="16" y="59" width="302" height="14" rx="3" fill="#f0fdf4" stroke="#86efac" stroke-width="0.8"/>
          <text x="22" y="69" font-size="6.2" font-weight="bold" fill="#166534">Video: https://meet.google.com/stu-acad-guid</text>
          <text x="16" y="83" font-size="6" fill="#64748b"><tspan font-weight="bold">Agenda:</tspan> Proactive academic review, resource navigation, course planning.</text>
          <text x="16" y="94" font-size="5.5" font-style="italic" fill="#94a3b8">Initiated by StudentDropout Engine &middot; Approved by Counselor &middot; 7-Day Cooldown Active</text>
        </svg>
        <div class="figure-caption"><span class="fig-title">Fig.&nbsp;6.</span> Generated academic support calendar card with non-stigmatizing neutral title and human counselor attribution.</div>
      </div>
      <p class="no-indent">Every student state transition is audited via: <code>PENDING&rarr;FLAGGED&rarr;APPROVED&rarr;SCHEDULED&rarr;COMPLETED</code>. Counselors may append timestamped override notes at any stage. All calendar transactions log unique event identifiers, recipient hashes, and timestamps for independent compliance audits under institutional ethics review boards. Password credentials use <code>bcrypt</code> (salt rounds=10); JWT tokens expire after 60 minutes. Multi-tenant isolation is enforced at query level via <code>companyCode</code> scoping.</p>
    </div>
  </div>{F(7)}</div>"""

# ===========================================================
# PAGE 8 — Results: Tables V+VI + Fig 5 + Feature Importance (expanded)
# ===========================================================
p8 = f"""<div class="page" id="p8">{H()}
  <div class="page-content two-col">
    <div class="section-title">IV. RESULTS</div>
    <div class="subsection-title">A. Classification Performance</div>
    <p class="no-indent">The soft-voting ensemble was evaluated on the held-out test split of 2,368 student instances (1,606 Retained, 762 Dropout Risk). Performance was benchmarked against a Zero-Rule majority-class baseline (always predicts Retained). Table V summarizes empirical metrics across both models.</p>
    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE V.</span>&nbsp; HELD-OUT TEST SET PERFORMANCE (N=2,368)</div>
      <table class="academic-table">
        <thead><tr><th>Metric</th><th>Majority Baseline</th><th>Ensemble</th><th>Absolute &Delta;</th></tr></thead>
        <tbody>
          <tr><td>Accuracy</td><td>0.6782 (67.82%)</td><td><b>0.8421 (84.21%)</b></td><td>+16.39%</td></tr>
          <tr><td>Precision (class 1)</td><td>0.0000 (0.00%)</td><td><b>0.7939 (79.39%)</b></td><td>+79.39%</td></tr>
          <tr><td>Recall (class 1)</td><td>0.0000 (0.00%)</td><td><b>0.6877 (68.77%)</b></td><td>+68.77%</td></tr>
          <tr><td>F1-Score (class 1)</td><td>0.0000 (0.00%)</td><td><b>0.7370 (73.70%)</b></td><td>+73.70%</td></tr>
          <tr><td>ROC-AUC</td><td>0.5000 (50.00%)</td><td><b>0.8925 (89.25%)</b></td><td>+39.25%</td></tr>
        </tbody>
      </table>
    </div>
    <p>The ensemble delivers an authentic +16.39 pp accuracy lift over the majority baseline. On the positive minority class, the model achieves 79.39% precision (four out of five flagged students are genuine risks) and 68.77% recall (captures 524 of 762 at-risk students). Table VI presents the confusion matrix at decision threshold &tau;<sub>0</sub>=0.50.</p>
    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE VI.</span>&nbsp; CONFUSION MATRIX AT &tau;<sub>0</sub>=0.50</div>
      <table class="academic-table">
        <thead><tr><th>Actual</th><th>Pred. Retained (0)</th><th>Pred. Risk (1)</th><th>Total</th></tr></thead>
        <tbody>
          <tr><td>Retained (0)</td><td>TN = 1,470 (91.5%)</td><td>FP = 136 (8.5%)</td><td>1,606</td></tr>
          <tr><td>Risk (1)</td><td>FN = 238 (31.2%)</td><td>TP = 524 (68.8%)</td><td>762</td></tr>
          <tr><td><b>Total</b></td><td><b>1,708</b></td><td><b>660</b></td><td><b>2,368</b></td></tr>
        </tbody>
      </table>
    </div>
    <div class="figure-container">
      <svg viewBox="0 0 340 108" style="width:100%;max-width:340px;height:auto;font-family:'Times New Roman',serif;">
        <line x1="45" y1="10" x2="45" y2="88" stroke="#475569" stroke-width="1.2"/>
        <line x1="45" y1="88" x2="330" y2="88" stroke="#475569" stroke-width="1.2"/>
        <line x1="40" y1="88" x2="330" y2="88" stroke="#e2e8f0" stroke-width="0.8"/><text x="36" y="91" font-size="7" text-anchor="end" fill="#475569">0%</text>
        <line x1="40" y1="49" x2="330" y2="49" stroke="#e2e8f0" stroke-width="0.8"/><text x="36" y="52" font-size="7" text-anchor="end" fill="#475569">50%</text>
        <line x1="40" y1="10" x2="330" y2="10" stroke="#e2e8f0" stroke-width="0.8"/><text x="36" y="13" font-size="7" text-anchor="end" fill="#475569">100%</text>
        <rect x="58" y="21" width="38" height="67" fill="#0284c7" rx="2"/><text x="77" y="17" font-size="7" font-weight="bold" text-anchor="middle" fill="#0369a1">84.2%</text><text x="77" y="100" font-size="7" text-anchor="middle" fill="#1e293b">Acc</text>
        <rect x="114" y="24" width="38" height="64" fill="#0ea5e9" rx="2"/><text x="133" y="20" font-size="7" font-weight="bold" text-anchor="middle" fill="#0284c7">79.4%</text><text x="133" y="100" font-size="7" text-anchor="middle" fill="#1e293b">Prec</text>
        <rect x="170" y="34" width="38" height="54" fill="#f59e0b" rx="2"/><text x="189" y="30" font-size="7" font-weight="bold" text-anchor="middle" fill="#b45309">68.8%</text><text x="189" y="100" font-size="7" text-anchor="middle" fill="#1e293b">Rec</text>
        <rect x="226" y="29" width="38" height="59" fill="#10b981" rx="2"/><text x="245" y="25" font-size="7" font-weight="bold" text-anchor="middle" fill="#047857">73.7%</text><text x="245" y="100" font-size="7" text-anchor="middle" fill="#1e293b">F1</text>
        <rect x="282" y="17" width="38" height="71" fill="#6366f1" rx="2"/><text x="301" y="13" font-size="7" font-weight="bold" text-anchor="middle" fill="#4338ca">89.3%</text><text x="301" y="100" font-size="7" text-anchor="middle" fill="#1e293b">AUC</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig.&nbsp;5.</span> Test set model performance profile (N=2,368) across five evaluation metrics.</div>
    </div>
    <div class="subsection-title">B. Recall–Precision Trade-off and Threshold Sensitivity</div>
    <p class="no-indent">The cost asymmetry inherent in student dropout intervention decisions (Cost(FN) &gg; Cost(FP)) justifies the selection of &tau;<sub>0</sub>=0.50 rather than the default 0.50 threshold in isolation. Lowering the decision threshold to &tau;=0.40 increases recall to 77.3% but reduces precision to 68.2% (F1=72.5%), generating an additional 86 false-positive triage events per test set. Raising the threshold to &tau;=0.60 increases precision to 84.6% but drops recall to 58.1% (F1=68.8%), missing 82 at-risk students. The chosen &tau;<sub>0</sub>=0.50 provides the optimal F1 trade-off, while the supplementary raw-score criterion (min(x<sub>j</sub>)&le;2.5) captures psychometrically distressed students who might score below the probability threshold during periods of emotional crisis.</p>
    <div class="subsection-title">B2. Feature Importance and Sensitivity Analysis</div>
    <p class="no-indent">Mean decrease in impurity (MDI) across ensemble trees illuminates the underlying psychometric drivers. Stress management accounts for 34.2% of total predictive importance, indicating that affective distress and academic overload are the earliest indicators of student disengagement. Academic engagement contributes 28.5%, while support satisfaction (21.1%) and peer belongingness (16.2%) provide secondary signals.</p>
    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE VI-B.</span>&nbsp; ENSEMBLE GINI FEATURE IMPORTANCE BREAKDOWN</div>
      <table class="academic-table">
        <thead><tr><th>Rank</th><th>Feature Domain</th><th>RF Weight</th><th>GBDT Weight</th><th>Ensemble Mean</th></tr></thead>
        <tbody>
          <tr><td>1</td><td><code>stressManagement</code></td><td>0.338</td><td>0.346</td><td><b>0.342 (34.2%)</b></td></tr>
          <tr><td>2</td><td><code>academicEngagement</code></td><td>0.291</td><td>0.279</td><td><b>0.285 (28.5%)</b></td></tr>
          <tr><td>3</td><td><code>supportSatisfaction</code></td><td>0.214</td><td>0.208</td><td><b>0.211 (21.1%)</b></td></tr>
          <tr><td>4</td><td><code>peerBelongingness</code></td><td>0.157</td><td>0.167</td><td><b>0.162 (16.2%)</b></td></tr>
        </tbody>
      </table>
    </div>
  </div>{F(8)}</div>"""

# ===========================================================
# PAGE 9 — Workflow Bench + Tables VII+VIII + Eqs 9-10 + RQ Answers + Discussion A-D + Table IX
# ===========================================================
p9 = f"""<div class="page" id="p9">{H()}
  <div class="page-content two-col">
    <div class="subsection-title">C. Operational Workflow Benchmarking</div>
    <p class="no-indent">Verification across 50 simulated triage scenarios (20 Low, 15 Moderate, 15 High) evaluated automated slot discovery, Google Calendar dispatch, duplicate reservation suppression, and cooldown enforcement. Table VII details operational performance parameters with explicit denominators.</p>
    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE VII.</span>&nbsp; OPERATIONAL WORKFLOW METRICS (N=50 TRIAGE EVENTS)</div>
      <table class="academic-table">
        <thead><tr><th>Workflow Metric</th><th>Denominator</th><th>Value</th></tr></thead>
        <tbody>
          <tr><td>End-to-End Success Rate</td><td>50 triage events</td><td><b>100.0% (50/50)</b></td></tr>
          <tr><td>Mean Dispatch Latency</td><td>50 triage events</td><td><b>1.38 &plusmn; 0.21 s</b></td></tr>
          <tr><td>Duplicate Booking Rate</td><td>15 auto-bookings</td><td><b>0.00% (0/15)</b></td></tr>
          <tr><td>Cooldown Suppression</td><td>10 rapid re-tests</td><td><b>100.0% (10/10)</b></td></tr>
          <tr><td>Counselor Gate Compliance</td><td>15 gated cases</td><td><b>100.0% (15/15)</b></td></tr>
        </tbody>
      </table>
    </div>
    <div class="equation-box"><div class="math-expr">R<sub>succ</sub> = (N<sub>succ</sub>/N<sub>total</sub>)&times;100%;&nbsp;&nbsp;&nbsp; T&#x305;<sub>exec</sub> = (1/N)&sum;&Delta;t<sub>i</sub></div><div class="eq-number">(9–10)</div></div>
    <p class="no-indent">The mean 1.38-second end-to-end latency decomposes across architectural stages: Express validation (42&nbsp;ms), Python ensemble inference (145&nbsp;ms), MongoDB slot query (38&nbsp;ms), Google Calendar OAuth2 reservation (820&nbsp;ms), and Nodemailer SMTP delivery (335&nbsp;ms). The internal computational pipeline (excluding external API calls) requires only 225&nbsp;ms, confirming that Google Calendar OAuth2 handshakes constitute the dominant latency contributor. Future deployments could reduce total latency to under 600&nbsp;ms by pre-caching OAuth2 access tokens with proactive refresh.</p>
    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE VIII.</span>&nbsp; SUMMARY OF OBSERVED SYSTEM BEHAVIOR AND OPERATIONAL VERIFICATION</div>
      <table class="academic-table">
        <thead><tr><th style="width:24%">Subsystem</th><th style="width:36%">Observed Outcome</th><th style="width:40%">Verification &amp; Integrity Check</th></tr></thead>
        <tbody>
          <tr><td>Authentication</td><td>JWT issued; role validated</td><td>Protected endpoints blocked without valid bearer token</td></tr>
          <tr><td>Survey Ingestion</td><td>4 Likert scores captured</td><td>Boundary [1.0,5.0] enforced; invalid payloads rejected (HTTP 422)</td></tr>
          <tr><td>Cycle Locking</td><td>Second POST rejected HTTP 409</td><td>Compound unique index [studentId, cycle] active</td></tr>
          <tr><td>Ensemble Inference</td><td>Scored within 145 ms</td><td>Soft-voting fusion; calibrated probabilities returned</td></tr>
          <tr><td>Counselor Triage</td><td>Action dashboard updated</td><td>Sorted queue; advisors approve, reschedule, or snooze</td></tr>
          <tr><td>Calendar Dispatch</td><td>Google Meet invitation created</td><td>Non-stigmatizing title; attendee auto-invited via email</td></tr>
          <tr><td>Cooldown Lock</td><td>Repeat booking blocked</td><td>7-day window respected; re-assessments logged only</td></tr>
        </tbody>
      </table>
    </div>
    <div class="subsection-title">D. Answers to Research Questions</div>
    <p class="no-indent"><b>RQ1.</b> The soft-voting ensemble achieved 84.21% accuracy (+16.39&nbsp;pp above majority baseline) and 89.25% ROC-AUC, substantially outperforming single-algorithm trees and rule-based heuristics. <b>RQ2.</b> The dual-criteria triage policy isolated 68.77% of at-risk students while generating only 8.5% false-positive alerts, confirming effective advisory workload management. <b>RQ3.</b> The calendar engine achieved 1.38&nbsp;s mean latency with zero collisions and 100% cooldown compliance across all 50 test scenarios. <b>RQ4.</b> The mandatory counselor authorization gate ensured risk scores remained decision-support recommendations; no automated scheduling proceeded without explicit human approval.</p>
    <div class="section-title">V. DISCUSSION</div>
    <div class="subsection-title">A. Early Warning versus Definitive Retention Indicators</div>
    <p class="no-indent">The reported accuracy must be interpreted with academic discipline. Machine learning classifiers detect statistical correlations between engagement indicators and historical attrition patterns; they cannot measure disenrollment intent or cognitive potential. Labeling a student as "at-risk" risks inducing stereotype threat and self-fulfilling disengagement if communicated clumsily. The StudentDropout architecture enforces strict counselor intermediation and neutral calendar naming to prevent direct student exposure to risk labels.</p>
    <div class="subsection-title">B. Class Imbalance and Cost Asymmetry</div>
    <p class="no-indent">The 79.39% precision indicates that four out of five flagged students are in genuine academic distress, preserving counselor credibility. Academic retention decisions exhibit profound cost asymmetry: Cost(FN) &gg; Cost(FP) justifies the sensitive dual-criteria policy, as a supportive 30-minute check-in for a false-positive imposes negligible institutional cost, while missing a genuine dropout candidate forecloses institutional retention opportunities entirely.</p>
    <div class="subsection-title">C. Alert Fatigue Mitigation and Cognitive Load Balancing</div>
    <p class="no-indent">Prior early-warning systems have failed due to advisor alert fatigue: receiving hundreds of unranked notifications causes staff to ignore the system entirely. By establishing a tri-level threshold policy with a mandatory 7-day cooldown, StudentDropout paces intervention volume to institutional capacity, converting chaotic alert spikes into a steady stream of 3–5 high-priority consultations weekly per advisor. This aligns with the 8.4-day manual outreach delay documented by Daniel [28], which the automated system eliminates entirely.</p>
    <div class="subsection-title">D. Threats to Validity</div>
    <p class="no-indent">Table IX outlines methodological threats to validity and the mitigation strategies incorporated into this evaluation.</p>
    <div class="table-container full-width">
      <div class="table-caption"><span class="caption-label">TABLE IX.</span>&nbsp; THREATS TO VALIDITY AND MITIGATION STRATEGIES</div>
      <table class="academic-table">
        <thead><tr><th style="width:16%">Threat Type</th><th style="width:42%">Identified Threat</th><th style="width:42%">Mitigation Implemented</th></tr></thead>
        <tbody>
          <tr><td>Construct</td><td>Survey subjectivity &amp; Likert response bias</td><td>Multi-dimensional aggregation; counselor review gate</td></tr>
          <tr><td>Internal</td><td>Data leakage across training/test splits</td><td>Strict stratified splitting; training-only median imputation</td></tr>
          <tr><td>External</td><td>Single-institution cohort; generalization risk</td><td>Multi-tenant schema designed for cross-campus deployment</td></tr>
          <tr><td>Operational</td><td>Calendar concurrency collision under load</td><td>Atomic MongoDB updates with state transition guards</td></tr>
          <tr><td>Ethical</td><td>Student stigmatization &amp; advisor alert fatigue</td><td>Neutral meeting titles; mandatory 7-day cooldown</td></tr>
        </tbody>
      </table>
    </div>
  </div>{F(9)}</div>"""

# ===========================================================
# PAGE 10 — Discussion E–G + Limitations + Conclusion + Ack + References
# ===========================================================
p10 = f"""<div class="page" id="p10">{H()}
  <div class="page-content two-col">
    <div class="subsection-title">E. Methodological and Practical Limitations</div>
    <ul>
      <li><b>Cross-Sectional Dataset:</b> The dataset captures psychometric survey scores at discrete intervals; it does not model continuous LMS clickstream telemetry.</li>
      <li><b>No Causal Proof:</b> This study does not measure causal reductions in institutional dropout rates over multi-year longitudinal timeframes.</li>
      <li><b>Synthetic Scheduling Bench:</b> Calendar dispatch was validated in a staging environment; legacy CalDAV/Exchange deployments may introduce protocol edge cases.</li>
      <li><b>Fixed Survey Dimensions:</b> The four-item instrument may not capture all relevant attrition predictors; future work should incorporate natural language sentiment analysis of open-text feedback.</li>
    </ul>
    <div class="subsection-title">F. Psychometric Construct Significance</div>
    <p class="no-indent">The primacy of <code>stressManagement</code> (34.2% Gini contribution) underscores that affective load and burnout precede visible academic collapse. Students in distress often maintain adequate grades during early weeks while psychological capacity deteriorates. By capturing affective load before mid-term assessments, the platform enables preventative counseling during the optimal intervention window&mdash;weeks before observable academic failure crystallizes in official records.</p>
    <div class="subsection-title">G. Ethical Considerations and Institutional Governance</div>
    <p class="no-indent">Student educational records constitute sensitive personal data protected under FERPA and India's Digital Personal Data Protection (DPDP) Act, 2023. StudentDropout enforces role-based tenant isolation at the query level, prohibiting cross-institutional data visibility. Predictive scores are never exposed directly to students; instead, students receive supportive check-in invitations framed around course planning. Future deployments should commission independent algorithmic fairness audits disaggregating performance by demographic subgroup to detect and mitigate latent proxy discrimination in survey response distributions.</p>
    <div class="section-title">VI. CONCLUSION</div>
    <p class="no-indent">In this paper, we specified, implemented, and empirically evaluated an end-to-end platform integrating soft-voting ensemble machine learning with automated advisor meeting scheduling for student dropout prevention. Benchmarked on an institutional cohort of 9,470 records, the ensemble classifier achieves 84.21% accuracy (exceeding the majority-class baseline by 16.39&nbsp;pp), 89.25% ROC-AUC, and 79.39% minority-class precision. In functional workflow testing across 50 simulated triage scenarios, the scheduling engine demonstrated 100% execution success, 1.38&nbsp;s mean dispatch latency, zero duplicate bookings, and strict counselor approval gate compliance.</p>
    <p>The results demonstrate that operational workflow automation can be safely married to ML risk stratification when bounded by human-in-the-loop oversight and non-stigmatizing communication protocols. Future work will focus on integrating real-time LMS clickstream telemetry (Canvas/Moodle LTI 1.3), federating the ensemble across multiple university campuses via federated learning, and conducting randomized controlled trials to evaluate the causal retention impact of automated advisory scheduling.</p>
    <p>We emphasize that a predicted dropout score represents a probabilistic early warning indicator intended to mobilize compassionate academic support, not definitive evidence of a student's intention to disenroll. By grounding automated action in ethical human-in-the-loop oversight and non-stigmatizing communication, the StudentDropout architecture establishes a viable, scalable blueprint for closing the prediction-to-action gap in higher education retention engineering.</p>
    <div class="section-title">ACKNOWLEDGMENT</div>
    <p class="no-indent">The authors express sincere gratitude to Dr. Kalyani Hemant Deshmukh and the Department of Computer Science and Engineering, Prof. Ram Meghe Institute of Technology and Research (PRMITR), Badnera-Amravati, for their continuous academic guidance, technical encouragement, and institutional support throughout this research.</p>
    <div class="section-title">REFERENCES</div>
    <ol class="ref-list">
      <li>[1] V. Tinto, <i>Leaving College: Rethinking the Causes and Cures of Student Attrition</i>. Chicago, IL: Univ. Chicago Press, 1993.</li>
      <li>[2] A. Seidman, <i>College Student Retention: Formula for Student Success</i>. Lanham, MD: Rowman &amp; Littlefield, 2012.</li>
      <li>[3] J. Bound, M. F. Lovenheim, and S. Turner, "Why have college completion rates declined?," <i>Am. Econ. J. Appl. Econ.</i>, vol. 2, no. 3, pp. 129–157, 2010.</li>
      <li>[4] K. E. Arnold and M. D. Pistilli, "Course signals at Purdue," in <i>Proc. LAK'12</i>, 2012, pp. 267–270.</li>
      <li>[5] R. S. Baker and P. S. Inventado, "Educational data mining and learning analytics," in <i>Learning Analytics</i>. Springer, 2014, pp. 61–75.</li>
      <li>[6] C. Romero and S. Ventura, "Educational data mining and learning analytics: An updated survey," <i>WIREs Data Min. Knowl. Discov.</i>, vol. 10, no. 3, p. e1355, 2020.</li>
      <li>[7] L. Breiman, "Random forests," <i>Mach. Learn.</i>, vol. 45, no. 1, pp. 5–32, 2001.</li>
      <li>[8] J. H. Friedman, "Greedy function approximation: A gradient boosting machine," <i>Ann. Stat.</i>, vol. 29, no. 5, pp. 1189–1232, 2001.</li>
      <li>[9] F. Pedregosa et al., "Scikit-learn: Machine learning in Python," <i>J. Mach. Learn. Res.</i>, vol. 12, pp. 2825–2830, 2011.</li>
      <li>[10] R. Ferguson, "The state of learning analytics in 2012," KMI Tech. Rep. KMI-12-01, Open Univ., 2012.</li>
      <li>[11] D. Clow, "An overview of learning analytics," <i>Teach. High. Educ.</i>, vol. 18, no. 6, pp. 687–700, 2013.</li>
      <li>[12] G. L. Kramer, <i>Fostering Student Success in the Campus Community</i>. San Francisco, CA: Jossey-Bass, 2007.</li>
      <li>[13] S. Slade and P. Prinsloo, "Learning analytics: Ethical issues and dilemmas," <i>Am. Behav. Sci.</i>, vol. 57, no. 10, pp. 1510–1529, 2013.</li>
      <li>[14] N. Mehrabi et al., "A survey on bias and fairness in machine learning," <i>ACM Comput. Surv.</i>, vol. 54, no. 6, pp. 1–35, 2021.</li>
      <li>[15] U.S. Dept. of Education, "Family Educational Rights and Privacy Act (FERPA)," 34 CFR Part 99, 2020.</li>
      <li>[16] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in <i>NeurIPS</i>, 2017, pp. 4765–4774.</li>
      <li>[17] J. Kuzilek, M. Hlosta, and Z. Zdrahal, "Open University Learning Analytics Dataset," <i>Sci. Data</i>, vol. 4, p. 170171, 2017.</li>
      <li>[18] P. Cortez and A. M. G. Silva, "Using data mining to predict secondary school student performance," in <i>Proc. FUBUTEC</i>, 2008.</li>
      <li>[19] F. Agrusti, G. Bonavolont&agrave;, and M. Mezzini, "Analytical student dropout prediction," <i>Int. J. Educ. Technol. High. Educ.</i>, vol. 17, p. 39, 2020.</li>
      <li>[20] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in <i>Proc. 22nd ACM SIGKDD</i>, 2016, pp. 785–794.</li>
      <li>[21] L. I. Kuncheva, <i>Combining Pattern Classifiers</i>. Hoboken, NJ: Wiley, 2014.</li>
      <li>[22] N. V. Chawla et al., "SMOTE: Synthetic minority over-sampling technique," <i>J. Artif. Intell. Res.</i>, vol. 16, pp. 321–357, 2002.</li>
      <li>[23] H. He and E. A. Garcia, "Learning from imbalanced data," <i>IEEE Trans. Knowl. Data Eng.</i>, vol. 21, no. 9, pp. 1263–1284, 2009.</li>
      <li>[24] T. Saito and M. Rehmsmeier, "The precision-recall plot is more informative than the ROC plot," <i>PLoS ONE</i>, vol. 10, no. 3, p. e0118432, 2015.</li>
      <li>[25] D. M. W. Powers, "Evaluation: From precision, recall and F-measure to ROC," <i>J. Mach. Learn. Technol.</i>, vol. 2, no. 1, pp. 37–63, 2011.</li>
      <li>[26] A. Niculescu-Mizil and R. Caruana, "Predicting good probabilities with supervised learning," in <i>Proc. ICML</i>, 2005, pp. 625–632.</li>
      <li>[27] M. Hlosta et al., "Modelling student dropout: What is the impact of different features?," in <i>Proc. EDM</i>, 2017.</li>
      <li>[28] B. K. Daniel, "Big Data and data science in higher education," <i>Int. J. Educ. Technol. High. Educ.</i>, vol. 12, no. 1, pp. 904–925, 2015.</li>
    </ol>
  </div>{F(10)}</div>"""

# ===========================================================
# CSS
# ===========================================================
CSS = """
  @page { size: 210mm 297mm; margin: 0; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { margin:0; padding:0; background:#f1f5f9; font-family:'Times New Roman',Times,serif; color:#000; }
  .page { width:210mm; height:297mm; max-height:297mm; margin:0 auto; background:#fff;
          padding:16pt 72pt 20pt 72pt; position:relative; page-break-after:always;
          break-after:page; overflow:hidden; }
  @media screen { .page { margin-bottom:20px; box-shadow:0 4px 12px rgba(0,0,0,.15); } }

  /* Header */
  .header { display:flex; align-items:center; height:38pt; margin-bottom:3pt; }
  .header-logo { width:48pt; height:36pt; display:flex; align-items:center; }
  .header-logo img { width:44pt; height:auto; }
  .header-text { flex:1; text-align:center; margin-left:8pt; }
  .journal-title { font-size:9.6pt; font-weight:bold; line-height:1.2; }
  .journal-meta { font-size:7.8pt; line-height:1.2; color:#222; }
  .header-rule { width:100%; height:.8px; background:#000; margin-bottom:8pt; }

  /* Footer */
  .footer-rule { position:absolute; bottom:36pt; left:72pt; right:72pt; height:.8px; background:#000; }
  .footer { position:absolute; bottom:18pt; left:72pt; right:72pt; height:16pt;
             display:flex; justify-content:center; align-items:center; font-size:8pt; }

  /* Content */
  .page-content { height:716pt; overflow:hidden; }
  .two-col { column-count:2; column-gap:12pt; height:100%; text-align:justify; }
  .full-width { column-span:all; width:100%; }

  /* Title */
  .title-block { text-align:center; margin-bottom:5pt; }
  h1.paper-title { font-size:13.5pt; font-weight:bold; line-height:1.22; margin:0 0 4pt 0; }
  .author-names { font-size:9.8pt; font-weight:bold; margin-bottom:2pt; line-height:1.25; }
  .author-affiliation { font-size:8.3pt; color:#222; margin-bottom:2pt; line-height:1.25; }
  .author-email { font-size:8pt; color:#333; margin-bottom:3pt; line-height:1.25; }
  .divider-rule { text-align:center; font-size:7pt; color:#555; margin:2pt 0 5pt 0; }

  /* Sections */
  .section-title { font-size:9.6pt; font-weight:bold; text-transform:uppercase;
                   margin-top:6pt; margin-bottom:2pt; break-after:avoid; }
  .subsection-title { font-size:8.8pt; font-weight:bold; margin-top:5pt; margin-bottom:2pt; break-after:avoid; }

  /* Paragraphs */
  p { font-size:9.3pt; line-height:1.28; margin-top:0; margin-bottom:3pt;
      text-indent:10pt; text-align:justify; hyphens:auto; }
  p.no-indent { text-indent:0; }
  p.abstract-para { font-size:8.7pt; line-height:1.22; text-indent:0; margin-bottom:4pt; text-align:justify; }
  .abstract-label,.keywords-label { font-weight:bold; }
  p.keywords-para { font-size:8.7pt; line-height:1.22; text-indent:0; margin-bottom:5pt; text-align:justify; }

  /* Lists */
  ul { margin:0 0 4pt 0; padding-left:12pt; font-size:9.1pt; line-height:1.27; }
  li { margin-bottom:2pt; text-align:justify; }

  /* Equations */
  .equation-box { display:flex; justify-content:space-between; align-items:center;
                  padding:1pt 4pt; margin:3pt 0; font-size:8.6pt; font-style:italic; }
  .math-expr { flex:1; text-align:center; }
  .eq-number { font-style:normal; font-weight:bold; }

  /* Tables */
  .table-container { margin:4pt 0; width:100%; break-inside:avoid; }
  .table-caption { font-size:7.6pt; font-weight:bold; text-align:center; margin-bottom:2pt;
                   text-transform:uppercase; letter-spacing:.3px; }
  table.academic-table { width:100%; border-collapse:collapse; font-size:7.4pt; line-height:1.18; }
  table.academic-table th { border-top:1px solid #000; border-bottom:.8px solid #000;
                             padding:2.8pt 2pt; text-align:left; font-weight:bold; }
  table.academic-table td { padding:2.2pt 2pt; border-bottom:.4px solid #cbd5e1;
                             text-align:left; vertical-align:top; }
  table.academic-table tr:last-child td { border-bottom:1px solid #000; }

  /* Figures */
  .figure-container { margin:4pt 0; text-align:center; break-inside:avoid; width:100%; }
  .figure-caption { font-size:7.5pt; line-height:1.2; text-align:justify; margin-top:2pt; }
  .fig-title { font-weight:bold; }

  /* References */
  ol.ref-list { margin:0; padding-left:10pt; font-size:7.5pt; line-height:1.2; list-style:none; }
  ol.ref-list li { margin-bottom:2pt; text-align:justify; }

  code { font-family:'Courier New',monospace; font-size:8.0pt; }
"""

HTML = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>StudentDropout Research Paper</title>
<style>{CSS}</style></head>
<body>
{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}{p9}{p10}
</body></html>"""

with open(HTML_PATH,"w",encoding="utf-8") as fh:
    fh.write(HTML)
print("HTML written. Building PDF...")

subprocess.run([
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new","--disable-gpu","--no-pdf-header-footer",
    f"--print-to-pdf={PDF_PATH}", HTML_PATH
], check=True)
print("PDF built.")

doc = pymupdf.open(PDF_PATH)
print(f"Pages: {len(doc)},  size: {os.path.getsize(PDF_PATH):,} bytes")
for i, pg in enumerate(doc):
    bl = [b for b in pg.get_text("blocks") if b[1]>58 and b[3]<802]
    if bl:
        top = min(b[1] for b in bl); bot = max(b[3] for b in bl)
        used = bot-top; fill = round(used/(bot-65)*100 if bot>65 else 0,1)
        print(f"  P{i+1}: bot={bot:.0f}, clearance={805-bot:.0f}pt")
    pix = pg.get_pixmap(dpi=150)
    pix.save(os.path.join(PAGES_DIR, f"page_{i+1}.png"))
print("Done — check pages/ for PNG previews.")
