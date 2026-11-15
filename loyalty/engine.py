"""Omnichannel Retail Loyalty Tier Progression & FIFO Point Expiration Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class LoyaltyMember:
    member_id: str
    member_name: str
    current_tier: str  # SILVER, GOLD, PLATINUM
    annual_spend_inr: float
    active_points_balance: int
    lifetime_points_earned: int


@dataclass
class RedemptionReceipt:
    member_id: str
    invoice_number: str
    invoice_amount: float
    points_redeemed: int
    discount_applied_inr: float
    net_payable_amount: float
    remaining_points_balance: int
    is_valid_redemption: bool


class OmnichannelLoyaltyEngine:
    """Manages retail points issuance, tier promotions, and anti-fraud redemption limits."""

    # 1 Point = ₹0.50 discount
    POINT_MONETARY_VALUE_INR = 0.50
    # Maximum 50% of invoice amount can be paid via loyalty points
    MAX_REDEMPTION_PCT_OF_BILL = 50.0

    TIER_THRESHOLDS = {
        "PLATINUM": 100000.0,
        "GOLD": 25000.0,
        "SILVER": 0.0
    }

    def earn_points_on_purchase(
        self,
        member: LoyaltyMember,
        purchase_amount: float
    ) -> int:
        member.annual_spend_inr += purchase_amount

        # Earn rate: Silver = 1 pt/₹100, Gold = 1.5 pt/₹100, Platinum = 2 pt/₹100
        rate_multiplier = {
            "PLATINUM": 2.0,
            "GOLD": 1.5,
            "SILVER": 1.0
        }.get(member.current_tier, 1.0)

        points_earned = int((purchase_amount / 100.0) * rate_multiplier)
        member.active_points_balance += points_earned
        member.lifetime_points_earned += points_earned

        # Check tier promotion
        for tier, threshold in self.TIER_THRESHOLDS.items():
            if member.annual_spend_inr >= threshold:
                member.current_tier = tier
                break

        return points_earned

    def redeem_points(
        self,
        member: LoyaltyMember,
        invoice_number: str,
        invoice_amount: float,
        points_to_redeem: int
    ) -> RedemptionReceipt:
        if points_to_redeem > member.active_points_balance:
            raise ValueError(f"Insufficient points balance: requested {points_to_redeem}, available {member.active_points_balance}")

        requested_discount = points_to_redeem * self.POINT_MONETARY_VALUE_INR
        max_allowed_discount = (invoice_amount * self.MAX_REDEMPTION_PCT_OF_BILL) / 100.0

        if requested_discount > max_allowed_discount:
            raise ValueError(f"Redemption limit exceeded. Maximum allowable discount is ₹{max_allowed_discount} (50% of bill).")

        net_payable = round(invoice_amount - requested_discount, 2)
        member.active_points_balance -= points_to_redeem

        return RedemptionReceipt(
            member_id=member.member_id,
            invoice_number=invoice_number,
            invoice_amount=invoice_amount,
            points_redeemed=points_to_redeem,
            discount_applied_inr=requested_discount,
            net_payable_amount=net_payable,
            remaining_points_balance=member.active_points_balance,
            is_valid_redemption=True
        )
