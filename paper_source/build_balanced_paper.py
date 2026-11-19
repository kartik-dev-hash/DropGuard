import os
import subprocess
import base64
import pymupdf

HTML_PATH = r"d:\StudentDropout\paper_source\StudentDropout_Research_Paper.html"
FINAL_PDF_PATH = r"d:\StudentDropout\StudentDropout_Research_Paper.pdf"
PAGES_DIR = r"d:\StudentDropout\paper_source\pages"

os.makedirs(PAGES_DIR, exist_ok=True)

# Read logo base64
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

# PAGE 1
page1 = f"""
<div class="page" id="page-1">
  {get_header()}
  
  <div class="title-block">
    <h1 class="paper-title">Integrating Machine Learning Ensembles and Automated Advisory Workflows for Early Student Dropout Prediction and Support Intervention Scheduling</h1>
    
    <div class="author-names">
      Kartik Nilesh Raghuwanshi<sup>1</sup>, Dr. Kalyani Hemant Deshmukh<sup>2</sup>
    </div>
    
    <div class="author-affiliation">
      1 B.Tech Final-Year Student, 2 Guide, Department of Computer Science and Engineering<br>
      Prof. Ram Meghe Institute of Technology and Research, Badnera-Amravati, Maharashtra, India
    </div>
    
    <div class="author-email">
      Corresponding e-mail: raghuwanshikartik521@gmail.com, khdeshmukh@mitra.ac.in
    </div>

    <div class="divider-rule">-------------------------------------------------------------***-------------------------------------------------------------</div>
  </div>

  <div class="page-content two-column">
    <div class="abstract-box">
      <p class="no-indent"><span class="abstract-title">Abstract &mdash;</span> Higher education institutions face significant student attrition rates that adversely impact institutional sustainability, degree completion metrics, and individual socioeconomic mobility. While supervised machine learning models can identify students exhibiting early signs of academic disengagement, generating a probabilistic risk score in isolation rarely initiates timely institutional intervention. This paper presents an end-to-end early warning and automated intervention platform that couples a dual-algorithm soft-voting ensemble classifier (combining Random Forest and Gradient Boosted Decision Trees) with an automated academic advisor meeting-scheduling engine. The predictive pipeline is evaluated on an institutional cohort of 9,470 student records parameterized across four core psychometric and academic engagement dimensions (academic engagement, support satisfaction, stress management, and peer belongingness), exhibiting a 32.20% positive dropout-risk class prevalence. Model inferences are governed by an actionable dual-criteria triage policy: students scoring below critical survey thresholds (&le; 2.5/5.0) or generating ensemble predicted dropout probabilities <i>p</i>(<b>x</b>) &ge; 0.50 trigger retention workflows, with direct calendar slot reservation activated at high risk (<i>p</i>(<b>x</b>) &ge; 0.80) subject to mandatory human counselor review and a 7-day cooldown mechanism. On a held-out test split of 2,368 students, the soft-voting ensemble achieves an accuracy of 84.21% (exceeding the 67.82% majority-class baseline by 16.39 percentage points), precision of 79.39%, recall of 68.77%, F1-score of 73.70%, and an area under the ROC curve (ROC-AUC) of 89.25%. In operational test-bench verification across 50 simulated triage scenarios, the automated calendar scheduling engine recorded a 100% execution success rate with a mean dispatch latency of 1.38 seconds, zero duplicate calendar bookings, and 100% adherence to human counselor approval gates. The test bench evaluates a cross-sectional dataset and automated dispatch rules; this study does not measure longitudinal graduation rates or causal attrition reduction in live campus environments. A predicted risk score constitutes a probabilistic early-warning indicator for supportive guidance rather than definitive evidence of disenrollment intent.</p>
      
      <div class="keywords-block">
        <span class="keywords-title">Key Words:</span> Student dropout prediction, Ensemble machine learning, Random Forest, Gradient Boosting, Academic advising, Workflow automation, Early warning system, Algorithmic fairness, Human-in-the-loop.
      </div>
    </div>

    <div class="section-title">I. INTRODUCTION</div>
    
    <div class="subsection-title">A. Background and Motivation</div>
    <p>Student attrition remains one of the most pressing structural and socioeconomic challenges confronting global higher education institutions [1]. Empirical studies indicate that between 25% and 40% of enrolled undergraduate students withdraw or disengage permanently prior to degree completion, with the acute attrition window occurring during the initial four semesters of study [2]. Beyond the substantial institutional revenue losses associated with uncollected tuition and underutilized academic facilities, student departure produces long-term personal economic scarring, diminishes social mobility, and compromises institutional completion benchmarks mandated by academic accrediting bodies [3].</p>
    
    <p>Historically, academic institutions have relied on retrospective early warning mechanisms, such as mid-term grade reports, delinquent tuition flags, and post-hoc academic probation notifications [4]. However, by the time academic failure or non-attendance appears on official transcripts, the underlying psychosocial, environmental, or financial stressors have typically compounded to an irreversible degree [5]. Educational Data Mining (EDM) and Learning Analytics (LA) have emerged to address this latency by training supervised machine learning models to identify subtle risk patterns across demographic, psychometric, and institutional feedback records [6].</p>

    <p>Ensemble machine learning architectures &mdash; most notably bagging via Random Forests and boosting via Gradient Boosted Decision Trees (GBDT) &mdash; have demonstrated superior predictive discrimination on tabular, non-linear educational data compared to classical logistic regression and over-parameterized deep neural networks [7, 8]. By combining a diverse manifold of randomized decision trees that minimize variance with sequential gradient-guided decision stumps that iteratively minimize residual bias, soft-voting ensembles deliver calibrated class probabilities that reflect multi-dimensional student vulnerability [9].</p>

    <div class="subsection-title">B. Research Problem and Contributions</div>
    <p>The research problem is how to combine an in-semester psychometric feedback instrument, a soft-voting ensemble classifier, a dual-criteria triage policy, and a conflict-free calendar scheduling engine into a fault-tolerant, privacy-conscious web platform, and how to evaluate its predictive accuracy and operational execution under measurable engineering criteria. This paper presents <b>StudentDropout</b> and makes the following contributions:</p>
    <ul>
      <li>An end-to-end architecture that links multi-tenant web portals, student survey capture, an ensemble machine learning classifier, dual-criteria triage policies, and an automated calendar slot allocation engine.</li>
    </ul>
  </div>
  {get_footer(1)}
</div>
"""

# PAGE 2
page2 = f"""
<div class="page" id="page-2">
  {get_header()}
  <div class="page-content two-column">
    <ul>
      <li>A dual-stage evaluation protocol separating classifier discrimination metrics (accuracy, precision, recall, F1, ROC-AUC) from operational workflow parameters (latency, execution success rate, duplicate booking rate), explicitly stating denominators for all quantitative findings.</li>
      <li>A human-in-the-loop decision-support framework incorporating counselor review queues, non-stigmatizing calendar artifacts, role-based data isolation, and a 7-day cooldown mechanism to address ethical and privacy mandates.</li>
      <li>An empirical benchmark on 9,470 verified student records, achieving an 84.21% classification accuracy (+16.39 percentage points above majority baseline) and validating automated advisory slot scheduling within 1.38 seconds across 50 functional test runs.</li>
    </ul>

    <p class="no-indent">The rest of the paper is organized as follows. Section II reviews related work, Section III describes the methodology and architecture, Section IV reports empirical results, Section V discusses validity, limitations, and ethics, and Section VI concludes.</p>

    <div class="section-title">II. LITERATURE REVIEW</div>
    
    <div class="subsection-title">A. Student Dropout Prediction in Higher Education</div>
    <p>Educational data mining has explored diverse feature spaces to forecast undergraduate discontinuation. Landmark investigations utilizing the Open University Learning Analytics Dataset (OULAD) [17] and Portuguese higher education cohorts [18] have demonstrated that continuous behavioural log attributes &mdash; such as Virtual Learning Environment (VLE) interaction frequency, quiz completion timeliness, and assessment score trajectories &mdash; exhibit strong correlations with student success. Agrusti et al. [19] applied logistic regression and artificial neural networks to administrative enrollment records, attaining classification accuracies between 72% and 78%. However, their analysis relied heavily on pre-entry variables (standardized test scores, high school rank), which offer limited utility for actionable, in-semester remediation once a student matriculates.</p>

    <div class="subsection-title">B. Ensemble Methods and Gradient Boosting</div>
    <p>Ensemble tree algorithms have repeatedly established empirical superiority on tabular educational benchmarks. Random Forests, formalized by Breiman [7], mitigate overfitting by aggregating decorrelated decision trees constructed on bootstrap samples with random feature subsampling. Concurrently, Gradient Boosted Decision Trees, developed by Friedman [8], optimize arbitrary differentiable loss functions via stagewise gradient descent in function space. Recent benchmark comparisons by Chen et al. [20] on educational datasets confirmed that tree ensembles consistently outperform deep multi-layer perceptrons, which are susceptible to overfitting on small-to-moderate tabular cohorts characterized by heterogeneous categorical and continuous scales. Soft-voting ensembles, which average class posterior probabilities across bagging and boosting estimators, have shown enhanced calibration and variance dampening in clinical and financial domains [21], yet their application to multi-tenant educational advising workflows remains under-explored.</p>

    <div class="subsection-title">C. Class Imbalance, Survey Subjectivity, and Algorithmic Fairness</div>
    <p>A persistent challenge in educational attrition modeling is target class imbalance, as retained students typically outnumber dropouts by margins ranging from 2:1 to 5:1 [22]. Standard classifiers optimizing global accuracy tend to collapse toward the majority class, producing inflated accuracy accompanied by unacceptably low minority recall [23]. Saito and Rehmsmeier [24] established that the Area Under the Precision-Recall Curve (PR-AUC) provides a more informative assessment of performance than ROC-AUC in skewed scenarios. Beyond numerical imbalance, self-reported student feedback introduces subjective reporting bias [25]. Consequently, researchers emphasize that algorithmic risk scores must be treated as probabilistic triage flags rather than deterministic categorizations, necessitating transparent feature contribution analysis and non-punitive intervention policies [13, 26].</p>

    <div class="subsection-title">D. Workflow Automation and Advisor Decision Support</div>
    <p>While algorithmic modeling has advanced substantially, workflow automation within institutional student affairs remains nascent [27]. Modern institutional interventions predominantly rely on manual case management systems, where academic advisors manually triage spreadsheets and initiate uncoordinated student contact [28]. Workflow automation frameworks, such as n8n, Apache Airflow, and webhook-driven cloud microservices, have transformed enterprise customer relationship management (CRM) and human resources [29], yet their integration into proactive academic advising remains rare. Recent studies exploring conversational AI agents and robotic process automation (RPA) in educational administration [30] highlight substantial reductions in administrative response latency, but frequently overlook human counselor oversight, calendar race conditions, and duplicate alert suppression.</p>

    <div class="subsection-title">E. Summary and Research Gap</div>
    <p class="no-indent">The sources above address largely separate questions: researchers optimize classification metrics in offline notebooks, while academic institutions deploy isolated advising software without predictive intelligence. Table I summarizes representative prior literature. What is missing is a unified, deployable platform joining student survey capture, an ensemble predictive model, an actionable triage policy, and an automated conflict-free calendar booking engine under strict human counselor oversight.</p>

    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE I.</span> SUMMARY OF SELECTED RELATED WORK</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th style="width:16%">Ref.</th>
            <th style="width:24%">Dataset / Setting</th>
            <th style="width:22%">Methodology</th>
            <th style="width:22%">Primary Finding</th>
            <th style="width:16%">Relevance Here</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>[19]</td>
            <td>Italian cohort (N = 3,420)</td>
            <td>Logistic Reg., ANN</td>
            <td>75.4% accuracy on pre-entry data</td>
            <td>Shows need for in-semester feedback</td>
          </tr>
          <tr>
            <td>[17]</td>
            <td>OULAD (N = 32,593)</td>
            <td>k-NN, Decision Trees</td>
            <td>Clickstream volume correlates with pass</td>
            <td>Motivates targeted survey dimensions</td>
          </tr>
          <tr>
            <td>[20]</td>
            <td>LMS logs (N = 12,800)</td>
            <td>XGBoost, CatBoost</td>
            <td>GBDT beats DNNs by +6.2% F1</td>
            <td>Validates tree boosting on tabular data</td>
          </tr>
          <tr>
            <td>[24]</td>
            <td>Class imbalance study</td>
            <td>PR-AUC vs ROC-AUC</td>
            <td>PR-AUC better under severe skew</td>
            <td>Governs metric reporting protocol</td>
          </tr>
          <tr>
            <td>[28]</td>
            <td>UK cohort (N = 1,200)</td>
            <td>Manual advisor alerts</td>
            <td>Early contact improves retention by 8%</td>
            <td>Motivates automated slot allocation</td>
          </tr>
          <tr>
            <td><b>Ours</b></td>
            <td><b>Cohort (N = 9,470)</b></td>
            <td><b>Soft-Voting Ensemble</b></td>
            <td><b>84.21% acc, 89.25% AUC, 1.38s booking</b></td>
            <td><b>Integrates ML with automated calendar</b></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  {get_footer(2)}
</div>
"""

# PAGE 3
page3 = f"""
<div class="page" id="page-3">
  {get_header()}
  <div class="page-content two-column">
    <div class="section-title">III. METHODOLOGY</div>
    
    <div class="subsection-title">A. Problem Formulation and Research Questions</div>
    <p class="no-indent">Let <i>S</i> denote an institution with <i>K</i> registered academic tenants. For a student <i>i</i> enrolled within tenant <i>k</i>, let <b>x</b><sub><i>i</i></sub> = [<i>x</i><sub><i>i</i>,1</sub>, <i>x</i><sub><i>i</i>,2</sub>, <i>x</i><sub><i>i</i>,3</sub>, <i>x</i><sub><i>i</i>,4</sub>]<sup><i>T</i></sup> &isin; [1.0, 5.0]<sup>4</sup> represent a multidimensional survey feature vector capturing academic engagement (<i>x</i><sub>1</sub>), support satisfaction (<i>x</i><sub>2</sub>), stress management (<i>x</i><sub>3</sub>), and belongingness (<i>x</i><sub>4</sub>). Let <i>Y</i><sub><i>i</i></sub> &isin; {{0, 1}} represent the true binary student retention state (0 = Retained, 1 = Dropout Risk). The prediction objective is to learn <i>f</i> : <b>x</b><sub><i>i</i></sub> &rarr; <i>p</i>(<b>x</b><sub><i>i</i></sub>), where <i>p</i>(<b>x</b><sub><i>i</i></sub>) = <i>P</i>(<i>Y</i><sub><i>i</i></sub> = 1 | <b>x</b><sub><i>i</i></sub>). The operational objective is to evaluate a policy &Phi;(<i>p</i>(<b>x</b><sub><i>i</i></sub>), <b>x</b><sub><i>i</i></sub>, <i>H</i><sub><i>i</i></sub>) &rarr; <i>A</i><sub><i>i</i></sub> mapping inferences to actions <i>A</i><sub><i>i</i></sub> &isin; {{Monitor, Flag_Advisor, Auto_Schedule_Meeting}} with latency &le; 2.0s, zero calendar collisions, and a 7-day cooldown (&Delta;<i>t</i> &ge; 7 days).</p>
    <p>Four research questions guide the evaluation. <b>RQ1:</b> Does a dual-model soft-voting ensemble achieve superior accuracy and recall over baseline heuristics on multi-attribute student feedback data? <b>RQ2:</b> Can a dual-criteria triage policy isolate acute retention candidates without imposing prohibitive false-positive alert burdens on academic counselors? <b>RQ3:</b> Does the automated calendar engine achieve sub-two-second latency while guaranteeing zero collisions and 100% cooldown compliance? <b>RQ4:</b> How does a human-in-the-loop counselor authorization stage mitigate ethical and privacy vulnerabilities?</p>

    <div class="subsection-title">B. System Architecture</div>
    <p class="no-indent">The architecture consists of ten modular functional components, as illustrated in Fig. 1. The student portal captures monthly Likert self-assessments. A database-level cycle locking engine enforces survey integrity via a compound unique index `[studentId, academicCycle]`. The backend service performs schema validation, boundary verification, and normalization before dispatching feature vectors to the Python ML microservice.</p>
    
    <p>The ML service invokes a soft-voting ensemble of Random Forest and Gradient Boosted Decision Trees, returning posterior risk probabilities <i>p</i>(<b>x</b>). The Retention Rule Engine evaluates dual criteria: students with raw scores &le; 2.5 or <i>p</i>(<b>x</b>) &ge; 0.50 are triaged into the Academic Counselor Action Center. For acute cases (<i>p</i> &ge; 0.80), the scheduling engine identifies the earliest contiguous 30-minute availability slot across seven business days (09:00 to 17:00), verifies cooldown status, executes an atomic reservation, and generates a Google Calendar event with a video conference link.</p>

    <div class="figure-container full-width" style="margin: 4px 0 6px 0;">
      <!-- SVG Fig 1 -->
      <svg viewBox="0 0 720 200" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
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

        <rect x="8" y="10" width="130" height="175" rx="5" fill="url(#g1)" stroke="#94a3b8" stroke-width="1.2"/>
        <text x="73" y="26" font-size="9" font-weight="bold" text-anchor="middle" fill="#0f172a">1. Ingestion & Portals</text>
        <rect x="18" y="34" width="110" height="30" rx="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
        <text x="73" y="48" font-size="7.5" text-anchor="middle" fill="#1e293b">Student Portal</text>
        <text x="73" y="58" font-size="6.5" text-anchor="middle" fill="#64748b">(Monthly Survey)</text>
        <rect x="18" y="70" width="110" height="30" rx="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
        <text x="73" y="84" font-size="7.5" text-anchor="middle" fill="#1e293b">Counselor Portal</text>
        <text x="73" y="94" font-size="6.5" text-anchor="middle" fill="#64748b">(Triage Action Center)</text>
        <rect x="18" y="106" width="110" height="30" rx="3" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
        <text x="73" y="120" font-size="7.5" text-anchor="middle" fill="#1e293b">Platform Admin</text>
        <text x="73" y="130" font-size="6.5" text-anchor="middle" fill="#64748b">(Tenant & RBAC)</text>
        <rect x="18" y="142" width="110" height="30" rx="3" fill="#f8fafc" stroke="#0284c7" stroke-width="0.8"/>
        <text x="73" y="155" font-size="7" font-weight="bold" text-anchor="middle" fill="#0369a1">Cycle Locking</text>
        <text x="73" y="165" font-size="6" text-anchor="middle" fill="#64748b">Compound Unique Index</text>

        <line x1="138" y1="95" x2="162" y2="95" stroke="#334155" stroke-width="1.5" marker-end="url(#arr1)"/>

        <rect x="165" y="10" width="130" height="175" rx="5" fill="url(#g2)" stroke="#7dd3fc" stroke-width="1.2"/>
        <text x="230" y="26" font-size="9" font-weight="bold" text-anchor="middle" fill="#0369a1">2. Data Engine & DB</text>
        <rect x="175" y="36" width="110" height="36" rx="3" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
        <text x="230" y="50" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0284c7">Feature Normalizer</text>
        <text x="230" y="62" font-size="6.5" text-anchor="middle" fill="#475569">4-D Psychometrics [1, 5]</text>
        <rect x="175" y="80" width="110" height="42" rx="3" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
        <text x="230" y="94" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0284c7">MongoDB Database</text>
        <text x="230" y="104" font-size="6.5" text-anchor="middle" fill="#475569">Tenants, Feedback,</text>
        <text x="230" y="114" font-size="6.5" text-anchor="middle" fill="#475569">RetentionActions</text>
        <rect x="175" y="130" width="110" height="36" rx="3" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
        <text x="230" y="144" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0284c7">Validation Engine</text>
        <text x="230" y="154" font-size="6.5" text-anchor="middle" fill="#475569">Schema & Bound Checks</text>

        <line x1="295" y1="95" x2="319" y2="95" stroke="#334155" stroke-width="1.5" marker-end="url(#arr1)"/>

        <rect x="322" y="10" width="140" height="175" rx="5" fill="url(#g3)" stroke="#fcd34d" stroke-width="1.2"/>
        <text x="392" y="26" font-size="9" font-weight="bold" text-anchor="middle" fill="#b45309">3. ML Ensemble & Triage</text>
        <rect x="332" y="36" width="120" height="38" rx="3" fill="#ffffff" stroke="#fde68a" stroke-width="0.8"/>
        <text x="392" y="50" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#b45309">Ensemble Classifier</text>
        <text x="392" y="62" font-size="6.5" text-anchor="middle" fill="#78350f">RF (180) + GBDT (150)</text>
        <rect x="332" y="82" width="120" height="36" rx="3" fill="#ffffff" stroke="#fde68a" stroke-width="0.8"/>
        <text x="392" y="96" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#b45309">Soft-Voting Aggregator</text>
        <text x="392" y="106" font-size="6.5" text-anchor="middle" fill="#78350f">p(x) = 0.5(P_RF + P_GB)</text>
        <rect x="332" y="126" width="120" height="40" rx="3" fill="#ffffff" stroke="#fde68a" stroke-width="0.8"/>
        <text x="392" y="140" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#b45309">Dual Triage Policy</text>
        <text x="392" y="150" font-size="6.5" text-anchor="middle" fill="#78350f">Score &le; 2.5 or p &ge; 0.50</text>

        <line x1="462" y1="95" x2="486" y2="95" stroke="#334155" stroke-width="1.5" marker-end="url(#arr1)"/>

        <rect x="489" y="10" width="222" height="175" rx="5" fill="url(#g4)" stroke="#86efac" stroke-width="1.2"/>
        <text x="600" y="26" font-size="9" font-weight="bold" text-anchor="middle" fill="#15803d">4. Counselor HITL & Automation</text>
        
        <rect x="499" y="34" width="202" height="36" rx="3" fill="#ffffff" stroke="#bbf7d0" stroke-width="0.8"/>
        <text x="600" y="48" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#166534">Counselor Oversight (HITL)</text>
        <text x="600" y="58" font-size="6.5" text-anchor="middle" fill="#334155">Confirm Intervention | Snooze Alert | Custom Override</text>

        <rect x="499" y="78" width="202" height="42" rx="3" fill="#ffffff" stroke="#bbf7d0" stroke-width="0.8"/>
        <text x="600" y="92" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#166534">Automated Scheduling Engine</text>
        <text x="600" y="102" font-size="6.5" text-anchor="middle" fill="#334155">Conflict-free 30-min slot search across 7 business days</text>
        <text x="600" y="112" font-size="6" text-anchor="middle" fill="#15803d">Atomic MongoDB upsert to prevent double-booking</text>

        <rect x="499" y="128" width="202" height="38" rx="3" fill="#ffffff" stroke="#bbf7d0" stroke-width="0.8"/>
        <text x="600" y="142" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#166534">Calendar & Email Dispatcher</text>
        <text x="600" y="152" font-size="6.5" text-anchor="middle" fill="#334155">Google Calendar Event + Google Meet Link</text>
        <text x="600" y="160" font-size="6" text-anchor="middle" fill="#64748b">Non-stigmatizing subject: "Academic Support & Guidance"</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 1.</span> End-to-end architecture of the StudentDropout platform, illustrating data flow from student survey entry and tenant isolation, through soft-voting ensemble ML inference and dual-criteria triage, to counselor oversight and automated conflict-free calendar booking.</div>
    </div>

    <div class="subsection-title">C. Dataset Description and Characteristics</div>
    <p class="no-indent">The empirical evaluation is conducted on a curated, verified institutional cohort comprising 9,470 student assessment records. Each record encompasses four continuous psychometric engagement metrics normalized to the domain [1.0, 5.0], alongside an empirical ground-truth retention indicator (0 = Retained, 1 = Dropout Risk). Table II summarizes the cohort characteristics and the stratified train-test partition.</p>

    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE II.</span> DATASET CHARACTERISTICS AND PARTITIONS</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th>Partition</th>
            <th>Total (N)</th>
            <th>Retained (0)</th>
            <th>Dropout Risk (1)</th>
            <th>Prevalence (%)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Training Split (75%)</td>
            <td>7,102</td>
            <td>4,815</td>
            <td>2,287</td>
            <td>32.20%</td>
          </tr>
          <tr>
            <td>Testing Split (25%)</td>
            <td>2,368</td>
            <td>1,606</td>
            <td>762</td>
            <td>32.18%</td>
          </tr>
          <tr>
            <td><b>Total Population</b></td>
            <td><b>9,470</b></td>
            <td><b>6,421</b></td>
            <td><b>3,049</b></td>
            <td><b>32.20%</b></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="figure-container">
      <!-- SVG Fig 2 Class Distribution -->
      <svg viewBox="0 0 340 120" style="width: 100%; max-width: 340px; height: auto; font-family: 'Times New Roman', serif;">
        <line x1="50" y1="10" x2="50" y2="95" stroke="#475569" stroke-width="1.2"/>
        <line x1="50" y1="95" x2="310" y2="95" stroke="#475569" stroke-width="1.2"/>
        
        <line x1="45" y1="95" x2="310" y2="95" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="40" y="98" font-size="7" text-anchor="end" fill="#475569">0</text>
        
        <line x1="45" y1="65" x2="310" y2="65" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="40" y="68" font-size="7" text-anchor="end" fill="#475569">3,500</text>
        
        <line x1="45" y1="25" x2="310" y2="25" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="40" y="28" font-size="7" text-anchor="end" fill="#475569">7,000</text>

        <rect x="90" y="23" width="65" height="72" fill="#0284c7" rx="3" stroke="#0369a1" stroke-width="0.8"/>
        <text x="122.5" y="18" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0369a1">6,421 (67.8%)</text>
        <text x="122.5" y="106" font-size="7.5" text-anchor="middle" fill="#1e293b">Retained (0)</text>

        <rect x="200" y="61" width="65" height="34" fill="#f59e0b" rx="3" stroke="#d97706" stroke-width="0.8"/>
        <text x="232.5" y="56" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#b45309">3,049 (32.2%)</text>
        <text x="232.5" y="106" font-size="7.5" text-anchor="middle" fill="#1e293b">Dropout Risk (1)</text>

        <text x="18" y="55" font-size="7.5" font-weight="bold" text-anchor="middle" transform="rotate(-90 18 55)" fill="#334155">Count</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 2.</span> Target class distribution across the complete student population (N = 9,470), indicating a 32.20% positive dropout risk prevalence.</div>
    </div>
  </div>
  {get_footer(3)}
</div>
"""

# PAGE 4: D. Preprocessing, E. Soft-Voting Classifier (Eqs 1-4), Table III, F. Metrics (Eqs 5-7), G. Decision Rule (Eq 8), Section III.K Implementation Stack, Table IV
page4 = f"""
<div class="page" id="page-4">
  {get_header()}
  <div class="page-content two-column">
    <div class="subsection-title">D. Data Preprocessing and Imputation</div>
    <p class="no-indent">Raw student survey records undergo programmatic cleansing. Missing entries are imputed using feature-wise medians computed strictly over training partitions to prevent data leakage. Input features are standardized via z-score normalization. Stratified sampling preserves the 32.2% positive prevalence across both splits (random seed = 42). Scale bounds are validated to ensure all values conform strictly to the continuous domain [1.0, 5.0].</p>

    <div class="subsection-title">E. Soft-Voting Ensemble Classifier</div>
    <p>To maximize predictive robustness, we formulate a dual-algorithm soft-voting ensemble combining Random Forest (RF) and Gradient Boosted Decision Trees (GBDT). The Random Forest model aggregates <i>B</i> bootstrap-sampled decision trees, where each tree <i>h</i><sub><i>b</i></sub> is trained on a distinct subset of data with randomized feature splits. The ensemble posterior probability is given by:</p>

    <div class="equation-box">
      <div class="math-expr">P<sub>RF</sub>(Y = 1 | <b>x</b>) = (1 / B) &sum;<sub>b=1</sub><sup>B</sup> P<sub>b</sub>(Y = 1 | <b>x</b>)</div>
      <div class="eq-number">(1)</div>
    </div>

    <p>Concurrently, the Gradient Boosting model fits <i>M</i> regression trees sequentially to minimize the negative log-likelihood loss function <i>L</i>(<i>y</i>, <i>F</i>(<b>x</b>)). At iteration <i>m</i>, the pseudo-residuals <i>r</i><sub><i>im</i></sub> are calculated via:</p>

    <div class="equation-box">
      <div class="math-expr">r<sub>im</sub> = &minus; [&part; L(y<sub>i</sub>, F(<b>x</b><sub>i</sub>)) / &part; F(<b>x</b><sub>i</sub>)]<sub>F=F<sub>m&minus;1</sub></sub></div>
      <div class="eq-number">(2)</div>
    </div>

    <p>A regression tree <i>h</i><sub><i>m</i></sub>(<b>x</b>) is trained on <i>r</i><sub><i>im</i></sub>, and the ensemble is updated with shrinkage rate &eta; = 0.08: <i>F</i><sub><i>m</i></sub>(<b>x</b>) = <i>F</i><sub><i>m</i>&minus;1</sub>(<b>x</b>) + &eta; <i>h</i><sub><i>m</i></sub>(<b>x</b>). The GBDT posterior probability is obtained via the logistic sigmoid transform: <i>P</i><sub>GB</sub>(<i>Y</i> = 1 | <b>x</b>) = [1 + exp(&minus;<i>F</i><sub><i>M</i></sub>(<b>x</b>))]<sup>&minus;1</sup>.</p>

    <p>The soft-voting ensemble computes the unweighted arithmetic mean of both base estimators:</p>

    <div class="equation-box">
      <div class="math-expr">p(<b>x</b>) = 0.5 &middot; P<sub>RF</sub>(Y = 1 | <b>x</b>) + 0.5 &middot; P<sub>GB</sub>(Y = 1 | <b>x</b>)</div>
      <div class="eq-number">(3)</div>
    </div>

    <p>The composite model optimizes the binary cross-entropy loss across all <i>N</i> training samples:</p>

    <div class="equation-box">
      <div class="math-expr">L<sub>log</sub> = &minus; (1 / N) &sum;<sub>i=1</sub><sup>N</sup> [ y<sub>i</sub> ln p(<b>x</b><sub>i</sub>) + (1 &minus; y<sub>i</sub>) ln(1 &minus; p(<b>x</b><sub>i</sub>)) ]</div>
      <div class="eq-number">(4)</div>
    </div>

    <div class="table-container">
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
    <p>Classification performance is evaluated using standard discriminative metrics derived from True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN):</p>

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
    <p>To prevent alert fatigue while ensuring vulnerable students receive timely support, we formalize a tripartite decision policy &Phi;(<i>p</i>(<b>x</b>), <b>x</b>) mapping predictions into operational tiers:</p>

    <div class="equation-box">
      <div class="math-expr">Tier(<b>x</b>) = <br>
        &nbsp;&nbsp;Low Risk (Monitor), if p(<b>x</b>) &lt; 0.40 and min(x<sub>j</sub>) &gt; 2.5<br>
        &nbsp;&nbsp;Moderate Risk (Advisor Flag), if 0.40 &le; p(<b>x</b>) &lt; 0.80 or min(x<sub>j</sub>) &le; 2.5<br>
        &nbsp;&nbsp;High Risk (Auto-Schedule), if p(<b>x</b>) &ge; 0.80 and &Delta;t &ge; 7 days
      </div>
      <div class="eq-number">(8)</div>
    </div>

    <div class="subsection-title">H. System Implementation Stack</div>
    <p class="no-indent">The backend is built with Node.js 18 LTS and Express.js, interfacing with MongoDB Community 7.0 via Mongoose ODM. Machine learning models are executed via Python 3.11 with Scikit-Learn 1.3 and Joblib. The frontend is built on React 18 with Tailwind CSS. Table IV outlines the technology stack.</p>

    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE IV.</span> SYSTEM IMPLEMENTATION STACK</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th style="width:25%">Component</th>
            <th style="width:35%">Technology Stack</th>
            <th style="width:40%">Implementation Purpose</th>
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
            <td>Node.js (`meetingScheduler.js`)</td>
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
  {get_footer(4)}
</div>
"""

# PAGE 5: I. Workflow Pipeline, Fig 3, Fig 4, J. Calendar Scheduling, Fig 6, K. Security & Privacy
page5 = f"""
<div class="page" id="page-5">
  {get_header()}
  <div class="page-content">
    <div class="subsection-title">I. Automated Advisory Action Workflow</div>
    <p class="no-indent">Fig. 3 illustrates the operational execution pipeline. Upon survey ingestion, the backend asynchronously issues a REST query to the Python ML microservice. Model probabilities are forwarded to the Retention Rule Engine. For High-Risk students, the system verifies cooldown status. If validated, the meeting allocation service executes an atomic slot reservation, issues calendar invites, and sends notifications simultaneously.</p>

    <div class="figure-container full-width" style="margin: 4px 0 6px 0;">
      <!-- SVG Fig 3 Canvas -->
      <svg viewBox="0 0 720 125" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
        <defs>
          <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b" />
          </marker>
        </defs>

        <rect x="15" y="38" width="105" height="46" rx="4" fill="#f8fafc" stroke="#64748b" stroke-width="1.2"/>
        <text x="67.5" y="56" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">Survey Submission</text>
        <text x="67.5" y="67" font-size="6.8" text-anchor="middle" fill="#475569">POST /api/feedback</text>
        <text x="67.5" y="76" font-size="6.2" text-anchor="middle" fill="#0284c7">Cycle Locked</text>

        <line x1="120" y1="61" x2="148" y2="61" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr2)"/>

        <rect x="152" y="38" width="105" height="46" rx="4" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/>
        <text x="204.5" y="56" font-size="8" font-weight="bold" text-anchor="middle" fill="#0369a1">Feature Validation</text>
        <text x="204.5" y="67" font-size="6.8" text-anchor="middle" fill="#0f172a">Extract 4-D Vector</text>
        <text x="204.5" y="76" font-size="6.2" text-anchor="middle" fill="#475569">Boundary [1.0, 5.0]</text>

        <line x1="257" y1="61" x2="285" y2="61" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr2)"/>

        <rect x="289" y="38" width="115" height="46" rx="4" fill="#fefce8" stroke="#d97706" stroke-width="1.2"/>
        <text x="346.5" y="56" font-size="8" font-weight="bold" text-anchor="middle" fill="#b45309">Ensemble ML Scoring</text>
        <text x="346.5" y="67" font-size="6.8" text-anchor="middle" fill="#78350f">RF + GBDT Inference</text>
        <text x="346.5" y="76" font-size="6.2" text-anchor="middle" fill="#92400e">Output: p(x) &isin; [0, 1]</text>

        <line x1="404" y1="61" x2="432" y2="61" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr2)"/>

        <polygon points="490,28 540,61 490,94 440,61" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/>
        <text x="490" y="58" font-size="7.2" font-weight="bold" text-anchor="middle" fill="#9a3412">Risk Tier?</text>
        <text x="490" y="68" font-size="6.2" text-anchor="middle" fill="#c2410c">Eq. (8)</text>

        <line x1="490" y1="28" x2="490" y2="12" stroke="#1e293b" stroke-width="1.2"/>
        <line x1="490" y1="12" x2="590" y2="12" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
        <text x="535" y="9" font-size="6.8" fill="#15803d">Low (p &lt; 0.40)</text>
        <rect x="595" y="3" width="115" height="22" rx="3" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
        <text x="652.5" y="16" font-size="7.2" text-anchor="middle" fill="#334155">Log & Monitor Only</text>

        <line x1="540" y1="61" x2="590" y2="61" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
        <text x="565" y="55" font-size="6.8" fill="#b45309">Mod (0.40–0.80)</text>
        <rect x="595" y="50" width="115" height="24" rx="3" fill="#fffbeb" stroke="#f59e0b" stroke-width="1"/>
        <text x="652.5" y="61" font-size="7.2" font-weight="bold" text-anchor="middle" fill="#92400e">Advisor Dashboard Flag</text>
        <text x="652.5" y="70" font-size="6.2" text-anchor="middle" fill="#78350f">Manual Review Queue</text>

        <line x1="490" y1="94" x2="490" y2="112" stroke="#1e293b" stroke-width="1.2"/>
        <line x1="490" y1="112" x2="590" y2="112" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arr2)"/>
        <text x="535" y="107" font-size="6.8" fill="#dc2626">High (p &ge; 0.80)</text>
        <rect x="595" y="100" width="115" height="24" rx="3" fill="#ecfdf5" stroke="#10b981" stroke-width="1"/>
        <text x="652.5" y="111" font-size="7.2" font-weight="bold" text-anchor="middle" fill="#065f46">Auto Meeting Engine</text>
        <text x="652.5" y="120" font-size="6.2" text-anchor="middle" fill="#047857">Check Cooldown & Schedule</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 3.</span> Workflow execution pipeline of the Academic Retention Action Engine, demonstrating survey event triggering, feature extraction, ML inference, and tier-based dispatch logic.</div>
    </div>

    <div class="figure-container full-width" style="margin: 4px 0 6px 0;">
      <!-- SVG Fig 4 Sequence Diagram -->
      <svg viewBox="0 0 720 150" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
        <defs>
          <marker id="arr3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 1 L 10 5 L 0 9 z" fill="#0f172a" />
          </marker>
        </defs>

        <rect x="15" y="4" width="85" height="17" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="57.5" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Student</text>
        <line x1="57.5" y1="21" x2="57.5" y2="142" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

        <rect x="130" y="4" width="95" height="17" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="177.5" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Frontend Client</text>
        <line x1="177.5" y1="21" x2="177.5" y2="142" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

        <rect x="255" y="4" width="100" height="17" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="305" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Backend Express</text>
        <line x1="305" y1="21" x2="305" y2="142" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

        <rect x="385" y="4" width="95" height="17" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="432.5" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">ML Service</text>
        <line x1="432.5" y1="21" x2="432.5" y2="142" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

        <rect x="510" y="4" width="95" height="17" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="557.5" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Counselor / Advisor</text>
        <line x1="557.5" y1="21" x2="557.5" y2="142" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

        <rect x="630" y="4" width="80" height="17" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
        <text x="670" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#0f172a">Calendar API</text>
        <line x1="670" y1="21" x2="670" y2="142" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

        <line x1="57.5" y1="31" x2="177.5" y2="31" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="117.5" y="27" font-size="6.2" text-anchor="middle" fill="#1e293b">1. Submit survey responses</text>

        <line x1="177.5" y1="44" x2="305" y2="44" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="241" y="40" font-size="6.2" text-anchor="middle" fill="#1e293b">2. POST /feedback (JWT)</text>

        <line x1="305" y1="57" x2="432.5" y2="57" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="368" y="53" font-size="6.2" text-anchor="middle" fill="#1e293b">3. Request ML inference (x)</text>

        <line x1="432.5" y1="70" x2="305" y2="70" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2,2" marker-end="url(#arr3)"/>
        <text x="368" y="66" font-size="6.2" text-anchor="middle" fill="#1e293b">4. Return p(x) & survey risk</text>

        <line x1="305" y1="85" x2="557.5" y2="85" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="431" y="81" font-size="6.2" text-anchor="middle" fill="#1e293b">5. Push triage event to Advisor Queue</text>

        <line x1="557.5" y1="99" x2="305" y2="99" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="431" y="95" font-size="6.2" text-anchor="middle" fill="#1e293b">6. Counselor validates / approves intervention</text>

        <line x1="305" y1="113" x2="670" y2="113" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="487" y="109" font-size="6.2" text-anchor="middle" fill="#1e293b">7. Allocate conflict-free 30-min slot & create event</text>

        <line x1="670" y1="125" x2="305" y2="125" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2,2" marker-end="url(#arr3)"/>
        <text x="487" y="121" font-size="6.2" text-anchor="middle" fill="#1e293b">8. Return event status & Meet link</text>

        <line x1="305" y1="137" x2="57.5" y2="137" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arr3)"/>
        <text x="181" y="133" font-size="6.2" text-anchor="middle" fill="#1e293b">9. Email invitation with neutral subject & Meet URL</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 4.</span> UML message sequence diagram detailing chronological interactions between the student, web interface, backend Express API, ensemble ML service, human advisor dashboard, and Google Calendar.</div>
    </div>

    <div class="two-column">
      <div class="subsection-title">J. Calendar Scheduling and Responsible Use</div>
      <p>The meeting allocation engine (`meetingScheduler.js`) automates calendar bookings across seven upcoming business days (09:00 to 17:00). Contiguous 30-minute slots are reserved via atomic MongoDB `findOneAndUpdate` operations on `RetentionAction` (`PENDING` &rarr; `SCHEDULED`). To prevent psychological stigmatization, calendar invitations are titled with neutral, supportive descriptors: "Academic Support & Guidance Check-in", as illustrated in Fig. 6.</p>

      <div class="figure-container">
        <!-- SVG Fig 6 Calendar Card -->
        <svg viewBox="0 0 340 120" style="width: 100%; max-width: 340px; height: auto; font-family: 'Times New Roman', serif;">
          <rect x="8" y="6" width="324" height="108" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
          <rect x="8" y="6" width="324" height="20" rx="4" fill="#0284c7"/>
          <rect x="8" y="18" width="324" height="8" fill="#0284c7"/>
          <circle cx="22" cy="16" r="4.5" fill="#ffffff"/>
          <text x="22" y="19" font-size="6.5" font-weight="bold" text-anchor="middle" fill="#0284c7">&check;</text>
          <text x="32" y="19" font-size="7" font-weight="bold" fill="#ffffff">Google Calendar &middot; Advisory Session Confirmed</text>

          <text x="18" y="38" font-size="7.5" font-weight="bold" fill="#0f172a">Event: Academic Support & Guidance Check-in</text>
          <text x="18" y="48" font-size="6.5" fill="#475569"><b>Date/Time:</b> Tuesday, Oct 27, 2026 &middot; 14:00 – 14:30 IST</text>
          <text x="18" y="58" font-size="6.5" fill="#475569"><b>Host:</b> Academic Counselor Office &middot; <b>Attendee:</b> Student (#STD-8492)</text>
          
          <rect x="18" y="64" width="298" height="16" rx="3" fill="#f0fdf4" stroke="#86efac" stroke-width="0.8"/>
          <text x="25" y="75" font-size="6.5" font-weight="bold" fill="#166534">Video Link: https://meet.google.com/stu-acad-guid</text>

          <text x="18" y="92" font-size="6.2" fill="#64748b"><b>Agenda:</b> Proactive academic review, resource navigation, course planning.</text>
          <text x="18" y="101" font-size="5.8" font-style="italic" fill="#94a3b8">Initiated by StudentDropout Retention Engine &middot; Approved by Counselor &middot; 7-Day Cooldown</text>
        </svg>
        <div class="figure-caption"><span class="fig-title">Fig. 6.</span> Generated academic support session calendar card, illustrating non-stigmatizing neutral titling, video conferencing link, and human counselor oversight attribution.</div>
      </div>

      <p class="no-indent"><b>Privacy & FERPA:</b> Password credentials are encrypted using `bcrypt` (salt rounds 10). Authentication utilizes stateless HMAC-SHA256 JWT tokens with 60-minute expiry. Multi-tenant database isolation is strictly enforced via institutional `companyCode` scoping, ensuring counselors cannot view external student records.</p>
    </div>
  </div>
  {get_footer(5)}
</div>
"""

# PAGE 6: IV. RESULTS (A. Classification, Table V, Table VI, Fig 5, B. Workflow Verification, Table VII, Eqs 9-10, C. Observed Behavior, Table VIII)
page6 = f"""
<div class="page" id="page-6">
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

    <p>The soft-voting ensemble demonstrates strong discrimination (84.21% accuracy, 89.25% ROC-AUC). Crucially, on the positive minority class, the model achieves 79.39% precision and 68.77% recall (F1 = 73.70%). The confusion matrix at &tau;<sub>0</sub> = 0.50 is presented in Table VI.</p>

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
      <svg viewBox="0 0 340 120" style="width: 100%; max-width: 340px; height: auto; font-family: 'Times New Roman', serif;">
        <line x1="45" y1="10" x2="45" y2="95" stroke="#475569" stroke-width="1.2"/>
        <line x1="45" y1="95" x2="330" y2="95" stroke="#475569" stroke-width="1.2"/>

        <line x1="40" y1="95" x2="330" y2="95" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="98" font-size="7" text-anchor="end" fill="#475569">0%</text>

        <line x1="40" y1="52" x2="330" y2="52" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="55" font-size="7" text-anchor="end" fill="#475569">50%</text>

        <line x1="40" y1="10" x2="330" y2="10" stroke="#e2e8f0" stroke-width="0.8"/>
        <text x="36" y="13" font-size="7" text-anchor="end" fill="#475569">100%</text>

        <rect x="58" y="24" width="38" height="71" fill="#0284c7" rx="2"/>
        <text x="77" y="20" font-size="7" font-weight="bold" text-anchor="middle" fill="#0369a1">84.2%</text>
        <text x="77" y="106" font-size="7" text-anchor="middle" fill="#1e293b">Acc</text>

        <rect x="114" y="28" width="38" height="67" fill="#0ea5e9" rx="2"/>
        <text x="133" y="24" font-size="7" font-weight="bold" text-anchor="middle" fill="#0284c7">79.4%</text>
        <text x="133" y="106" font-size="7" text-anchor="middle" fill="#1e293b">Prec</text>

        <rect x="170" y="37" width="38" height="58" fill="#f59e0b" rx="2"/>
        <text x="189" y="33" font-size="7" font-weight="bold" text-anchor="middle" fill="#b45309">68.8%</text>
        <text x="189" y="106" font-size="7" text-anchor="middle" fill="#1e293b">Rec</text>

        <rect x="226" y="33" width="38" height="62" fill="#10b981" rx="2"/>
        <text x="245" y="29" font-size="7" font-weight="bold" text-anchor="middle" fill="#047857">73.7%</text>
        <text x="245" y="106" font-size="7" text-anchor="middle" fill="#1e293b">F1</text>

        <rect x="282" y="19" width="38" height="76" fill="#6366f1" rx="2"/>
        <text x="301" y="15" font-size="7" font-weight="bold" text-anchor="middle" fill="#4338ca">89.3%</text>
        <text x="301" y="106" font-size="7" text-anchor="middle" fill="#1e293b">AUC</text>
      </svg>
      <div class="figure-caption"><span class="fig-title">Fig. 5.</span> Test set model performance profile (N = 2,368).</div>
    </div>

    <div class="subsection-title">B. Operational Workflow Verification</div>
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
      <div class="math-expr">R<sub>succ</sub> = (N<sub>succ</sub> / N<sub>total</sub>) &times; 100%, &nbsp;&nbsp; T̄<sub>exec</sub> = (1/N) &sum; &Delta;t<sub>i</sub></div>
      <div class="eq-number">(9–10)</div>
    </div>

    <div class="subsection-title">C. Observed Behavior and System Walkthrough</div>
    <p class="no-indent">Functional walkthroughs verified the complete user lifecycle. Upon login, students access the digital survey form. Duplicate monthly submissions are rejected with HTTP 409 by the compound index. When a student submits ratings with severe distress (e.g., stressManagement = 1.2, academicEngagement = 1.8), the dual triage policy flags the record into the counselor queue within 180 ms. The counselor dashboard presents individual feature breakdowns, allowing advisors to approve automated scheduling with one click.</p>

    <div class="table-container">
      <div class="table-caption"><span class="caption-label">TABLE VIII.</span> SUMMARY OF OBSERVED SYSTEM BEHAVIOR</div>
      <table class="academic-table">
        <thead>
          <tr>
            <th style="width:28%">Function</th>
            <th style="width:34%">Observed Outcome</th>
            <th style="width:38%">Operational Verification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>User Authentication</td>
            <td>JWT issued; role validated</td>
            <td>Protected endpoints blocked</td>
          </tr>
          <tr>
            <td>Survey Ingestion</td>
            <td>Captured 4 Likert scores</td>
            <td>Boundary validation [1.0, 5.0]</td>
          </tr>
          <tr>
            <td>Cycle Locking</td>
            <td>Second POST rejected</td>
            <td>Compound unique index locked</td>
          </tr>
          <tr>
            <td>Ensemble Inference</td>
            <td>Scored within 145 ms</td>
            <td>Calibrated probabilities output</td>
          </tr>
          <tr>
            <td>Counselor Triage</td>
            <td>Action dashboard updated</td>
            <td>Advisors approve or snooze</td>
          </tr>
          <tr>
            <td>Calendar Dispatch</td>
            <td>Created Meet invitation</td>
            <td>Non-stigmatizing titling used</td>
          </tr>
          <tr>
            <td>Cooldown Lock</td>
            <td>Blocked repeat booking</td>
            <td>7-day window respected</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  {get_footer(6)}
</div>
"""

# PAGE 7: D. Answers to RQs, V. DISCUSSION (A. Early Warning, B. Class Imbalance, C. Alert Fatigue, D. Threats to Validity, Table IX, E. Limitations)
page7 = f"""
<div class="page" id="page-7">
  {get_header()}
  <div class="page-content two-column">
    <div class="subsection-title">D. Answers to the Research Questions</div>
    <p class="no-indent"><b>RQ1.</b> On the held-out test split, the soft-voting ensemble achieved 84.21% accuracy (+16.39 percentage points above majority baseline) and 89.25% ROC-AUC, outperforming single-model trees and baseline heuristics. <b>RQ2.</b> The dual-criteria triage policy successfully isolated acute intervention candidates (68.77% recall on minority dropout risk) while containing false positives to 8.47%, limiting advisor alert fatigue. <b>RQ3.</b> The automated calendar engine achieved a mean latency of 1.38 seconds, zero calendar collisions, and 100% cooldown suppression compliance. <b>RQ4.</b> The counselor human-in-the-loop review stage ensured that algorithmic risk scores remained decision-support recommendations rather than automated disciplinary actions, preventing student alienation and preserving FERPA compliance.</p>

    <div class="section-title">V. DISCUSSION</div>
    
    <div class="subsection-title">A. Early Warning versus Definitive Retention</div>
    <p class="no-indent">The reported accuracy must be interpreted with academic discipline. Machine learning classifiers detect statistical correlations between engagement indicators and historical attrition patterns; they do not measure student disenrollment intent or cognitive potential. Labeling a student as "at-risk" risks inducing stereotype threat, anxiety, and self-fulfilling disengagement if communicated clumsily. For this reason, the StudentDropout architecture enforces strict counselor intermediation and neutral calendar naming conventions.</p>

    <div class="subsection-title">B. Class Imbalance and Choice of Metrics</div>
    <p>In the experimental cohort, 32.20% of instances belong to the positive dropout class. A naive classifier predicting retention for every student would achieve 67.82% accuracy. The soft-voting ensemble's 84.21% accuracy represents an authentic +16.39 percentage point lift. Furthermore, the 79.39% precision indicates that four out of five flagged students are in genuine academic distress, which preserves counselor credibility and institutional resources.</p>

    <div class="subsection-title">C. Alert Fatigue and Cooldown Policy</div>
    <p>Prior academic early-warning systems have failed largely due to advisor alert fatigue: receiving hundreds of unranked email notifications causes staff to ignore the system entirely. By establishing a tri-level threshold policy and a mandatory 7-day cooldown between automated calendar bookings, StudentDropout paces intervention volume to institutional capacity.</p>

    <div class="subsection-title">D. Threats to Validity</div>
    <p class="no-indent">Table IX outlines methodological threats to validity and the mitigation strategies incorporated into this evaluation.</p>

    <div class="table-container">
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
            <td>Survey subjectivity & Likert response bias</td>
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
            <td>Student stigmatization & alert fatigue</td>
            <td>Neutral meeting titles; 7-day mandatory cooldown</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="subsection-title">E. Limitations</div>
    <p class="no-indent">Several methodological and practical limitations warrant acknowledgment:</p>
    <ul>
      <li><b>Cross-Sectional Dataset Bounds:</b> The dataset captures standardized psychometric survey scores at discrete monthly intervals; it does not model continuous clickstream telemetry available in enterprise LMS environments.</li>
      <li><b>Absence of Longitudinal Causal Proof:</b> While technical feasibility and scheduling latency are verified, this study does not measure causal reductions in institutional dropout rates over a multi-year timeframe.</li>
      <li><b>Synthetic Scheduling Bench:</b> Calendar dispatch was validated across a staging test bench; institutional deployments with legacy CalDAV/Exchange servers may introduce protocol-specific edge cases.</li>
      <li><b>Fixed Survey Dimensions:</b> The current survey instrument relies on four fixed dimensions; incorporating natural language student feedback via sentiment analysis represents an important future enhancement.</li>
    </ul>
  </div>
  {get_footer(7)}
</div>
"""

# PAGE 8: F. Ethics & Privacy, VI. CONCLUSION, ACKNOWLEDGMENT, REFERENCES ([1] to [24])
page8 = f"""
<div class="page" id="page-8">
  {get_header()}
  <div class="page-content two-column">
    <div class="subsection-title">F. Ethical Considerations and Data Privacy</div>
    <p class="no-indent">Student educational records constitute sensitive personal data protected under regulations including FERPA and India's Digital Personal Data Protection (DPDP) Act, 2023. StudentDropout enforces role-based tenant isolation at the query level, prohibiting cross-institutional data visibility. Predictive scores are never exposed directly to students; instead, students receive supportive check-in invitations framed around course planning and resource navigation.</p>

    <div class="section-title">VI. CONCLUSION</div>
    <p class="no-indent">In this paper, we specified, implemented, and empirically evaluated an end-to-end platform integrating soft-voting ensemble machine learning with automated advisor meeting scheduling for student dropout prevention. Benchmarked on an institutional cohort of 9,470 records, the ensemble classifier achieves an accuracy of 84.21% (exceeding the majority-class baseline by 16.39 percentage points), an ROC-AUC of 89.25%, and a minority-class precision of 79.39%. In functional workflow testing across 50 simulated triage scenarios, the scheduling engine demonstrated a 100% execution success rate with a mean dispatch latency of 1.38 seconds, zero duplicate bookings, and strict adherence to counselor approval gates.</p>

    <p>The results demonstrate that operational workflow automation can be safely married to machine learning risk stratification when bounded by human-in-the-loop oversight and non-stigmatizing communication. Future work will focus on integrating real-time LMS clickstream telemetry (Canvas/Moodle LTI 1.3), federating the ensemble across multiple university campuses, and conducting randomized controlled trials to evaluate the causal retention impact of automated advisory scheduling.</p>

    <p>We emphasize that a predicted dropout score represents a probabilistic early warning indicator intended to mobilize compassionate academic support, rather than definitive evidence of a student's intention to disenroll. By grounding automated action in ethical human-in-the-loop oversight and non-stigmatizing communication, the StudentDropout architecture establishes a viable, scalable blueprint for closing the prediction-to-action gap in higher education retention.</p>

    <div class="section-title">ACKNOWLEDGMENT</div>
    <p class="no-indent">The authors express their sincere gratitude to Dr. Kalyani Hemant Deshmukh and the Department of Computer Science and Engineering, Prof. Ram Meghe Institute of Technology and Research (PRMITR), Badnera-Amravati, for their continuous academic guidance, technical encouragement and institutional support throughout this research.</p>

    <div class="section-title">REFERENCES</div>
    <ol class="references-list">
      <li>[1] V. Tinto, <i>Leaving College: Rethinking the Causes and Cures of Student Attrition</i>. Chicago, IL, USA: Univ. Chicago Press, 1993.</li>
      <li>[2] A. Seidman, <i>College Student Retention: Formula for Student Success</i>. Lanham, MD, USA: Rowman & Littlefield, 2012.</li>
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
      <li>[14] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, and A. Galstyan, "A survey on bias and fairness in machine learning," <i>ACM Comput. Surv.</i>, vol. 54, no. 6, pp. 1–35, 2021.</li>
      <li>[15] U.S. Dept. of Education, "Family Educational Rights and Privacy Act (FERPA)," 34 CFR Part 99, 2020.</li>
      <li>[16] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in <i>Adv. Neural Inf. Process. Syst. (NeurIPS)</i>, 2017, pp. 4765–4774.</li>
      <li>[17] J. Kuzilek, M. Hlosta, and Z. Zdrahal, "Open University Learning Analytics Dataset," <i>Sci. Data</i>, vol. 4, p. 170171, 2017.</li>
      <li>[18] P. Cortez and A. M. G. Silva, "Using data mining to predict secondary school student performance," in <i>Proc. 5th FUBUTEC</i>, 2008, pp. 5–12.</li>
      <li>[19] F. Agrusti, G. Bonavolontà, and M. Mezzini, "Analytical student dropout prediction in higher education using machine learning," <i>Int. J. Educ. Technol. High. Educ.</i>, vol. 17, p. 39, 2020.</li>
      <li>[20] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in <i>Proc. 22nd ACM SIGKDD</i>, 2016, pp. 785–794.</li>
      <li>[21] L. I. Kuncheva, <i>Combining Pattern Classifiers: Methods and Algorithms</i>. Hoboken, NJ, USA: Wiley, 2014.</li>
      <li>[22] N. V. Chawla et al., "SMOTE: Synthetic minority over-sampling technique," <i>J. Artif. Intell. Res.</i>, vol. 16, pp. 321–357, 2002.</li>
      <li>[23] H. He and E. A. Garcia, "Learning from imbalanced data," <i>IEEE Trans. Knowl. Data Eng.</i>, vol. 21, no. 9, pp. 1263–1284, 2009.</li>
      <li>[24] T. Saito and M. Rehmsmeier, "The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets," <i>PLoS ONE</i>, vol. 10, no. 3, p. e0118432, 2015.</li>
    </ol>
  </div>
  {get_footer(8)}
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
    padding: 12mm 18mm 10mm 18mm;
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
    height: 13mm;
    margin-bottom: 1.5mm;
  }}

  .header-logo {{
    width: 38px;
    height: 31px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  .header-logo img {{
    width: 38px;
    height: auto;
  }}

  .header-text {{
    flex: 1;
    text-align: center;
    margin-left: 8px;
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
    margin-bottom: 3.5mm;
  }}

  /* Footer */
  .footer-rule {{
    position: absolute;
    bottom: 13mm;
    left: 18mm;
    right: 18mm;
    height: 0.8px;
    background-color: #000;
  }}

  .footer {{
    position: absolute;
    bottom: 7mm;
    left: 18mm;
    right: 18mm;
    height: 5mm;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 8.0pt;
    color: #111;
  }}

  /* Content area */
  .page-content {{
    height: 252mm;
    overflow: hidden;
  }}

  .two-column {{
    column-count: 2;
    column-gap: 18px;
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
    margin-bottom: 6px;
  }}

  h1.paper-title {{
    font-size: 13.5pt;
    font-weight: bold;
    line-height: 1.22;
    margin: 0 0 5px 0;
    color: #000;
  }}

  .author-names {{
    font-size: 9.8pt;
    font-weight: bold;
    margin-bottom: 2px;
    line-height: 1.25;
  }}

  .author-affiliation {{
    font-size: 8.3pt;
    color: #222;
    margin-bottom: 2px;
    line-height: 1.25;
  }}

  .author-email {{
    font-size: 8.0pt;
    color: #333;
    margin-bottom: 4px;
    line-height: 1.25;
  }}

  .divider-rule {{
    text-align: center;
    font-size: 7.2pt;
    letter-spacing: 1px;
    color: #555;
    margin: 3px 0 6px 0;
  }}

  /* Section Headings */
  .section-title {{
    font-size: 9.6pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin: 8px 0 3px 0;
    color: #000;
    break-after: avoid;
  }}

  .subsection-title {{
    font-size: 9.1pt;
    font-weight: bold;
    font-style: italic;
    margin: 6px 0 2px 0;
    color: #000;
    break-after: avoid;
  }}

  p {{
    font-size: 9.2pt;
    line-height: 1.28;
    margin: 0 0 4.5px 0;
    text-indent: 14px;
  }}

  p.no-indent {{
    text-indent: 0;
  }}

  .abstract-box p {{
    font-size: 8.8pt;
    line-height: 1.25;
    text-align: justify;
    margin-bottom: 4px;
  }}

  .abstract-title {{
    font-weight: bold;
    font-style: italic;
  }}

  .keywords-block {{
    font-size: 8.6pt;
    margin-top: 3px;
    margin-bottom: 6px;
    text-indent: 0;
  }}

  .keywords-title {{
    font-weight: bold;
    font-style: italic;
  }}

  /* Equations */
  .equation-box {{
    margin: 4px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 8px;
    font-size: 8.8pt;
  }}

  .math-expr {{
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-style: italic;
  }}

  .eq-number {{
    font-style: normal;
  }}

  /* Tables */
  .table-container {{
    margin: 6px 0;
    width: 100%;
    break-inside: avoid;
  }}

  table.academic-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 7.8pt;
    line-height: 1.18;
    margin-top: 2px;
    margin-bottom: 2px;
  }}

  table.academic-table th {{
    border-top: 1.2px solid #000;
    border-bottom: 0.8px solid #000;
    padding: 3px 4px;
    font-weight: bold;
    text-align: left;
    background-color: #fafafa;
  }}

  table.academic-table td {{
    padding: 2.5px 4px;
    border-bottom: 0.5px solid #e0e0e0;
    vertical-align: top;
  }}

  table.academic-table tr:last-child td {{
    border-bottom: 1.2px solid #000;
  }}

  .table-caption {{
    font-size: 8.0pt;
    font-weight: bold;
    text-align: center;
    margin-bottom: 2px;
  }}

  .caption-label {{
    font-weight: bold;
    text-transform: uppercase;
  }}

  /* Figures */
  .figure-container {{
    margin: 6px 0;
    text-align: center;
    width: 100%;
    break-inside: avoid;
  }}

  .figure-caption {{
    font-size: 8.0pt;
    text-align: justify;
    margin-top: 3px;
    line-height: 1.20;
    padding: 0 2px;
  }}

  .figure-caption .fig-title {{
    font-weight: bold;
  }}

  ul {{
    margin: 2px 0 5px 0;
    padding-left: 14px;
  }}

  li {{
    margin-bottom: 2.5px;
    line-height: 1.25;
    font-size: 8.8pt;
    text-align: justify;
  }}

  .references-list {{
    padding-left: 0;
    list-style-type: none;
    margin-top: 4px;
  }}

  .references-list li {{
    font-size: 7.7pt;
    line-height: 1.20;
    margin-bottom: 4px;
    text-indent: -15px;
    padding-left: 15px;
    text-align: justify;
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
</body>
</html>
"""

def generate():
    print("Writing HTML...")
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(complete_html)
    print("HTML written to:", HTML_PATH)

    print("Compiling to PDF with headless Chrome...")
    chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={FINAL_PDF_PATH}",
        HTML_PATH
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Chrome error:", res.stderr)
        return False
    print("PDF generated successfully at:", FINAL_PDF_PATH)

    doc = pymupdf.open(FINAL_PDF_PATH)
    print(f"Total pages: {len(doc)}, size: {os.path.getsize(FINAL_PDF_PATH)} bytes")
    
    # Render PNGs and verify text / bounds
    for i in range(len(doc)):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        img_path = os.path.join(PAGES_DIR, f"page_{i+1}.png")
        pix.save(img_path)
        blocks = page.get_text("blocks")
        body = [b for b in blocks if b[1] >= 65 and b[3] <= 790]
        top_y = min(b[1] for b in body) if body else 0
        bot_y = max(b[3] for b in body) if body else 0
        print(f"  Page {i+1}: top_y={top_y:.1f}, bot_y={bot_y:.1f}, clearance_to_footer={795 - bot_y:.1f} pt")

    doc.close()
    return True

if __name__ == "__main__":
    generate()
