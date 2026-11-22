"""Tyrone Palmer's Blueprint: F-05 Dynamic Pricing Estimates (FX & Engine CC Duties)."""

from flask import Blueprint

tyrone_bp = Blueprint(
    "tyrone_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/tyrone/static",
)

from tyrone_palmer import routes  # noqa: E402, F401
