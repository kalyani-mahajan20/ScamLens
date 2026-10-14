import re


SIGNAL_PATTERNS = {

    # ============================================================
    # 1. URGENCY / PRESSURE
    # ============================================================

    "urgency": [
        "urgent",
        "urgently",
        "immediately",
        "act now",
        "right now",
        "within 24 hours",
        "within 48 hours",
        "hurry",
        "as soon as possible",
        "today",
        "now",
        "limited time",
        "last chance",
        "deadline",
        "expires today",
        "respond immediately",
        "before it expires",
        "without delay"
    ],

    # ============================================================
    # 2. THREAT / FEAR
    # ============================================================

    "threat": [
        "account will be blocked",
        "account will be suspended",
        "account suspended",
        "has been suspended",
        "suspended",
        "blocked",
        "will be blocked",
        "legal action",
        "police complaint",
        "police case",
        "penalty",
        "fine",
        "will be terminated",
        "terminate",
        "avoid legal action",
        "court action",
        "arrest",
        "prosecution",
        "service will be stopped",
        "account will be closed",
        "further action",
        "held by customs",
        "customs has held",
        "complaint registered"
    ],

    # ============================================================
    # 3. FINANCIAL REQUEST
    # ============================================================

    "financial_request": [
        "send money",
        "transfer money",
        "transfer funds",
        "make a payment",
        "payment",
        "pay now",
        "pay immediately",
        "processing fee",
        "pay a small fee",
        "registration fee",
        "required fee",
        "delivery fee",
        "small delivery fee",
        "bank details",
        "account details",
        "card details",
        "payment details",
        "credit card",
        "debit card",
        "upi",
        "upi payment",
        "upi pin",
        "cash prize",
        "money",
        "refund fee",
        "transaction",
        "deposit",
        "wire transfer",
        "pay rs",
        "transfer rs",
        "send rs",
        "guaranteed returns",
        "guaranteed profit",
        "double returns"
    ],

    # ============================================================
    # 4. CREDENTIAL / SENSITIVE INFORMATION REQUEST
    # ============================================================

    "credential_request": [
        "password",
        "otp",
        "one time password",
        "one-time password",
        "pin",
        "cvv",
        "login details",
        "login credentials",
        "verification code",
        "security code",
        "send your otp",
        "send your pin",
        "enter your otp",
        "enter your pin",
        "enter your cvv",
        "share your password",
        "share your otp",
        "verify your identity",
        "card details",
        "bank details",
        "account details",
        "payment details",
        "verification details"
    ],

    # ============================================================
    # 5. REWARD / PRIZE
    # ============================================================

    "reward": [
        "you won",
        "you have won",
        "winner",
        "lottery winner",
        "prize",
        "reward",
        "lottery",
        "cashback",
        "congratulations",
        "cash prize",
        "won a cash prize",
        "gift voucher",
        "free gift",
        "bonus",
        "lucky winner",
        "claim your prize",
        "claim your reward"
    ],

    # ============================================================
    # 6. AUTHORITY / ORGANIZATION IMPERSONATION
    # ============================================================

    "authority_impersonation": [
        "bank",
        "your bank",
        "government",
        "government authorities",
        "income tax",
        "income tax department",
        "police",
        "customs",
        "customs department",
        "official department",
        "customer support",
        "bank representative",
        "bank officer",
        "government officer",
        "tax department",
        "security team",
        "police complaint",
        "delivery company",
        "courier",
        "loan department"
    ],

    # ============================================================
    # 7. SUSPICIOUS LINK / PHISHING
    # ============================================================

    "suspicious_link": [
        "http://",
        "https://",
        "www.",
        "click here",
        "click the link",
        "clicking this link",
        "click this link",
        "open this link",
        "open the link",
        "verify here",
        "verify your account",
        "verify now",
        "login here",
        "tap here",
        "visit this link",
        "link to verify",
        "link to confirm"
    ],

    # ============================================================
    # 8. INVESTMENT / FINANCIAL OPPORTUNITY SCAM
    # ============================================================

    "investment_scam": [
        "investment opportunity",
        "limited time investment",
        "invest now",
        "guaranteed returns",
        "guaranteed return",
        "guaranteed profit",
        "guaranteed profits",
        "double returns",
        "double your money",
        "earn guaranteed",
        "premium investment",
        "investment account",
        "activate your investment",
        "high returns",
        "quick returns"
    ],

    # ============================================================
    # 9. JOB / EMPLOYMENT SCAM
    # ============================================================

    "job_scam": [
        "work from home job",
        "work from home",
        "job opportunity",
        "job offer",
        "selected for a job",
        "selected for the job",
        "employee account",
        "registration fee",
        "job registration",
        "employment opportunity",
        "earn money from home"
    ],

    # ============================================================
    # 10. DELIVERY / PARCEL SCAM
    # ============================================================

    "delivery_scam": [
        "parcel could not be delivered",
        "parcel could not",
        "package is waiting",
        "delivery failed",
        "delivery is on hold",
        "courier delivery",
        "parcel delivery",
        "reschedule your shipment",
        "reschedule delivery",
        "incorrect address",
        "address verification",
        "delivery notification",
        "parcel is on hold",
        "package is on hold"
    ],

    # ============================================================
    # 11. LOAN / REFUND SCAM
    # ============================================================

    "loan_refund_scam": [
        "loan application is approved",
        "loan approved",
        "receive the loan",
        "loan amount",
        "loan processing fee",
        "your refund is ready",
        "refund is ready",
        "receive the refund",
        "refund immediately",
        "refund payment"
    ]
}


def detect_signals(text: str) -> dict[str, list[str]]:
    """
    Detect predefined social-engineering signals
    from the normalized input text.
    """

    detected = {}

    for category, patterns in SIGNAL_PATTERNS.items():

        matches = []

        for pattern in patterns:
            if pattern in text:
                matches.append(pattern)

        if matches:
            detected[category] = matches

    # ------------------------------------------------------------
    # Detect actual URLs separately
    # ------------------------------------------------------------

    urls = re.findall(
        r"https?://[^\s]+|www\.[^\s]+",
        text,
        flags=re.IGNORECASE
    )

    if urls:
        detected["url_detected"] = urls

    return detected