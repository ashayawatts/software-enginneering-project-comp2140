"""F-06 Service: Update transit status, override ETA, and soft-delete shipments."""

from datetime import date

VALID_STATUSES = {"In Transit", "Delayed", "Arrived", "Cleared"}


def update_shipment_status(
    bill_of_lading: str,
    new_status: str,
    new_eta: date | None = None,
    delay_reason: str | None = None,
):
    """
    TODO (Shakir - F-06 SR-1, SR-2, SR-3):
    1. Validate new_status in VALID_STATUSES.
    2. Look up active Shipment by bill_of_lading (is_deleted=False).
    3. Update status, eta_date, delay_reason, and commit to shared.database.db.
    """
    raise NotImplementedError("TODO: Implement F-06 update_shipment_status()")
