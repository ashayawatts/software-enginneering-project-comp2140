"""Shared Input Validation & Sanitization Helpers (SRS §3.2 SQLi Protection)."""

import re

BOL_PATTERN = re.compile(r"^[A-Za-z0-9\-_]{3,64}$")
SAFE_SEARCH_PATTERN = re.compile(r"[^A-Za-z0-9\s\-]")


def sanitize_search_query(query: str) -> str:
    """Strip unsafe characters from customer/staff search strings."""
    if not query:
        return ""
    return SAFE_SEARCH_PATTERN.sub("", query).strip()[:100]


def is_valid_bill_of_lading(bol: str) -> bool:
    """Validate Bill of Lading format before querying the database."""
    if not bol:
        return False
    return bool(BOL_PATTERN.match(bol.strip()))
