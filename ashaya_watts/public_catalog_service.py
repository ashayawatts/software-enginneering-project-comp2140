
"""F-04 Service: Public Inventory Filtering with Strict View Restriction."""

from shared.models import Vehicle
from shared.validators import sanitize_search_query


def serialize_public_vehicle(vehicle: Vehicle) -> dict:
    """
    Return only information that customers are allowed to view.
    Internal purchasing costs and other sensitive data are excluded.
    """
    return {
        "id": vehicle.id,
        "make": vehicle.make,
        "model": vehicle.model,
        "year": vehicle.year,
        "category": vehicle.category,
        "color": vehicle.color,
        "mileage_km": vehicle.mileage_km,
        "engine_cc": vehicle.engine_cc,
        "features": vehicle.features,
        "photo_urls": vehicle.photo_urls,
        "availability": (
            "Available Now"
            if vehicle.shipment and vehicle.shipment.status == "Arrived"
            else "Upcoming Arrival"
        ),
        "estimated_arrival": (
            vehicle.shipment.eta_date.isoformat()
            if vehicle.shipment and vehicle.shipment.eta_date
            else None
        ),
    }


def search_public_inventory(raw_query: str = "") -> list[dict]:
    """
    Filter available and upcoming vehicles by make and model.
    Return only information that customers are allowed to access.
    """
    clean_q = sanitize_search_query(raw_query)

    # Only include non-deleted vehicles with paid deposits.
    q = Vehicle.query.filter_by(
        is_deleted=False,
        deposit_paid=True
    )

    # Allow customers to search by make, model or both.
    if clean_q:
        for term in clean_q.split():
            like = f"%{term}%"

            q = q.filter(
                (Vehicle.make.ilike(like)) |
                (Vehicle.model.ilike(like))
            )

    vehicles = q.all()

    # Return an empty list if no matching vehicles are found.
    if not vehicles:
        return []

    # Return only customer-safe vehicle information.
    return [serialize_public_vehicle(v) for v in vehicles]


def get_public_vehicle(vehicle_id: int) -> dict | None:
    """
    Retrieve vehicle details without exposing sensitive information.
    """
    vehicle = Vehicle.query.filter_by(
        id=vehicle_id,
        is_deleted=False,
        deposit_paid=True
    ).first()

    if vehicle is None:
        return None

    return serialize_public_vehicle(vehicle)

