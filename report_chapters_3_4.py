"""
Chapters 3 & 4 for StudentDropout B.Tech Honors Project Report.
Exhaustive technical analysis, system architecture, requirements, database schemas,
Algorithms 1-4 with full pseudocode, and API specifications.
"""

CHAPTER_3_TITLE = "CHAPTER 3: SYSTEM ARCHITECTURE & REQUIREMENTS ANALYSIS"

CHAPTER_3_SECTIONS = [
    ("3.1 Existing System Analysis & Structural Deficiencies", [
        """Higher education institutions currently employ a mosaic of legacy software applications, departmental spreadsheets, and paper records to monitor student progress. An exhaustive architectural audit of existing university retention workflows reveals four fundamental structural deficiencies:""",
        """1. Temporal Latency and Retrospective Tracking: Existing student information systems (SIS) track academic performance through end-of-semester grade submissions, examination results, and mid-term detention lists. This introduces a structural lag of 8 to 16 weeks between the onset of academic disengagement and official administrative notification. By the time an advisor receives a detention list, the student has often accumulated irreversible deficits.""",
        """2. Disconnected Data Silos: Academic grades reside within registrar databases; attendance is logged in departmental registers; mentorship logs are maintained in faculty notebooks; and mental health visits remain locked in separate clinical files. Counselors lack a unified, holistic glass-pane view that correlates academic struggle with emotional stress and institutional dissatisfaction.""",
        """3. Reactive Interventions: University advisory cells operate primarily as reactive bodies: counselors intervene only after an academic dismissal notice is generated or a student formally requests a withdrawal certificate. Proactive, preventative intervention is virtually non-existent.""",
        """4. Administrative Friction & Alert Fatigue: When early-warning software is deployed, it frequently outputs unranked bulk CSV spreadsheets containing hundreds of flagged students. Advisors face cognitive overload and lack the administrative support to coordinate calendar availability, discover open slots, and draft personalized outreach emails."""
    ]),
    ("3.2 Proposed System Framework", [
        """The proposed STUDENTDROPOUT (DropGuard) platform fundamentally re-engineers institutional retention by delivering an intelligent, proactive, multi-tenant digital ecosystem. The core architectural innovations of the proposed framework include:""",
        """- Multi-Tenant Institutional Isolation: Partitioning university departments and affiliated institutions into logically isolated tenant domains via encrypted institutionCode scoping, ensuring strict FERPA compliance.""",
        """- Continuous Wellbeing Pulse Ingestion: Capturing monthly Likert-scaled student feedback across four key academic and psychosocial dimensions, enforcing database cycle-locking to prevent duplicate responses.""",
        """- Calibrated Ensemble Machine Learning: Integrating Random Forest and Gradient Boosted Decision Trees via an unweighted soft-voting rule to compute reliable, calibrated dropout risk probability vectors p(x).""",
        """- Dual-Criteria Triage Engine: Evaluating both composite risk probabilities and single-dimension acute distress thresholds (min(xj) <= 2.5) to prevent compensatory masking of emotional burnout.""",
        """- Automated Calendar Scheduling Engine: Autonomously discovering conflict-free 30-minute counseling slots across seven business days and reserving Google Calendar and Google Meet sessions in sub-two-second latency.""",
        """- Human-in-the-Loop Governance: Safeguarding student dignity through counselor approval gates, neutral non-stigmatizing meeting titling, and automated 7-day cooldown locks against alert fatigue."""
    ]),
    ("3.3 Functional Requirements", [
        """The functional capabilities of the StudentDropout platform are formally specified across eight core functional modules:""",
        """- FR-1: User Authentication & Role-Based Access Control: The system shall provide secure authentication via email and bcryptjs-salted passwords, issuing stateless HMAC-SHA256 JWT tokens. The system shall enforce role-based access for Students, Counselors, and Platform Admins.""",
        """- FR-2: Tenant Institutional Registration: Platform Admins shall review and approve incoming institutional tenant registrations, establishing unique workspace codes (companyCode).""",
        """- FR-3: Wellbeing Pulse Survey Ingestion: Students shall submit monthly ratings across four dimensions (1.0 to 5.0) and qualitative feedback. The system shall enforce compound unique indexing {studentId, feedbackPeriod} to prevent multiple submissions in a single monthly cycle.""",
        """- FR-4: Real-Time Machine Learning Inference: Upon survey ingestion, the backend shall invoke the Python ensemble microservice to calculate calibrated risk probabilities p(x) in sub-200ms latency.""",
        """- FR-5: Retention Triage & Action Queue: The Counselor Dashboard shall automatically sort students into Low Risk (On Track), Moderate Risk (Advisor Flagged), and High Risk (Action Required) queues.""",
        """- FR-6: Automated Conflict-Free Calendar Scheduling: For High Risk cases, the system shall discover open 30-minute counselor slots over the subsequent seven business days and reserve appointments via Google Calendar API.""",
        """- FR-7: Notification & Calendar Invite Dispatch: The platform shall dispatch neutral, non-stigmatizing meeting invitations ('Academic Support & Guidance Check-in') containing Google Meet URLs to student and counselor emails.""",
        """- FR-8: Cooldown Enforcement & Status Auditing: The system shall enforce a mandatory 7-day cooldown lockout per student, logging subsequent survey scores while suppressing duplicate calendar bookings."""
    ]),
    ("3.4 Non-Functional Requirements", [
        """To ensure production-grade institutional reliability, the platform complies with the following non-functional requirements:""",
        """- NFR-1: Performance & Response Latency: The backend REST API shall maintain mean response times <= 100 ms for transactional queries, and the end-to-end calendar allocation pipeline shall complete within <= 2.0 seconds.""",
        """- NFR-2: Scalability & High Throughput: The decoupled architecture shall support horizontal scaling across tenant institutions, accommodating >= 10,000 active student accounts and >= 500 concurrent survey submissions.""",
        """- NFR-3: Security & Cryptographic Safeguards: Passwords must be salted and hashed using bcrypt with cost factor 10. JWT tokens must expire after 60 minutes. All HTTP traffic must be encrypted via TLS 1.3.""",
        """- NFR-4: Availability & Fault Tolerance: The platform shall maintain 99.9% uptime during academic operating hours, utilizing health-check probes and automated MongoDB connection pool recovery.""",
        """- NFR-5: Usability & Responsive Design: The React single-page application must conform to WCAG 2.1 AA accessibility guidelines and render responsively across mobile, tablet, and desktop viewports.""",
        """- NFR-6: Privacy & Regulatory Compliance: The data persistence layer must strictly comply with FERPA and India's Digital Personal Data Protection (DPDP) Act 2023, ensuring cross-tenant data isolation."""
    ]),
    ("3.5 Feasibility Study", [
        """A comprehensive feasibility assessment confirms the viability of the StudentDropout platform across three standard dimensions:""",
        """1. Technical Feasibility: The implementation utilizes industry-standard, battle-tested open-source technologies (Node.js, Express, MongoDB, React, Tailwind CSS, Python, scikit-learn). The computational complexity of the soft-voting ensemble is O(B * d * N_trees) for inference, which executes in ~145 ms on modest commodity hardware. Machine learning serialization via Joblib ensures sub-second model loading.""",
        """2. Operational Feasibility: The user interface is specifically engineered to eliminate counselor alert fatigue by prioritizing cases into three discrete operational tiers. Faculty advisors require minimal technical training, as the system automates calendar coordination and meeting link creation.""",
        """3. Economic Feasibility: The software stack is built entirely on open-source frameworks without commercial licensing fees. Hosting requirements are modest, requiring standard cloud virtual machines (2 vCPU, 4GB RAM) or existing on-premise university server infrastructure, making institutional adoption highly cost-effective."""
    ]),
    ("3.6 Hardware and Software Specifications", [
        """Tables 3.1 and 3.2 detail the physical and logical operating specifications for both development and institutional production environments."""
    ]),
    ("3.7 End-to-End System Architecture", [
        """Figure 3.1 illustrates the decoupled four-tier architecture of the StudentDropout platform. The system is partitioned into strictly bounded layers:""",
        """1. Presentation Tier (Client SPA): Built with React 19.2, Tailwind CSS 4.3, and Vite 7.2. It delivers responsive, role-delineated portals: Student Wellbeing Portal (self-service feedback submission and appointment confirmation), Counselor Retention Dashboard (triage queues, risk gauges, and session scheduler), and Platform Admin Portal (institutional tenant management).""",
        """2. Application & API Tier: Implemented in Node.js 20+ and Express.js 4.19 utilizing native ES Modules. It encapsulates JWT authentication guards, role-based authorization middleware (requireRole), the dual-criteria triage policy engine, the calendar reservation orchestrator (meetingScheduler.js), and automated email dispatchers.""",
        """3. Persistence Tier: Powered by MongoDB 8.x Community Server managed through Mongoose ODM 8.14. It enforces multi-tenant indexing, schema validation, and compound unique constraints ensuring cycle-locked survey submissions.""",
        """4. Intelligence Tier: Implemented in Python 3.13 utilizing scikit-learn 1.6+ and Joblib 1.4. It executes feature z-score standardization, Random Forest bagging inference, Gradient Boosted tree scoring, and probability calibration via soft voting."""
    ]),
    ("3.8 Use Case Analysis & Persona Modeling", [
        """Figure 3.2 depicts the system Use Case diagram, detailing the interactions of three core system personas:""",
        """- Student Persona: Submits monthly wellbeing surveys (UC1), views personal academic risk badges and support advice (UC2), and confirms scheduled advisory check-in meetings.""",
        """- Academic Counselor Persona: Reviews prioritized triage queues (UC3), inspects individual student dimension breakdowns (UC4), approves or customizes automated calendar bookings, and logs meeting outcomes.""",
        """- Platform Administrator Persona: Reviews and approves institutional tenant registrations (UC5), oversees global student and counselor account rosters (UC6), monitors system audit logs, and triggers scheduled model retraining runs."""
    ]),
    ("3.9 Technology Stack Justification", [
        """Every technology in the StudentDropout stack was chosen based on concrete architectural and performance justifications:""",
        """- React 19: Declarative component architecture with concurrent rendering and custom hooks (useState, useEffect, useMemo), enabling instant reactive UI updates without page reloads.""",
        """- Vite 7: Lightning-fast Hot Module Replacement (HMR) and optimized Rollup bundling, reducing production build times to under 7 seconds.""",
        """- Node.js & Express: Asynchronous, event-driven, non-blocking I/O runtime optimal for handling concurrent survey ingestions and asynchronous Google Calendar API calls.""",
        """- MongoDB & Mongoose: Flexible document model ideally suited for polymorphic survey responses and nested retention logs, with powerful compound indexing capabilities.""",
        """- Python & scikit-learn: The industry gold-standard for ensemble decision trees, providing mature hyperparameter controls, probability calibration, and sub-second Joblib persistence."""
    ])
]

# Table 3.1 Data
TABLE_3_1_HEADERS = ["Component Parameter", "Development Workstation Specs", "Production University Server Specs"]
TABLE_3_1_ROWS = [
    ("Processor (CPU)", "AMD Ryzen 5 / Intel Core i5 (6 cores, 3.8 GHz)", "Intel Xeon E5 / AMD EPYC (8 vCPUs, 2.8+ GHz)"),
    ("System Memory (RAM)", "16 GB DDR4 3200 MHz", "32 GB ECC DDR4 Server Memory"),
    ("Primary Storage (SSD)", "512 GB NVMe PCIe Gen 3 M.2 SSD", "1 TB Enterprise NVMe SSD (RAID-1 Mirroring)"),
    ("Network Interface", "1 Gbps Realtek Ethernet / Wi-Fi 6", "10 Gbps Redundant Fiber Uplink"),
    ("Operating System", "Microsoft Windows 11 Enterprise (64-bit)", "Ubuntu Server 22.04 LTS / 24.04 LTS (64-bit)")
]

# Table 3.2 Data
TABLE_3_2_HEADERS = ["Software Layer", "Framework / Runtime", "Exact Version", "Architectural Purpose"]
TABLE_3_2_ROWS = [
    ("Client Framework", "React SPA", "19.2.0", "Declarative component-driven user interface"),
    ("CSS Engine", "Tailwind CSS", "4.3.3", "Utility-first responsive styling and layout"),
    ("Build Bundler", "Vite", "7.2.4", "Optimized production Rollup bundling and HMR"),
    ("Server Runtime", "Node.js (ESM)", "v20.18.0+", "Asynchronous non-blocking event-driven API engine"),
    ("API Framework", "Express.js", "4.19.2", "RESTful routing, middleware guards, and controllers"),
    ("Database Engine", "MongoDB Community", "8.0.4", "High-throughput document store with multi-tenant indexing"),
    ("Object Modeling", "Mongoose ODM", "8.14.0", "Schema enforcement, validation hooks, and queries"),
    ("ML Framework", "Python / scikit-learn", "3.13 / 1.6.0+", "Dual-model ensemble classification and evaluation"),
    ("Model Serialization", "Joblib", "1.4.2", "High-efficiency disk serialization for .joblib models"),
    ("Calendar Protocol", "Google Calendar API", "v3 (REST)", "Automated slot discovery and Google Meet event booking")
]

# ======================================================================
# CHAPTER 4 DATA
# ======================================================================

CHAPTER_4_TITLE = "CHAPTER 4: SYSTEM DESIGN & METHODOLOGY"

CHAPTER_4_SECTIONS = [
    ("4.1 Architectural Design Principles", [
        """The StudentDropout system design adheres to five fundamental architectural principles:""",
        """1. Separation of Concerns: Strict decoupling among the presentation tier (React), business API tier (Express), persistence tier (MongoDB), and machine learning inference tier (Python). Each tier communicates via standard JSON over HTTP or IPC child_process streams.""",
        """2. Multi-Tenant Data Isolation: Strict logical partitioning of institutional records. Every query against student feedback or retention actions is strictly scoped by the authenticated user's institutionCode, preventing cross-institutional data leakage.""",
        """3. Asynchronous Non-Blocking Processing: Long-running external tasks—such as Google Calendar API OAuth2 handshakes and SMTP email deliveries—are executed asynchronously to prevent blocking the Node.js event loop.""",
        """4. Idempotence & Cycle Locking: Survey submissions and calendar bookings are designed to be idempotent. Database compound unique indexes guarantee that a student cannot submit duplicate evaluations in a single monthly cycle.""",
        """5. Human-in-the-Loop Governance: Machine learning predictions serve strictly as decision support. No student is disciplined, transferred, or officially flagged without human academic counselor review and authorization."""
    ]),
    ("4.2 Data Flow Modeling (Level 0 and Level 1 DFD)", [
        """Data flow modeling articulates the functional transformation of data as it traverses system boundaries:""",
        """- Figure 4.1 depicts the Level 0 Data Flow Diagram (Context Diagram). The central StudentDropout Platform process (0.0) interacts with four external entities: the Student (submitting survey responses, receiving check-in confirmations), the Academic Counselor (receiving prioritized triage alerts, approving intervention bookings), the Platform Administrator (managing institutional tenant codes), and the Google Calendar API (receiving event creation payloads, returning Google Meet URLs).""",
        """- Figure 4.2 details the Level 1 Data Flow Diagram, decomposing the system into four discrete sub-processes: Process 1.0 (Survey Ingestion & Boundary Validation, writing to D1 Feedback Store), Process 2.0 (Machine Learning Ensemble Inference, writing to D2 Analytics Store), Process 3.0 (Retention Triage & Discordance Filtering, updating counselor queues), and Process 4.0 (Calendar Scheduling & Notification Dispatch, writing to D3 Retention Action Store and notifying students)."""
    ]),
    ("4.3 Database and Schema Design", [
        """The application database is implemented in MongoDB under the database namespace studentDropout. Figure 4.3 illustrates the Entity-Relationship (ER) diagram encompassing the six core operational collections:""",
        """1. users Collection: Stores authenticated account records across Student, Counselor, and Platform Admin personas, storing email, bcrypt hash, role, institutionCode, studentCode, and contact phone.""",
        """2. companies Collection: Stores institutional tenant records (such as 'PRMIT&R Badnera'), tracking institutionName, institutionCode, primaryAdmin, and approvalStatus.""",
        """3. feedback Collection: Stores periodic monthly pulse evaluations, recording studentId, feedbackPeriod (format 'YYYY-MM'), academicEngagement (1-5), supportSatisfaction (1-5), stressManagement (1-5), peerBelongingness (1-5), and qualitative feedback text. Enforces compound unique index { studentId: 1, feedbackPeriod: 1 }.""",
        """4. employeeanalytics Collection: Stores rolling dimension averages, descriptive survey risk tiers, calibrated ML probabilities p(x), and operational risk badges.""",
        """5. retentionactions Collection: Tracks advisory interventions, recording assignedCounselor, status ('Pending', 'Scheduled', 'Completed'), meetingDate, meetingTime, meetLink, and counselor notes.""",
        """6. modelmetadatas Collection: Maintains machine learning lineage, storing modelVersion ('1.0.0'), trainingTimestamp, datasetSize (9,470), evaluation metrics (accuracy, precision, recall, f1Score, rocAuc), and artifactPath."""
    ]),
    ("4.4 Data Collection & Feature Dictionary", [
        """The predictive engine is trained on a validated institutional cohort of 9,470 student records. Each record is parameterized across four core psychometric and academic engagement dimensions evaluated on continuous Likert scales in the range [1.0, 5.0]. Table 4.1 defines the complete feature dictionary, including mean values, standard deviations, and mapping onto educational constructs."""
    ]),
    ("4.5 Core System Modules and Subsystems", [
        """The application software architecture is modularized into five collaborating subsystems:""",
        """- Authentication & Authorization Subsystem: Handles user registration, bcrypt password hashing, JWT signing, and route protection via isLogedIn and requireRole middleware.""",
        """- Pulse Survey Engine: Manages survey rendering, client-side scale validation, server-side boundary checks, cycle-lock verification, and MongoDB persistence.""",
        """- Ensemble ML Inference Bridge: Manages child_process execution of the Python inference script, passing JSON payloads over stdin/stdout and returning calibrated risk probabilities within 145 ms.""",
        """- Triage Rules Engine: Implements the dual-criteria decision logic, evaluating both ensemble risk probability p(x) and single-dimension minimum rating min(xj).""",
        """- Calendar Allocation & Outreach Subsystem: Implements slot discovery across counselor business hours, manages MongoDB atomic reservation state updates, invokes Google Calendar API, and dispatches email invitations via Nodemailer / EmailJS."""
    ]),
    ("4.6 Algorithmic Formulations and Mathematical Derivations", [
        """This section provides the formal mathematical foundations and complete pseudocode for the four core algorithms governing the StudentDropout platform:""",
        """Algorithm 1: Data Preprocessing and Leakage-Free Stratified Partitioning.""",
        """Algorithm 2: Dual-Model Soft-Voting Ensemble Classifier Training & Calibration.""",
        """Algorithm 3: Dual-Criteria Retention Triage and Discordance Resolution.""",
        """Algorithm 4: Conflict-Free Calendar Slot Allocation and Cooldown Enforcement.""",
        """The mathematical formulations are derived below:""",
        """Equation (1) defines the Random Forest bagging probability estimator:""",
        """P_RF(Y = 1 | x) = (1 / B) * SUM_{b=1}^{B} P_b(Y = 1 | x)       [Eq. 1]""",
        """Equation (2) defines the Gradient Boosted pseudo-residuals at iteration m:""",
        """r_{im} = - [ d L(y_i, F(x_i)) / d F(x_i) ]_{F = F_{m-1}}       [Eq. 2]""",
        """Equation (3) defines the unweighted soft-voting ensemble probability:""",
        """p(x) = 0.5 * P_RF(Y = 1 | x) + 0.5 * P_GB(Y = 1 | x)           [Eq. 3]""",
        """Equation (4) defines the binary cross-entropy loss function:""",
        """L_log = - (1 / N) * SUM_{i=1}^{N} [ y_i * ln(p(x_i)) + (1 - y_i) * ln(1 - p(x_i)) ]   [Eq. 4]""",
        """Equations (5) to (7) define the standard classification metrics:""",
        """Accuracy = (TP + TN) / (TP + TN + FP + FN)                     [Eq. 5]""",
        """Precision = TP / (TP + FP),   Recall = TP / (TP + FN)          [Eq. 6]""",
        """F1 = 2 * (Precision * Recall) / (Precision + Recall)           [Eq. 7]""",
        """Equation (8) defines the tripartite operational triage decision policy:""",
        """Tier(x) = Low Risk (Monitor) if p(x) < 0.40 and min(x_j) > 2.5;""",
        """          Moderate Risk (Advisor Flag) if 0.40 <= p(x) < 0.80 or min(x_j) <= 2.5;""",
        """          High Risk (Auto-Schedule) if p(x) >= 0.80 and Delta_t >= 7 days    [Eq. 8]"""
    ]),
    ("4.7 Workflow Pipeline Flowchart", [
        """Figure 4.4 details the end-to-end operational execution flowchart. The workflow initiates when a student submits a monthly pulse survey. The system verifies domain boundary compliance [1.0, 5.0] and queries the database for active cycle locks. If locked, the submission terminates with HTTP 409 Conflict. If clean, the survey is persisted, and the Python ML microservice is invoked. The soft-voting ensemble scores the vector, emitting calibrated probability p(x). The Triage Rules Engine routes the case into Low Risk (monitor only), Moderate Risk (pushed to counselor review queue), or High Risk (checking the 7-day cooldown guard). If cooldown has expired, the calendar allocation service reserves an open 30-minute slot, issues a Google Meet link, and dispatches neutral email invitations."""
    ]),
    ("4.8 Interaction Sequence Modeling", [
        """Figure 4.5 presents the UML Sequence Diagram illustrating chronological message passing across six collaborating lifelines: Student, React Client, Express API, Python ML Service, Academic Counselor, and Google Calendar API. All synchronous REST interactions complete within a tight sub-200ms window, while calendar and email dispatches execute asynchronously, ensuring optimal user responsiveness."""
    ]),
    ("4.9 RESTful API Specification", [
        """Table 4.2 provides the comprehensive RESTful API endpoint inventory, detailing HTTP methods, URL routes, authorized roles, request body schemas, and response descriptions."""
    ]),
    ("4.10 Security, Privacy & Ethical Governance", [
        """Higher education records represent highly sensitive personal information. The StudentDropout platform implements four rigorous layers of data protection:""",
        """1. Cryptographic Credential Protection: Passwords are encrypted using bcrypt with 10 salt rounds prior to persistence. Plaintext passwords never touch logs or databases.""",
        """2. Stateless Token Authentication: Authentication utilizes HMAC-SHA256 signed JSON Web Tokens (JWT) carrying user ID, role, and institution code, configured with 60-minute expiry.""",
        """3. Double-Layer RBAC Middleware: Every protected route enforces isLogedIn token verification followed by requireRole database validation, preventing privilege escalation.""",
        """4. FERPA & DPDP Act Compliance: Multi-tenant database query scoping guarantees complete cross-institutional data isolation. Students never see raw risk scores; invitations use supportive phrasing ('Academic Support & Guidance Check-in') to avoid psychological stigmatization."""
    ])
]

# Table 4.1 Data
TABLE_4_1_HEADERS = ["Feature Identifier", "Educational Construct", "Domain Scale", "Cohort Mean ± SD", "Behavioral & Psychometric Indicators"]
TABLE_4_1_ROWS = [
    ("academicEngagement (x1)", "Cognitive & Academic Effort", "[1.0, 5.0]", "3.42 ± 0.88", "Lecture attendance consistency, assignment completion rate, active study hours per week"),
    ("supportSatisfaction (x2)", "Institutional Support Utility", "[1.0, 5.0]", "3.15 ± 0.94", "Faculty mentor responsiveness, accessibility of tutoring labs, departmental advising adequacy"),
    ("stressManagement (x3)", "Psychological & Affective Load", "[1.0, 5.0]", "2.88 ± 1.05", "Perceived examination pressure, emotional burnout resilience, work-life-study balance"),
    ("peerBelongingness (x4)", "Social Integration & Belonging", "[1.0, 5.0]", "3.31 ± 0.91", "Peer study group collaboration, feeling accepted on campus, subjective isolation risk")
]

# Table 4.2 Data
TABLE_4_2_HEADERS = ["HTTP Method", "Endpoint URI", "Authorized Role", "Request Payload Schema", "Response Description & Status"]
TABLE_4_2_ROWS = [
    ("POST", "/api/auth/login", "Public", "{ email, password }", "Authenticates user; verifies tenant approval; returns signed JWT (200 OK)"),
    ("POST", "/api/auth/register-institution", "Public", "{ institutionName, code, adminEmail, password }", "Registers pending institutional tenant workspace (201 Created)"),
    ("POST", "/api/students/onboard", "Counselor / Admin", "{ fullName, email, department, semester }", "Creates student record with auto-generated STD-XXXXXX code (201 Created)"),
    ("POST", "/api/feedback", "Student", "{ ratings: [x1, x2, x3, x4], comments }", "Validates 4-D scores; enforces cycle lock; stores survey response (200 OK)"),
    ("GET", "/api/feedback/cycle-status", "Student", "None (Bearer Token)", "Returns boolean submission status for current monthly cycle (200 OK)"),
    ("POST", "/api/predict", "Internal / Service", "{ studentId, features: [x1, x2, x3, x4] }", "Spawns Python ensemble; returns p(x) and calibrated risk badge (200 OK)"),
    ("GET", "/api/counselor/roster", "Counselor", "Query: ?riskLevel=HIGH_RISK", "Returns institutional student directory with ML scores and triage badges (200 OK)"),
    ("POST", "/api/retention/schedule", "Counselor", "{ studentId, preferredSlot, notes }", "Allocates 30-min slot; creates Google Calendar event; emails invite (201 Created)"),
    ("GET", "/api/retention/actions", "Counselor", "Query: ?status=Pending", "Returns active intervention queue and scheduled counseling sessions (200 OK)"),
    ("GET", "/api/admin/system-stats", "Platform Admin", "None (Bearer Token)", "Returns global counts of institutions, users, model lineage, and audit logs (200 OK)")
]

# Algorithms Pseudocode Text
ALGORITHM_1_TEXT = """Algorithm 1: Data Preprocessing and Leakage-Free Stratified Partitioning
Input: Raw institutional cohort dataset D_raw with N = 9,470 records; target labels Y in {0, 1}; split ratio r = 0.25; random seed s = 42.
Output: Normalized training partition X_train, Y_train and test partition X_test, Y_test; fitted Scaler object S.

1: Initialize feature matrix X in R^{N x 4} from columns [academicEngagement, supportSatisfaction, stressManagement, peerBelongingness].
2: For each feature column j in {1, 2, 3, 4}:
3:     Compute training median m_j over valid non-null entries.
4:     Impute missing entries in column j with m_j.
5: Validate boundary constraints: Assert that all x_{i,j} in [1.0, 5.0].
6: Perform stratified train-test split:
       (X_train_raw, X_test_raw, Y_train, Y_test) = StratifiedSplit(X, Y, test_size=r, stratify=Y, random_state=s).
7: Instantiate Standard Scaler: S = StandardScaler().
8: Fit scaler strictly on training split: S.fit(X_train_raw).
9: Compute normalized feature matrices to prevent data leakage:
       X_train = S.transform(X_train_raw)
       X_test  = S.transform(X_test_raw)
10: Return X_train, X_test, Y_train, Y_test, S."""

ALGORITHM_2_TEXT = """Algorithm 2: Dual-Model Soft-Voting Ensemble Classifier Training & Probability Calibration
Input: Normalized training data (X_train, Y_train); hyperparameter sets Theta_RF and Theta_GB.
Output: Serialized ensemble model pipeline M_ens; empirical validation metrics E.

1: Configure Random Forest estimator:
       RF = RandomForestClassifier(n_estimators=180, max_depth=6, min_samples_leaf=4, class_weight='balanced', random_state=42).
2: Configure Gradient Boosted Decision Tree estimator:
       GB = GradientBoostingClassifier(n_estimators=150, learning_rate=0.08, max_depth=4, random_state=42).
3: Instantiate Soft-Voting Ensemble Classifier:
       VotingClf = VotingClassifier(estimators=[('rf', RF), ('gb', GB)], voting='soft', weights=[0.5, 0.5]).
4: Execute 5-fold stratified cross-validation over (X_train, Y_train) to verify fold stability:
       CV_Scores = StratifiedKFoldCV(VotingClf, X_train, Y_train, k=5, scoring=['accuracy', 'roc_auc', 'f1']).
5: Fit final ensemble model on complete training partition:
       VotingClf.fit(X_train, Y_train).
6: For candidate student feature vector x in X_test:
       Compute Random Forest posterior: P_RF = (1/B) * SUM_{b=1}^{B} P_b(Y = 1 | x).
       Compute Gradient Boosting posterior: P_GB = [1 + exp(-F_M(x))]^{-1}.
       Compute calibrated ensemble probability: p(x) = 0.5 * P_RF + 0.5 * P_GB.
7: Evaluate performance on held-out split (X_test, Y_test) across Accuracy, Precision, Recall, F1, and ROC-AUC.
8: Serialize trained pipeline to disk: joblib.dump(VotingClf, 'attrition_model_1.0.0.joblib').
9: Return VotingClf, CV_Scores, E."""

ALGORITHM_3_TEXT = """Algorithm 3: Dual-Criteria Retention Triage and Discordance Resolution
Input: Enrolled student survey vector x_i = [x_{i,1}, x_{i,2}, x_{i,3}, x_{i,4}]; trained ensemble model M_ens; cooldown history Delta_t.
Output: Operational triage action A_i in {Monitor, Advisor_Flag, Auto_Schedule_Meeting}.

1: Scale input vector using stored pipeline statistics: x_norm = Scaler.transform(x_i).
2: Compute ensemble dropout risk probability: p(x_i) = M_ens.predict_proba(x_norm)[1].
3: Extract minimum individual dimension rating: min_val = min(x_{i,1}, x_{i,2}, x_{i,3}, x_{i,4}).
4: If p(x_i) < 0.40 AND min_val > 2.5:
5:     Assign Risk Badge: 'ON TRACK' (Low Risk).
6:     A_i = Monitor (Log survey scores; no advisory alert triggered).
7: Else If (0.40 <= p(x_i) < 0.80) OR (min_val <= 2.5 AND p(x_i) < 0.80):
8:     Assign Risk Badge: 'ADVISOR FLAGGED' (Moderate Risk / Single-Dimension Distress).
9:     A_i = Advisor_Flag (Queue on counselor triage dashboard with highlighted distress dimensions).
10: Else If p(x_i) >= 0.80:
11:    Assign Risk Badge: 'HIGH RISK' (Acute Attrition Risk).
12:    If Delta_t < 7 days:
13:        A_i = Advisor_Flag (Cooldown active: log telemetry; suppress duplicate calendar booking).
14:    Else:
15:        A_i = Auto_Schedule_Meeting (Trigger Algorithm 4 for conflict-free calendar booking).
16: Return A_i, p(x_i), Risk_Badge."""

ALGORITHM_4_TEXT = """Algorithm 4: Conflict-Free Calendar Slot Allocation and Cooldown Enforcement
Input: Flagged student ID s_id; counselor ID c_id; tenant workspace code t_code; current timestamp T_curr.
Output: Reservation status R in {CONFIRMED, COOLDOWN_SUPPRESSED, FAILED}; Google Meet link URL.

1: Query RetentionAction collection for last intervention timestamp: T_last = GetLastInterventionTime(s_id).
2: If (T_curr - T_last) < 7 days:
3:     Log audit trail: 'Automated booking suppressed due to active 7-day cooldown guard.'
4:     Return COOLDOWN_SUPPRESSED, null.
5: Define search window: Next 7 business days [T_curr + 24h, T_curr + 8 days], daily hours 09:00 to 17:00 IST.
6: Retrieve existing booked slots from MongoDB and Counselor Google Calendar via API.
7: Iterate across 30-minute time intervals [t_start, t_end]:
8:     If interval [t_start, t_end] does not overlap with any existing counselor commitment:
9:         Candidate_Slot = [t_start, t_end].
10:        Break iteration.
11: If Candidate_Slot is found:
12:    Execute atomic MongoDB update on RetentionAction collection:
           findOneAndUpdate({ studentId: s_id, status: 'PENDING' },
                            { $set: { status: 'SCHEDULED', slot: Candidate_Slot, counselorId: c_id } },
                            { upsert: true }).
13:    Invoke Google Calendar API v3:
           Event = CreateEvent(summary='Academic Support & Guidance Check-in',
                               start=Candidate_Slot.start, end=Candidate_Slot.end,
                               attendees=[student.email, counselor.email],
                               conferenceData={ createRequest: { requestId: UUID() } }).
14:    Extract generated video URL: URL = Event.hangoutLink.
15:    Update student lastInterventionTimestamp = T_curr.
16:    Dispatch asynchronous email invitation with non-stigmatizing subject and Meet link.
17:    Return CONFIRMED, URL.
18: Else:
19:    Queue for manual counselor triage: FlagForManualScheduling(s_id).
20:    Return FAILED, null."""

print("Chapters 3 & 4 loaded.")
