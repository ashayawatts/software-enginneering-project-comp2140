# Shakir Russell — Feature Ownership (`shakir_russell/`)

- **Student ID:** `620181663`
- **Email:** `shakir.russell@mymona.uwi.edu`
- **Branch:** `member/shakir`
- **Push Rule:** Only edit and push files inside `shakir_russell/` during feature sprint.

---

## Assigned SRS Feature

### F-06: Shipment Status and ETA Updating (`Update Shipment Status`)
- **Priority:** High | **Depends on:** F-02 Manual Data Entry
- **User Requirement:** Allow authorized staff to modify the transit status and estimated arrival date (ETA) of an existing shipment record when notified by suppliers.
- **SR-1:** Provide an interface (dropdown) to change a vehicle's transit status (`In Transit`, `Delayed`, `Arrived`, `Cleared`).
- **SR-2:** Allow authorized staff to override the existing ETA with a new date (and optional delay reason).
- **SR-3:** Commit updates immediately to the central database so they reflect instantly on Bill of Lading tracking queries (F-01) and customer timelines (F-04).
- **Security & Safety (SRS §3.2):**
  - Require staff authentication before granting access to administrative update functions.
  - Support soft-delete (`is_deleted = True`) so outdated records are hidden without permanently erasing history.
- **Test Scenarios:**
  - `TS-1 [AC-1]`: Authorized staff changes shipment status from `In Transit` to `Arrived` and commits to DB.
  - `TS-2 [AC-2]`: Entering a new ETA overwrites the old date and immediately appears on F-01 BoL tracking searches.

---

## Files in This Folder
- `routes.py` — Flask Blueprint (`shakir_bp`) for `/shipments/manage`, `/shipments/update/<bol>`, `/staff/login`, `/staff/logout`
- `status_update_service.py` — Transit status update, ETA override, and soft-delete logic
- `templates/update_shipment.html` & `templates/staff_login.html`
- `static/shipment_admin.css` & `static/eta_editor.js`
- `tests/test_f06_status_update.py`
