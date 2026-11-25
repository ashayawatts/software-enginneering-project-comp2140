"""Routes for F-03 Mobile Portability Access (Sales Tablet Interface)."""

from flask import render_template, request, abort
from amanda_morgan import amanda_bp
from amanda_morgan.specs_service import list_active_vehicles, get_vehicle_profile

# NOTE: these are staff routes (sales_staff / owner). Per integration/fuse_checklist.md the
# @role_required decorator from shared/auth.py is applied to every internal route at fusion.


@amanda_bp.route("/tablet/", methods=["GET"])
def tablet_dashboard():
    """F-03: Touch-friendly tablet inventory grid for sales staff on the lot."""
    query = request.args.get("q", "").strip()[:100]
    vehicles = list_active_vehicles(query)
    return render_template("tablet_dashboard.html", vehicles=vehicles, query=query)


@amanda_bp.route("/tablet/vehicle/<int:vehicle_id>", methods=["GET"])
def vehicle_profile(vehicle_id: int):
    """F-03: Display vehicle photo gallery, mileage, and full spec sheet."""
    vehicle = get_vehicle_profile(vehicle_id)
    if vehicle is None:
        abort(404)
    return render_template("vehicle_profile.html", vehicle=vehicle)
