SIGNAL_WEIGHTS = {
    "urgency": 15,
    "threat": 20,
    "financial_request": 20,
    "credential_request": 20,
    "reward": 10,
    "authority_impersonation": 10,
    "suspicious_link": 15,
    "url_detected": 15,
    "investment_scam": 20,
    "job_scam": 15,
    "delivery_scam": 15,
    "loan_refund_scam": 15
}


def calculate_risk_score(signals: dict[str, list[str]]) -> int:
    """
    Calculate a transparent 0-100 scam risk score.

    The score combines:
    1. Base weights for detected signal categories.
    2. Contextual combinations between related signals.
    3. Strong multi-signal patterns.
    """

    score = 0
    signal_set = set(signals.keys())

    # ============================================================
    # 1. BASE SIGNAL SCORE
    # ============================================================

    for signal_category in signal_set:
        score += SIGNAL_WEIGHTS.get(signal_category, 0)

    # ============================================================
    # 2. GENERAL SOCIAL-ENGINEERING COMBINATIONS
    # ============================================================

    if "threat" in signal_set and "credential_request" in signal_set:
        score += 15

    if "urgency" in signal_set and "credential_request" in signal_set:
        score += 10

    if (
        "authority_impersonation" in signal_set
        and "credential_request" in signal_set
    ):
        score += 10

    if "threat" in signal_set and "financial_request" in signal_set:
        score += 10

    if "reward" in signal_set and "financial_request" in signal_set:
        score += 25

    if "reward" in signal_set and "urgency" in signal_set:
        score += 5

    if (
        "suspicious_link" in signal_set
        and "credential_request" in signal_set
    ):
        score += 10

    if (
        "suspicious_link" in signal_set
        and "authority_impersonation" in signal_set
    ):
        score += 5

    # ============================================================
    # 3. NEW CATEGORY-SPECIFIC CONTEXT
    # ============================================================

    # Delivery scams become significantly more suspicious
    # when they also request payment or sensitive information.
    if (
        "delivery_scam" in signal_set
        and "financial_request" in signal_set
    ):
        score += 20

    if (
        "delivery_scam" in signal_set
        and "suspicious_link" in signal_set
    ):
        score += 15

    if (
        "delivery_scam" in signal_set
        and "urgency" in signal_set
    ):
        score += 10

    # Job scams become stronger when a registration/payment
    # request is combined with the job opportunity.
    if (
        "job_scam" in signal_set
        and "financial_request" in signal_set
    ):
        score += 20

    if (
        "job_scam" in signal_set
        and "urgency" in signal_set
    ):
        score += 10

    # Investment scams are especially suspicious when money
    # transfer is combined with guaranteed/high returns.
    if (
        "investment_scam" in signal_set
        and "financial_request" in signal_set
    ):
        score += 25

    if (
        "investment_scam" in signal_set
        and "urgency" in signal_set
    ):
        score += 10

    # Loan/refund scams become stronger when payment or
    # urgency is involved.
    if (
        "loan_refund_scam" in signal_set
        and "financial_request" in signal_set
    ):
        score += 20

    if (
        "loan_refund_scam" in signal_set
        and "urgency" in signal_set
    ):
        score += 10

    # ============================================================
    # 4. STRONG MULTI-SIGNAL PATTERN
    # ============================================================

    strong_signals = {
        "threat",
        "credential_request",
        "financial_request",
        "suspicious_link",
        "investment_scam",
        "job_scam",
        "delivery_scam",
        "loan_refund_scam"
    }

    strong_signal_count = len(
        signal_set.intersection(strong_signals)
    )

    if strong_signal_count >= 3:
        score += 10

    # ============================================================
    # 5. FINAL SCORE NORMALIZATION
    # ============================================================

    return min(score, 100)


def get_risk_level(score: int) -> str:
    """
    Convert numerical score into a risk category.
    """

    if score >= 70:
        return "HIGH"

    if score >= 40:
        return "MEDIUM"

    return "LOW"