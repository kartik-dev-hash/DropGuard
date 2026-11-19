
"""Run inference using a trained employee attrition model."""

import sys
import json
import os

try:
    import joblib
    import numpy as np
except ImportError:
    print(json.dumps({
        "success": False,
        "message": "Install joblib, numpy, and scikit-learn."
    }))
    sys.exit(1)


FEATURE_NAMES = [
    "academicEngagement",
    "supportSatisfaction",
    "stressManagement",
    "belongingness",
]


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "success": False,
            "message": "Inference payload JSON argument required."
        }))
        sys.exit(1)

    try:
        data = json.loads(sys.argv[1])
        artifact_path = data.get("artifactPath")
        features = data.get("features")

        if not artifact_path or not os.path.isfile(artifact_path):
            raise ValueError("Trained model artifact was not found.")

        if not isinstance(features, dict):
            raise ValueError("Features must be provided as a JSON object.")

        # Extract academic features with legacy fallback support
        academic_engagement = features.get("academicEngagement", features.get("jobSatisfaction"))
        support_satisfaction = features.get("supportSatisfaction", features.get("environmentSatisfaction", features.get("workEnvironment")))
        stress_management = features.get("stressManagement", features.get("workLifeBalance"))
        belongingness = features.get("belongingness", features.get("relationshipSatisfaction", features.get("growth")))

        missing = []
        if academic_engagement is None:
            missing.append("academicEngagement")
        if support_satisfaction is None:
            missing.append("supportSatisfaction")
        if stress_management is None:
            missing.append("stressManagement")
        if belongingness is None:
            missing.append("belongingness")

        if missing:
            raise ValueError(
                "Missing required features: " + ", ".join(missing)
            )

        # Scale or clamp to model's expected 1 to 4 range
        values = [
            float(max(1, min(4, round(float(academic_engagement))))),
            float(max(1, min(4, round(float(support_satisfaction))))),
            float(max(1, min(4, round(float(stress_management))))),
            float(max(1, min(4, round(float(belongingness))))),
        ]

        artifact = joblib.load(artifact_path)

        # The current training script saves a dictionary, not a bare model.
        if not isinstance(artifact, dict) or "model" not in artifact:
            raise ValueError(
                "Unexpected artifact format. Retrain using the current "
                "train_model.py script."
            )

        clf = artifact["model"]
        saved_features = artifact.get("features", FEATURE_NAMES)

        if saved_features != FEATURE_NAMES and saved_features != [
            "JobSatisfaction", "EnvironmentSatisfaction", "WorkLifeBalance", "RelationshipSatisfaction"
        ]:
            raise ValueError("Model feature order does not match inference.")

        X = np.array([values], dtype=float)
        pred = int(clf.predict(X)[0])

        probability = None
        if hasattr(clf, "predict_proba"):
            probabilities = clf.predict_proba(X)[0]
            classes = list(clf.classes_)

            if 1 in classes:
                probability = float(probabilities[classes.index(1)])

        print(json.dumps({
            "success": True,
            "prediction": "Yes" if pred == 1 else "No",
            "probability": (
                round(probability, 4)
                if probability is not None else None
            ),
            "riskCategory": (
                "HIGH_RISK"
                if probability is not None and probability >= 0.5
                else "LOW_RISK"
                if probability is not None
                else "UNKNOWN"
            ),
        }))

    except Exception as error:
        print(json.dumps({
            "success": False,
            "message": str(error)
        }))
        sys.exit(1)


if __name__ == "__main__":
    main()