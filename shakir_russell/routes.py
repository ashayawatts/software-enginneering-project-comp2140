"""Routes for F-06 Shipment Status & ETA Updating and Staff Authentication."""

from flask import render_template, request, session, redirect, url_for
from shakir_russell import shakir_bp
from shakir_russell.status_update_service import update_shipment_status


@shakir_bp.route("/shipments/manage", methods=["GET", "POST"])
def manage_shipments():
    """F-06: Search shipment by BoL and update transit status / ETA."""
    if request.method == "POST":
        # TODO (Shakir): Enforce auth, validate input, call update_shipment_status(...)
        _ = update_shipment_status
    return render_template("update_shipment.html")


@shakir_bp.route("/staff/login", methods=["GET", "POST"])
def staff_login():
    """Staff login entry point for RBAC (SRS §3.2)."""
    return render_template("staff_login.html")


@shakir_bp.route("/staff/logout", methods=["POST"])
def staff_logout():
    session.clear()
    return redirect(url_for("ashaya_bp.customer_home"))
