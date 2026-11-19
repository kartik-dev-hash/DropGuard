# Project Overview and Technical Documentation: Employee Attrition Model

**Candidate**: Prithvi Raghuwanshi  
**Project**: Employee Attrition Model — Multi-Tenant Enterprise Workforce Intelligence & Predictive Attrition Analytics Platform  
**Academic Year**: 2025–2026  
**Department**: Computer Science & Engineering  

---

## 1. Executive Summary & Problem Scope

Employee turnover (attrition) is among the most disruptive and expensive challenges facing modern technology and corporate organizations. Replacing an experienced team member typically costs between 150% and 200% of their annual salary in direct recruitment costs, onboarding, productivity loss, and domain knowledge drain.

Traditional corporate retention methodologies suffer from three fundamental architectural flaws:
1. **Infrequent Assessment**: Annual or bi-annual appraisals fail to detect sudden workload surges, managerial disconnects, or rapid burnout.
2. **Disconnected Tooling**: Feedback collected via ad-hoc spreadsheets or survey forms is isolated from employee tenure histories and human resources records.
3. **Reactive Interventions**: Exit interviews occur after resignation letters are tendered, making retention virtually impossible.

The **Employee Attrition Model** project solves this by delivering an end-to-end, multi-tenant workforce intelligence platform. It systematically collects periodic monthly feedback, performs automated descriptive risk evaluations, connects with a trained scikit-learn Random Forest model, and provides HR teams with a dedicated **Retention Action Center** to execute proactive interventions via WhatsApp.

---

## 2. System Architecture

The project implements a decoupled 4-tier architecture designed for maintainability, horizontal scalability, and strict multi-tenant data isolation.

```
+-----------------------------------------------------------------------------------+
|                              PRESENTATION TIER (SPA)                              |
|   React 19.2 + Tailwind CSS 4.3 + Lucide React + Vite 7.2                        |
|   - Portals: Employee Portal, HR Admin Portal, Platform Admin Portal              |
|   - Features: Full-Page EmployeeDetailView, Responsive Custom Scrollbar Modals    |
+-----------------------------------------------------------------------------------+
                                          |
                                   HTTPS / REST (JWT)
                                          v
+-----------------------------------------------------------------------------------+
|                             APPLICATION & API TIER                                |
|   Node.js 20+ (ES Modules) + Express.js 4.19 + JWT 9.0 + bcryptjs 2.4             |
|   - Middleware: isLogedIn (Bearer token verify), requireRole() (RBAC db guard)    |
|   - Scheduled Services: reminderScheduler.js (Automated monthly cycle dispatch)  |
|   - Integration Bridge: emailService.js (EmailJS HTTPS API direct delivery)       |
+-----------------------------------------------------------------------------------+
                   |                                               |
         Mongoose ODM Queries                            child_process.spawn()
                   v                                               v
+--------------------------------------+       +------------------------------------+
|          PERSISTENCE TIER            |       |         INTELLIGENCE TIER          |
|   MongoDB 8.x + Mongoose 8.14        |       |   Python 3.13 + scikit-learn 1.6+  |
|   - Multi-tenant indexing            |       |   - train_model.py (Random Forest) |
|   - Collections: users, companies,   |       |   - predict.py (JSON CLI bridge)   |
|     feedback, employeeanalytics,     |       |   - Serialized joblib artifacts    |
|     retentionactions, modelmetadatas |       |     (backend/ml/artifacts/)        |
+--------------------------------------+       +------------------------------------+
```

---

## 3. Technology Stack & Component Justifications

| Tier / Component | Technology | Exact Version | Architectural Justification |
| :--- | :--- | :--- | :--- |
| **Frontend Framework** | React | `19.2.0` | Declarative UI components, reactive hooks (`useState`, `useEffect`, `useMemo`), clean routing. |
| **Build Tooling** | Vite | `7.2.4` | Near-instant Hot Module Replacement (HMR) and optimized Rollup bundling (build in 6.66s). |
| **Styling & Design** | Tailwind CSS | `4.3.3` | Utility-first CSS engine with custom scrollbar extensions (`.custom-scrollbar`). |
| **UI Vector Icons** | Lucide React | `1.46.0` | Modern, consistent icon library utilized across navigation bars and metric cards. |
| **Backend Runtime** | Node.js | `v20+` (ESM) | Asynchronous non-blocking event-driven runtime with native ES Module imports. |
| **API Framework** | Express.js | `4.19.2` | Robust routing architecture, middleware composition, JSON body parsing, and error handlers. |
| **Database Engine** | MongoDB | `8.x` | High-throughput document store ideal for polymorphic feedback surveys and analytics schemas. |
| **Object Data Modeling** | Mongoose | `8.14.0` | Enforces strict schema validations, compound unique indexes, and document lifecycle hooks. |
| **Authentication** | JWT (`jsonwebtoken`) | `9.0.3` | Cryptographically signed stateless Bearer tokens carrying user identity, role, and tenant code. |
| **Password Security** | `bcryptjs` | `2.4.3` | One-way cryptographic salting and hashing with cost factor 10 to protect credentials at rest. |
| **Machine Learning** | `scikit-learn` | `1.6.0+` | Industry standard ensemble classification (Random Forest), evaluation metrics, and stratification. |
| **Model Serialization** | `joblib` | `1.4.2` | High-efficiency disk persistence for scikit-learn pipeline objects and metadata dictionaries. |
| **Numerical Array Ops** | `numpy` | `2.2.0` | Vectorized array operations supporting machine learning feature formatting and matrices. |

---

## 4. Database Design & Schemas

The application database is named `empAttrition` and contains 6 operational collections:

### 1. `users` (`backend/models/User.js`)
Stores authenticated user accounts across all three personas.
- `_id`: ObjectId (Primary key)
- `email`: String (Required, unique, trimmed, lowercase)
- `password`: String (Required, bcrypt hash)
- `fullName`: String (Required, trimmed)
- `role`: String (Enum: `['platformAdmin', 'hr', 'employee']`, required)
- `companyCode`: String (Uppercase, indexed, represents tenant association)
- `employeeCode`: String (Unique sparse index, auto-generated `EMP-XXXXXX`)
- `phoneNumber`: String (Contact number for WhatsApp integration)
- `timestamps`: `createdAt`, `updatedAt`

### 2. `companies` (`backend/models/company.js`)
Stores tenant enterprise organizations.
- `_id`: ObjectId
- `companyName`: String (Required, trimmed)
- `industry`: String (Required, trimmed)
- `companyCode`: String (Required, unique, uppercase)
- `primaryHR`: ObjectId (Ref: `User`, primary administrator contact)
- `status`: String (Enum: `['pending', 'approved', 'rejected']`, default `'pending'`)
- `timestamps`: `createdAt`, `updatedAt`

### 3. `feedback` (`backend/models/feedback.js`)
Stores monthly survey submissions from employees.
- `_id`: ObjectId
- `employeeId`: ObjectId (Ref: `User`, required, indexed)
- `feedbackPeriod`: String (Required, indexed, format `"YYYY-MM"`, e.g. `"2026-10"`)
- `jobSatisfaction`: Number (Required, 1 to 4 scale)
- `workEnvironment`: Number (Required, 1 to 4 scale)
- `workLifeBalance`: Number (Required, 1 to 4 scale)
- `growth`: Number (Required, 1 to 4 scale)
- `manager`: String (Required, written supervisor feedback)
- `likedMost`: String (Qualitative strengths)
- `improvement`: String (Qualitative constructive criticism)
- `comments`: String (General feedback)
- `submittedAt`: Date (Default: `Date.now`)
- **Key Index**: Compound unique index `{ employeeId: 1, feedbackPeriod: 1 }` to enforce cycle locking.

### 4. `employeeanalytics` (`backend/models/EmployeeAnalytics.js`)
Stores aggregated survey scores and model inference snapshots per employee.
- `employeeId`: ObjectId (Ref: `User`, indexed)
- `companyCode`: String (Indexed)
- `currentAverages`: `{ jobSatisfaction, workEnvironment, workLifeBalance, growth, overall }`
- `experimentalSurveyRisk`: `{ level: ['HEALTHY', 'NEEDS_ATTENTION', 'HIGH_RISK', 'NO_FEEDBACK'], score, disclaimer }`
- `mlPrediction`: `{ outcome, probability, modelVersion, predictionTimestamp, isAvailable }`

### 5. `retentionactions` (`backend/models/RetentionAction.js`)
Tracks HR retention interventions and meetings.
- `employeeId`: ObjectId (Ref: `User`, indexed)
- `companyCode`: String (Indexed)
- `assignedHR`: String (Name of HR representative)
- `status`: String (Enum: `['Pending', 'In Progress', 'Completed']`)
- `meetingDate`, `meetingTime`, `meetingLocation`: String
- `contactMethod`: String (Enum: `['Email', 'WhatsApp', 'In-Person', 'Phone']`)
- `agreedActionPlan`: String
- `contactHistory`: Array of logs `{ contactMethod, contactedAt, contactedBy, status, note }`

### 6. `modelmetadatas` (`backend/models/ModelMetadata.js`)
Stores the lineage, metrics, and artifact references for the Machine Learning model.
- `modelVersion`: String (Default: `"1.0.0"`)
- `trainingTimestamp`: Date
- `datasetSize`: Number (1,470 records)
- `validLabeledRecords`: Number (1,470 records)
- `features`: Array of Strings
- `evaluationMetrics`: `{ accuracy, precision, recall, f1Score, confusionMatrix, rocAuc }`
- `status`: String (Enum: `['UNTRAINED', 'NEEDS_LABELED_DATA', 'TRAINING', 'TRAINED', 'FAILED']`)
- `artifactPath`: String (Absolute path to `.joblib` file)

---

## 5. Security & Authentication Architecture

1. **Password Encryption**: When a user registers or is onboarded by an HR Admin, their plaintext password is processed through `bcrypt.hash(password, 10)` before persistence. Plaintext passwords never touch the database.
2. **Stateless JWT Tokens**: Upon successful credentials verification at `POST /login`, Express signs a JSON Web Token with HMAC SHA-256 using `process.env.JWT_SECRET`. The payload contains:
   ```json
   {
     "userId": "67...a1",
     "email": "employee@company.com",
     "role": "employee",
     "companyCode": "TECHCORP"
   }
   ```
3. **Double-Layer Authorization Middleware**:
   - `isLogedIn(req, res, next)`: Extracts `Authorization: Bearer <token>`, verifies the signature and expiration, and attaches `req.user`.
   - `requireRole(role)`: Queries the MongoDB `User` collection directly using `req.user.userId`. This ensures that even if a token payload were somehow spoofed or a user's permissions were revoked in the database, access is immediately blocked with HTTP 403.
4. **Tenant Approval Lockdown**: Lines 133–157 of `app.js` verify that an employee or HR user's associated company has `status: 'approved'`. If pending or rejected, authentication terminates with HTTP 403 Forbidden.

---

## 6. Machine Learning Implementation & Verified Empirical Metrics

### Algorithm Details
The predictive component uses a **Random Forest Classifier** implemented in Python (`backend/ml/train_model.py`):
```python
clf = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    class_weight="balanced",
    random_state=42
)
```

### Dataset Characteristics
- **Source**: IBM HR Employee Attrition benchmark dataset (`WA_Fn-UseC_-HR-Employee-Attrition.csv`).
- **Total Records**: 1,470 validated employee records.
- **Target Variable**: `Attrition` (`"Yes"` = 1, `"No"` = 0).
- **Target Distribution**: Highly imbalanced: ~16.1% Attrition Yes (237 records) vs. ~83.9% Attrition No (1,233 records).
- **Selected Features**: Four self-reported workplace dimensions aligned directly with monthly survey questions:
  1. `JobSatisfaction` (1 to 4)
  2. `EnvironmentSatisfaction` (1 to 4)
  3. `WorkLifeBalance` (1 to 4)
  4. `RelationshipSatisfaction` (1 to 4)

### Train/Test Stratification
- **Split Ratio**: 75% Training (1,102 samples) / 25% Testing (368 samples).
- **Stratified**: Uses `stratify=y` to maintain exact class proportions across train and test sets.

### Verified Empirical Evaluation Results (Held-Out Test Set, N = 368)
Executing `python train_model.py` verifies the exact performance metrics:
- **Accuracy**: `67.39%` (0.6739)
- **Precision**: `22.02%` (0.2202)
- **Recall**: `40.68%` (0.4068)
- **F1-Score**: `0.2857` (0.2857)
- **ROC-AUC**: `0.6179` (0.6179)
- **Confusion Matrix**:
  - True Negatives (TN): `224` (Retained employees correctly identified)
  - False Positives (FP): `85` (Retained employees flagged as at-risk)
  - False Negatives (FN): `35` (Turnover employees missed)
  - True Positives (TP): `24` (Turnover employees correctly predicted)

### Why Recall is Prioritized Over Precision
In enterprise human resource retention, a **False Negative** (failing to identify an employee about to quit) results in a severe financial loss of $50,000–$100,000 in replacement costs. A **False Positive** merely results in an HR representative scheduling a friendly 1-on-1 check-in with a satisfied employee. Configuring `class_weight='balanced'` deliberately biases the model to capture more turnover instances, yielding a 40.68% recall rate despite the severe class imbalance.

---

## 7. Node.js to Python Inference Bridge

Instead of introducing the overhead of a dedicated microservice (such as Flask or FastAPI), Node.js executes Python inference on demand via `child_process.spawn()` (`backend/services/mlService.js`):
1. `predictOutcome(features)` loads model metadata from MongoDB.
2. Spawns `python backend/ml/predict.py <payload_json>`.
3. `predict.py` loads the serialized `.joblib` model from `backend/ml/artifacts/attrition_model_1.0.0.joblib`.
4. Executes `clf.predict(X)` and `clf.predict_proba(X)`.
5. Emits structured JSON to `stdout`:
   ```json
   {
     "success": true,
     "prediction": "Left",
     "probability": 0.584,
     "riskCategory": "HIGH_RISK"
   }
   ```
6. The Node.js event listener receives the payload in ~45ms, parses the response, and persists the score to `EmployeeAnalytics`.

---

## 8. Verified REST API Endpoints

| Method | Endpoint | Allowed Role | Request Body | Response Description |
| :--- | :--- | :--- | :--- | :--- |
| `POST` | `/login` | Public | `{ email, password }` | Authenticates user; checks company approval; returns JWT. |
| `POST` | `/form` | Public | `{ companyName, industry, adminEmail, password }` | Registers tenant company with `'pending'` status. |
| `POST` | `/Save` | HR Admin | `{ fullName, email, password }` | Creates employee with auto-generated `EMP-XXXXXX` code. |
| `GET` | `/hr/employees` | HR Admin | None (Header Token) | Returns employees for HR's company with survey & ML risk status. |
| `POST` | `/predict` | Employee | `{ feedbacks: { ratings, text } }` | Validates and stores monthly feedback for current cycle. |
| `GET` | `/predict/status`| Employee | None (Header Token) | Returns whether employee submitted feedback for current month. |
| `GET` | `/api/hr/analytics/overview` | HR Admin | None (Header Token) | Company-level metrics, participation %, risk distribution. |
| `POST` | `/api/hr/analytics/train` | HR Admin | `{ modelVersion }` | Retrains Random Forest model; updates metadata & `.joblib`. |
| `GET` | `/admin/all-companies` | Platform Admin | None (Header Token) | Lists all tenant companies with live employee & HR counts. |
| `PUT` | `/admin/approve-company/:id` | Platform Admin | None | Updates tenant status to `'approved'`. |
| `PUT` | `/admin/reject-company/:id` | Platform Admin | None | Updates tenant status to `'rejected'`. |
| `GET` | `/admin/users` | Platform Admin | None (Header Token) | Lists all platform users across tenants (passwords stripped). |
| `GET` | `/admin/platform-stats` | Platform Admin | None (Header Token) | Live counts of companies, users, employees, and monthly trends. |

---

## 9. Known Technical Limitations & Honest Boundaries

1. **Benchmark vs. Live Retraining**: The supervised ML model is trained on 1,470 historical benchmark records. Live employee survey submissions do not immediately have a verified 'Attrition' ground truth label until employees actually leave over 6–12 months.
2. **Text Feature Utilization**: Qualitative text fields (`likedMost`, `improvement`) are currently reviewed manually by HR in the full-page Feedback Explorer and are not yet parsed through an automated NLP transformer.
3. **WhatsApp Outreach Protocol**: WhatsApp contact is initiated via direct personalized deep links (`https://wa.me/<number>?text=...`) rather than an automated WhatsApp Business Cloud API webhook.
