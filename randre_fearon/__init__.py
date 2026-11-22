"""Randre Fearon's Blueprint: F-01 Shipment Tracking & F-02 Manual Data Entry."""

from flask import Blueprint

randre_bp = Blueprint(
    "randre_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/randre/static",
)

from randre_fearon import routes  # noqa: E402, F401
