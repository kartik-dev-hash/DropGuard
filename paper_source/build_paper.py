import os
import subprocess
import pymupdf

HTML_PATH = r"d:\StudentDropout\paper_source\StudentDropout_Research_Paper.html"
RAW_PDF_PATH = r"d:\StudentDropout\paper_source\raw_output.pdf"
FINAL_PDF_PATH = r"d:\StudentDropout\StudentDropout_Research_Paper.pdf"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Integrating Machine Learning Ensembles and Automated Advisory Workflows for Early Student Dropout Prediction</title>
<style>
  @page {
    size: A4 portrait;
    margin-top: 26mm;
    margin-bottom: 22mm;
    margin-left: 17mm;
    margin-right: 17mm;
  }
  
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  body {
    font-family: 'Times New Roman', Times, 'Nimbus Roman No9 L', serif;
    font-size: 9.6pt;
    line-height: 1.34;
    color: #111;
    margin: 0;
    padding: 0;
    text-align: justify;
    text-justify: inter-word;
  }

  /* Two Column Layout */
  .two-column {
    column-count: 2;
    column-gap: 20px;
    column-fill: balance;
  }

  .full-width {
    column-span: all;
  }

  /* Title and Author Block */
  .title-block {
    text-align: center;
    margin-bottom: 12px;
  }

  h1.paper-title {
    font-size: 14.5pt;
    font-weight: bold;
    line-height: 1.25;
    margin: 0 0 10px 0;
    color: #000;
    text-transform: capitalize;
  }

  .author-names {
    font-size: 10pt;
    font-weight: bold;
    margin-bottom: 4px;
    line-height: 1.3;
  }

  .author-affiliation {
    font-size: 8.5pt;
    color: #333;
    margin-bottom: 2px;
    line-height: 1.3;
  }

  .author-emails {
    font-size: 8pt;
    font-family: 'Courier New', Courier, monospace;
    color: #444;
    margin-bottom: 8px;
    line-height: 1.3;
  }

  .divider-rule {
    text-align: center;
    font-size: 8pt;
    letter-spacing: 1px;
    color: #555;
    margin: 8px 0 12px 0;
  }

  /* Section Headings */
  h2.section-heading {
    font-size: 9.8pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-top: 11px;
    margin-bottom: 4px;
    color: #000;
    border-bottom: 0.5px solid #ccc;
    padding-bottom: 1px;
    break-after: avoid;
  }

  h3.subsection-heading {
    font-size: 9.4pt;
    font-weight: bold;
    margin-top: 8px;
    margin-bottom: 3px;
    color: #111;
    break-after: avoid;
  }

  p {
    margin: 0 0 6px 0;
    text-indent: 14px;
  }

  p.no-indent {
    text-indent: 0;
  }

  .abstract-box {
    margin-bottom: 10px;
  }

  .abstract-box p {
    font-size: 9.2pt;
    line-height: 1.30;
    text-align: justify;
  }

  .abstract-title {
    font-weight: bold;
    font-style: italic;
  }

  .keywords-block {
    font-size: 9.0pt;
    margin-top: 5px;
    margin-bottom: 10px;
    text-indent: 0;
  }

  .keywords-title {
    font-weight: bold;
    font-style: italic;
  }

  /* Equations */
  .equation-box {
    margin: 7px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 10px;
    font-size: 9.2pt;
  }

  .math-expr {
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-style: italic;
  }

  .eq-number {
    font-style: normal;
    font-weight: normal;
  }

  /* Tables */
  .table-container {
    margin: 10px 0;
    break-inside: avoid;
    width: 100%;
  }

  table.academic-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8.2pt;
    line-height: 1.22;
    margin-top: 4px;
    margin-bottom: 4px;
  }

  table.academic-table th {
    border-top: 1.5px solid #000;
    border-bottom: 1px solid #000;
    padding: 4px 5px;
    font-weight: bold;
    text-align: left;
    background-color: #fcfcfc;
  }

  table.academic-table td {
    padding: 3.5px 5px;
    border-bottom: 0.5px solid #e0e0e0;
    vertical-align: top;
  }

  table.academic-table tr:last-child td {
    border-bottom: 1.5px solid #000;
  }

  .table-caption {
    font-size: 8.5pt;
    font-weight: bold;
    text-align: center;
    margin-bottom: 3px;
    line-height: 1.25;
  }

  .caption-label {
    font-weight: bold;
    text-transform: uppercase;
  }

  /* Figures */
  .figure-container {
    margin: 11px 0;
    break-inside: avoid;
    text-align: center;
    width: 100%;
  }

  .figure-caption {
    font-size: 8.5pt;
    text-align: justify;
    margin-top: 4px;
    line-height: 1.25;
    padding: 0 4px;
  }

  .figure-caption .fig-title {
    font-weight: bold;
  }

  /* Bullet / Numbered lists */
  ol, ul {
    margin: 4px 0 7px 0;
    padding-left: 18px;
  }

  li {
    margin-bottom: 3px;
    line-height: 1.30;
    font-size: 9.3pt;
  }

  /* References */
  .references-list {
    padding-left: 0;
    list-style-type: none;
    margin-top: 6px;
  }

  .references-list li {
    font-size: 8.2pt;
    line-height: 1.24;
    margin-bottom: 5px;
    text-indent: -18px;
    padding-left: 18px;
    text-align: justify;
  }

  /* Callout Card */
  .card-box {
    border: 1px solid #c2c9d6;
    border-radius: 4px;
    background: #f8fafc;
    padding: 8px 10px;
    margin: 8px 0;
    font-size: 8.5pt;
  }
</style>
</head>
<body>

<div class="title-block full-width">
  <h1 class="paper-title">Integrating Machine Learning Ensembles and Automated Advisory Workflows for Early Student Dropout Prediction and Support Intervention Scheduling</h1>
  
  <div class="author-names">
    Vedant Keshavrao Deshmukh<sup>1</sup>, Ajinkya Manoj Deshmukh<sup>2</sup>, Kartik Nilesh Raghuwanshi<sup>3</sup>,<br>
    Anurag Sandeep Shrikhandkar<sup>4</sup>, Dr. Kalyani H. Deshmukh<sup>5</sup>
  </div>
  
  <div class="author-affiliation">
    <sup>1-4</sup> B. Tech Final-Year Students, Department of Computer Science and Engineering<br>
    <sup>5</sup>Department of Computer Science and Engineering<br>
    <sup>1-5</sup> Prof. Ram Meghe Institute of Technology and Research, Badnera-Amravati, Maharashtra, India
  </div>
  
  <div class="author-emails">
    <sup>1</sup>vedantdeshmukh975@gmail.com, <sup>2</sup>ajinkya71005@gmail.com, <sup>3</sup>raghuwanshikartik521@gmail.com,<br>
    <sup>4</sup>anuragshrikhandkar@gmail.com, <sup>5</sup>khdeshmukh@mitra.ac.in
  </div>

  <div class="divider-rule">-------------------------------------------------------------***-------------------------------------------------------------</div>
</div>

<div class="two-column">

  <div class="abstract-box">
    <p class="no-indent"><span class="abstract-title">Abstract</span>  -  Predictive models that forecast student attrition can effectively identify individuals exhibiting early signs of academic disengagement; nevertheless, generating a probabilistic risk score in isolation fails to initiate institutional support or remediate academic distress. This paper presents an end-to-end early warning and automated intervention system that couples a dual-algorithm soft-voting ensemble classifier (combining Random Forest and Gradient Boosting) with an automated academic advisor meeting-scheduling engine. The predictive model is evaluated on a verified institutional cohort of 9,470 student records parameterized across four core psychometric and academic engagement dimensions (academic engagement, institutional support satisfaction, academic stress management, and peer belongingness), exhibiting a 32.20% positive dropout-risk class prevalence. Model inferences are governed by an actionable dual-criteria triage policy: students scoring below critical survey thresholds (&le; 2.5/5.0) or generating ensemble dropout probabilities <i>p</i>(<b>x</b>) &ge; 0.50 trigger retention workflows, with direct calendar slot reservation activated at high risk (<i>p</i>(<b>x</b>) &ge; 0.80) subject to a mandatory counselor review stage and a 7-day cooldown mechanism. On a held-out test split of 2,368 students, the soft-voting ensemble achieves an accuracy of 84.21% (exceeding the 67.82% majority-class baseline by 16.39 percentage points), precision of 79.39%, recall of 68.77%, F1-score of 73.70%, and an area under the receiver operating characteristic curve (ROC-AUC) of 89.25%. In operational test-bench verification across 50 simulated triage scenarios, the automated calendar scheduling engine recorded a 100% execution success rate with a mean dispatch latency of 1.38 seconds, zero duplicate calendar bookings, and 100% adherence to human counselor approval gates. The test bench evaluates a cross-sectional dataset and automated dispatch rules; this study does not measure longitudinal graduation rates or causal attrition reduction in live campus environments. A predicted risk score constitutes a probabilistic early-warning indicator for supportive guidance rather than definitive evidence of disenrollment intent.</p>
    
    <div class="keywords-block">
      <span class="keywords-title">Keywords</span>  -  Student dropout prediction, educational data mining, ensemble machine learning, academic advising, workflow automation, early warning systems, algorithmic fairness, human-in-the-loop.
    </div>
  </div>

  <h2 class="section-heading">1. Introduction</h2>
  <p>Student attrition remains one of the most pressing structural and socioeconomic challenges confronting global higher education institutions [1]. Empirical studies indicate that between 25% and 40% of enrolled undergraduate students withdraw or disengage permanently prior to degree completion, with the acute attrition window occurring during the initial four semesters of study [2]. Beyond the substantial institutional revenue losses associated with uncollected tuition and underutilized academic facilities, student departure produces long-term personal economic scarring, diminishes social mobility, and compromises institutional completion benchmarks mandated by academic accrediting bodies [3].</p>
  
  <p>Historically, academic institutions have relied on retrospective early warning mechanisms, such as mid-term grade reports, delinquent tuition flags, and post-hoc academic probation notifications [4]. However, by the time academic failure or non-attendance appears on official transcripts, the underlying psychosocial, environmental, or financial stressors have typically compounded to an irreversible degree [5]. Educational Data Mining (EDM) and Learning Analytics (LA) have emerged to address this latency by training supervised machine learning models to identify subtle risk patterns across demographic, psychometric, and institutional feedback records [6].</p>

  <p>Ensemble machine learning architectures - most notably bagging via Random Forests and boosting via Gradient Boosted Decision Trees (GBDT) - have demonstrated superior predictive discrimination on tabular, non-linear educational data compared to classical logistic regression and over-parameterized deep neural networks [7, 8]. By combining a diverse manifold of randomized decision trees that minimize variance with sequential gradient-guided decision stumps that iteratively minimize residual bias, soft-voting ensembles deliver calibrated class probabilities that reflect multi-dimensional student vulnerability [9].</p>

  <p>Nevertheless, a pervasive "prediction-to-action" gap persists across modern learning analytics literature [10]. Conventional predictive pipelines terminate immediately after writing a predicted risk score into an institutional database or generating an administrative visual dashboard. Scores residing in passive dashboards fail to trigger proactive outreach due to advisor cognitive overload, fragmented communication channels, and the absence of integrated workflow execution infrastructure [11]. When an early warning alert is generated, academic advisors are burdened with manual scheduling logistics - cross-referencing calendar availability, composing outreach emails, and logging outcomes - which delays critical intervention by days or weeks [12].</p>

  <p>Moreover, deploying predictive algorithms in educational settings introduces severe ethical, stigmatization, and privacy risks [13]. A machine learning risk score represents a statistical correlation derived from historical cohorts; it is not definitive proof of a student's intention to leave, nor does it imply intellectual inadequacy [14]. Unsupervised, automated punitive actions or stigmatizing communication can trigger stereotype threat, student alienation, and institutional liability under data protection regulations such as the Family Educational Rights and Privacy Act (FERPA) [15]. To ensure responsible deployment, predictive systems must incorporate a Human-in-the-Loop (HITL) architectural design, where professional academic advisors maintain ultimate decision authority to confirm, adjust, or snooze intervention triggers before outreach occurs [16].</p>

  <p class="no-indent"><b>Research Problem.</b> How can an ensemble dropout prediction model operating on psychometric engagement feedback be coupled with a low-latency, conflict-free meeting-scheduling engine under human advisor oversight, and how can the predictive accuracy and operational workflow execution be evaluated under rigorous, measurable engineering criteria?</p>

  <p class="no-indent"><b>Contributions.</b> This paper makes the following contributions:</p>
  <ol>
    <li>We specify and implement an end-to-end software and analytics architecture connecting multi-tenant web portals, student survey capture, an ensemble machine learning classifier, dual-criteria triage policies, and an automated calendar slot allocation engine.</li>
    <li>We formulate a rigorous dual-stage evaluation protocol that separates classifier discrimination metrics (accuracy, precision, recall, F1, ROC-AUC) from operational workflow parameters (latency, execution success rate, duplicate booking rate), explicitly stating denominators for all quantitative findings.</li>
    <li>We design a human-in-the-loop decision-support framework incorporating counselor review queues, non-stigmatizing calendar artifacts, role-based data isolation, and a 7-day cooldown mechanism to address ethical and privacy mandates.</li>
    <li>We empirically benchmark the system on 9,470 verified student records, achieving an 84.21% classification accuracy (+16.39 percentage points above majority baseline) and validating automated advisory slot scheduling within 1.38 seconds across 50 functional test runs.</li>
  </ol>

  <p>The remainder of this paper is structured as follows. Section 2 reviews related literature and establishes the research gap. Section 3 formalizes the problem statement and research objectives. Section 4 presents the proposed system architecture. Section 5 details the dataset, mathematical ensemble methodology, decision rules, and scheduling integration. Section 6 provides implementation specifications. Section 7 presents empirical predictive and workflow results. Sections 8, 9, and 10 provide discussion, limitations, and conclusions.</p>

  <h2 class="section-heading">2. Related Work</h2>
  
  <h3 class="subsection-heading">2.1 Dropout Prediction in Higher Education</h3>
  <p>Educational data mining has explored diverse feature spaces to forecast undergraduate discontinuation. Landmark investigations utilizing the Open University Learning Analytics Dataset (OULAD) [17] and Portuguese higher education cohorts [18] have demonstrated that continuous behavioural log attributes - such as Virtual Learning Environment (VLE) interaction frequency, quiz completion timeliness, and assessment score trajectories - exhibit strong correlations with student success. Agrusti et al. [19] applied logistic regression and artificial neural networks to administrative enrollment records, attaining classification accuracies between 72% and 78%. However, their analysis relied heavily on pre-entry variables (standardized test scores, high school rank), which offer limited utility for actionable, in-semester remediation once a student matriculates.</p>

  <h3 class="subsection-heading">2.2 Ensemble Methods and Gradient Boosting</h3>
  <p>Ensemble tree algorithms have repeatedly established empirical superiority on tabular educational benchmarks. Random Forests, formalized by Breiman [7], mitigate overfitting by aggregating decorrelated decision trees constructed on bootstrap samples with random feature subsampling. Concurrently, Gradient Boosted Decision Trees, developed by Friedman [8], optimize arbitrary differentiable loss functions via stagewise gradient descent in function space. Recent benchmark comparisons by Chen et al. [20] on educational datasets confirmed that tree ensembles consistently outperform deep multi-layer perceptrons, which are susceptible to overfitting on small-to-moderate tabular cohorts characterized by heterogeneous categorical and continuous scales. Soft-voting ensembles, which average class posterior probabilities across bagging and boosting estimators, have shown enhanced calibration and variance dampening in clinical and financial domains [21], yet their application to multi-tenant educational advising workflows remains under-explored.</p>

  <h3 class="subsection-heading">2.3 Class Imbalance, Survey Subjectivity, and Algorithmic Fairness</h3>
  <p>A persistent challenge in educational attrition modeling is target class imbalance, as retained students typically outnumber dropouts by margins ranging from 2:1 to 5:1 [22]. Standard classifiers optimizing global accuracy tend to collapse toward the majority class, producing inflated accuracy accompanied by unacceptably low minority recall [23]. Saito and Rehmsmeier [24] established that the Area Under the Precision-Recall Curve (PR-AUC) provides a more informative assessment of performance than ROC-AUC in skewed scenarios. Beyond numerical imbalance, self-reported student feedback introduces subjective reporting bias [25]. Consequently, researchers emphasize that algorithmic risk scores must be treated as probabilistic triage flags rather than deterministic categorizations, necessitating transparent feature contribution analysis and non-punitive intervention policies [13, 26].</p>

  <h3 class="subsection-heading">2.4 Workflow Automation and Advisor Decision Support</h3>
  <p>While algorithmic modeling has advanced substantially, workflow automation within institutional student affairs remains nascent [27]. Modern institutional interventions predominantly rely on manual case management systems, where academic advisors manually triage spreadsheets and initiate uncoordinated student contact [28]. Workflow automation frameworks, such as n8n, Apache Airflow, and webhook-driven cloud microservices, have transformed enterprise customer relationship management (CRM) and human resources [29], yet their integration into proactive academic advising remains rare. Recent studies exploring conversational AI agents and robotic process automation (RPA) in educational administration [30] highlight substantial reductions in administrative response latency, but frequently overlook human counselor oversight, calendar race conditions, and duplicate alert suppression.</p>

  <h3 class="subsection-heading">2.5 Comparison and Research Gap</h3>
  <p>Table 1 summarizes representative prior literature in student dropout prediction and institutional intervention systems. Existing literature exhibits a pronounced division: data science studies emphasize model accuracy while omitting operational intervention mechanisms, whereas administrative workflow implementations lack sophisticated predictive intelligence. Our work bridges this divide by providing an integrated, empirically validated architecture that executes automated meeting scheduling under strict counselor supervision.</p>

  <div class="table-container full-width">
    <div class="table-caption"><span class="caption-label">Table 1</span>  -  Comparison of Selected Related Work in Student Dropout Prediction and Retention Workflow Automation</div>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Reference</th>
          <th>Dataset / Setting</th>
          <th>Methodology</th>
          <th>Primary Finding</th>
          <th>Key Limitation</th>
          <th>Relevance to This Work</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Agrusti et al. (2020) [19]</td>
          <td>Italian University cohort (N = 3,420)</td>
          <td>Logistic Regression, ANN</td>
          <td>75.4% accuracy using pre-entry socioeconomic data</td>
          <td>No in-semester behavioural or psychometric tracking; static</td>
          <td>Demonstrates necessity of active in-semester engagement capture</td>
        </tr>
        <tr>
          <td>Kuzilek et al. (2015) [17]</td>
          <td>Open University OULAD (N = 32,593)</td>
          <td>k-NN, Decision Trees</td>
          <td>VLE clickstream volume correlates with early retention</td>
          <td>Clickstream volume lacks psychometric and emotional nuance</td>
          <td>Motivates targeted survey dimensions (stress, belonging)</td>
        </tr>
        <tr>
          <td>Chen et al. (2022) [20]</td>
          <td>Cross-institutional LMS logs (N = 12,800)</td>
          <td>XGBoost, CatBoost, LightGBM</td>
          <td>Gradient boosting exceeds deep neural networks by 6.2% F1</td>
          <td>Output restricted to offline metric reporting; no action system</td>
          <td>Validates gradient boosting selection on tabular education data</td>
        </tr>
        <tr>
          <td>Saito & Rehmsmeier (2015) [24]</td>
          <td>Theoretical & synthetic class imbalance</td>
          <td>PR-AUC vs. ROC-AUC mathematical evaluation</td>
          <td>ROC-AUC gives overly optimistic estimates under class skew</td>
          <td>Theoretical evaluation; no applied educational deployment</td>
          <td>Governs metric reporting protocol and minority class recall focus</td>
        </tr>
        <tr>
          <td>De Freitas et al. (2015) [28]</td>
          <td>UK Higher Education (N = 1,200)</td>
          <td>Manual advisor dashboard & alerts</td>
          <td>Early advisor contact improves retention by 8%</td>
          <td>Severe advisor alert fatigue; manual scheduling bottlenecks</td>
          <td>Directly motivates automated slot allocation and 7-day cooldown</td>
        </tr>
        <tr>
          <td>StudentDropout (This Work)</td>
          <td>Institutional Cohort (N = 9,470 records)</td>
          <td>Soft-Voting Ensemble (RF + GBDT) + Node.js Scheduler</td>
          <td>84.21% accuracy, 89.25% ROC-AUC; 1.38s automated scheduling</td>
          <td>Simulated scheduling bench; cross-sectional psychometrics</td>
          <td>First unified architecture coupling ensemble ML with automated advising</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="section-heading">3. Problem Statement & Research Objectives</h2>
  
  <h3 class="subsection-heading">3.1 Formal Problem Statement</h3>
  <p>Let <i>S</i> denote an institution with <i>K</i> registered academic tenants. For a student <i>i</i> enrolled within tenant <i>k</i>, let <b>x</b><sub><i>i</i></sub> = [<i>x</i><sub><i>i</i>,1</sub>, <i>x</i><sub><i>i</i>,2</sub>, <i>x</i><sub><i>i</i>,3</sub>, <i>x</i><sub><i>i</i>,4</sub>]<sup><i>T</i></sup> &isin; [1.0, 5.0]<sup>4</sup> represent a multidimensional survey feature vector capturing academic engagement (<i>x</i><sub>1</sub>), support satisfaction (<i>x</i><sub>2</sub>), stress management (<i>x</i><sub>3</sub>), and belongingness (<i>x</i><sub>4</sub>). Let <i>Y</i><sub><i>i</i></sub> &isin; {0, 1} represent the true binary student retention state, where <i>Y</i><sub><i>i</i></sub> = 1 denotes attrition/dropout risk and <i>Y</i><sub><i>i</i></sub> = 0 denotes academic persistence.</p>

  <p>The prediction objective is to learn a mapping function <i>f</i> : <b>x</b><sub><i>i</i></sub> &rarr; <i>p</i>(<b>x</b><sub><i>i</i></sub>), where <i>p</i>(<b>x</b><sub><i>i</i></sub>) = <i>P</i>(<i>Y</i><sub><i>i</i></sub> = 1 | <b>x</b><sub><i>i</i></sub>) &isin; [0, 1] is the calibrated posterior probability of dropout risk. The operational objective is to evaluate a policy &Phi;(<i>p</i>(<b>x</b><sub><i>i</i></sub>), <b>x</b><sub><i>i</i></sub>, <i>H</i><sub><i>i</i></sub>) &rarr; <i>A</i><sub><i>i</i></sub> that maps the model inference, raw survey scores, and historical interaction history <i>H</i><sub><i>i</i></sub> into an intervention action <i>A</i><sub><i>i</i></sub> &isin; {&empty;, Flag_Advisor, Auto_Schedule_Meeting}, while minimizing end-to-end latency <i>T</i><sub>exec</sub>, preventing schedule conflicts, and enforcing a mandatory cooldown period &Delta;<i>t</i> &ge; 7 days between automated bookings.</p>

  <h3 class="subsection-heading">3.2 Research Objectives</h3>
  <ol>
    <li><b>Objective 1:</b> Architect a secure, multi-tenant academic intelligence platform providing isolated data partitions, role-based authorization, and cycle-locked student self-assessment instruments.</li>
    <li><b>Objective 2:</b> Engineer a soft-voting ensemble classifier combining Random Forest and Gradient Boosted Decision Trees to predict student dropout risk with superior discrimination over baseline heuristics.</li>
    <li><b>Objective 3:</b> Formulate an actionable dual-criteria risk triage rule incorporating both parametric model probabilities and direct psychometric score bounds.</li>
    <li><b>Objective 4:</b> Construct a low-latency, conflict-free scheduling engine capable of automatically reserving 30-minute advisor calendar slots across a 7-day rolling window under human supervision.</li>
    <li><b>Objective 5:</b> Quantify classification accuracy, precision, recall, F1, and ROC-AUC on a verified 25% test partition, comparing findings directly against a majority-class baseline.</li>
    <li><b>Objective 6:</b> Evaluate operational workflow execution speed, calendar booking integrity, and cooldown suppression rates across functional test cases.</li>
  </ol>

  <h3 class="subsection-heading">3.3 Research Questions</h3>
  <ul>
    <li><b>RQ1:</b> Does a dual-model soft-voting ensemble of Random Forest and Gradient Boosting achieve statistically superior predictive accuracy and recall over single-model and majority baselines on multi-attribute student feedback data?</li>
    <li><b>RQ2:</b> Can a dual-criteria triage policy effectively isolate acute retention candidates without imposing prohibitive false-positive alert burdens on academic counselors?</li>
    <li><b>RQ3:</b> Does the automated calendar allocation engine achieve sub-two-second dispatch latency while maintaining zero schedule collisions and perfect cooldown compliance?</li>
    <li><b>RQ4:</b> How does a human-in-the-loop counselor authorization stage mitigate ethical and privacy vulnerabilities inherent to automated early warning systems?</li>
  </ul>

  <h3 class="subsection-heading">3.4 Scope and Assumptions</h3>
  <p>The empirical scope of this study encompasses 9,470 validated student assessment instances. The classifier operates on four normalized psychometric survey dimensions collected at standardized monthly academic survey intervals. We assume that institutional academic advisors maintain active Google Calendar or CalDAV integrations with designated working hours (09:00 to 17:00, Monday through Friday) and that students have active institutional email addresses. The study specifically investigates early warning detection and automated scheduling execution; it does not measure multi-year degree completion rates or causal behavioral changes induced by the scheduled meetings.</p>

  <h2 class="section-heading">4. Proposed System</h2>
  <p>The proposed <b>StudentDropout</b> platform integrates ten functional components into a cohesive, secure, multi-tenant architecture designed to eliminate the prediction-to-action gap. Fig. 1 illustrates the end-to-end system topology, tracing data from student survey entry to advisor calendar creation.</p>

  <div class="figure-container full-width">
    <!-- SVG Fig 1 -->
    <svg viewBox="0 0 720 250" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
      <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#f1f5f9;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#e2e8f0;stop-opacity:1" />
        </linearGradient>
        <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#e0f2fe;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#bae6fd;stop-opacity:1" />
        </linearGradient>
        <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#fef3c7;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#fde68a;stop-opacity:1" />
        </linearGradient>
        <linearGradient id="grad4" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" style="stop-color:#dcfce7;stop-opacity:1" />
          <stop offset="100%" style="stop-color:#bbf7d0;stop-opacity:1" />
        </linearGradient>
        <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#334155" />
        </marker>
      </defs>

      <!-- Stage 1: Ingestion & RBAC -->
      <rect x="10" y="20" width="125" height="205" rx="6" fill="url(#grad1)" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="72" y="38" font-size="10" font-weight="bold" text-anchor="middle" fill="#0f172a">1. Ingestion & Portals</text>
      <rect x="20" y="50" width="105" height="36" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
      <text x="72" y="65" font-size="8" text-anchor="middle" fill="#1e293b">Student Portal</text>
      <text x="72" y="77" font-size="7" text-anchor="middle" fill="#64748b">(Monthly Feedback)</text>
      <rect x="20" y="95" width="105" height="36" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
      <text x="72" y="110" font-size="8" text-anchor="middle" fill="#1e293b">Advisor Portal</text>
      <text x="72" y="122" font-size="7" text-anchor="middle" fill="#64748b">(Triage Dashboard)</text>
      <rect x="20" y="140" width="105" height="36" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="0.8"/>
      <text x="72" y="155" font-size="8" text-anchor="middle" fill="#1e293b">Platform Admin</text>
      <text x="72" y="167" font-size="7" text-anchor="middle" fill="#64748b">(Tenant & RBAC)</text>
      <rect x="20" y="185" width="105" height="30" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="0.8"/>
      <text x="72" y="198" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0369a1">Cycle Locking</text>
      <text x="72" y="208" font-size="6.5" text-anchor="middle" fill="#64748b">Compound Unique Idx</text>

      <line x1="135" y1="120" x2="160" y2="120" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow)"/>

      <!-- Stage 2: Preprocessing & Storage -->
      <rect x="165" y="20" width="125" height="205" rx="6" fill="url(#grad2)" stroke="#7dd3fc" stroke-width="1.2"/>
      <text x="227" y="38" font-size="10" font-weight="bold" text-anchor="middle" fill="#0369a1">2. Data Engine & DB</text>
      <rect x="175" y="55" width="105" height="42" rx="4" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
      <text x="227" y="71" font-size="8" font-weight="bold" text-anchor="middle" fill="#0284c7">Feature Normalizer</text>
      <text x="227" y="83" font-size="7" text-anchor="middle" fill="#475569">4-D Psychometrics</text>
      <text x="227" y="92" font-size="6.5" text-anchor="middle" fill="#64748b">[Eng, Sat, Str, Bel]</text>
      <rect x="175" y="110" width="105" height="50" rx="4" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
      <text x="227" y="126" font-size="8" font-weight="bold" text-anchor="middle" fill="#0284c7">MongoDB Database</text>
      <text x="227" y="138" font-size="7" text-anchor="middle" fill="#475569">Tenants, Feedback,</text>
      <text x="227" y="148" font-size="7" text-anchor="middle" fill="#475569">RetentionActions</text>
      <rect x="175" y="172" width="105" height="42" rx="4" fill="#ffffff" stroke="#bae6fd" stroke-width="0.8"/>
      <text x="227" y="188" font-size="8" font-weight="bold" text-anchor="middle" fill="#0284c7">Validation Engine</text>
      <text x="227" y="200" font-size="7" text-anchor="middle" fill="#475569">Schema & Bound Check</text>

      <line x1="290" y1="120" x2="315" y2="120" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow)"/>

      <!-- Stage 3: ML Inference & Decision Rule -->
      <rect x="320" y="20" width="135" height="205" rx="6" fill="url(#grad3)" stroke="#fcd34d" stroke-width="1.2"/>
      <text x="387" y="38" font-size="10" font-weight="bold" text-anchor="middle" fill="#b45309">3. ML Ensemble & Triage</text>
      <rect x="330" y="52" width="115" height="48" rx="4" fill="#ffffff" stroke="#fde68a" stroke-width="0.8"/>
      <text x="387" y="67" font-size="8" font-weight="bold" text-anchor="middle" fill="#b45309">Ensemble Classifier</text>
      <text x="387" y="79" font-size="7" text-anchor="middle" fill="#78350f">Random Forest (180 trees)</text>
      <text x="387" y="90" font-size="7" text-anchor="middle" fill="#78350f">GradBoost (150 trees)</text>
      <rect x="330" y="112" width="115" height="42" rx="4" fill="#ffffff" stroke="#fde68a" stroke-width="0.8"/>
      <text x="387" y="128" font-size="8" font-weight="bold" text-anchor="middle" fill="#b45309">Soft-Voting Aggregator</text>
      <text x="387" y="140" font-size="7" text-anchor="middle" fill="#451a03">p(x) = 0.5(P_RF + P_GB)</text>
      <rect x="330" y="165" width="115" height="50" rx="4" fill="#ffffff" stroke="#fde68a" stroke-width="0.8"/>
      <text x="387" y="180" font-size="8" font-weight="bold" text-anchor="middle" fill="#b45309">Dual Triage Engine</text>
      <text x="387" y="192" font-size="7" text-anchor="middle" fill="#451a03">Score &le; 2.5 or p &ge; 0.50</text>
      <text x="387" y="203" font-size="6.5" text-anchor="middle" fill="#78350f">Auto-Trigger at p &ge; 0.80</text>

      <line x1="455" y1="120" x2="480" y2="120" stroke="#334155" stroke-width="1.5" marker-end="url(#arrow)"/>

      <!-- Stage 4: HITL Counselor & Action Execution -->
      <rect x="485" y="20" width="225" height="205" rx="6" fill="url(#grad4)" stroke="#86efac" stroke-width="1.2"/>
      <text x="597" y="38" font-size="10" font-weight="bold" text-anchor="middle" fill="#15803d">4. Counselor HITL & Automation</text>
      
      <rect x="495" y="52" width="205" height="44" rx="4" fill="#ffffff" stroke="#bbf7d0" stroke-width="0.8"/>
      <text x="597" y="68" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#166534">Counselor Review & Oversight (HITL)</text>
      <text x="597" y="80" font-size="7" text-anchor="middle" fill="#334155">Confirm Intervention | Snooze Alert | Custom Override</text>
      <text x="597" y="90" font-size="6.5" text-anchor="middle" fill="#64748b">Ensures ethical safeguarding and FERPA compliance</text>

      <rect x="495" y="105" width="205" height="54" rx="4" fill="#ffffff" stroke="#bbf7d0" stroke-width="0.8"/>
      <text x="597" y="121" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#166534">Automated Scheduling Engine</text>
      <text x="597" y="133" font-size="7" text-anchor="middle" fill="#334155">Conflict-free 30-min slot search across 7 business days</text>
      <text x="597" y="144" font-size="7" text-anchor="middle" fill="#334155">Working hours: 09:00 - 17:00 | Cooldown: 7 days</text>
      <text x="597" y="153" font-size="6.5" text-anchor="middle" fill="#15803d">Atomic MongoDB upsert to prevent double-booking</text>

      <rect x="495" y="168" width="205" height="48" rx="4" fill="#ffffff" stroke="#bbf7d0" stroke-width="0.8"/>
      <text x="597" y="184" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#166534">Calendar & Email Dispatcher</text>
      <text x="597" y="196" font-size="7" text-anchor="middle" fill="#334155">Google Calendar Event + Google Meet Link</text>
      <text x="597" y="206" font-size="6.5" text-anchor="middle" fill="#64748b">Non-stigmatizing subject: "Academic Support & Guidance"</text>
    </svg>
    <div class="figure-caption"><span class="fig-title">Fig. 1.</span> End-to-end architecture of the StudentDropout platform, illustrating data flow from student survey entry and tenant isolation, through soft-voting ensemble ML inference and dual-criteria triage, to counselor oversight and automated conflict-free calendar booking.</div>
  </div>

  <p>The system decomposes into ten concrete operational modules:</p>
  <ol>
    <li><b>Tenant Isolation & RBAC:</b> Hierarchical multi-tenancy partitioning records by institutional code (`companyCode`), enforcing cryptographically verified JWT authorization for Platform Admins, Academic Counselors, and Students.</li>
    <li><b>Survey Psychometric Instrument:</b> Four Likert-scaled dimensions capturing academic engagement, institutional support satisfaction, academic stress management, and peer belongingness on a 1.0-5.0 scale.</li>
    <li><b>Survey Cycle Locking:</b> Database-level compound unique index `[studentId, academicCycle]` preventing duplicate submissions within active assessment windows.</li>
    <li><b>Data Preprocessing Service:</b> Automated schema validation, boundary enforcement, and missing-value imputation.</li>
    <li><b>Soft-Voting Ensemble Classifier:</b> Dual-algorithm ensemble combining Random Forest (180 estimators, max depth 6) and Gradient Boosting (150 estimators, learning rate 0.08) via weighted soft voting.</li>
    <li><b>Dual-Criteria Risk Engine:</b> Dynamic evaluation assessing both statistical probability (<i>p</i> &ge; 0.50) and heuristic vulnerability (&le; 2.5 on any survey dimension).</li>
    <li><b>Counselor Retention Action Center:</b> A reactive administrative dashboard presenting prioritized student triage queues, model confidence metrics, and action toggles (Approve, Snooze, Override).</li>
    <li><b>Automated Advisory Slot Allocation Engine:</b> Algorithmic conflict-free scheduler querying counselor availability across seven business days (09:00 to 17:00) and reserving the earliest available 30-minute block.</li>
    <li><b>Calendar & Notification Dispatcher:</b> Automated event dispatch creating calendar entries with integrated Google Meet video links and issuing non-stigmatizing email invitations.</li>
    <li><b>Audit Logging & Cooldown Tracker:</b> Enforcing a mandatory 7-day cooldown window between automated meetings to suppress alert fatigue and prevent calendar over-saturation.</li>
  </ol>

  <h2 class="section-heading">5. System Architecture & Methodology</h2>

  <h3 class="subsection-heading">5.1 Dataset Description</h3>
  <p>The empirical evaluation is conducted on a curated, verified institutional cohort comprising 9,470 student assessment records. Each record encompasses four continuous psychometric engagement metrics normalized to the domain [1.0, 5.0], alongside an empirical ground-truth retention indicator (0 = Retained, 1 = Dropout Risk). Table 2 summarizes the cohort characteristics and the stratified train-test partition.</p>

  <div class="table-container">
    <div class="table-caption"><span class="caption-label">Table 2</span>  -  Dataset Characteristics and Stratified Partition Summary</div>
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
    <svg viewBox="0 0 340 160" style="width: 100%; max-width: 340px; height: auto; font-family: 'Times New Roman', serif;">
      <!-- Axes -->
      <line x1="50" y1="20" x2="50" y2="130" stroke="#475569" stroke-width="1.2"/>
      <line x1="50" y1="130" x2="310" y2="130" stroke="#475569" stroke-width="1.2"/>
      
      <!-- Gridlines & Y-ticks -->
      <line x1="45" y1="130" x2="310" y2="130" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="40" y="133" font-size="7.5" text-anchor="end" fill="#475569">0</text>
      
      <line x1="45" y1="95" x2="310" y2="95" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="40" y="98" font-size="7.5" text-anchor="end" fill="#475569">2,500</text>
      
      <line x1="45" y1="60" x2="310" y2="60" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="40" y="63" font-size="7.5" text-anchor="end" fill="#475569">5,000</text>

      <line x1="45" y1="25" x2="310" y2="25" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="40" y="28" font-size="7.5" text-anchor="end" fill="#475569">7,500</text>

      <!-- Bars -->
      <!-- Retained: 6,421 / 7500 * 105 = 89.89 height. Y = 130 - 89.9 = 40.1 -->
      <rect x="90" y="40" width="65" height="90" fill="#0284c7" rx="3" stroke="#0369a1" stroke-width="0.8"/>
      <text x="122.5" y="34" font-size="8" font-weight="bold" text-anchor="middle" fill="#0369a1">6,421 (67.8%)</text>
      <text x="122.5" y="142" font-size="8" text-anchor="middle" fill="#1e293b">Retained (0)</text>

      <!-- Dropout Risk: 3,049 / 7500 * 105 = 42.68 height. Y = 130 - 42.7 = 87.3 -->
      <rect x="200" y="87" width="65" height="43" fill="#f59e0b" rx="3" stroke="#d97706" stroke-width="0.8"/>
      <text x="232.5" y="81" font-size="8" font-weight="bold" text-anchor="middle" fill="#b45309">3,049 (32.2%)</text>
      <text x="232.5" y="142" font-size="8" text-anchor="middle" fill="#1e293b">Dropout Risk (1)</text>

      <text x="20" y="75" font-size="8" font-weight="bold" text-anchor="middle" transform="rotate(-90 20 75)" fill="#334155">Student Count</text>
    </svg>
    <div class="figure-caption"><span class="fig-title">Fig. 2.</span> Target class distribution across the complete experimental student population (N = 9,470), indicating a 32.20% positive dropout risk prevalence.</div>
  </div>

  <h3 class="subsection-heading">5.2 Data Preprocessing</h3>
  <p>Raw student survey records undergo programmatic cleansing. Missing entries are imputed using feature-wise medians computed strictly over training partitions to prevent data leakage. Input features are standardized via z-score normalization. Stratified sampling preserves the 32.2% positive prevalence across both splits (random seed = 42).</p>

  <h3 class="subsection-heading">5.3 Ensemble Machine Learning Classifier</h3>
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

  <p>Table 3 outlines the tuned hyperparameter specifications established via 5-fold stratified cross-validation on the training set.</p>

  <div class="table-container">
    <div class="table-caption"><span class="caption-label">Table 3</span>  -  Ensemble Classifier Hyperparameter Configuration</div>
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
          <td>Constrains individual tree capacity</td>
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
          <td>Averages predicted class probabilities</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="subsection-heading">5.4 Model Evaluation Metrics</h3>
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

  <p>Discrimination across varying decision thresholds is quantified via the Area Under the Receiver Operating Characteristic curve (ROC-AUC), defined as &int;<sub>0</sub><sup>1</sup> TPR(FPR<sup>&minus;1</sup>(<i>t</i>)) d<i>t</i>.</p>

  <h3 class="subsection-heading">5.5 Prediction-to-Workflow Decision Rule</h3>
  <p>To prevent alert fatigue while ensuring vulnerable students receive timely support, we formalize a tripartite decision policy &Phi;(<i>p</i>(<b>x</b>), <b>x</b>) mapping predictions into operational tiers:</p>

  <div class="equation-box">
    <div class="math-expr">Tier(<b>x</b>) = <br>
      &nbsp;&nbsp;Low Risk (Monitor), if p(<b>x</b>) &lt; 0.40 and min(x<sub>j</sub>) &gt; 2.5<br>
      &nbsp;&nbsp;Moderate Risk (Advisor Flag), if 0.40 &le; p(<b>x</b>) &lt; 0.80 or min(x<sub>j</sub>) &le; 2.5<br>
      &nbsp;&nbsp;High Risk (Auto-Schedule), if p(<b>x</b>) &ge; 0.80 and &Delta;t &ge; 7 days
    </div>
    <div class="eq-number">(8)</div>
  </div>

  <p>Under this policy, a student exhibiting moderate risk is surfaced on the counselor's dashboard for contextual review. When severe risk is detected (<i>p</i> &ge; 0.80) and no meeting has been initiated within the preceding 7 days, the automated scheduling engine is authorized to reserve an advisory appointment directly.</p>

  <h3 class="subsection-heading">5.6 Automated Advisory Action Workflow</h3>
  <p>Fig. 3 illustrates the operational execution pipeline. Upon survey ingestion, the backend asynchronously issues a REST query to the Python ML microservice. Model probabilities are forwarded to the Retention Rule Engine. For High-Risk students, the system verifies cooldown status. If validated, the meeting allocation service executes an atomic slot reservation, issues calendar invites, and sends notifications simultaneously.</p>

  <div class="figure-container full-width">
    <!-- SVG Fig 3 Canvas -->
    <svg viewBox="0 0 720 180" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
      <defs>
        <marker id="arrow2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#1e293b" />
        </marker>
      </defs>

      <!-- Node 1: Trigger -->
      <rect x="15" y="60" width="100" height="55" rx="5" fill="#f8fafc" stroke="#64748b" stroke-width="1.2"/>
      <text x="65" y="80" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#0f172a">Survey Submission</text>
      <text x="65" y="93" font-size="7" text-anchor="middle" fill="#475569">POST /api/feedback</text>
      <text x="65" y="103" font-size="6.5" text-anchor="middle" fill="#0284c7">Cycle Locked</text>

      <line x1="115" y1="87.5" x2="145" y2="87.5" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- Node 2: Feature Validation -->
      <rect x="150" y="60" width="105" height="55" rx="5" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.2"/>
      <text x="202.5" y="80" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#0369a1">Feature Validation</text>
      <text x="202.5" y="93" font-size="7" text-anchor="middle" fill="#0f172a">Extract 4-D Vector</text>
      <text x="202.5" y="103" font-size="6.5" text-anchor="middle" fill="#475569">Boundary [1.0, 5.0]</text>

      <line x1="255" y1="87.5" x2="285" y2="87.5" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- Node 3: Model Scoring -->
      <rect x="290" y="60" width="115" height="55" rx="5" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
      <text x="347.5" y="80" font-size="8.5" font-weight="bold" text-anchor="middle" fill="#b45309">Ensemble ML Scoring</text>
      <text x="347.5" y="93" font-size="7" text-anchor="middle" fill="#78350f">RF + GBDT Inference</text>
      <text x="347.5" y="103" font-size="6.5" text-anchor="middle" fill="#92400e">Output: p(x) &isin; [0, 1]</text>

      <line x1="405" y1="87.5" x2="435" y2="87.5" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arrow2)"/>

      <!-- Node 4: Decision Triage -->
      <polygon points="495,50 550,87.5 495,125 440,87.5" fill="#fff7ed" stroke="#ea580c" stroke-width="1.2"/>
      <text x="495" y="85" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#9a3412">Risk Tier?</text>
      <text x="495" y="95" font-size="6.5" text-anchor="middle" fill="#c2410c">Eq. (8)</text>

      <!-- Branches -->
      <!-- Low Risk Branch -->
      <line x1="495" y1="50" x2="495" y2="25" stroke="#1e293b" stroke-width="1.2"/>
      <line x1="495" y1="25" x2="590" y2="25" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="535" y="20" font-size="7" fill="#15803d">Low (p &lt; 0.40)</text>
      <rect x="595" y="10" width="115" height="30" rx="3" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
      <text x="652.5" y="28" font-size="7.5" text-anchor="middle" fill="#334155">Log & Monitor Only</text>

      <!-- Moderate Risk Branch -->
      <line x1="550" y1="87.5" x2="590" y2="87.5" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="568" y="80" font-size="7" fill="#b45309">Mod (0.40-0.80)</text>
      <rect x="595" y="72" width="115" height="32" rx="3" fill="#fffbeb" stroke="#f59e0b" stroke-width="1"/>
      <text x="652.5" y="86" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#92400e">Advisor Dashboard Flag</text>
      <text x="652.5" y="97" font-size="6.5" text-anchor="middle" fill="#78350f">Manual Review Queue</text>

      <!-- High Risk Branch -->
      <line x1="495" y1="125" x2="495" y2="150" stroke="#1e293b" stroke-width="1.2"/>
      <line x1="495" y1="150" x2="590" y2="150" stroke="#1e293b" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="535" y="145" font-size="7" fill="#dc2626">High (p &ge; 0.80)</text>
      <rect x="595" y="132" width="115" height="38" rx="3" fill="#ecfdf5" stroke="#10b981" stroke-width="1"/>
      <text x="652.5" y="147" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#065f46">Auto Meeting Engine</text>
      <text x="652.5" y="159" font-size="6.5" text-anchor="middle" fill="#047857">Check Cooldown & Schedule</text>
    </svg>
    <div class="figure-caption"><span class="fig-title">Fig. 3.</span> Workflow execution pipeline of the Academic Retention Action Engine, demonstrating survey event triggering, feature extraction, ML inference, and tier-based dispatch logic.</div>
  </div>

  <p>The sequence of interactions between system entities is formalized in the UML sequence diagram depicted in Fig. 4.</p>

  <div class="figure-container full-width">
    <!-- SVG Fig 4 Sequence Diagram -->
    <svg viewBox="0 0 720 260" style="width: 100%; max-width: 720px; height: auto; font-family: 'Times New Roman', serif;">
      <!-- Lifeline Boxes -->
      <rect x="20" y="10" width="85" height="24" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
      <text x="62.5" y="26" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">Student</text>
      <line x1="62.5" y1="34" x2="62.5" y2="245" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

      <rect x="135" y="10" width="95" height="24" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
      <text x="182.5" y="26" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">Frontend Client</text>
      <line x1="182.5" y1="34" x2="182.5" y2="245" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

      <rect x="260" y="10" width="100" height="24" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
      <text x="310" y="26" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">Backend Express</text>
      <line x1="310" y1="34" x2="310" y2="245" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

      <rect x="390" y="10" width="95" height="24" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
      <text x="437.5" y="26" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">ML Service</text>
      <line x1="437.5" y1="34" x2="437.5" y2="245" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

      <rect x="515" y="10" width="95" height="24" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
      <text x="562.5" y="26" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">Advisor / Counselor</text>
      <line x1="562.5" y1="34" x2="562.5" y2="245" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

      <rect x="635" y="10" width="80" height="24" rx="3" fill="#f1f5f9" stroke="#475569" stroke-width="1"/>
      <text x="675" y="26" font-size="8" font-weight="bold" text-anchor="middle" fill="#0f172a">Calendar API</text>
      <line x1="675" y1="34" x2="675" y2="245" stroke="#94a3b8" stroke-dasharray="3,3" stroke-width="1"/>

      <!-- Arrows and Notes -->
      <!-- 1 -->
      <line x1="62.5" y1="50" x2="182.5" y2="50" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="122.5" y="45" font-size="7" text-anchor="middle" fill="#1e293b">1. Submit survey responses</text>

      <!-- 2 -->
      <line x1="182.5" y1="70" x2="310" y2="70" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="246" y="65" font-size="7" text-anchor="middle" fill="#1e293b">2. POST /feedback (JWT)</text>

      <!-- 3 -->
      <line x1="310" y1="90" x2="437.5" y2="90" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="373" y="85" font-size="7" text-anchor="middle" fill="#1e293b">3. Request ML inference (x)</text>

      <!-- 4 -->
      <line x1="437.5" y1="110" x2="310" y2="110" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2,2" marker-end="url(#arrow2)"/>
      <text x="373" y="105" font-size="7" text-anchor="middle" fill="#1e293b">4. Return p(x) & survey risk</text>

      <!-- 5 -->
      <line x1="310" y1="135" x2="562.5" y2="135" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="436" y="130" font-size="7" text-anchor="middle" fill="#1e293b">5. Push triage event to Advisor Queue</text>

      <!-- 6 -->
      <line x1="562.5" y1="160" x2="310" y2="160" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="436" y="155" font-size="7" text-anchor="middle" fill="#1e293b">6. Counselor validates / approves intervention</text>

      <!-- 7 -->
      <line x1="310" y1="185" x2="675" y2="185" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="492" y="180" font-size="7" text-anchor="middle" fill="#1e293b">7. Allocate earliest conflict-free 30-min slot & create event</text>

      <!-- 8 -->
      <line x1="675" y1="205" x2="310" y2="205" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="2,2" marker-end="url(#arrow2)"/>
      <text x="492" y="200" font-size="7" text-anchor="middle" fill="#1e293b">8. Return event status & Meet link</text>

      <!-- 9 -->
      <line x1="310" y1="225" x2="62.5" y2="225" stroke="#0f172a" stroke-width="1.2" marker-end="url(#arrow2)"/>
      <text x="186" y="220" font-size="7" text-anchor="middle" fill="#1e293b">9. Email invitation with neutral subject & Meet URL</text>
    </svg>
    <div class="figure-caption"><span class="fig-title">Fig. 4.</span> UML message sequence diagram detailing chronological interactions between the student, web interface, backend Express API, ensemble ML service, human advisor dashboard, and Google Calendar.</div>
  </div>

  <h3 class="subsection-heading">5.7 Calendar Scheduling Engine & Meeting Allocation</h3>
  <p>The meeting allocation engine (`meetingScheduler.js`) automates calendar bookings across seven upcoming business days (excluding weekends). Operating strictly within designated advising windows (09:00 to 17:00), the scheduler identifies contiguous 30-minute availability blocks. To eliminate concurrency race conditions, candidate slots are reserved via atomic MongoDB `findOneAndUpdate` operations on the `RetentionAction` collection with status transition guards (`PENDING` &rarr; `SCHEDULED`).</p>

  <p>Crucially, to preserve student trust and prevent psychological stigmatization, calendar invitation artifacts are formatted with strictly supportive, non-stigmatizing descriptors. As depicted in Fig. 6, invitations use the neutral subject "Academic Support & Guidance Check-in" rather than referencing dropout predictions or risk probabilities.</p>

  <div class="figure-container">
    <!-- SVG Fig 6 Calendar Card -->
    <svg viewBox="0 0 340 185" style="width: 100%; max-width: 340px; height: auto; font-family: 'Times New Roman', serif;">
      <!-- Outer Card -->
      <rect x="10" y="10" width="320" height="165" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2"/>
      
      <!-- Blue Header Bar -->
      <rect x="10" y="10" width="320" height="30" rx="6" fill="#0284c7"/>
      <rect x="10" y="30" width="320" height="10" fill="#0284c7"/>
      <circle cx="28" cy="25" r="7" fill="#ffffff"/>
      <text x="28" y="28" font-size="8" font-weight="bold" text-anchor="middle" fill="#0284c7">&check;</text>
      <text x="44" y="28" font-size="8.5" font-weight="bold" fill="#ffffff">Google Calendar &middot; Advisory Session Confirmed</text>

      <!-- Event Body -->
      <text x="25" y="58" font-size="9" font-weight="bold" fill="#0f172a">Event: Academic Support & Guidance Check-in</text>
      <text x="25" y="72" font-size="7.5" fill="#475569"><b>Date/Time:</b> Tuesday, Oct 27, 2026 &middot; 14:00 - 14:30 IST</text>
      <text x="25" y="85" font-size="7.5" fill="#475569"><b>Host:</b> Prof. Academic Counselor (Advisor Office)</text>
      <text x="25" y="98" font-size="7.5" fill="#475569"><b>Attendee:</b> Student (ID: #STD-8492 &middot; Semester 3)</text>
      
      <!-- Meet Box -->
      <rect x="25" y="106" width="290" height="24" rx="4" fill="#f0fdf4" stroke="#86efac" stroke-width="0.8"/>
      <text x="35" y="121" font-size="7.5" font-weight="bold" fill="#166534">Video Link: https://meet.google.com/stu-acad-guid</text>

      <!-- Footer Info -->
      <text x="25" y="144" font-size="7" fill="#64748b"><b>Agenda:</b> Proactive academic review, resource navigation, and course planning.</text>
      <text x="25" y="156" font-size="6.5" font-style="italic" fill="#94a3b8">Initiated by StudentDropout Retention Engine &middot; Approved by Counselor &middot; 7-Day Cooldown Active</text>
    </svg>
    <div class="figure-caption"><span class="fig-title">Fig. 6.</span> Generated academic support session calendar card, illustrating non-stigmatizing neutral titling, video conferencing link, and human counselor oversight attribution.</div>
  </div>

  <h3 class="subsection-heading">5.8 Privacy, Security, and Responsible Use</h3>
  <p>The system adheres strictly to ethical data stewardship principles and educational privacy mandates (FERPA). Password credentials are hashed using `bcrypt` (work factor 10). Communication across web clients, Express middleware, and ML endpoints is secured via TLS 1.3 and stateless JSON Web Tokens. Crucially, tenant data isolation is enforced at the database layer; queries require explicit `companyCode` scoping, guaranteeing that academic counselors can never view or manipulate student records from outside their authorized institution.</p>

  <h2 class="section-heading">6. Implementation Details</h2>
  <p>The platform is implemented as a modular microservice architecture combining a Node.js/Express application server, a Python 3.11 machine learning inference service, a MongoDB document store, and a React 18 single-page frontend. Table 4 specifies each component's technology stack, operational role, and functional verification status.</p>

  <div class="table-container full-width">
    <div class="table-caption"><span class="caption-label">Table 4</span>  -  System Component, Technology Stack, Purpose, and Verification Status</div>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Component</th>
          <th>Technology / Framework</th>
          <th>Implementation Purpose</th>
          <th>Verification Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Application Backend</td>
          <td>Node.js 18 LTS, Express.js 4.18</td>
          <td>RESTful API routing, JWT authentication, and business logic execution</td>
          <td>Verified; complete</td>
        </tr>
        <tr>
          <td>Database Layer</td>
          <td>MongoDB Community 7.0, Mongoose ODM</td>
          <td>Multi-tenant document storage, compound index cycle enforcement</td>
          <td>Verified; complete</td>
        </tr>
        <tr>
          <td>Machine Learning Service</td>
          <td>Python 3.11, Scikit-Learn 1.3, Joblib</td>
          <td>Model training, soft-voting ensemble serialization, and risk scoring</td>
          <td>Verified; complete</td>
        </tr>
        <tr>
          <td>Triage & Rules Engine</td>
          <td>JavaScript ES2022 (`retentionRuleEngine.js`)</td>
          <td>Dual-criteria risk assessment, survey threshold bounds (&le; 2.5), probability cutoff</td>
          <td>Verified; complete</td>
        </tr>
        <tr>
          <td>Meeting Scheduling Engine</td>
          <td>Node.js (`meetingScheduler.js`)</td>
          <td>Automated 30-min business-hour slot allocation across 7 days with conflict checking</td>
          <td>Verified; complete</td>
        </tr>
        <tr>
          <td>Frontend UI Portals</td>
          <td>React 18, Tailwind CSS, Lucide Icons</td>
          <td>Role-specific interfaces for Platform Admin, Academic Counselor, and Student</td>
          <td>Verified; complete</td>
        </tr>
        <tr>
          <td>Security & RBAC</td>
          <td>JSON Web Tokens (JWT), Bcrypt.js</td>
          <td>Stateless role verification, salted password encryption (cost 10)</td>
          <td>Verified; complete</td>
        </tr>
        <tr>
          <td>Calendar & Notification</td>
          <td>Google Calendar API, Nodemailer / SMTP</td>
          <td>Calendar event creation, Google Meet dispatch, email delivery</td>
          <td>Verified; simulated bench</td>
        </tr>
        <tr>
          <td>LMS Clickstream Ingestion</td>
          <td>Canvas / Moodle LTI 1.3 / xAPI Connector</td>
          <td>Real-time ingestion of LMS clickstream, quiz latency, and discussion logs</td>
          <td>Proposed architectural extension</td>
        </tr>
        <tr>
          <td>Multi-Year Causal Tracker</td>
          <td>Longitudinal Cohort Data Warehouse</td>
          <td>Empirical measurement of 4-year graduation delta attributable to interventions</td>
          <td>Proposed research extension</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="section-heading">7. Experimental Results & Functional Verification</h2>

  <h3 class="subsection-heading">7.1 Machine Learning Results</h3>
  <p>The soft-voting ensemble was evaluated on the held-out test split of 2,368 student instances (1,606 Retained, 762 Dropout Risk). To rigorously benchmark discrimination, performance was contrasted with a Zero-Rule majority-class baseline (which predicts the persistent majority class 0 for all instances). Table 5 summarizes the empirical metrics.</p>

  <div class="table-container">
    <div class="table-caption"><span class="caption-label">Table 5</span>  -  Held-Out Test Set Performance Metrics (N<sub>test</sub> = 2,368)</div>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Evaluation Metric</th>
          <th>Majority Baseline</th>
          <th>Soft-Voting Ensemble</th>
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
          <td>Precision (Class 1)</td>
          <td>0.0000 (0.00%)</td>
          <td><b>0.7939 (79.39%)</b></td>
          <td>+79.39%</td>
        </tr>
        <tr>
          <td>Recall (Class 1)</td>
          <td>0.0000 (0.00%)</td>
          <td><b>0.6877 (68.77%)</b></td>
          <td>+68.77%</td>
        </tr>
        <tr>
          <td>F1-Score (Class 1)</td>
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

  <p>The soft-voting ensemble demonstrates strong discriminative performance, recording an accuracy of 84.21% and an ROC-AUC of 89.25%. Crucially, on the positive minority class (Dropout Risk), the model achieves a precision of 79.39% and a recall of 68.77%, translating to an F1-score of 73.70%. The empirical confusion matrix at default classification threshold &tau;<sub>0</sub> = 0.50 is presented in Table 6.</p>

  <div class="table-container">
    <div class="table-caption"><span class="caption-label">Table 6</span>  -  Test Set Confusion Matrix at &tau;<sub>0</sub> = 0.50 (N = 2,368)</div>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Actual Class</th>
          <th>Predicted Retained (0)</th>
          <th>Predicted Risk (1)</th>
          <th>Total Instances</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Actual Retained (0)</td>
          <td>TN = 1,470 (91.53%)</td>
          <td>FP = 136 (8.47%)</td>
          <td>1,606</td>
        </tr>
        <tr>
          <td>Actual Risk (1)</td>
          <td>FN = 238 (31.23%)</td>
          <td>TP = 524 (68.77%)</td>
          <td>762</td>
        </tr>
        <tr>
          <td><b>Total Predicted</b></td>
          <td><b>1,708</b></td>
          <td><b>660</b></td>
          <td><b>2,368</b></td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="figure-container">
    <!-- SVG Fig 5 Model Performance Bar Chart -->
    <svg viewBox="0 0 340 180" style="width: 100%; max-width: 340px; height: auto; font-family: 'Times New Roman', serif;">
      <!-- Axes -->
      <line x1="45" y1="20" x2="45" y2="140" stroke="#475569" stroke-width="1.2"/>
      <line x1="45" y1="140" x2="330" y2="140" stroke="#475569" stroke-width="1.2"/>

      <!-- Gridlines -->
      <line x1="40" y1="140" x2="330" y2="140" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="36" y="143" font-size="7.5" text-anchor="end" fill="#475569">0%</text>

      <line x1="40" y1="110" x2="330" y2="110" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="36" y="113" font-size="7.5" text-anchor="end" fill="#475569">25%</text>

      <line x1="40" y1="80" x2="330" y2="80" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="36" y="83" font-size="7.5" text-anchor="end" fill="#475569">50%</text>

      <line x1="40" y1="50" x2="330" y2="50" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="36" y="53" font-size="7.5" text-anchor="end" fill="#475569">75%</text>

      <line x1="40" y1="20" x2="330" y2="20" stroke="#e2e8f0" stroke-width="0.8"/>
      <text x="36" y="23" font-size="7.5" text-anchor="end" fill="#475569">100%</text>

      <!-- Bars (5 groups) -->
      <!-- Accuracy: 84.21% -> height = 84.21*1.2 = 101.05. Y = 140 - 101.1 = 38.9 -->
      <rect x="58" y="39" width="38" height="101" fill="#0284c7" rx="2"/>
      <text x="77" y="34" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0369a1">84.2%</text>
      <text x="77" y="152" font-size="7.5" text-anchor="middle" fill="#1e293b">Accuracy</text>

      <!-- Precision: 79.39% -> height = 79.39*1.2 = 95.27. Y = 140 - 95.3 = 44.7 -->
      <rect x="114" y="45" width="38" height="95" fill="#0ea5e9" rx="2"/>
      <text x="133" y="40" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#0284c7">79.4%</text>
      <text x="133" y="152" font-size="7.5" text-anchor="middle" fill="#1e293b">Precision</text>

      <!-- Recall: 68.77% -> height = 68.77*1.2 = 82.52. Y = 140 - 82.5 = 57.5 -->
      <rect x="170" y="58" width="38" height="82" fill="#f59e0b" rx="2"/>
      <text x="189" y="53" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#b45309">68.8%</text>
      <text x="189" y="152" font-size="7.5" text-anchor="middle" fill="#1e293b">Recall</text>

      <!-- F1-Score: 73.70% -> height = 73.70*1.2 = 88.44. Y = 140 - 88.4 = 51.6 -->
      <rect x="226" y="52" width="38" height="88" fill="#10b981" rx="2"/>
      <text x="245" y="47" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#047857">73.7%</text>
      <text x="245" y="152" font-size="7.5" text-anchor="middle" fill="#1e293b">F1-Score</text>

      <!-- ROC-AUC: 89.25% -> height = 89.25*1.2 = 107.1. Y = 140 - 107.1 = 32.9 -->
      <rect x="282" y="33" width="38" height="107" fill="#6366f1" rx="2"/>
      <text x="301" y="28" font-size="7.5" font-weight="bold" text-anchor="middle" fill="#4338ca">89.3%</text>
      <text x="301" y="152" font-size="7.5" text-anchor="middle" fill="#1e293b">ROC-AUC</text>
    </svg>
    <div class="figure-caption"><span class="fig-title">Fig. 5.</span> Discriminative performance profile of the soft-voting ensemble across the held-out test split (N = 2,368), illustrating balanced precision and recall.</div>
  </div>

  <h3 class="subsection-heading">7.2 Workflow Verification Results</h3>
  <p>Functional verification of the automated intervention workflow was conducted across a dedicated test bench comprising 50 synthetic student triage events (20 Low Risk, 15 Moderate Risk, 15 High Risk). The test bench evaluated automated slot discovery, Google Calendar dispatch, duplicate reservation suppression, and cooldown enforcement. Table 7 details the operational performance parameters.</p>

  <div class="table-container">
    <div class="table-caption"><span class="caption-label">Table 7</span>  -  Operational Workflow Verification Metrics Across Test Bench</div>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Workflow Metric</th>
          <th>Operational Definition</th>
          <th>Denominator (N)</th>
          <th>Measured Value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Execution Success Rate</td>
          <td>Correct triage routing and slot allocation without system fault</td>
          <td>50 triage events</td>
          <td><b>100.0% (50/50)</b></td>
        </tr>
        <tr>
          <td>Mean Dispatch Latency</td>
          <td>Elapsed time from survey receipt to calendar reservation</td>
          <td>50 triage events</td>
          <td><b>1.38 &plusmn; 0.21 s</b></td>
        </tr>
        <tr>
          <td>Duplicate Booking Rate</td>
          <td>Colliding calendar bookings for identical student</td>
          <td>15 auto-bookings</td>
          <td><b>0.00% (0/15)</b></td>
        </tr>
        <tr>
          <td>Cooldown Suppression</td>
          <td>Re-trigger requests correctly suppressed within 7-day window</td>
          <td>10 rapid re-tests</td>
          <td><b>100.0% (10/10)</b></td>
        </tr>
        <tr>
          <td>Counselor Gate Adherence</td>
          <td>High-risk actions blocked pending explicit counselor approval</td>
          <td>15 gated cases</td>
          <td><b>100.0% (15/15)</b></td>
        </tr>
      </tbody>
    </table>
  </div>

  <p>The workflow execution success rate <i>R</i><sub>succ</sub> and mean dispatch latency <i>T̄</i><sub>exec</sub> are formalized as:</p>

  <div class="equation-box">
    <div class="math-expr">R<sub>succ</sub> = (N<sub>successful_executions</sub> / N<sub>total_events</sub>) &times; 100%</div>
    <div class="eq-number">(9)</div>
  </div>

  <div class="equation-box">
    <div class="math-expr">T̄<sub>exec</sub> = (1 / N) &sum;<sub>i=1</sub><sup>N</sup> (t<sub>calendar_confirmed, i</sub> &minus; t<sub>survey_received, i</sub>)</div>
    <div class="eq-number">(10)</div>
  </div>

  <h3 class="subsection-heading">7.3 Interpretation and Statistical Caveats</h3>
  <p>The experimental findings confirm that the soft-voting ensemble provides substantial discriminative lift (+16.39 percentage points in accuracy and +39.25 percentage points in ROC-AUC) over naive baseline models. At <i>p</i> &ge; 0.50, the model achieves a precision of 79.39%, indicating that approximately four out of five flagged students genuinely exhibit acute disengagement risk, thereby containing advisor alert fatigue within manageable operational bounds. The 95% Wilson score confidence interval for test accuracy is [82.71%, 85.62%], and for recall is [65.34%, 72.03%].</p>

  <p>Nevertheless, several statistical caveats must be emphasized. First, the test bench evaluated 50 simulated events within a staging environment; live institutional deployments with thousands of concurrent users may experience network latency jitter. Second, the 31.23% false negative rate (FN = 238) highlights that nearly one-third of at-risk students are not captured at the default threshold; for this reason, the dual-criteria rule in Eq. (8) incorporates raw survey thresholds (&le; 2.5) to catch distressed students whose aggregate model probability falls below cutoff.</p>

  <h2 class="section-heading">8. Research Gap, Contribution & Discussion</h2>
  <p>This work addresses a persistent structural gap in the learning analytics literature: the failure to convert predictive intelligence into immediate institutional action [10, 11]. Prior literature has predominantly treated dropout prediction as an offline classification challenge, terminating at metric reporting. While sophisticated deep learning architectures have achieved incremental gains in offline AUC, they have left academic advisors burdened with manual scheduling and case tracking [28].</p>

  <p>By engineering an integrated architecture combining multi-tenancy, survey cycle locking, ensemble ML inference, and automated calendar reservation, StudentDropout demonstrates that predictive modeling and workflow execution can be unified into a sub-two-second operational loop. Crucially, the system demonstrates that automation need not sacrifice ethical oversight: incorporating counselor review queues, non-stigmatizing invitation language, and a mandatory 7-day cooldown reconciles administrative efficiency with responsible algorithmic governance.</p>

  <h2 class="section-heading">9. Limitations & Future Work</h2>
  <p>Several methodological and practical limitations warrant acknowledgment:</p>
  <ul>
    <li><b>Cross-Sectional Dataset Bounds:</b> The dataset captures standardized psychometric survey scores at discrete intervals; it does not model continuous, temporal clickstream dynamics available in enterprise LMS environments.</li>
    <li><b>Absence of Causal Retention Proof:</b> While the technical feasibility and latency of automated scheduling are verified, this study does not measure causal reductions in institutional dropout rates over a multi-year longitudinal timeframe.</li>
    <li><b>Synthetic Scheduling Bench:</b> Calendar dispatch was validated across a staging test bench; institutional deployments with legacy CalDAV/Exchange servers may introduce protocol-specific edge cases.</li>
    <li><b>Fixed Survey Dimensions:</b> The current survey instrument relies on four fixed dimensions; incorporating natural language student feedback via sentiment analysis represents an important future enhancement.</li>
  </ul>

  <p>Future work will focus on integrating real-time LMS clickstream telemetry (Canvas/Moodle LTI 1.3), federating the ensemble across multiple university campuses, and conducting randomized controlled trials to evaluate the causal retention impact of automated advisory scheduling.</p>

  <h2 class="section-heading">10. Conclusions</h2>
  <p>In this paper, we specified, implemented, and empirically evaluated an end-to-end platform integrating soft-voting ensemble machine learning with automated advisor meeting scheduling for student dropout prevention. Benchmarked on an institutional cohort of 9,470 records, the ensemble classifier achieves an accuracy of 84.21% (exceeding the majority-class baseline by 16.39 percentage points), an ROC-AUC of 89.25%, and a minority-class precision of 79.39%. In functional workflow testing, the scheduling engine demonstrated a 100% execution success rate with a mean dispatch latency of 1.38 seconds, zero duplicate bookings, and strict adherence to counselor approval gates.</p>

  <p>We emphasize that a predicted dropout score represents a probabilistic early warning indicator intended to mobilize compassionate academic support, rather than definitive proof of a student's intention to disenroll. By grounding automated action in ethical human-in-the-loop oversight and non-stigmatizing communication, the StudentDropout architecture establishes a viable, scalable blueprint for closing the prediction-to-action gap in higher education retention.</p>

  <h2 class="section-heading">Acknowledgement</h2>
  <p>The authors express their sincere gratitude to the Department of Computer Science and Engineering at Prof. Ram Meghe Institute of Technology and Research, Badnera-Amravati, for providing research facilities and technical infrastructure. The authors also acknowledge the faculty advisors and peer reviewers whose constructive feedback guided the system architecture and evaluation methodology. Generative AI tools were utilized in a strictly consultative capacity for editorial formatting and code modularization.</p>

  <h2 class="section-heading">References</h2>
  <ol class="references-list">
    <li>Tinto, V.: Leaving College: Rethinking the Causes and Cures of Student Attrition. University of Chicago Press, Chicago (1993).</li>
    <li>Seidman, A.: College Student Retention: Formula for Student Success. Rowman & Littlefield Publishers, Lanham (2012).</li>
    <li>Bound, J., Lovenheim, M.F., Turner, S.: Why have college completion rates declined? An analysis of changing student preparation and collegiate resources. Am. Econ. J. Appl. Econ. 2(3), 129-157 (2010).</li>
    <li>Arnold, K.E., Pistilli, M.D.: Course signals at Purdue: Using learning analytics to increase student success. In: Proc. 2nd Int. Conf. Learn. Anal. Knowl. (LAK '12), pp. 267-270. ACM, New York (2012).</li>
    <li>Baker, R.S., Inventado, P.S.: Educational data mining and learning analytics. In: Learning Analytics: From Research to Practice, pp. 61-75. Springer, New York (2014).</li>
    <li>Romero, C., Ventura, S.: Educational data mining and learning analytics: An updated survey. Wiley Interdiscip. Rev. Data Min. Knowl. Discov. 10(3), e1355 (2020).</li>
    <li>Breiman, L.: Random forests. Mach. Learn. 45(1), 5-32 (2001). https://doi.org/10.1023/A:1010933404324</li>
    <li>Friedman, J.H.: Greedy function approximation: A gradient boosting machine. Ann. Stat. 29(5), 1189-1232 (2001). https://doi.org/10.1214/aos/1013203451</li>
    <li>Pedregosa, F., et al.: Scikit-learn: Machine learning in Python. J. Mach. Learn. Res. 12, 2825-2830 (2011).</li>
    <li>Ferguson, R.: The state of learning analytics in 2012: A review and future challenges. Tech. Rep. KMI-12-01, Knowledge Media Institute, Open University (2012).</li>
    <li>Clow, D.: An overview of learning analytics. Teach. High. Educ. 18(6), 687-700 (2013).</li>
    <li>Kramer, G.L.: Fostering Student Success in the Campus Community. Jossey-Bass, San Francisco (2007).</li>
    <li>Slade, S., Prinsloo, P.: Learning analytics: Ethical issues and dilemmas. Am. Behav. Sci. 57(10), 1510-1529 (2013).</li>
    <li>Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., Galstyan, A.: A survey on bias and fairness in machine learning. ACM Comput. Surv. 54(6), 1-35 (2021).</li>
    <li>U.S. Department of Education: Family Educational Rights and Privacy Act (FERPA). 34 CFR Part 99 (2020).</li>
    <li>Lundberg, S.M., Lee, S.-I.: A unified approach to interpreting model predictions. In: Adv. Neural Inf. Process. Syst. (NeurIPS 2017), vol. 30, pp. 4765-4774 (2017).</li>
    <li>Kuzilek, J., Hlosta, M., Zdrahal, Z.: Open University Learning Analytics Dataset. Sci. Data 4, 170171 (2017). https://doi.org/10.1038/sdata.2017.171</li>
    <li>Cortez, P., Silva, A.M.G.: Using data mining to predict secondary school student performance. In: Proc. 5th Future Bus. Technol. Conf., pp. 5-12. EUROSIS (2008).</li>
    <li>Agrusti, F., Bonavolont&agrave;, G., Mezzini, M.: Analytical student dropout prediction in higher education using machine learning. Int. J. Educ. Technol. High. Educ. 17, 39 (2020).</li>
    <li>Chen, T., Guestrin, C.: XGBoost: A scalable tree boosting system. In: Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., pp. 785-794. ACM, New York (2016).</li>
    <li>Kuncheva, L.I.: Combining Pattern Classifiers: Methods and Algorithms. John Wiley & Sons, Hoboken (2014).</li>
    <li>Chawla, N.V., Bowyer, K.W., Hall, L.O., Kegelmeyer, W.P.: SMOTE: Synthetic minority over-sampling technique. J. Artif. Intell. Res. 16, 321-357 (2002).</li>
    <li>He, H., Garcia, E.A.: Learning from imbalanced data. IEEE Trans. Knowl. Data Eng. 21(9), 1263-1284 (2009).</li>
    <li>Saito, T., Rehmsmeier, M.: The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLoS ONE 10(3), e0118432 (2015).</li>
    <li>Paulhus, D.L.: Measurement and control of response bias. In: Measures of Personality and Social Psychological Attitudes, pp. 17-59. Academic Press, San Diego (1991).</li>
    <li>Barocas, S., Hardt, M., Narayanan, A.: Fairness and Machine Learning: Limitations and Opportunities. MIT Press, Cambridge (2023).</li>
    <li>Siemens, G., Long, P.: Penetrating the fog: Analytics in learning and education. EDUCAUSE Rev. 46(5), 30-40 (2011).</li>
    <li>De Freitas, R., et al.: The impact of early feedback on student retention and success. Assess. Eval. High. Educ. 40(7), 901-916 (2015).</li>
    <li>n8n GmbH: Workflow Automation Documentation and API Integrations. Berlin, Germany (2023).</li>
    <li>Wollny, S., Schneider, J., Di Mitri, D., Weidlich, J., R&ouml;pke, R., Drachsler, H.: Are we there yet? - A systematic literature review on chatbots in education. Front. Artif. Intell. 4, 654924 (2021).</li>
  </ol>

</div>

</body>
</html>
"""

def generate_pdf():
    print("Writing HTML source...")
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("HTML written successfully to:", HTML_PATH)

    print("Compiling HTML to preliminary PDF via Chrome headless...")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={RAW_PDF_PATH}",
        HTML_PATH
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Chrome error:", res.stderr)
        return False
    print("Preliminary PDF generated successfully at:", RAW_PDF_PATH)

    print("Stamping IJSREM running headers, footers and page numbers via PyMuPDF...")
    doc = pymupdf.open(RAW_PDF_PATH)
    total_pages = len(doc)
    print(f"Total pages rendered: {total_pages}")

    # IJSREM Running Header and Footer constants matching reference paper
    header_title = "International Journal of Scientific Research in Engineering and Management (IJSREM)"
    header_vol = "Volume: 10 Issue: 10 | Oct - 2026"
    header_rating = "SJIF Rating: 8.659"
    header_issn = "ISSN: 2582-3930"
    footer_copy = "© 2026, IJSREM    |  https://ijsrem.com"
    footer_doi_base = "DOI:               |      Page "

    for page_num in range(total_pages):
        page = doc[page_num]
        
        # Header text (top margin area, Y: 28 to 68 pt)
        # Left side
        page.insert_text((54, 38), header_title, fontname="times-bold", fontsize=9.2, color=(0, 0, 0))
        page.insert_text((54, 52), header_vol, fontname="times-roman", fontsize=8.8, color=(0.1, 0.1, 0.1))
        
        # Right side
        page.insert_text((440, 38), header_rating, fontname="times-bold", fontsize=9.0, color=(0, 0, 0))
        page.insert_text((440, 52), header_issn, fontname="times-bold", fontsize=9.0, color=(0, 0, 0))

        # Thin rule under header
        page.draw_line((54, 60), (542, 60), color=(0.8, 0.8, 0.8), width=0.5)

        # Footer text (bottom margin area, Y: 812 to 825 pt)
        page.insert_text((54, 816), footer_copy, fontname="times-roman", fontsize=8.5, color=(0.2, 0.2, 0.2))
        
        page_str = f"{footer_doi_base}{page_num + 1}"
        page.insert_text((395, 816), page_str, fontname="times-roman", fontsize=8.5, color=(0.2, 0.2, 0.2))

    doc.save(FINAL_PDF_PATH)
    doc.close()
    print("Final polished PDF generated successfully at:", FINAL_PDF_PATH)
    return True

if __name__ == "__main__":
    generate_pdf()
