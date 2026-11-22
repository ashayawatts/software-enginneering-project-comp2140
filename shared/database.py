"""Shared SQLAlchemy database instance and backup utilities (SRS §3.2)."""

import shutil
from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def backup_sqlite_database(db_path: str, backup_dir: str = "backups") -> str:
    """Create a timestamped backup copy of a local SQLite database file."""
    import os

    os.makedirs(backup_dir, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(backup_dir, f"karmanjahni_backup_{stamp}.db")
    shutil.copy2(db_path, dest)
    return dest
