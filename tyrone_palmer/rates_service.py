"""F-05 Service: Manage updatable FX rates and CC duty percentages in DB (SRS §3.3)."""

from shared.models import FxRate, DutyTier


def get_all_fx_rates():
    return FxRate.query.order_by(FxRate.currency_code).all()


def get_all_duty_tiers():
    return DutyTier.query.order_by(DutyTier.vehicle_category, DutyTier.min_cc).all()
