"""F-01 Service: Shipment and Inventory Tracking by Bill of Lading."""

from shared.models import Shipment
from shared.validators import is_valid_bill_of_lading


def find_shipment_by_bol(bill_of_lading: str):
    """
    TODO (Randre - F-01 SR-1, SR-2, SR-3):
    1. Validate bill_of_lading via is_valid_bill_of_lading().
    2. Query Shipment where bill_of_lading matches and is_deleted is False.
    3. Return shipment + boolean flag `is_delayed = (shipment.status == 'Delayed')`.
    """
    if not is_valid_bill_of_lading(bill_of_lading):
        return None
    return Shipment.query.filter_by(
        bill_of_lading=bill_of_lading.strip(),
        is_deleted=False,
    ).first()
