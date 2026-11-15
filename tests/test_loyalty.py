import unittest
from loyalty.engine import OmnichannelLoyaltyEngine, LoyaltyMember

class TestOmnichannelLoyalty(unittest.TestCase):
    def test_earn_and_tier_promotion(self):
        engine = OmnichannelLoyaltyEngine()
        member = LoyaltyMember(
            member_id="CUST-881",
            member_name="Aakash Chopra",
            current_tier="SILVER",
            annual_spend_inr=20000.0,
            active_points_balance=200,
            lifetime_points_earned=200
        )

        # Spend ₹10,000 -> Annual spend becomes ₹30,000 (> 25k threshold for GOLD)
        pts = engine.earn_points_on_purchase(member, 10000.0)
        self.assertEqual(pts, 100) # Silver rate 1 pt / ₹100
        self.assertEqual(member.current_tier, "GOLD")
        self.assertEqual(member.active_points_balance, 300)

    def test_redemption_validation(self):
        engine = OmnichannelLoyaltyEngine()
        member = LoyaltyMember(
            member_id="CUST-881",
            member_name="Aakash Chopra",
            current_tier="GOLD",
            annual_spend_inr=30000.0,
            active_points_balance=500,
            lifetime_points_earned=500
        )

        # Redeem 200 points (₹100 discount) on ₹1,000 invoice (max 50% = ₹500)
        receipt = engine.redeem_points(member, "INV-2026-90", 1000.0, 200)
        self.assertTrue(receipt.is_valid_redemption)
        self.assertEqual(receipt.discount_applied_inr, 100.0)
        self.assertEqual(receipt.net_payable_amount, 900.0)
        self.assertEqual(receipt.remaining_points_balance, 300)

if __name__ == "__main__":
    unittest.main()
