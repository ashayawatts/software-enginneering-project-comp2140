"""Routes for F-05 Dynamic Pricing Estimates & Rate Maintenance."""

from flask import render_template, jsonify, abort
from tyrone_palmer import tyrone_bp
from tyrone_palmer.pricing_engine import calculate_estimated_jmd_price
from tyrone_palmer.rates_service import get_all_fx_rates, get_all_duty_tiers
from shared.models import Vehicle


@tyrone_bp.route("/pricing/estimate/<int:vehicle_id>", methods=["GET"])
def pricing_estimate(vehicle_id: int):
    """F-05: Return calculated JMD estimate (safe for public & tablet embedding)."""
    vehicle = Vehicle.query.filter_by(id=vehicle_id, is_deleted=False).first()
    if vehicle is None:
        abort(404)
    # TODO (Tyrone): Call calculate_estimated_jmd_price(vehicle)
    _ = calculate_estimated_jmd_price
    return jsonify({"vehicle_id": vehicle.id, "estimated_jmd_price": None, "status": "TODO"})


@tyrone_bp.route("/admin/pricing-rates", methods=["GET", "POST"])
def manage_rates():
    """F-05 / SRS §3.3: Admin panel for updating FX rates and CC duty tiers without code edits."""
    fx_rates = get_all_fx_rates()
    duty_tiers = get_all_duty_tiers()
    return render_template("manage_rates.html", fx_rates=fx_rates, duty_tiers=duty_tiers)
