"""
Shared Staff Authentication & Role-Based Access Control (RBAC) Helpers (SRS §3.2).
Roles: owner | purchasing_manager | sales_staff | internal_staff
"""

from functools import wraps
from flask import session, redirect, url_for, abort


VALID_ROLES = {"owner", "purchasing_manager", "sales_staff", "internal_staff"}


def login_required(view_func):
    """Ensure a staff member is authenticated before accessing internal routes."""

    @wraps(view_func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("shakir_bp.staff_login"))
        return view_func(*args, **kwargs)

    return wrapper


def role_required(*allowed_roles):
    """Restrict a route to specific staff roles (Owner always permitted)."""

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            if "user_id" not in session:
                return redirect(url_for("shakir_bp.staff_login"))
            user_role = session.get("user_role")
            if user_role != "owner" and user_role not in allowed_roles:
                abort(403)
            return view_func(*args, **kwargs)

        return wrapper

    return decorator
