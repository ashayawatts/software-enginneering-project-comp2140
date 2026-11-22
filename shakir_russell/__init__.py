"""Shakir Russell's Blueprint: F-06 Shipment Status & ETA Updating (+ Staff Login)."""

from flask import Blueprint

shakir_bp = Blueprint(
    "shakir_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/shakir/static",
)

from shakir_russell import routes  # noqa: E402, F401
