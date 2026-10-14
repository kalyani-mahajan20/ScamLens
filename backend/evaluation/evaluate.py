from analyzer.preprocessing import preprocess_text
from analyzer.signals import detect_signals
from analyzer.risk_engine import calculate_risk_score, get_risk_level

from evaluation.dataset import EVALUATION_DATASET


def predict_message(message: str) -> tuple[str, int, str]:
    """
    Run a message through the same ScamLens analysis pipeline
    and return:
        prediction, risk score, risk level
    """

    cleaned_text = preprocess_text(message)
    signals = detect_signals(cleaned_text)

    score = calculate_risk_score(signals)
    risk_level = get_risk_level(score)

    if risk_level in ["MEDIUM", "HIGH"]:
        prediction = "SCAM"
    else:
        prediction = "SAFE"

    return prediction, score, risk_level


def calculate_metrics(true_labels: list[str], predicted_labels: list[str]):
    """
    Calculate confusion matrix and standard classification metrics.
    """

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

    scam_count = 0
    safe_count = 0

    print("=" * 75)
    print("SCAMLENS — PROTOTYPE EVALUATION")
    print("=" * 75)

    print(f"Total evaluation samples: {len(EVALUATION_DATASET)}")

    for item in EVALUATION_DATASET:

        message = item["message"]
        actual = item["actual_label"]

        predicted, score, risk_level = predict_message(message)

        true_labels.append(actual)
        predicted_labels.append(predicted)

        if actual == "SCAM":
            scam_count += 1
        else:
            safe_count += 1

        status = "PASS" if actual == predicted else "FAIL"

        print()
        print("-" * 75)
        print("Message   :", message)
        print("Actual    :", actual)
        print("Predicted :", predicted)
        print("Risk Score:", f"{score}/100")
        print("Risk Level:", risk_level)
        print("Status    :", status)

    metrics = calculate_metrics(
        true_labels,
        predicted_labels
    )

    print()
    print("=" * 75)
    print("DATASET SUMMARY")
    print("=" * 75)

    print(f"Total Samples : {len(EVALUATION_DATASET)}")
    print(f"SCAM Samples  : {scam_count}")
    print(f"SAFE Samples  : {safe_count}")

    print()
    print("=" * 75)
    print("CONFUSION MATRIX")
    print("=" * 75)

    print(f"True Positives : {metrics['true_positive']}")
    print(f"True Negatives : {metrics['true_negative']}")
    print(f"False Positives: {metrics['false_positive']}")
    print(f"False Negatives: {metrics['false_negative']}")

    print()
    print("=" * 75)
    print("EVALUATION METRICS")
    print("=" * 75)

    print(f"Accuracy :  {metrics['accuracy']:.2%}")
    print(f"Precision:  {metrics['precision']:.2%}")
    print(f"Recall   :  {metrics['recall']:.2%}")
    print(f"F1 Score :  {metrics['f1_score']:.2%}")

    print()
    print("=" * 75)
    print("INTERPRETATION")
    print("=" * 75)

    print(
        "Accuracy measures the proportion of correctly classified messages."
    )

    print(
        "Precision measures how many messages predicted as SCAM were actually SCAM."
    )

    print(
        "Recall measures how many actual SCAM messages were successfully detected."
    )

    print(
        "F1 Score provides a balance between precision and recall."
    )

    print()
    print(
        "Note: This is a small prototype evaluation dataset. "
        "The results should not be interpreted as real-world accuracy."
    )

    print("=" * 75)


if __name__ == "__main__":
    main()