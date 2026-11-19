"""
Academic Report Content for:
STUDENTDROPOUT: STUDENT DROPOUT PREDICTION USING MACHINE LEARNING
Candidate: Prithvi Raghuwanshi
Institution: Prof. Ram Meghe Institute of Technology & Research (PRMIT&R), Badnera - Amravati
Guide: Dr. Kalyani H. Deshmukh | HOD: Dr. M. A. Pund
Academic Year: 2026-2027
"""

# ======================================================================
# FRONT MATTER DATA
# ======================================================================

TITLE = "STUDENTDROPOUT: STUDENT DROPOUT PREDICTION USING MACHINE LEARNING"
SUBTITLE = "A Machine Learning-Driven Multi-Tenant Higher Education Retention and Support Intervention Scheduling Platform"
STUDENT_NAME = "Kartik.N.Raghuwanshi"
GUIDE_NAME = "Dr. Kalyani H. Deshmukh"
GUIDE_TITLE = "Associate Professor, Department of Computer Science & Engineering"
HOD_NAME = "Dr. M. A. Pund"
HOD_TITLE = "Head of Department, Department of Computer Science & Engineering"
COLLEGE_NAME = "Prof. Ram Meghe Institute of Technology & Research"
COLLEGE_LOCATION = "Badnera - Amravati (M.S.) India - 444701"
COLLEGE_AFFILIATION = "An Autonomous Institute Affiliated to Sant Gadge Baba Amravati University, Amravati"
DEPARTMENT_NAME = "Department of Computer Science & Engineering (Honors)"
ACADEMIC_YEAR = "2026-2027"

CERTIFICATE_TEXT = f"""This is to certify that the project report entitled "{TITLE}" submitted by {STUDENT_NAME} in partial fulfillment of the requirements for the award of the Degree of Bachelor of Technology in Computer Science & Engineering (Honors) of Sant Gadge Baba Amravati University, Amravati, is a bonafide record of the work carried out under my guidance and supervision at {COLLEGE_NAME}, Badnera-Amravati during the academic year {ACADEMIC_YEAR}.

The project embodies original work and has not been submitted previously to this or any other university or institution for the award of any degree, diploma, or fellowship."""

ACKNOWLEDGEMENT_TEXT = f"""I take this opportunity to express my profound gratitude and deep reverence to my respected project guide, {GUIDE_NAME}, {DEPARTMENT_NAME}, for her invaluable guidance, intellectual stimulation, continuous encouragement, and constructive critique throughout the conceptualization, system modeling, machine learning implementation, and documentation of this B.Tech Honors project. Her penetrating insights into educational data mining, algorithmic rigor, and operational software systems have been instrumental in shaping this dissertation.

I express my sincere thanks to {HOD_NAME}, Head of the {DEPARTMENT_NAME}, for extending state-of-the-art computational laboratory facilities, administrative assistance, and an academically enriching environment that facilitated the seamless execution of this project.

I am deeply indebted to the respected Principal of {COLLEGE_NAME}, Badnera-Amravati, for his visionary institutional leadership and for providing world-class infrastructure that encourages applied engineering research and technological innovation.

I also convey my warm appreciation to all the esteemed faculty members and technical staff of the {DEPARTMENT_NAME} for their cooperation, direct and indirect assistance, and insightful suggestions during various project reviews.

Finally, I express my heartfelt devotion to my parents and family members for their unconditional sacrifices, moral strength, and spiritual backing, and to my fellow classmates and friends for their constant companionship, technical debates, and constructive feedback during this academic voyage."""

ABSTRACT_TEXT = f"""Student attrition and premature undergraduate departure represent critical structural challenges confronting global higher education institutions, directly undermining institutional sustainability, student economic mobility, and degree completion benchmarks. Conventional institutional retention approaches rely on retrospective academic failure metrics (such as semester grade reports and academic probation notices) that manifest only after psychological distress and academic disengagement have hardened to an irreversible degree. Furthermore, while predictive Educational Data Mining (EDM) models have achieved notable classification performance, an acute operational gap persists between predictive risk scoring and proactive advisory intervention. Administrative dashboards often inundate faculty counselors with unranked risk lists, causing cognitive overload and severe intervention latency.

To address these fundamental structural bottlenecks, this project designs, implements, and evaluates STUDENTDROPOUT (commercially branded as DropGuard): an end-to-end, multi-tenant academic retention and automated support intervention platform. The system couples a dual-algorithm soft-voting ensemble classifier—integrating Random Forest (180 randomized decision trees) and Gradient Boosted Decision Trees (150 sequential gradient-guided stumps)—with an automated academic advisory scheduling engine. The machine learning pipeline is developed and verified on an institutional cohort of 9,470 student records parameterized across four core psychometric and academic engagement dimensions: academic engagement (x1), support satisfaction (x2), stress and workload management (x3), and peer belongingness (x4), exhibiting a 32.20% positive dropout risk prevalence.

Operational workflows are governed by an actionable dual-criteria triage policy: students exhibiting acute single-dimension distress (min(xj) <= 2.5 on a 5-point scale) or generating composite ensemble predicted dropout probabilities p(x) >= 0.50 are triaged into structured intervention queues. For students flagged at acute risk (p(x) >= 0.80), the system triggers an automated calendar allocation engine that discovers conflict-free 30-minute counseling slots across seven business days, generates Google Calendar and Google Meet reservations, and delivers non-stigmatizing support invitations subject to human counselor review and a mandatory 7-day cooldown guard.

On an independent held-out test split of 2,368 students (stratified 25%), the soft-voting ensemble achieves an accuracy of 84.21% (outperforming the 67.80% majority-class baseline by 16.39 percentage points), an area under the ROC curve (ROC-AUC) of 89.25%, a precision of 79.39%, a recall of 68.77%, and an F1-score of 73.70%. In rigorous operational benchmarking across 50 simulated triage scenarios, the automated calendar scheduling engine recorded a 100.0% execution success rate with a mean dispatch latency of 1.38 seconds, zero calendar concurrency collisions, and 100% adherence to human counselor approval gates. The platform provides higher education administrators with an ethically sound, mathematically verified, and operationalized architecture that successfully bridges the prediction-to-action divide in student retention."""

print("Front matter text loaded.")
