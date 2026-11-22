# Randre Fearon — Feature Ownership (`randre_fearon/`)

- **Student ID:** `620167746`
- **Email:** `randre.fearon@mymona.uwi.edu`
- **Branch:** `member/randre`
- **Push Rule:** Only edit and push files inside `randre_fearon/`.

---

## Assigned SRS Features

### F-01: Shipment and Inventory Tracking (`Track Shipment Status`)
- **Priority:** High | **Depends on:** F-06
- **SR-1:** Query internal database using the provided Bill of Lading (BoL) number.
- **SR-2:** Retrieve and display the saved transit status and ETA of the vehicle.
- **SR-3:** Flag/visibly highlight a status when it is marked as `Delayed`.
- **Performance (SRS §3.1):** Retrieve shipment tracking data in **under 3 seconds**.
- **Test Scenarios:**
  - `TS-1 [AC-1]`: Entering an existing BoL retrieves stored status and ETA.
  - `TS-2 [AC-1]`: Error handling when an invalid or non-existent BoL is entered.
  - `TS-3 [AC-2]`: Visibly highlights status text when DB returns `Delayed` (use `.badge-delayed` from `resources/design/theme.css`).

### F-02: Manual Data Entry (`Log Vehicle Inventory`)
- **Priority:** High | **Depends on:** None
- **SR-1:** Provide a data entry form for vehicle specs, photos, BoL, and purchase details.
- **SR-2:** Require confirmation that a **deposit is paid** before a unit is activated/saved.
- **SR-3:** Save the logged unit to the central database (`shared.models.Vehicle` & `Shipment`).
- **Test Scenarios:**
  - `TS-1 [AC-1]`: Submitting all required vehicle details saves the record correctly.
  - `TS-2 [AC-2]`: Throws a validation error and blocks saving if deposit is not marked as paid.

---

## Files in This Folder
- `routes.py` — Flask Blueprint (`randre_bp`) for `/tracking/*` and `/inventory/*`
- `tracking_service.py` — F-01 database lookup & delayed flag logic
- `entry_service.py` — F-02 deposit validation & vehicle/shipment creation logic
- `templates/track_shipment.html` & `templates/log_vehicle.html`
- `static/tracking.css` & `static/entry_form.js`
- `tests/test_f01_tracking.py` & `tests/test_f02_data_entry.py`
