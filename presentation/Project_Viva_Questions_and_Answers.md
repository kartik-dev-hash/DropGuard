# College Project Viva Questions and Answers: Employee Attrition Model

**Candidate**: Prithvi Raghuwanshi  
**Project**: Employee Attrition Model  
**Total Questions Prepared**: 35 Questions across System Architecture, Security, Machine Learning, Database Design, and Business Logic  

---

## SECTION 1: PROJECT CONCEPT & HIGH-LEVEL ARCHITECTURE

### Q1: What is the main objective of your project?
**Answer**:  
The primary objective of this project is to provide organizations with a proactive, data-driven workforce intelligence platform. Instead of relying on traditional annual appraisals or reactive exit interviews after an employee has already resigned, our system gathers monthly feedback, tracks satisfaction trends, predicts attrition risk using a trained Machine Learning model, and equips HR with an actionable Retention Action Center to conduct timely interventions.

---

### Q2: What are the three primary user roles in your application, and how do they differ?
**Answer**:  
Our system enforces three distinct user personas:
1. **Employee**: Can securely log in, submit one survey per monthly cycle, and review their personal submission history. They are strictly restricted from viewing other employees' data or organizational attrition scores.
2. **HR Administrator**: Scoped strictly to their own company tenant (`companyCode`). They can onboard employees and co-HR administrators, view submitted feedback and satisfaction ratings, trigger ML pipeline training checks, and schedule retention meetings with at-risk team members.
3. **Platform Admin**: The super-administrator who oversees the entire platform. They review and approve new company registrations, inspect platform-wide user accounts across all tenants, and analyze platform growth metrics.

---

### Q3: Why did you choose a Decoupled (SPA + REST API) architecture instead of Server-Side Rendering (SSR like EJS or Next.js)?
**Answer**:  
A decoupled architecture using React 19 on the frontend and an Express REST API on the backend provides three major advantages:
1. **Separation of Concerns**: The frontend handles UI state, responsive views, and user interactions, while the backend focuses purely on business logic, security middleware, and database persistence.
2. **Reusability & Extensibility**: The Express API endpoints can easily serve future clients, such as a native mobile app or external enterprise webhooks, without rewriting backend controllers.
3. **Optimized User Experience**: React's client-side routing delivers near-instant page transitions without full-page browser reloads.

---

### Q4: How is Multi-Tenancy implemented in your application?
**Answer**:  
Multi-tenancy is implemented through logical data isolation using an indexed `companyCode` field:
- When a company registers, the backend generates a unique 6-character alphanumeric `companyCode`.
- Every employee and HR administrator created under that company has this `companyCode` stored on their user record.
- Every API endpoint accessed by an HR Admin extracts the verified `companyCode` from their authenticated JWT session and enforces query filters such as `{ companyCode: hr.companyCode }`.
- This ensures complete data privacy: HR Admin A cannot view or alter employees or survey feedback belonging to Company B.

---

### Q5: What happens when a new company registers on the platform?
**Answer**:  
When a company registers via the public `/register-company` route, its initial status is set to `'pending'` in the database. During this pending state, neither the primary HR administrator nor their employees are allowed to log into the application. The Platform Admin must first review the registration in the Platform Admin Company Management dashboard and approve it. Once approved, the company status changes to `'approved'`, and users can authenticate successfully.

---

## SECTION 2: FRONTEND & USER INTERFACE DESIGN

### Q6: What version of React and build tooling are you using?
**Answer**:  
We are using React 19.2.0 bundled with Vite 7.2.4. Vite provides native ES module serving during development for sub-second hot module replacement (HMR) and utilizes Rollup for optimized, tree-shaken production builds. Our full frontend production build compiles 2,006 modules cleanly in under 7 seconds.

---

### Q7: Why did you transition from modal popups to a full-page view for the Employee Feedback Explorer?
**Answer**:  
During initial user testing, opening extensive employee feedback inside a modal dialog led to vertical clipping and scrollbar contention on smaller laptop screens. Comprehensive qualitative feedback includes detailed supervisor evaluations, liked aspects, and suggested workplace improvements. Transitioning to a dedicated full-page component (`EmployeeDetailView`) provided an unclipped, clean reading experience with average rating badges, back navigation, and complete layout accessibility.

---

### Q8: How did you fix the recent issue where modal bottom content was hidden during employee creation?
**Answer**:  
The modal dialog had two interacting constraints:
1. When opened, `document.body.style.overflow = "hidden"` locked document scrolling to prevent double scrollbars.
2. The modal overlay lacked an explicit `overflow-y-auto` property, and the inner container had a rigid viewport height calculation.
To fix this, we added `overflow-y-auto` and `min-h-full` to the modal backdrop overlay, assigned a flexible `max-h-[85vh]` with `my-auto` centering to the modal container, and applied a dedicated `.custom-scrollbar` utility to the form body. This guarantees that all form fields and the submit button remain fully visible and scrollable across all screen heights.

---

### Q9: What styling framework is used, and how are icons rendered?
**Answer**:  
We use Tailwind CSS (v4.3.3) for modern utility-first responsive styling and Lucide React (v1.46.0) for accessible, lightweight vector SVG iconography.

---

## SECTION 3: BACKEND, API & DATABASE DESIGN

### Q10: How do you prevent an employee from submitting multiple feedback surveys in the same month?
**Answer**:  
Cycle enforcement is guaranteed at two levels:
1. **Application Logic**: When an employee attempts to submit feedback, `POST /predict` computes the current monthly cycle tag (e.g., `"2026-10"`) and queries the `feedback` collection for an existing submission by that `employeeId` during that period. If found, it returns HTTP 400.
2. **Database Schema Constraint**: In `backend/models/feedback.js`, we established a compound unique index:
   ```javascript
   attritionSchema.index({ employeeId: 1, feedbackPeriod: 1 }, { unique: true });
   ```
   This ensures that even if concurrent race conditions occur, the MongoDB storage engine rejects duplicate submissions with an E11000 duplicate key error.

---

### Q11: Explain your authentication workflow from login to accessing a protected route.
**Answer**:  
1. The user sends their email and password to `POST /login`.
2. The backend queries `User.findOne({ email })`. If found, `bcrypt.compare()` verifies the password against the stored bcrypt hash.
3. For HR and employees, the backend verifies that the associated company's status is `'approved'`.
4. Express generates a signed JWT containing `{ userId, email, role, companyCode }` signed with `JWT_SECRET`.
5. The frontend stores this token and passes it in the `Authorization: Bearer <token>` header on subsequent requests.
6. The `isLogedIn` middleware verifies the token signature, and `requireRole(role)` validates that the database user possesses the required permissions before allowing the controller to execute.

---

### Q12: Why do you query the MongoDB database in `requireRole()` instead of relying solely on the JWT payload?
**Answer**:  
Relying solely on JWT claims can lead to security vulnerabilities. If a user's role is demoted, their account suspended, or their company revoked in the database after their JWT was issued, a purely stateless token check would still grant them access until the token expires. By performing `await User.findById(req.user.userId)` inside `requireRole()`, we verify that the user's live database record is active and authorized.

---

### Q13: How are passwords secured in your database?
**Answer**:  
Passwords are encrypted using `bcryptjs` with 10 salt rounds before being persisted in MongoDB. Bcrypt incorporates a unique random cryptographic salt into each hash, preventing rainbow table attacks. When querying user profiles (such as in the Platform Admin user list or employee directory), controllers explicitly execute `.select("-password")` so password hashes are never serialized over the network.

---

### Q14: What email service does your project use, and why was it chosen?
**Answer**:  
Our project integrates **EmailJS** (`backend/services/emailService.js` and `src/utils/emailService.js`). In academic, local development, and corporate network environments, traditional SMTP ports (like 25, 465, or 587) are frequently blocked by firewalls or require complex OAuth2 configurations. EmailJS uses an HTTPS REST API (`https://api.emailjs.com/api/v1.0/email/send`) with corporate certificate fallback (`rejectUnauthorized: false`), guaranteeing reliable delivery for welcome emails and monthly feedback cycle reminders.

---

## SECTION 4: MACHINE LEARNING & PREDICTIVE ANALYTICS

### Q15: What machine learning algorithm is used, and what type of problem does it solve?
**Answer**:  
The model implements a **Random Forest Classifier** (`RandomForestClassifier`) from the `scikit-learn` library. It solves a **Supervised Binary Classification** problem where the goal is to predict whether an employee will voluntarily leave the company (`Attrition = 1 / "Yes"`) or remain (`Attrition = 0 / "No"`).

---

### Q16: What dataset was used to train the model?
**Answer**:  
The model is trained on the benchmark **IBM HR Employee Attrition and Performance dataset** (`WA_Fn-UseC_-HR-Employee-Attrition.csv`). The dataset contains 1,470 validated employee records with 35 original attributes detailing demographic, compensation, tenure, and satisfaction metrics.

---

### Q17: Which specific features are selected for training, and why?
**Answer**:  
Our model extracts four key satisfaction features:
1. `JobSatisfaction` (Rating from 1 to 4)
2. `EnvironmentSatisfaction` (Rating from 1 to 4)
3. `WorkLifeBalance` (Rating from 1 to 4)
4. `RelationshipSatisfaction` (Rating from 1 to 4)

**Rationale**: Many features in the IBM dataset (such as hourly rate, distance from home, or total working years) are static administrative fields that employees do not self-report each month. We chose these four dimensions because they map directly to monthly employee survey feedback, allowing our live application to feed real survey responses directly into the prediction pipeline.

---

### Q18: What are the exact empirical evaluation metrics of your trained model?
**Answer**:  
Our model was evaluated on a 25% stratified held-out test set consisting of 368 employee samples:
- **Accuracy**: `67.39%` (0.6739)
- **Precision**: `22.02%` (0.2202)
- **Recall**: `40.68%` (0.4068)
- **F1-Score**: `0.2857` (0.2857)
- **ROC-AUC**: `0.6179` (0.6179)
- **Confusion Matrix**:
  - True Negatives (TN): `224` (Retained employees correctly predicted)
  - False Positives (FP): `85` (Retained employees flagged as at-risk)
  - False Negatives (FN): `35` (Turnover cases missed)
  - True Positives (TP): `24` (Turnover cases correctly flagged)

---

### Q19: Why is Precision only 22.02% while Recall is 40.68%? Is this an intentional design decision?
**Answer**:  
Yes, this is an intentional and scientifically sound machine learning design choice.  
The dataset suffers from severe class imbalance: only 16.1% of employees actually leave (237 out of 1,470). If a classifier simply predicted "No Attrition" for every single person, it would achieve 83.9% accuracy but would be completely useless in practice because its recall would be 0%!  
To prevent this, we configured `class_weight="balanced"` in our Random Forest. This instructs the algorithm to penalize False Negatives heavily. In corporate HR, a False Negative (missing an employee who is about to quit) costs thousands of dollars, whereas a False Positive (checking in on an employee who turns out to be happy) has virtually zero negative cost. Therefore, we deliberately prioritized Recall over Precision.

---

### Q20: How does the Node.js backend communicate with the Python ML scripts?
**Answer**:  
Node.js interacts with Python using native asynchronous child process execution (`child_process.spawn()` in `backend/services/mlService.js`). When an inference request is made, Node spawns:
```bash
python backend/ml/predict.py '<json_features_payload>'
```
The Python script loads the pre-trained serialized model from `backend/ml/artifacts/attrition_model_1.0.0.joblib`, runs `predict_proba()`, formats the resulting risk probability into a JSON string, and writes it to standard output (`stdout`). Node.js parses the stream and returns the structured result in approximately 45 milliseconds without requiring a separate web server.

---

### Q21: What is the difference between your 'Survey Risk Level' and your 'ML Prediction'?
**Answer**:  
This is a critical distinction in our architecture:
1. **Descriptive Survey Risk Level**: A heuristic indicator computed directly from the employee's current survey ratings (e.g., if average ratings fall below 2.5, the employee is flagged as `NEEDS_ATTENTION` or `HIGH_RISK`). It is descriptive and transparent.
2. **Supervised ML Prediction**: A statistical probability score generated by our trained Random Forest classifier based on how the employee's 4 satisfaction dimensions compare to historical turnover patterns in the 1,470-record benchmark dataset.

---

### Q22: Why doesn't the model retrain on the live company survey data immediately?
**Answer**:  
Supervised machine learning requires labeled data with ground truth outcomes (`Attrition: True / False`). When current employees submit monthly surveys, they are actively employed at the company; their future retention or resignation outcome is not yet known. Until employees eventually depart over an extended period (6 to 12 months) and their records are updated with actual turnover dates, new surveys lack the target label necessary for supervised training. Therefore, our system uses the benchmark model for inference while accumulating live survey data for future longitudinal retraining.

---

## SECTION 5: HR WORKFLOWS & RETENTION ACTION CENTER

### Q23: What is the Retention Action Center, and why was it created?
**Answer**:  
The Retention Action Center is a dedicated dashboard section designed to turn predictive analytics into concrete human interventions. Simply showing that an employee is at high risk of leaving does not solve the problem. The Retention Action Center displays at-risk employees, allows HR to assign a dedicated HR representative, set proposed meeting dates and times, record agreed-upon retention action plans, and track follow-up progress across status states (`Pending`, `In Progress`, `Completed`).

---

### Q24: How does the WhatsApp integration work in the Retention Action Center?
**Answer**:  
When HR reviews an at-risk employee, they can click **"Contact via WhatsApp"**. The frontend generates a pre-formatted WhatsApp deep link:
```
https://wa.me/<employee_phone>?text=<encoded_meeting_invitation>
```
This opens WhatsApp with a professional, respectful message inviting the employee to a confidential feedback and career support discussion. It avoids email clutter and provides an immediate, modern communication channel.

---

### Q25: What is the function of the "Run ML Pipeline Check" button on the HR Dashboard?
**Answer**:  
The "Run ML Pipeline Check" button triggers an administrative endpoint (`POST /api/hr/analytics/train` and `refreshCompanyAnalytics`). It executes the Python training and verification script (`train_model.py`), validates that the scikit-learn dependency and dataset are intact, updates the serialized `.joblib` model artifact, refreshes test metrics in the database, and updates the dashboard status indicator to confirm model readiness.

---

## SECTION 6: PLATFORM ADMIN & GOVERNANCE

### Q26: What are the three core modules of the Platform Admin interface?
**Answer**:  
1. **Company Management**: View all registered companies, inspect registration dates, company codes, and employee counts, and manage onboarding status (Approve, Reject, Revoke, Re-approve).
2. **User & Admin Management**: A centralized user directory displaying all users across the platform, categorizing them by role badges, with search and account detail modals.
3. **Platform Analytics**: Aggregate platform-wide statistics showing total registered companies, approval ratios, total users, and role distribution breakdowns.

---

### Q27: Does the Platform Admin have access to confidential employee feedback?
**Answer**:  
No. In accordance with enterprise privacy and multi-tenant security principles, Platform Admin permissions are restricted to platform governance (approving companies and managing accounts). Qualitative survey feedback, supervisor ratings, and individual employee responses are strictly restricted to the authorized HR Administrators of that specific company.

---

## SECTION 7: TESTING, CHALLENGES & VIVA DEFENSE

### Q28: How did you test your application?
**Answer**:  
We conducted testing across four key areas:
1. **Authentication & RBAC Testing**: Tested valid/invalid logins, verified token expiration, and attempted cross-role URL navigation to ensure unauthorized requests return 401 or 403.
2. **Tenant Isolation Testing**: Created two distinct companies (Company A and Company B); verified that HR Admin A cannot query, view, or modify Company B's employees or feedback.
3. **Cycle Lock Testing**: Attempted duplicate feedback submissions within the same month to verify that the compound unique index rejects the second entry.
4. **Build & Script Testing**: Verified frontend compilation using `vite build` (0 errors) and executed `python train_model.py` and `predict.py` directly from PowerShell to verify JSON output and artifact creation.

---

### Q29: What was the biggest technical challenge you faced during this project?
**Answer**:  
The most significant technical challenge was bridging the asynchronous Node.js JavaScript environment with the Python Machine Learning pipeline cleanly without introducing the resource overhead and failure points of a second background HTTP server. By architecting a JSON-over-stdio CLI bridge via `child_process.spawn()`, we achieved fast, reliable inference in under 50ms while keeping deployment lightweight and self-contained.

---

### Q30: What are the main limitations of your current implementation?
**Answer**:  
1. **Qualitative Text Not Machine-Analyzed**: While quantitative ratings feed directly into the ML classifier, written comments (`likedMost`, `improvement`) are currently reviewed manually by HR rather than through an automated NLP sentiment model.
2. **Dataset Domain Specificity**: The model is trained on the standard IBM benchmark dataset; while highly correlated with general workplace satisfaction, it may not reflect culture-specific nuances of every industry.
3. **WhatsApp Link vs. Cloud API**: WhatsApp invitations use direct `wa.me` browser deep links rather than automated backend WhatsApp Business API webhooks.

---

### Q31: If you had another 3 months to work on this project, what would you add?
**Answer**:  
1. **Natural Language Processing**: Implement a Hugging Face RoBERTa transformer to perform sentiment scoring and topic modeling on employee comments to flag burnout keywords automatically.
2. **Survival Analysis**: Transition from simple binary classification ("Will they leave?") to time-to-event survival analysis (estimating probability of departure within 3, 6, or 12 months).
3. **Calendar Integration**: Connect the Retention Action Center directly with the Google Calendar and Outlook APIs to auto-schedule meeting slots.
4. **Enterprise Single Sign-On (SSO)**: Add SAML 2.0 and OAuth2 (Google/Microsoft Workspace) logins.

---

### Q32: Why did you use MongoDB instead of a Relational Database like PostgreSQL?
**Answer**:  
MongoDB was selected because:
1. **Document Flexibility**: Employee survey structures frequently evolve across quarters (adding new optional feedback prompts or rating categories); MongoDB's JSON document model accommodates these changes without complex database schema migrations.
2. **Nested Analytics Objects**: Models like `EmployeeAnalytics` store complex nested metrics, trend summaries, and model inference objects that map naturally to BSON documents.
3. **Development Agility with Node.js**: JSON data flows seamlessly from React to Express to MongoDB without object-relational mapping impedance mismatch.

---

### Q33: How does your system handle missing or incomplete feedback submissions?
**Answer**:  
In the employee feedback schema, core rating fields (`jobSatisfaction`, `workEnvironment`, `workLifeBalance`, `growth`, `manager`) have `required: true`. If an employee omits any rating, Mongoose schema validation fails immediately with a descriptive HTTP 400 error. For optional qualitative fields (`likedMost`, `improvement`, `comments`), the schema assigns a default empty string `""`, ensuring that the record remains valid for querying and review.

---

### Q34: What is the significance of the ROC-AUC score of 0.6179 in your model?
**Answer**:  
ROC-AUC (Receiver Operating Characteristic — Area Under Curve) measures the model's ability to distinguish between employees who leave and those who stay across all possible classification probability thresholds. A score of 0.5 represents a random coin flip, while 1.0 represents a perfect classifier. Our score of 0.6179 demonstrates that, even using only 4 subjective self-reported satisfaction dimensions, the model possesses genuine discriminative signal superior to random guessing.

---

### Q35: What is the single most important lesson you learned while building this project?
**Answer**:  
The most important lesson was that **machine learning is only as valuable as the software workflow that surrounds it**. A predictive model running in a standalone Jupyter notebook creates zero business value. By building an entire multi-tenant web application around the model — with secure authentication, cycle enforcement, email reminders, and a human-centered Retention Action Center — we transformed an abstract statistical algorithm into a real-world tool that helps organizations care for and retain their people.
