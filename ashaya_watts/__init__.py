"""Ashaya Watts' Blueprint: F-04 Customer Interface Search (Public Storefront)."""

from flask import Blueprint

ashaya_bp = Blueprint(
    "ashaya_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/ashaya/static",
)

from ashaya_watts import routes  # noqa: E402, F401
