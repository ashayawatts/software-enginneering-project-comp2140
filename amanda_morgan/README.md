# Amanda Morgan — Feature Ownership (`amanda_morgan/`)

- **Student ID:** `620170322`
- **Email:** `amanda.morgan02@mymona.uwi.edu`
- **Branch:** `member/amanda`
- **Push Rule:** Only edit and push files inside `amanda_morgan/`.

---

## Assigned SRS Feature

### F-03: Mobile Portability Access (`View Vehicle Specifications`)
- **Priority:** High | **Depends on:** F-02 Manual Data Entry
- **User Requirement:** Allow sales staff to view vehicle specs, mileage, and photos on a tablet while standing on the lot with customers.
- **SR-1:** Responsively adapt to tablet screen dimensions (iPad & Android tablets, `768px–1180px`).
- **SR-2:** Display image galleries and specifications in a touch-friendly layout (`>= 44px` tap targets, swipeable gallery).
- **SR-3:** Retrieve mileage, color, features (e.g., sunroof, rims, keyless entry), and photos for the selected vehicle.
- **Acceptance Criteria:**
  - `AC-1 [SR-1, SR-2]`: UI elements are appropriately sized and touch-responsive on tablets.
  - `AC-2 [SR-3]`: Accessing a vehicle profile immediately displays associated mileage and uploaded photos.
- **Test Scenarios:**
  - `TS-1 [AC-1]`: Verify UI rendering on an iPad/Android tablet simulator.
  - `TS-2 [AC-2]`: Verify tapping a vehicle profile opens the photo gallery and spec sheet.

---

## Files in This Folder
- `routes.py` — Flask Blueprint (`amanda_bp`) for `/tablet/` and `/tablet/vehicle/<id>`
- `specs_service.py` — Retrieves vehicle profile, mileage, features, and photos
- `templates/tablet_dashboard.html` & `templates/vehicle_profile.html`
- `static/tablet.css` & `static/gallery.js`
- `tests/test_f03_tablet_ui.py`
