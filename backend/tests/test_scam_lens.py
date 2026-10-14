import unittest

from analyzer.preprocessing import preprocess_text
from analyzer.signals import detect_signals
from analyzer.risk_engine import calculate_risk_score, get_risk_level
from analyzer.explanation import generate_explanation
from analyzer.recommendations import generate_recommendations
from models.schemas import AnalyzeRequest


class TestScamLens(unittest.TestCase):

    def test_preprocessing(self):
        text = "  URGENT   Bank Message  "
        result = preprocess_text(text)

        self.assertEqual(result, "urgent bank message")

    def test_bank_scam_detection(self):
        message = (
            "URGENT! Your bank account will be blocked today. "
            "Verify your account immediately and enter your OTP."
        )

        cleaned = preprocess_text(message)
        signals = detect_signals(cleaned)
        score = calculate_risk_score(signals)

        self.assertIn("urgency", signals)
        self.assertIn("threat", signals)
        self.assertIn("credential_request", signals)
        self.assertIn("authority_impersonation", signals)
        self.assertGreaterEqual(score, 70)
        self.assertEqual(get_risk_level(score), "HIGH")

    def test_delivery_scam_detection(self):
        message = (
            "Your parcel could not be delivered. "
            "Pay a small delivery fee immediately to reschedule your shipment."
        )

        cleaned = preprocess_text(message)
        signals = detect_signals(cleaned)

        self.assertIn("delivery_scam", signals)
        self.assertIn("financial_request", signals)
        self.assertIn("urgency", signals)

    def test_investment_scam_detection(self):
        message = (
            "Earn guaranteed returns on your investment. "
            "Transfer Rs 10000 immediately to activate your account."
        )

        cleaned = preprocess_text(message)
        signals = detect_signals(cleaned)
        score = calculate_risk_score(signals)

        self.assertIn("investment_scam", signals)
        self.assertIn("financial_request", signals)
        self.assertGreaterEqual(score, 70)
        self.assertEqual(get_risk_level(score), "HIGH")

    def test_safe_message(self):
        message = (
            "Hi Kalyani, your class presentation is scheduled "
            "for Friday at 3:30 PM."
        )

        cleaned = preprocess_text(message)
        signals = detect_signals(cleaned)
        score = calculate_risk_score(signals)

        self.assertEqual(signals, {})
        self.assertEqual(score, 0)
        self.assertEqual(get_risk_level(score), "LOW")

    def test_url_detection(self):
        message = (
            "Verify your account immediately at "
            "https://example.com and enter your OTP."
        )

        cleaned = preprocess_text(message)
        signals = detect_signals(cleaned)

        self.assertIn("suspicious_link", signals)
        self.assertIn("url_detected", signals)

    def test_explanation_generation(self):
        signals = {
            "urgency": ["urgent"],
            "credential_request": ["otp"]
        }

        explanation = generate_explanation(signals)

        self.assertIn("Urgency or pressure", explanation)
        self.assertIn("Request for sensitive credentials", explanation)

    def test_recommendation_generation(self):
        signals = {
            "credential_request": ["otp"]
        }

        recommendations = generate_recommendations(signals)

        self.assertTrue(len(recommendations) > 0)
        self.assertIn("Never share OTPs", recommendations[0])

    def test_empty_message_validation(self):
        with self.assertRaises(Exception):
            AnalyzeRequest(message="")

    def test_long_message_validation(self):
        long_message = "A" * 5001

        with self.assertRaises(Exception):
            AnalyzeRequest(message=long_message)

    def test_valid_message_validation(self):
        request = AnalyzeRequest(
            message="This is a valid message."
        )

        self.assertEqual(
            request.message,
            "This is a valid message."
        )


if __name__ == "__main__":
    unittest.main()