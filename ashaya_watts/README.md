# Ashaya Watts — Feature Ownership (`ashaya_watts/`)

- **Student ID:** `620169617`
- **Email:** `ashaya.watts@mymona.uwi.edu`
- **Branch:** `member/ashaya`
- **Push Rule:** Only edit and push files inside `ashaya_watts/`.

---

## Assigned SRS Feature

### F-04: Customer Interface Search (`Browse Inventory`)
- **Priority:** Medium | **Depends on:** F-01 Shipment Tracking
- **User Requirement:** Provide a website-like public interface allowing customers to search for specific vehicles (e.g., "Tacoma pickup") and view upcoming & available inventory.
- **SR-1:** Provide a search bar capable of filtering by vehicle make and model.
- **SR-2:** Display a list of matching upcoming and available vehicles with estimated timelines.
- **SR-3 (CRITICAL SECURITY):** Strictly restrict this view to **omit all sensitive internal company data** (base foreign purchasing cost, Bill of Lading number, supplier notes, deposit records).
- **Performance (SRS §3.1):** Return filtered inventory results in **under 2 seconds**.
- **Test Scenarios:**
  - `TS-1 [AC-1]`: Entering a specific car model successfully filters the inventory list.
  - `TS-2 [AC-2]`: Verify internal financial data (`base_foreign_price`, `bill_of_lading`) is NEVER present in customer search HTML or JSON results.

---

## Files in This Folder
- `routes.py` — Flask Blueprint (`ashaya_bp`) for `/`, `/browse`, and `/api/public/vehicles`
- `public_catalog_service.py` — Safe query & strict public serializer (strips internal fields)
- `templates/customer_home.html` & `templates/customer_vehicle_detail.html`
- `static/storefront.css` & `static/search.js`
- `tests/test_f04_customer_search.py`
