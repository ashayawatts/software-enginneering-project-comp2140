# Karmanjahni Shipment and Inventory Tracking System

**Course:** COMP2140 – Introduction to Software Engineering (UWI Mona)  
**Group:** `THUR_9-11_G01`  
**Course Instructor:** Dr. Ricardo Anderson  
**Studio Facilitator:** Dr. Claudine Allen  
**Client:** Karmanjahni Company Limited (Kingston, Jamaica)

---

## Tech Stack

- **Backend:** Python 3.11+ with **Flask** (Modular Blueprints) & **SQLAlchemy**
- **Frontend:** HTML5, CSS3 (shared `resources/design/theme.css`), Vanilla JavaScript
- **Database:** SQLite (local development) / PostgreSQL (production deployment)
- **Testing:** `pytest`
- **Cloud Hosting:** Vercel (`vercel.json` included per SRS §3.3)

---

## Team Ownership & Folder Structure

> **GOLDEN RULE:** Every team member works and pushes **ONLY** inside their own named folder during development. Do **not** modify another member's folder. Shared database contracts live in `shared/` and brand styling lives in `resources/design/`. Once everyone finishes their feature and tests, we come together and fuse everything through `app.py` and `integration/`.

| Folder | Team Member | Student ID | SRS Feature(s) |
| :--- | :--- | :--- | :--- |
| [`randre_fearon/`](randre_fearon/README.md) | **Randre Fearon** | `620167746` | **F-01** Shipment & Inventory Tracking, **F-02** Manual Data Entry |
| [`amanda_morgan/`](amanda_morgan/README.md) | **Amanda Morgan** | `620170322` | **F-03** Mobile Portability Access (Tablet Vehicle Specs & Gallery) |
| [`ashaya_watts/`](ashaya_watts/README.md) | **Ashaya Watts** | `620169617` | **F-04** Customer Interface Search (Restricted Public Storefront) |
| [`tyrone_palmer/`](tyrone_palmer/README.md) | **Tyrone Palmer** | `620181645` | **F-05** Dynamic Pricing Estimates (FX Rates & Engine CC Duties) |
| [`shakir_russell/`](shakir_russell/README.md) | **Shakir Russell** | `620181663` | **F-06** Shipment Status & ETA Updating (Staff Admin) |

### Shared & Integration Directories

- `resources/design/` — Official Karmanjahni color palette, theme CSS, design tokens, brand guide, and logo assets.
- `shared/` — Shared SQLAlchemy models (`Vehicle`, `Shipment`, `FxRate`, `DutyTier`, `User`), RBAC helpers, validators, seed SQL, and base HTML templates.
- `docs/` — API & DB schema contract (`API_AND_DB_CONTRACT.md`) and Git workflow (`GIT_WORKFLOW.md`).
- `integration/` — Final fusion checklist and end-to-end tests.

---

## Quick Start (Local Development)

```bash
# 1. Clone the repository
git clone https://github.com/wearecyberrock/software-enginneering-project-comp2140.git
cd software-enginneering-project-comp2140

# 2. Create and activate a virtual environment
python -m venv venv
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# macOS / Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the starter app
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## Running Tests

```bash
# Run only your own folder's tests (example):
pytest randre_fearon/tests/

# Run all tests during integration:
pytest
```

See [`docs/GIT_WORKFLOW.md`](docs/GIT_WORKFLOW.md) before making your first commit.
