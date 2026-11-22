"""F-05 Pricing Engine: Dynamic JMD estimate using active FX rates and CC duty tiers."""

from decimal import Decimal
from shared.models import Vehicle


def calculate_estimated_jmd_price(vehicle: Vehicle) -> Decimal:
    """
    TODO (Tyrone - F-05 SR-1, SR-2, SR-3):
    1. Fetch FxRate for vehicle.base_currency.
    2. Match DutyTier for vehicle.category and vehicle.engine_cc.
    3. Compute: base_jmd = base_foreign_price * rate_to_jmd
       estimated_total = base_jmd * (1 + duty_percentage / 100)
    4. Return Decimal rounded to 2 decimal places.
    """
    raise NotImplementedError("TODO: Implement F-05 calculate_estimated_jmd_price()")
