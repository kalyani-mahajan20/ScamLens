RECOMMENDATIONS = {
    "urgency": (
        "Do not make rushed decisions. "
        "Take time to verify the request independently."
    ),

    "threat": (
        "Do not respond to threats immediately. "
        "Contact the organization through an official channel."
    ),

    "financial_request": (
        "Do not transfer money or make payments until "
        "the request is independently verified."
    ),

    "credential_request": (
        "Never share OTPs, passwords, PINs, CVV or "
        "verification codes with anyone."
    ),

    "reward": (
        "Be cautious of unexpected prizes, rewards or lottery claims. "
        "Do not pay fees to claim an unexpected reward."
    ),

    "authority_impersonation": (
        "Verify the sender through the organization's "
        "official website or verified contact number."
    ),

    "suspicious_link": (
        "Do not click suspicious links. "
        "Open the official website manually instead."
    ),

    "url_detected": (
        "Treat links in unexpected messages with caution "
        "and verify their destination independently."
    ),

    "investment_scam": (
        "Do not invest money based on guaranteed-profit or "
        "high-return claims. Verify the investment source independently."
    ),

    "job_scam": (
        "Do not pay registration or processing fees for an unexpected "
        "job opportunity. Verify the employer independently."
    ),

    "delivery_scam": (
        "Verify delivery or parcel claims through the official "
        "courier website or app instead of using links in the message."
    ),

    "loan_refund_scam": (
        "Do not pay upfront fees to receive a loan or refund. "
        "Verify the claim through the official organization."
    )
}


def generate_recommendations(
    signals: dict[str, list[str]]
) -> list[str]:

    recommendations = []

    for category in signals:
        recommendation = RECOMMENDATIONS.get(category)

        if recommendation and recommendation not in recommendations:
            recommendations.append(recommendation)

    if not recommendations:
        recommendations.append(
            "If the message requests sensitive information or action, "
            "verify it through an independent official source."
        )

    return recommendations