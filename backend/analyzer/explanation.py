SIGNAL_LABELS = {
    "urgency": "Urgency or pressure",
    "threat": "Threat or fear-based language",
    "financial_request": "Financial or payment-related request",
    "credential_request": "Request for sensitive credentials",
    "reward": "Reward or prize-related language",
    "authority_impersonation": "Possible authority or organization impersonation",
    "suspicious_link": "Suspicious link-related language",
    "url_detected": "URL detected in the message",
    "investment_scam": "Investment or guaranteed-return language",
    "job_scam": "Potential job or employment scam indicators",
    "delivery_scam": "Potential delivery or parcel scam indicators",
    "loan_refund_scam": "Potential loan or refund scam indicators"
}


def generate_explanation(signals: dict[str, list[str]]) -> str:

    if not signals:
        return (
            "No major predefined social-engineering warning signals "
            "were detected in the submitted message."
        )

    reasons = []

    for category in signals:
        label = SIGNAL_LABELS.get(category, category)
        reasons.append(label)

    if len(reasons) == 1:
        return (
            "The message contains the following warning indicator: "
            + reasons[0]
            + "."
        )

    return (
        "The message contains the following warning indicators: "
        + ", ".join(reasons)
        + "."
    )