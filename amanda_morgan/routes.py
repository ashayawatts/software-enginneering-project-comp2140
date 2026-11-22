"""Routes for F-03 Mobile Portability Access (Sales Tablet Interface)."""

from flask import render_template, abort
from amanda_morgan import amanda_bp
from amanda_morgan.specs_service import list_active_vehicles, get_vehicle_profile


@amanda_bp.route("/tablet/", methods=["GET"])
def tablet_dashboard():
    """F-03: Touch-friendly tablet inventory grid for sales staff on the lot."""
    vehicles = list_active_vehicles()
    return render_template("tablet_dashboard.html", vehicles=vehicles)


@amanda_bp.route("/tablet/vehicle/<int:vehicle_id>", methods=["GET"])
def vehicle_profile(vehicle_id: int):
    """F-03: Display vehicle photo gallery, mileage, and full spec sheet."""
    vehicle = get_vehicle_profile(vehicle_id)
    if vehicle is None:
        abort(404)
    return render_template("vehicle_profile.html", vehicle=vehicle)
