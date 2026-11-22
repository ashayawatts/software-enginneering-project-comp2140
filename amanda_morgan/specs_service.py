"""F-03 Service: Retrieve vehicle specs, mileage, features, and photos for tablet view."""

from shared.models import Vehicle


def list_active_vehicles():
    """Return all non-deleted, deposit-paid vehicles for the sales tablet dashboard."""
    return Vehicle.query.filter_by(is_deleted=False, deposit_paid=True).all()


def get_vehicle_profile(vehicle_id: int):
    """
    TODO (Amanda - F-03 SR-3, AC-2):
    Retrieve a single active vehicle with parsed photo gallery URLs,
    mileage, color, features, and linked estimated pricing from F-05.
    """
    return Vehicle.query.filter_by(id=vehicle_id, is_deleted=False).first()
