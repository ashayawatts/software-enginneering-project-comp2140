"""Routes for F-01 (Shipment Tracking) and F-02 (Manual Data Entry)."""

from flask import render_template, request
from randre_fearon import randre_bp
from randre_fearon.tracking_service import find_shipment_by_bol
from randre_fearon.entry_service import log_new_vehicle


@randre_bp.route("/tracking/", methods=["GET"])
def track_shipment():
    """F-01: Render Bill of Lading search page and tracking results."""
    bol = request.args.get("bol", "").strip()
    shipment = find_shipment_by_bol(bol) if bol else None
    return render_template("track_shipment.html", bol=bol, shipment=shipment)


@randre_bp.route("/inventory/add", methods=["GET", "POST"])
def add_vehicle():
    """F-02: Render and handle manual vehicle logging form (deposit-paid required)."""
    error = None
    if request.method == "POST":
        # TODO (Randre): Extract form fields & call log_new_vehicle(...)
        _ = log_new_vehicle
    return render_template("log_vehicle.html", error=error)
