"""Amanda Morgan's Blueprint: F-03 Mobile Portability Access (Sales Tablet UI)."""

from flask import Blueprint

amanda_bp = Blueprint(
    "amanda_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/amanda/static",
)

from amanda_morgan import routes  # noqa: E402, F401
