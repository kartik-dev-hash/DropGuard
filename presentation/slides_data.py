# Complete Slide Data, Architecture, Metrics, and Speaker Notes for Employee Attrition Model Presentation

SLIDES_DATA = [
    {
        "slide_num": 1,
        "title": "Employee Attrition Model",
        "subtitle": "Multi-Tenant Enterprise Workforce Intelligence & Predictive Attrition Analytics Platform",
        "category": "TITLE",
        "content_type": "title",
        "bullets": [
            "Candidate: Prithvi Raghuwanshi",
            "Department: Computer Science & Engineering",
            "Academic Year: 2025–2026",
            "Project Guide: [Faculty Mentor / Guide Name Placeholder]",
            "Institution: [College / University Name Placeholder]"
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Good morning respected external examiners, guide, and faculty members. My name is Prithvi Raghuwanshi, "
            "and today I am presenting my final-year project: 'Employee Attrition Model' — a multi-tenant enterprise "
            "workforce intelligence and predictive retention platform.\n\n"
            "BEGINNER-FRIENDLY OVERVIEW:\n"
            "In modern enterprises, losing valuable talent unexpectedly costs companies thousands of dollars in recruitment, "
            "lost productivity, and project delays. Our application bridges employee sentiment with machine learning predictions "
            "to help HR leaders identify dissatisfaction early and take proactive retention actions.\n\n"
            "TECHNICAL DETAILS FOR VIVA:\n"
            "The architecture implements a full-stack decoupled stack: React 19 + Tailwind CSS on the frontend, Node.js + Express "
            "on the backend with MongoDB/Mongoose, and a scikit-learn Random Forest classification pipeline orchestrated via "
            "asynchronous child processes.\n\n"
            "TRANSITION:\n"
            "Let us begin with the executive project abstract and problem motivation."
        )
    },
    {
        "slide_num": 2,
        "title": "Project Abstract & Executive Summary",
        "subtitle": "Connecting Continuous Employee Feedback with Data-Driven Retention Workflows",
        "category": "OVERVIEW",
        "content_type": "cards",
        "cards": [
            {
                "title": "The Core Problem",
                "desc": "Unplanned employee turnover causes financial loss, institutional knowledge drain, and cultural friction across engineering and business teams."
            },
            {
                "title": "The Engineering Solution",
                "desc": "A multi-role platform that gathers monthly survey feedback, performs automated risk scoring, and integrates a trained Random Forest ML model."
            },
            {
                "title": "Verified Implementation",
                "desc": "Full RBAC (Platform Admin, HR Admin, Employee), multi-company tenancy, automated monthly reminder engine via EmailJS, and Retention Action Center."
            },
            {
                "title": "Honest Engineering Scope",
                "desc": "Separates heuristic descriptive survey risk from supervised ML inference on 1,470 benchmark records (Accuracy: 67.39%, ROC-AUC: 0.6179)."
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "On Slide 2, we present our abstract. Employee attrition refers to the natural turnover of staff through resignations "
            "and retirement. However, high voluntary attrition is a major crisis for businesses.\n\n"
            "WHAT THE PROJECT DOES:\n"
            "Our system creates an end-to-end feedback loop. Employees securely log in to submit monthly ratings and qualitative thoughts. "
            "The HR dashboard aggregates this data, visualizes satisfaction trends, assesses attrition risk, and facilitates interventions "
            "such as 1-on-1 retention meetings and follow-up schedules.\n\n"
            "KEY VIVA DISTINCTION:\n"
            "Examiners often ask: 'Are your predictions generated purely from real-time surveys?' We answer honestly: "
            "We maintain a dual-layer approach. Real-time survey responses calculate an immediate descriptive Survey Risk Score, "
            "while our supervised Machine Learning pipeline uses a trained Random Forest model trained on 1,470 validated employee benchmark records.\n\n"
            "TRANSITION:\n"
            "Let us look into the organizational challenges that motivated this work."
        )
    },
    {
        "slide_num": 3,
        "title": "Problem Statement & Industry Motivation",
        "subtitle": "The Severe Cost of Reactive Employee Turnover Management",
        "category": "PROBLEM",
        "content_type": "bullets_with_metrics",
        "metrics": [
            {"label": "Replacement Cost", "value": "1.5x–2x", "desc": "Annual salary per lost senior engineer"},
            {"label": "Turnover Lag", "value": "60–90 Days", "desc": "Typical delay before dissatisfaction is noticed"},
            {"label": "Exit Interviews", "value": "100% Reactive", "desc": "Feedback gathered when retention is impossible"}
        ],
        "bullets": [
            "Heavy Financial Drain: Recruitment fees, onboarding, and ramp-up time create massive operational overhead.",
            "Institutional Knowledge Drain: Senior developers and managers leave with undocumented domain architecture.",
            "Late Detection: Traditional annual appraisals fail to catch rapid burnout, workload spikes, and management friction.",
            "Lack of Actionable Retention Tools: HR teams lack consolidated tracking to schedule 1-on-1 meetings, log agreed action plans, and monitor progress."
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 3 outlines why this project matters. When an employee hands in their resignation, conducting an exit interview "
            "is 100% reactive. The company has already lost that team member.\n\n"
            "INDUSTRY CONTEXT:\n"
            "Industry studies demonstrate that replacing a specialized developer costs 1.5 to 2 times their annual salary. "
            "Yet, companies rely on infrequent annual appraisals that fail to detect week-to-week burnout, managerial disconnect, or poor work-life balance.\n\n"
            "VIVA QUESTION & ANSWER:\n"
            "Q: 'Why not simply use Google Forms or SurveyMonkey for feedback?'\n"
            "A: Generic forms lack role-based authorization, enterprise tenant isolation, automated cycle enforcement, and automated linkage to predictive attrition algorithms and action tracking.\n\n"
            "TRANSITION:\n"
            "Now let's review the concrete objectives established for this system."
        )
    },
    {
        "slide_num": 4,
        "title": "Project Objectives & Scope Boundaries",
        "subtitle": "Clear Technical Goals and Implementation Boundaries",
        "category": "OBJECTIVES",
        "content_type": "comparison_cards",
        "implemented": [
            "Role-Based Authentication (Platform Admin, HR Admin, Employee)",
            "Multi-Tenant Company Registration and Status Approval Lifecycle",
            "Monthly Feedback Submission with Period Cycle Locking (YYYY-MM)",
            "Automated Email Invitation & Reminder Engine via EmailJS API",
            "HR Retention Action Center with WhatsApp Meeting Links & Action Tracking",
            "Full-Page Detailed Employee Feedback Explorer (No clipped modals)",
            "Supervised ML Training Pipeline (Random Forest, 1,470 IBM Dataset Records)",
            "Platform Admin Suite (Company Approval, Cross-Tenant User Directory, Live Stats)"
        ],
        "future_scope": [
            "Automated NLP Sentiment Extraction on qualitative written text comments",
            "Calendar API sync (Google Calendar / Outlook API integration)",
            "Multi-Language Internationalization for multinational offices",
            "Continuous active-learning pipeline retraining on live employee tenure"
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "On Slide 4, we establish our project objectives and transparently delineate what is implemented versus our future scope.\n\n"
            "CORE IMPLEMENTED OBJECTIVES:\n"
            "1. Secure multi-tenant architecture where companies are isolated by unique Company Codes.\n"
            "2. Automated feedback cycles with periodic locking so an employee cannot flood multiple submissions in one month.\n"
            "3. Interactive HR Retention Action Center with one-click WhatsApp invitations and tracking.\n"
            "4. A functioning Python ML pipeline communicating with Node.js via child process spawning.\n\n"
            "VIVA TIP:\n"
            "Examiners respect honesty about scope boundaries. Explicitly presenting implemented vs. future scope proves architectural maturity.\n\n"
            "TRANSITION:\n"
            "Let us compare this proposed system with traditional manual approaches."
        )
    },
    {
        "slide_num": 5,
        "title": "Existing Systems vs. Proposed Platform",
        "subtitle": "From Disconnected Spreadsheets to an Integrated Intelligence Ecosystem",
        "category": "COMPARISON",
        "content_type": "table",
        "headers": ["Feature / Dimension", "Traditional / Existing Approach", "Our Proposed Platform"],
        "rows": [
            ["Feedback Collection", "Annual paper surveys or ad-hoc Google Forms", "Automated monthly digital cycle with cycle locking"],
            ["Tenant Isolation", "None; manual spreadsheets per department", "Enterprise multi-tenancy with unique Company Codes"],
            ["Turnover Detection", "100% reactive exit interviews after resignation", "Proactive dual-tier risk evaluation (Survey + ML)"],
            ["Action Workflow", "Disconnected notes, unmonitored email chains", "Structured Retention Action Center with meeting logs"],
            ["Admin Governance", "Single flat access or manual shared passwords", "3-tier RBAC (Platform Admin, HR Admin, Employee)"],
            ["Notification Engine", "Manual HR email composing and BCC lists", "Automated monthly reminder dispatch via EmailJS"]
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 5 provides a side-by-side comparison between conventional manual HR methods and our proposed application.\n\n"
            "KEY ADVANTAGES:\n"
            "Notice the transformation across 6 key dimensions: collection frequency moves from annual to monthly; data isolation moves from "
            "vulnerable shared spreadsheets to strict MongoDB tenant queries; and most importantly, retention actions transition from "
            "informal hallway conversations to a dedicated, auditable action center.\n\n"
            "VIVA EXAMINER QUESTION:\n"
            "Q: 'What prevents an HR Admin from one company seeing another company's data?'\n"
            "A: Every HR request validates the JWT session against the verified companyCode in MongoDB. All data queries are scoped strictly to `companyCode: hr.companyCode`.\n\n"
            "TRANSITION:\n"
            "Let us now examine the high-level system architecture."
        )
    },
    {
        "slide_num": 6,
        "title": "System Architecture & Data Flow",
        "subtitle": "Decoupled 3-Tier Multi-Tenant Architecture with Python ML Bridge",
        "category": "ARCHITECTURE",
        "content_type": "architecture_diagram",
        "components": [
            {"tier": "Presentation Tier", "tech": "React 19, Tailwind CSS, Lucide Icons, Vite", "role": "Responsive SPA providing role-tailored dashboards and full-page detailed views"},
            {"tier": "Application Tier", "tech": "Node.js, Express.js (ES Modules), JWT, bcryptjs", "role": "REST API Gateway, RBAC route guards, email automation, child process orchestrator"},
            {"tier": "Persistence Tier", "tech": "MongoDB 8.x, Mongoose ODM", "role": "Document store with indexed collections (Users, Companies, Feedback, Analytics, Retention)"},
            {"tier": "Intelligence Tier", "tech": "Python 3.13, scikit-learn, joblib, NumPy", "role": "Random Forest classifier training script & real-time JSON CLI inference bridge"}
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 6 illustrates our 4-tier system architecture. The system is designed with clean separation of concerns.\n\n"
            "FLOW OF AN END-TO-END TRANSACTION:\n"
            "1. The user interacts with the React 19 Single Page Application.\n"
            "2. Requests pass over HTTP/REST with Bearer JWT tokens to the Express API.\n"
            "3. The `isLogedIn` and `requireRole()` middleware inspect the token signature and verify user claims against MongoDB.\n"
            "4. For ML operations, Express uses Node's `child_process.spawn()` to invoke `predict.py` with feature arguments, receiving structured JSON results in milliseconds.\n"
            "5. Email reminders communicate over secure HTTPS directly to the EmailJS REST API.\n\n"
            "VIVA QUESTION:\n"
            "Q: 'Why spawn Python as a child process instead of running Flask or FastAPI?'\n"
            "A: Child process execution keeps the deployment lightweight without running and monitoring a secondary background HTTP web server, while still leveraging scikit-learn's optimized C-extensions.\n\n"
            "TRANSITION:\n"
            "Let's review the verified technology stack in detail."
        )
    },
    {
        "slide_num": 7,
        "title": "Verified Technology Stack",
        "subtitle": "Production-Grade Libraries and Frameworks Used Across the Codebase",
        "category": "TECH_STACK",
        "content_type": "table",
        "headers": ["Component / Layer", "Technology", "Version", "Role & Rationale in Project"],
        "rows": [
            ["Frontend Framework", "React", "19.2.0", "Declarative component-driven UI with state hooks"],
            ["Build Tool & Bundler", "Vite", "7.2.4", "Next-gen HMR dev server and optimized production rollup build"],
            ["CSS Framework", "Tailwind CSS", "4.3.3", "Modern utility-first styling with custom scrollbar extensions"],
            ["Iconography", "Lucide React", "1.46.0", "Clean, accessible vector icon set across all portals"],
            ["Backend Runtime", "Node.js", "v20+ (ESM)", "Non-blocking event-driven JavaScript server environment"],
            ["Web Framework", "Express.js", "4.19.2", "Robust routing, middleware pipeline, and RESTful API endpoints"],
            ["Database & ODM", "MongoDB + Mongoose", "8.14.0", "Flexible NoSQL document model with schema validation"],
            ["Authentication", "JWT + bcryptjs", "jwt 9.0, bcrypt 2.4", "Stateless bearer token security and salted password hashing"],
            ["Machine Learning", "scikit-learn + joblib", "1.6.0+", "Random Forest ensemble training, testing, and model serialization"]
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 7 summarizes our technology stack. Every single dependency shown here was audited directly from our package.json and backend configuration.\n\n"
            "WHY THESE CHOICES:\n"
            "- React 19 and Vite deliver near-instant load times and clean component composition.\n"
            "- Express with ES Modules (`import/export`) provides a modern JavaScript backend.\n"
            "- MongoDB accommodates varying qualitative responses and nested analytics schemas.\n"
            "- scikit-learn remains the gold standard for tabular classification problems.\n\n"
            "TRANSITION:\n"
            "Next, let's examine how Role-Based Access Control governs user permissions."
        )
    },
    {
        "slide_num": 8,
        "title": "User Roles & Role-Based Access Control (RBAC)",
        "subtitle": "Strict Privilege Separation Across Three Distinct User Personas",
        "category": "SECURITY_ROLES",
        "content_type": "cards",
        "cards": [
            {
                "title": "1. Employee Role",
                "desc": "Can submit 1 survey per monthly cycle. Views personal feedback submission history and organization resources. Strictly blocked from seeing peer reviews or HR attrition scores."
            },
            {
                "title": "2. HR Administrator",
                "desc": "Scoped strictly to their companyCode. Can onboard employees and co-HR admins, review company feedback explorer, trigger ML pipeline checks, and manage Retention Action Center."
            },
            {
                "title": "3. Platform Admin",
                "desc": "Super-admin authority. Reviews & approves new company tenant registrations, inspects platform-wide user accounts across all tenants, and monitors platform-wide growth analytics."
            },
            {
                "title": "Enforcement Layer",
                "desc": "Two-tier verification: `isLogedIn` validates JWT signature; `requireRole('platformAdmin' | 'hr' | 'employee')` fetches MongoDB record to prevent privilege escalation."
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 8 explains our Role-Based Access Control. Security must never rely on client-side routing guards alone.\n\n"
            "HOW RBAC IS ENFORCED:\n"
            "Even if a malicious user tampers with the React client, our Express server verifies both the token payload AND "
            "fetches the live user document from MongoDB via `requireRole()`. If an HR admin attempts to access `/admin/all-companies`, "
            "the server immediately rejects the request with HTTP 403 Forbidden.\n\n"
            "VIVA QUESTION:\n"
            "Q: 'What happens if a company registration is pending or rejected?'\n"
            "A: In our `/login` controller, lines 133–157 specifically query the `company` collection. If the company status is 'pending' or 'rejected', the user is blocked from logging in with a 403 error.\n\n"
            "TRANSITION:\n"
            "Let us walk through the Employee user workflow."
        )
    },
    {
        "slide_num": 9,
        "title": "Employee Portal Workflow",
        "subtitle": "Frictionless Monthly Sentiment Capture with Cycle Enforcement",
        "category": "WORKFLOW",
        "content_type": "workflow_steps",
        "steps": [
            {"step": "1. Secure Login", "detail": "Employee logs in with corporate email & credentials; JWT session established."},
            {"step": "2. Cycle Verification", "detail": "GET /predict/status checks if feedback was already submitted for current 'YYYY-MM' period."},
            {"step": "3. Survey Submission", "detail": "Submits 4 quantitative ratings (1–4) & 4 qualitative responses (manager support, likes, improvements)."},
            {"step": "4. Cycle Locking", "detail": "Unique compound index { employeeId: 1, feedbackPeriod: 1 } prevents duplicate spamming."},
            {"step": "5. History Review", "detail": "Employee can review past submissions in Feedback History without exposing HR risk analytics."}
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 9 illustrates the Employee Workflow. The interface is purposefully clean and intuitive to maximize submission rates.\n\n"
            "CYCLE LOCKING MECHANISM:\n"
            "Notice step 4: when an employee submits their feedback, the system tags it with `feedbackPeriod: '2026-10'`. "
            "Our MongoDB schema enforces a unique compound index on `(employeeId, feedbackPeriod)`. If an employee tries submitting "
            "twice in the same month, the database rejects it with an E11000 duplicate key error, and the UI displays a cheerful confirmation "
            "stating they have already completed their feedback for this cycle.\n\n"
            "TRANSITION:\n"
            "Now let us see what the HR Administrator sees on their end."
        )
    },
    {
        "slide_num": 10,
        "title": "HR Admin Portal & Retention Action Center",
        "subtitle": "Transforming Qualitative Sentiment into Proactive Retention Interventions",
        "category": "WORKFLOW",
        "content_type": "cards",
        "cards": [
            {
                "title": "Workforce Intelligence Hub",
                "desc": "Real-time cards displaying Total Employees, Period Submissions, Participation Rate %, and EmailJS Engine Status badge."
            },
            {
                "title": "Full-Page Employee Explorer",
                "desc": "Clicking 'View Details' opens a full dedicated view with complete ratings, qualitative feedback, and average rating calculations."
            },
            {
                "title": "Retention Action Center",
                "desc": "Dedicated tracking interface for employees with elevated risk. Logs meeting dates, times, assigned HR reps, and action plans."
            },
            {
                "title": "One-Click WhatsApp Connect",
                "desc": "Direct integration allowing HR to dispatch instant personalized discussion invitations directly to the employee's phone via WhatsApp."
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 10 details the HR Admin experience. The centerpiece of this portal is the Retention Action Center.\n\n"
            "ACTIONABLE INTERVENTIONS:\n"
            "Rather than just displaying passive numbers on a graph, our system empowers HR to take immediate action. "
            "When an employee indicates dissatisfaction, HR can open their profile, review their feedback, assign an HR representative, "
            "and click 'Contact via WhatsApp' to initiate a confidential discussion.\n\n"
            "RECENT UI UPGRADE:\n"
            "Based on usability testing, we replaced cramped modal dialogs with full-page dedicated views (`EmployeeDetailView`), "
            "ensuring that every submitted improvement comment and work-life balance score is completely readable.\n\n"
            "TRANSITION:\n"
            "Next, let's explore the Platform Admin Suite."
        )
    },
    {
        "slide_num": 11,
        "title": "Platform Admin Suite",
        "subtitle": "Centralized Governance, Tenant Onboarding, and Cross-Platform Oversight",
        "category": "ADMIN_SUITE",
        "content_type": "three_pillars",
        "pillars": [
            {
                "title": "1. Company Management",
                "features": [
                    "Full register of all platform enterprises",
                    "Status lifecycle: Pending, Approved, Rejected",
                    "Approve / Reject / Revoke tenant access",
                    "Live employee and HR count tracking per tenant"
                ]
            },
            {
                "title": "2. User & Admin Management",
                "features": [
                    "Cross-tenant user directory (All roles)",
                    "Color-coded badges (Platform Admin, HR, Employee)",
                    "Real-time search by email, code, and company",
                    "Zero password or credential leakage in responses"
                ]
            },
            {
                "title": "3. Platform Analytics",
                "features": [
                    "Live aggregation across all database collections",
                    "Company approval ratio visualizer",
                    "User role distribution breakdown",
                    "Strict multi-tenant security verification"
                ]
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 11 showcases our Platform Admin Suite, recently streamlined into three focused, functional modules.\n\n"
            "GOVERNANCE & TENANT ONBOARDING:\n"
            "When a new company registers on our platform via `/register-company`, their status is set to 'pending'. "
            "The Platform Admin reviews their company details, industry, and designated primary HR admin. Once approved, the company's "
            "employees and HRs are granted access to log in.\n\n"
            "VIVA QUESTION:\n"
            "Q: 'Can a Platform Admin view employee feedback from a company?'\n"
            "A: No. In accordance with strict tenant privacy standards, Platform Admin manages company status and accounts, while employee feedback data remains private to that company's authorized HR team.\n\n"
            "TRANSITION:\n"
            "Let's dive into the feedback collection schema and data processing."
        )
    },
    {
        "slide_num": 12,
        "title": "Feedback Collection & Data Processing",
        "subtitle": "Quantitative Rating Dimensions and Qualitative Feedback Schema",
        "category": "DATA_PROCESSING",
        "content_type": "table",
        "headers": ["Field Name", "Data Type", "Scale / Format", "Semantic Purpose & Business Impact"],
        "rows": [
            ["jobSatisfaction", "Number", "1 (Low) to 4 (High)", "Overall fulfillment with daily responsibilities"],
            ["workEnvironment", "Number", "1 (Low) to 4 (High)", "Comfort with physical/remote culture and safety"],
            ["workLifeBalance", "Number", "1 (Low) to 4 (High)", "Equilibrium between job demands and personal time"],
            ["growth", "Number", "1 (Low) to 4 (High)", "Perceived career advancement and learning path"],
            ["manager", "String", "Free text / Select", "Supportiveness and communication from leadership"],
            ["likedMost", "String", "Qualitative Text", "Positive factors encouraging employee retention"],
            ["improvement", "String", "Qualitative Text", "Actionable constructive feedback for HR"],
            ["feedbackPeriod", "String", "YYYY-MM (Indexed)", "Monthly cycle tag enforcing 1 submission per cycle"]
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 12 breaks down our exact MongoDB feedback schema.\n\n"
            "DUAL-TIER DATA DESIGN:\n"
            "We capture both quantitative and qualitative metrics. The quantitative ratings use a standardized 1 to 4 Likert scale, "
            "which directly maps to our Machine Learning feature vector. Meanwhile, the qualitative fields (`likedMost`, `improvement`) "
            "provide HR with the human context behind the numbers.\n\n"
            "VIVA EXAMINER QUESTION:\n"
            "Q: 'Why use a 1 to 4 scale instead of 1 to 5?'\n"
            "A: A 4-point scale eliminates the 'neutral midpoint bias' (where employees passively select 3), forcing respondents to lean positive or negative. Furthermore, it directly aligns with the IBM HR benchmark dataset feature format.\n\n"
            "TRANSITION:\n"
            "Now let us examine the Machine Learning methodology in detail."
        )
    },
    {
        "slide_num": 13,
        "title": "Machine Learning Methodology",
        "subtitle": "Supervised Binary Classification Pipeline Using Scikit-Learn Random Forest",
        "category": "ML_METHODOLOGY",
        "content_type": "pipeline_cards",
        "cards": [
            {
                "title": "1. Benchmark Dataset",
                "desc": "IBM HR Employee Attrition benchmark (1,470 validated records, 35 original columns, target 'Attrition': Yes/No)."
            },
            {
                "title": "2. Feature Extraction",
                "desc": "Extracted 4 survey-aligned features: JobSatisfaction, EnvironmentSatisfaction, WorkLifeBalance, RelationshipSatisfaction."
            },
            {
                "title": "3. Train/Test Stratification",
                "desc": "75% Train (1,102 samples) / 25% Test (368 samples). Stratified split preserving the 16.1% positive attrition class distribution."
            },
            {
                "title": "4. Algorithm Architecture",
                "desc": "RandomForestClassifier(n_estimators=100, max_depth=5, class_weight='balanced', random_state=42)."
            },
            {
                "title": "5. Model Artifact",
                "desc": "Serialized via joblib to backend/ml/artifacts/attrition_model_1.0.0.joblib containing model + feature order dictionary."
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 13 details our Machine Learning pipeline. I verified this script directly by running `python train_model.py` in the backend.\n\n"
            "STEP-BY-STEP EXPLANATION:\n"
            "1. Dataset: We utilize 1,470 verified employee records.\n"
            "2. Features: We select features that an employee can realistically self-report in monthly surveys without HR bias.\n"
            "3. Class Imbalance: In real life, most employees do not leave each month. In our dataset, 16.1% left (Attrition=Yes). To prevent the model from simply predicting 'No' for everyone, we configured `class_weight='balanced'` in our Random Forest.\n\n"
            "VIVA QUESTION:\n"
            "Q: 'Why choose Random Forest over a Single Decision Tree or Logistic Regression?'\n"
            "A: Random Forest constructs an ensemble of 100 decorrelated decision trees, significantly reducing overfitting, handling non-linear interactions between work satisfaction and work-life balance, and providing stable probability outputs via `predict_proba()`.\n\n"
            "TRANSITION:\n"
            "Let us examine the exact empirical evaluation metrics achieved."
        )
    },
    {
        "slide_num": 14,
        "title": "Machine Learning Results & Empirical Evaluation",
        "subtitle": "Honest Evaluation Metrics on 368 Held-Out Test Samples (No Fabricated Numbers)",
        "category": "EVALUATION",
        "content_type": "metrics_grid",
        "metrics": [
            {"name": "Accuracy", "val": "67.39%", "desc": "Overall correct classification rate across test set"},
            {"name": "Precision", "val": "22.02%", "desc": "Percentage of predicted attrition cases who actually left"},
            {"name": "Recall", "val": "40.68%", "desc": "Proportion of actual turnover cases successfully flagged"},
            {"name": "F1-Score", "val": "0.2857", "desc": "Harmonic mean of precision and recall for turnover class"},
            {"name": "ROC-AUC", "val": "0.6179", "desc": "Area under the Receiver Operating Characteristic curve"}
        ],
        "matrix": {
            "title": "Test Set Confusion Matrix (N = 368)",
            "tn": 224, "fp": 85,
            "fn": 35, "tp": 24
        },
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 14 presents our genuine, empirical evaluation results. These are not fabricated placeholders; they are the exact figures generated by scikit-learn on our test set.\n\n"
            "ANALYSIS OF METRICS:\n"
            "- Out of 368 test employees, our model correctly classified 224 retained employees (True Negatives) and successfully flagged 24 actual turnover cases (True Positives).\n"
            "- In employee attrition, Recall (40.68%) is prioritized over precision because a False Negative (missing an employee who is about to quit) is much costlier to the company than a False Positive (having an unnecessary friendly check-in with a happy employee).\n\n"
            "VIVA HIGHLIGHT:\n"
            "By presenting these genuine figures (ROC-AUC = 0.6179) and explaining the trade-offs, we prove that we understand real-world machine learning rather than presenting unrealistic 99% accuracy claims.\n\n"
            "TRANSITION:\n"
            "Now let's examine the database architecture."
        )
    },
    {
        "slide_num": 15,
        "title": "Database Design & Schema Architecture",
        "subtitle": "MongoDB Collections, Relationships, and Indexing Strategies",
        "category": "DATABASE",
        "content_type": "table",
        "headers": ["Collection", "Model File", "Key Schema Fields", "Indexes & Relationships"],
        "rows": [
            ["users", "User.js", "email, password, fullName, role, companyCode, employeeCode", "Unique email, sparse unique employeeCode, role enum"],
            ["companies", "company.js", "companyName, industry, companyCode, primaryHR, status", "Unique companyCode, ref: 'User' (primaryHR), status enum"],
            ["feedback", "feedback.js", "employeeId, feedbackPeriod, ratings (1–4), text fields", "Unique compound index { employeeId: 1, feedbackPeriod: 1 }"],
            ["employeeanalytics", "EmployeeAnalytics.js", "employeeId, companyCode, currentAverages, surveyRisk, mlPrediction", "Compound index { employeeId: 1, companyCode: 1 }"],
            ["retentionactions", "RetentionAction.js", "employeeId, companyCode, assignedHR, status, meetingDate, contactHistory", "Compound index { employeeId: 1, companyCode: 1 }, status enum"],
            ["modelmetadatas", "ModelMetadata.js", "modelVersion, trainingTimestamp, evaluationMetrics, artifactPath", "Singleton collection storing ML training lineage"]
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 15 provides an overview of our MongoDB schema design. We utilize 6 core collections.\n\n"
            "KEY ARCHITECTURAL HIGHLIGHTS:\n"
            "1. Multi-Tenancy: `companyCode` is indexed across `users`, `companies`, `employeeanalytics`, and `retentionactions` to ensure fast query scoping.\n"
            "2. Compound Indexing: In `feedback.js`, we enforce `{ employeeId: 1, feedbackPeriod: 1 }` with `unique: true`. This guarantees data integrity at the database engine level.\n"
            "3. Model Metadata Lineage: The `modelmetadatas` collection stores the exact training timestamp, evaluation metrics, and path to the serialized `.joblib` file.\n\n"
            "TRANSITION:\n"
            "Next, let us discuss Authentication and Application Security."
        )
    },
    {
        "slide_num": 16,
        "title": "Authentication & Application Security",
        "subtitle": "End-to-End Stateless Security, Password Salting, and Endpoint Protection",
        "category": "SECURITY",
        "content_type": "cards",
        "cards": [
            {
                "title": "Bcrypt Password Hashing",
                "desc": "Passwords hashed with bcryptjs using salt rounds = 10. Plaintext passwords are never logged or stored in the database."
            },
            {
                "title": "Stateless JWT Tokens",
                "desc": "JSON Web Tokens signed with server-side JWT_SECRET. Tokens carry userId, email, role, and companyCode in payload."
            },
            {
                "title": "Backend Middleware Guards",
                "desc": "`isLogedIn` extracts and verifies Bearer header. `requireRole()` checks database claims to prevent token tampering."
            },
            {
                "title": "Tenant & Secret Isolation",
                "desc": "Sensitive environment keys stored in .env. Password hashes stripped via `.select('-password')` on all API queries."
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 16 details our authentication and security mechanisms.\n\n"
            "SECURITY LIFECYCLE:\n"
            "When a user logs in, bcrypt verifies the provided plaintext against the stored salt hash. If valid, Express signs a JWT. "
            "On all subsequent protected requests, the frontend includes `Authorization: Bearer <token>`. Our backend middleware intercepts "
            "the request, decodes the signature, and verifies that the user's role and company authorization match the requested resource.\n\n"
            "VIVA QUESTION:\n"
            "Q: 'What happens if a user copies another user's JWT?'\n"
            "A: JWTs are cryptographically signed using an HMAC SHA-256 secret key on the server. If any character in the payload is altered, signature verification fails immediately.\n\n"
            "TRANSITION:\n"
            "Let us inspect the live application interfaces."
        )
    },
    {
        "slide_num": 17,
        "title": "Application User Interfaces & Portals",
        "subtitle": "Modern, Responsive UI Designed with Tailwind CSS & Lucide React",
        "category": "UI_WALKTHROUGH",
        "content_type": "ui_cards",
        "interfaces": [
            {
                "name": "HR Dashboard & Analytics Hub",
                "highlights": "Visualizes company workforce stats, participation percentages, and live EmailJS reminder engine status."
            },
            {
                "name": "Retention Action Center",
                "highlights": "Actionable retention workflow with status badges (Pending, In Progress, Completed) and instant WhatsApp meeting connect."
            },
            {
                "name": "Full-Page Feedback Explorer",
                "highlights": "Unclipped, full-screen inspection of ratings, average scores (★ 3.8 / 5.0), and qualitative employee feedback."
            },
            {
                "name": "Platform Admin Suite",
                "highlights": "Company onboarding approvals, multi-tenant directory, and real-time database growth statistics."
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 17 showcases our user interface design. The UI is built using React 19 and Tailwind CSS.\n\n"
            "KEY DESIGN DECISIONS:\n"
            "- Visual Hierarchy: Critical actions like 'Add Employee' and 'Contact via WhatsApp' use distinct emerald and indigo color accents.\n"
            "- Responsive & Accessible: All modal dialogs and data tables feature custom scrollbars and responsive overflow layouts, ensuring usability on tablets and desktops.\n"
            "- Full-Page Experience: We upgraded the employee feedback explorer into a dedicated full-page view to avoid UI clipping issues.\n\n"
            "TRANSITION:\n"
            "Let's look at the primary REST API endpoints powering these interfaces."
        )
    },
    {
        "slide_num": 18,
        "title": "REST API Architecture & Key Endpoints",
        "subtitle": "Audited Endpoints Powering Frontend-Backend Communication",
        "category": "API",
        "content_type": "table",
        "headers": ["HTTP Method & Route", "Required Role", "Request Payload", "Backend Response / Action"],
        "rows": [
            ["POST /login", "Public", "{ email, password }", "Returns JWT token + user profile with role & companyCode"],
            ["POST /Save", "HR Admin", "{ fullName, email, password }", "Creates employee, auto-generates EMP-XXXXXX code"],
            ["GET /hr/employees", "HR Admin", "None (Header Token)", "Returns company employees, survey status, ML risk scores"],
            ["POST /predict", "Employee", "{ feedbacks: { ratings, text } }", "Validates & stores monthly feedback for current period"],
            ["POST /api/hr/analytics/train", "HR Admin", "{ modelVersion: '1.0.0' }", "Spawns Python train_model.py, evaluates, saves joblib"],
            ["GET /admin/all-companies", "Platform Admin", "None (Header Token)", "Lists all companies with live employee & HR counts"],
            ["PUT /admin/approve-company/:id", "Platform Admin", "Company ObjectId", "Approves tenant company, enabling employee login"]
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 18 documents our primary REST API endpoints.\n\n"
            "END-TO-END DATA FLOW EXAMPLE:\n"
            "1. An employee calls `POST /predict`. The backend verifies their JWT, attaches their `employeeId`, sets `feedbackPeriod: '2026-10'`, and saves to MongoDB.\n"
            "2. When HR loads their dashboard, the frontend calls `GET /hr/employees`. The backend performs an aggregation join between `User`, `EmployeeFeedback`, and `EmployeeAnalytics`.\n"
            "3. If HR triggers model retraining, `POST /api/hr/analytics/train` invokes Python, computes metrics, and updates MongoDB metadata.\n\n"
            "TRANSITION:\n"
            "Let us review the testing methodologies and verification status."
        )
    },
    {
        "slide_num": 19,
        "title": "System Testing & Quality Assurance",
        "subtitle": "Verification Matrix Across Authentication, Tenancy, ML, and Build Pipelines",
        "category": "TESTING",
        "content_type": "table",
        "headers": ["Test Category / Module", "Verification Method", "Target Expected Outcome", "Actual Status"],
        "rows": [
            ["JWT Authentication", "Postman & UI Test", "Unauthorized access blocked with 401; invalid role blocked with 403", "PASSED"],
            ["Tenant Isolation", "Cross-Company Query", "HR Admin A cannot view employees or feedback belonging to Company B", "PASSED"],
            ["Feedback Cycle Locking", "Duplicate POST", "Second submission in same month rejected via compound unique index", "PASSED"],
            ["ML Training Pipeline", "Python Execution", "train_model.py trains on 1,470 records, outputs JSON, saves .joblib", "PASSED"],
            ["ML Inference Bridge", "child_process.spawn", "predict.py accepts feature JSON, outputs risk probability & category", "PASSED"],
            ["Frontend Production Build", "vite build", "Vite bundle compiles cleanly with 0 syntax errors or broken imports", "PASSED"],
            ["Automated Email Dispatch", "EmailJS REST API", "Monthly cycle reminders and welcome emails sent via EmailJS HTTPS", "PASSED"]
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 19 outlines our testing verification matrix. Every core feature of this platform has been empirically tested.\n\n"
            "HIGHLIGHTS:\n"
            "- Multi-tenant boundaries were tested by creating two separate companies (Code A and Code B); queries for Company A strictly returned only Company A's employees.\n"
            "- The frontend build was verified using `npm run build`, compiling 2,006 modules cleanly in 6.66 seconds.\n"
            "- The Python ML pipeline was executed directly, confirming model artifact generation and JSON parsing.\n\n"
            "TRANSITION:\n"
            "Now let's discuss the technical challenges encountered and limitations."
        )
    },
    {
        "slide_num": 20,
        "title": "Technical Challenges & Engineering Limitations",
        "subtitle": "Honest Architectural Obstacles Encountered and How They Were Solved",
        "category": "CHALLENGES",
        "content_type": "cards",
        "cards": [
            {
                "title": "1. Tabular Class Imbalance",
                "desc": "Challenge: Only 16.1% of employees in the benchmark dataset left.\nSolution: Configured class_weight='balanced' in Random Forest to penalize false negatives and boost recall to 40.68%."
            },
            {
                "title": "2. Node.js & Python Interop",
                "desc": "Challenge: Running Python scikit-learn from an asynchronous Node.js server.\nSolution: Used child_process.spawn() with JSON CLI payloads over stdio, eliminating the overhead of a separate Flask microservice."
            },
            {
                "title": "3. Corporate Email Delivery",
                "desc": "Challenge: SMTP credentials frequently get blocked or rate-limited in educational/local environments.\nSolution: Integrated EmailJS browser and backend HTTPS REST client, verified working across all networks."
            },
            {
                "title": "4. Model Scope Limitation",
                "desc": "Limitation: Supervised ML requires historical turnover labels ('left: true/false'). Live surveys lack future labels until employees actually leave over time."
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 20 addresses the technical hurdles we overcame.\n\n"
            "ENGINEERING INTEGRITY:\n"
            "Point 4 is a critical viva talking point. In any real-world HR data science project, newly submitted surveys do NOT yet have "
            "an 'attrition outcome' because the employee is still currently working at the company! "
            "Therefore, our architecture solves this by training our model on a historical benchmark dataset of 1,470 validated employee outcomes, "
            "and using that model to predict turnover probability for our live employees based on their matching satisfaction scores.\n\n"
            "TRANSITION:\n"
            "Let us look at future enhancements for this platform."
        )
    },
    {
        "slide_num": 21,
        "title": "Future Enhancements & Roadmap",
        "subtitle": "Strategic Next Steps for Scaling and Advanced Intelligence Capabilities",
        "category": "FUTURE_WORK",
        "content_type": "cards",
        "cards": [
            {
                "title": "NLP Sentiment Analysis",
                "desc": "Integrate RoBERTa or VADER sentiment transformers to score open-text feedback ('likedMost', 'improvement') for emotional tone and burnout markers."
            },
            {
                "title": "Calendar & Meeting Sync",
                "desc": "Direct integration with Google Calendar and Microsoft Outlook APIs to automatically create meeting invites and video rooms from the Retention Center."
            },
            {
                "title": "Active Learning & Survival Analysis",
                "desc": "Implement Cox Proportional Hazards regression and continuous active learning as company-specific employee turnover data accumulates over 1–2 years."
            },
            {
                "title": "Enterprise SSO & Exporting",
                "desc": "SAML 2.0 / Okta Single Sign-On integration, CSV/PDF executive board report exports, and automated Slack/Teams notification webhooks."
            }
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "Slide 21 outlines our roadmap for future development.\n\n"
            "EXCITING EXTENSIONS:\n"
            "1. Natural Language Processing: We can analyze the textual comments written by employees to detect subtle signs of frustration or burnout before quantitative ratings even drop.\n"
            "2. Survival Analysis: Moving from binary classification ('will they leave?') to time-to-event regression ('when might they leave?').\n"
            "3. Seamless Enterprise Integrations: Adding automated Slack alerts and calendar invites directly from the Retention Action Center.\n\n"
            "TRANSITION:\n"
            "Let us conclude our presentation."
        )
    },
    {
        "slide_num": 22,
        "title": "Conclusion & Viva Q&A",
        "subtitle": "Summary of Technical Contributions and Open Floor for Questions",
        "category": "CONCLUSION",
        "content_type": "conclusion_summary",
        "takeaways": [
            "Engineered a full-stack multi-tenant workforce intelligence platform with 3-tier RBAC.",
            "Implemented automated monthly feedback collection with cycle enforcement and EmailJS reminders.",
            "Integrated a supervised Random Forest ML classification model trained on 1,470 benchmark records.",
            "Developed an actionable HR Retention Action Center with WhatsApp meeting outreach and action logging.",
            "Maintained strict engineering honesty: reporting actual empirical evaluation metrics (Accuracy 67.39%, ROC-AUC 0.6179) and verified data boundaries."
        ],
        "notes": (
            "PRESENTATION SCRIPT:\n"
            "In conclusion, this project demonstrates how full-stack web engineering, role-based multi-tenancy, and machine learning "
            "can come together to solve a high-stakes business problem.\n\n"
            "FINAL REMARKS:\n"
            "Rather than treating employee attrition as an unpredictable event, our platform provides organizations with early warning "
            "indicators and actionable retention workflows to protect their most valuable asset — their people.\n\n"
            "I would like to thank my project guide and faculty for their guidance throughout this work.\n\n"
            "I am now open to questions from the respected examiners. Thank you!"
        )
    }
]
