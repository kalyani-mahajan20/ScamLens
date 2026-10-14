EVALUATION_DATASET = [

    # ============================================================
    # SCAM MESSAGES — BANK / OTP / CREDENTIALS
    # ============================================================

    {
        "message": "URGENT! Your bank account will be blocked today. Verify your account immediately by clicking this link and enter your OTP.",
        "actual_label": "SCAM"
    },
    {
        "message": "Your account has been suspended. Send your OTP and PIN immediately to restore access.",
        "actual_label": "SCAM"
    },
    {
        "message": "Your credit card verification is pending. Click here and enter your CVV and OTP.",
        "actual_label": "SCAM"
    },
    {
        "message": "Security alert! Your banking access will expire today. Verify your password and OTP now.",
        "actual_label": "SCAM"
    },
    {
        "message": "Your debit card has been temporarily blocked. Click the link to reactivate it and provide your verification code.",
        "actual_label": "SCAM"
    },

    # ============================================================
    # SCAM MESSAGES — PRIZE / LOTTERY / REWARD
    # ============================================================

    {
        "message": "Congratulations! You have won a cash prize of Rs 50,000. Pay a small processing fee to claim your reward.",
        "actual_label": "SCAM"
    },
    {
        "message": "You are selected as a lottery winner. Send your bank details to receive the prize.",
        "actual_label": "SCAM"
    },
    {
        "message": "Congratulations! You have won a lucky reward. Pay the registration fee immediately to receive your cash prize.",
        "actual_label": "SCAM"
    },
    {
        "message": "You are our lucky winner. Click here to claim your free gift voucher before the offer expires today.",
        "actual_label": "SCAM"
    },
    {
        "message": "Your mobile number has been selected for a special cashback reward. Pay the processing fee now to receive the money.",
        "actual_label": "SCAM"
    },

    # ============================================================
    # SCAM MESSAGES — GOVERNMENT / AUTHORITY IMPERSONATION
    # ============================================================

    {
        "message": "Government authorities have issued a penalty against you. Pay the amount immediately to avoid legal action.",
        "actual_label": "SCAM"
    },
    {
        "message": "Income Tax Department notice: your account will be blocked unless you complete verification immediately.",
        "actual_label": "SCAM"
    },
    {
        "message": "Police complaint registered against your number. Pay the fine now to avoid arrest and legal action.",
        "actual_label": "SCAM"
    },
    {
        "message": "Customs department has held your parcel. Pay the required fee immediately to avoid further action.",
        "actual_label": "SCAM"
    },
    {
        "message": "Government security team requires your bank details for urgent verification. Send them immediately.",
        "actual_label": "SCAM"
    },

    # ============================================================
    # SCAM MESSAGES — DELIVERY / PHISHING LINKS
    # ============================================================

    {
        "message": "Your parcel could not be delivered. Click this link and pay the small delivery fee to reschedule your shipment.",
        "actual_label": "SCAM"
    },
    {
        "message": "Your package is waiting for address verification. Open the link and enter your card details immediately.",
        "actual_label": "SCAM"
    },
    {
        "message": "Delivery failed because of an incorrect address. Click here and pay Rs 25 to receive your parcel today.",
        "actual_label": "SCAM"
    },
    {
        "message": "Your courier delivery is on hold. Verify your details at http://delivery-check.example.com immediately.",
        "actual_label": "SCAM"
    },
    {
        "message": "Important delivery notification! Click the link to confirm your address and enter your OTP.",
        "actual_label": "SCAM"
    },

    # ============================================================
    # SCAM MESSAGES — JOB / INVESTMENT / PAYMENT
    # ============================================================

    {
        "message": "You have been selected for a work from home job. Pay a registration fee today to activate your employee account.",
        "actual_label": "SCAM"
    },
    {
        "message": "Earn guaranteed returns on your investment. Transfer Rs 10,000 immediately to activate your premium investment account.",
        "actual_label": "SCAM"
    },
    {
        "message": "Your loan application is approved. Pay the processing fee now to receive the loan amount.",
        "actual_label": "SCAM"
    },
    {
        "message": "Limited time investment opportunity! Send money today and receive guaranteed double returns within 24 hours.",
        "actual_label": "SCAM"
    },
    {
        "message": "Your refund is ready. Click here and enter your UPI PIN to receive the refund immediately.",
        "actual_label": "SCAM"
    },

    # ============================================================
    # SAFE MESSAGES — NORMAL PERSONAL COMMUNICATION
    # ============================================================

    {
        "message": "Hi, are we still meeting at 5 PM today?",
        "actual_label": "SAFE"
    },
    {
        "message": "Please send me the notes from today's lecture when you get time.",
        "actual_label": "SAFE"
    },
    {
        "message": "Can you call me when you are free?",
        "actual_label": "SAFE"
    },
    {
        "message": "I will reach the college by 10 AM tomorrow.",
        "actual_label": "SAFE"
    },
    {
        "message": "Please remind me about the project meeting tomorrow.",
        "actual_label": "SAFE"
    },

    # ============================================================
    # SAFE MESSAGES — COLLEGE / WORK
    # ============================================================

    {
        "message": "The project presentation has been scheduled for Friday at 3:30 PM.",
        "actual_label": "SAFE"
    },
    {
        "message": "The college library will remain open until 8 PM today.",
        "actual_label": "SAFE"
    },
    {
        "message": "Please submit the assignment before the deadline mentioned by the professor.",
        "actual_label": "SAFE"
    },
    {
        "message": "The placement training session will begin at 10 AM tomorrow.",
        "actual_label": "SAFE"
    },
    {
        "message": "Our team meeting has been moved to Monday afternoon.",
        "actual_label": "SAFE"
    },

    # ============================================================
    # SAFE MESSAGES — DELIVERY / SHOPPING
    # ============================================================

    {
        "message": "Your order has been delivered successfully. Thank you for shopping with us.",
        "actual_label": "SAFE"
    },
    {
        "message": "Your grocery order will arrive between 6 PM and 8 PM today.",
        "actual_label": "SAFE"
    },
    {
        "message": "Your order has been shipped and is expected to arrive tomorrow.",
        "actual_label": "SAFE"
    },
    {
        "message": "Your return request has been received and will be processed within three working days.",
        "actual_label": "SAFE"
    },
    {
        "message": "Thank you for shopping with us. Your invoice is available in your account.",
        "actual_label": "SAFE"
    },

    # ============================================================
    # SAFE MESSAGES — APPOINTMENTS / SERVICES
    # ============================================================

    {
        "message": "Your appointment with the doctor is confirmed for tomorrow at 10 AM. Please carry your previous reports.",
        "actual_label": "SAFE"
    },
    {
        "message": "Your dentist appointment has been confirmed for Monday at 4 PM.",
        "actual_label": "SAFE"
    },
    {
        "message": "The electricity maintenance work is scheduled for Sunday morning.",
        "actual_label": "SAFE"
    },
    {
        "message": "Your internet service request has been registered successfully.",
        "actual_label": "SAFE"
    },
    {
        "message": "Your bank statement for this month is now available through the official banking application.",
        "actual_label": "SAFE"
    },

    # ============================================================
    # SAFE MESSAGES — GENERAL NOTIFICATIONS
    # ============================================================

    {
        "message": "The weather forecast shows rain tomorrow, so please carry an umbrella.",
        "actual_label": "SAFE"
    },
    {
        "message": "The train is expected to arrive at platform number three.",
        "actual_label": "SAFE"
    },
    {
        "message": "The meeting room has been changed to Room 204.",
        "actual_label": "SAFE"
    },
    {
        "message": "Please bring your college ID card for tomorrow's event.",
        "actual_label": "SAFE"
    },
    {
        "message": "The office will remain closed on Monday due to the public holiday.",
        "actual_label": "SAFE"
    },
]