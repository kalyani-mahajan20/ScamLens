import re

from evaluation.dataset import EVALUATION_DATASET
from analyzer.preprocessing import preprocess_text


# ============================================================
# SIMPLE KEYWORD-COUNT BASELINE
# ============================================================

BASELINE_KEYWORDS = [
    "urgent",
    "immediately",
    "now",
    "blocked",
    "suspended",
    "penalty",
    "fine",
    "otp",
    "password",
    "pin",
    "cvv",
    "bank details",
    "card details",
    "payment",
    "pay",
    "fee",
    "money",
    "transfer",
    "prize",
    "reward",
    "lottery",
    "winner",
    "cashback",
    "click here",
    "click the link",
    "verify",
    "account",
    "investment",
    "guaranteed returns",
    "job",
    "registration fee",
    "parcel",
    "delivery",
    "loan",
    "refund",
    "police",
    "customs",
    "government"
]


def baseline_predict(message: str):
    """
    Simple baseline method.

    Counts suspicious keywords and converts
    the count into a basic risk score.
    """

    text = preprocess_text(message)

    matched_keywords = []

    for keyword in BASELINE_KEYWORDS:
        if keyword in text:
            matched_keywords.append(keyword)

    keyword_count = len(matched_keywords)

    # Simple score:
    # Each suspicious keyword contributes 10 points.
    score = min(keyword_count * 10, 100)

    if score >= 40:
        prediction = "SCAM"
    else:
        prediction = "SAFE"

    return prediction, score, matched_keywords


def calculate_metrics(true_labels, predicted_labels):

    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    for actual, predicted in zip(true_labels, predicted_labels):

        if actual == "SCAM" and predicted == "SCAM":
            true_positive += 1

        elif actual == "SAFE" and predicted == "SAFE":
            true_negative += 1

        elif actual == "SAFE" and predicted == "SCAM":
            false_positive += 1

        elif actual == "SCAM" and predicted == "SAFE":
            false_negative += 1

    total = len(true_labels)

    accuracy = (
        (true_positive + true_negative) / total
        if total > 0
        else 0
    )

    precision = (
        true_positive / (true_positive + false_positive)
        if (true_positive + false_positive) > 0
        else 0
    )

    recall = (
        true_positive / (true_positive + false_negative)
        if (true_positive + false_negative) > 0
        else 0
    )

    f1_score = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) > 0
        else 0
    )

    return {
        "true_positive": true_positive,
        "true_negative": true_negative,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score
    }


def main():

    true_labels = []
    predicted_labels = []

    print("=" * 75)
    print("SCAMLENS — BASELINE COMPARISON")
    print("=" * 75)

    print(f"Total evaluation samples: {len(EVALUATION_DATASET)}")

    for item in EVALUATION_DATASET:

        message = item["message"]
        actual = item["actual_label"]

        predicted, score, matched_keywords = baseline_predict(message)

        true_labels.append(actual)
        predicted_labels.append(predicted)

        status = "PASS" if actual == predicted else "FAIL"

        print()
        print("-" * 75)
        print("Message   :", message)
        print("Actual    :", actual)
        print("Predicted :", predicted)
        print("Risk Score:", f"{score}/100")
        print("Keywords  :", ", ".join(matched_keywords))
        print("Status    :", status)

    metrics = calculate_metrics(
        true_labels,
        predicted_labels
    )

    print()
    print("=" * 75)
    print("BASELINE CONFUSION MATRIX")
    print("=" * 75)

    print(f"True Positives : {metrics['true_positive']}")
    print(f"True Negatives : {metrics['true_negative']}")
    print(f"False Positives: {metrics['false_positive']}")
    print(f"False Negatives: {metrics['false_negative']}")

    print()
    print("=" * 75)
    print("BASELINE METRICS")
    print("=" * 75)

    print(f"Accuracy :  {metrics['accuracy']:.2%}")
    print(f"Precision:  {metrics['precision']:.2%}")
    print(f"Recall   :  {metrics['recall']:.2%}")
    print(f"F1 Score :  {metrics['f1_score']:.2%}")

    print()
    print("=" * 75)
    print("BASELINE INTERPRETATION")
    print("=" * 75)

    print(
        "The baseline uses a simple suspicious-keyword count "
        "without category-specific weights or contextual combinations."
    )

    print(
        "ScamLens improves upon this baseline by using categorized "
        "signals and contextual risk scoring."
    )

    print("=" * 75)


if __name__ == "__main__":
    main()