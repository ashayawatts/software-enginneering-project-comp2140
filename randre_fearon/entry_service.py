"""F-02 Service: Manual Data Entry for newly deposited vehicles."""


def log_new_vehicle(form_data: dict):
    """
    TODO (Randre - F-02 SR-1, SR-2, SR-3):
    1. Reject & raise ValueError if deposit_paid is not True (AC-2).
    2. Validate required specs (make, model, year, engine_cc, base_foreign_price, bill_of_lading).
    3. Save Vehicle + linked Shipment record to shared.database.db (AC-1).
    """
    raise NotImplementedError("TODO: Implement F-02 log_new_vehicle()")
