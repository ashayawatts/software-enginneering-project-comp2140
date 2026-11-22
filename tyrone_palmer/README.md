# Tyrone Palmer — Feature Ownership (`tyrone_palmer/`)

- **Student ID:** `620181645`
- **Email:** `tyrone.palmer@mymona.uwi.edu`
- **Branch:** `member/tyrone`
- **Push Rule:** Only edit and push files inside `tyrone_palmer/`.

---

## Assigned SRS Feature

### F-05: Dynamic Pricing Estimates (`View Dynamic Pricing`)
- **Priority:** High | **Depends on:** F-02 Manual Data Entry
- **User Requirement:** Calculate and display estimated localized JMD prices accounting for shifting foreign exchange rates and government duties based on engine CC size / vehicle category.
- **SR-1:** Use the stored base foreign currency price of the vehicle (`Vehicle.base_foreign_price`, `base_currency`).
- **SR-2:** Apply a calculation algorithm factoring in current exchange rates (`FxRate`) and the matching CC size / category duty percentage (`DutyTier`).
- **SR-3:** Output the final localized estimated price (JMD) instantaneously when a vehicle profile loads (SRS §3.1).
- **Maintainability (SRS §3.3):** FX rates and duty percentages MUST live in the database (`fx_rates`, `duty_tiers`) so staff can adjust them via UI without altering code.
- **Test Scenarios:**
  - `TS-1 [AC-1]`: Verify final price output changes immediately before and after modifying the active FX rate.
  - `TS-2 [AC-2]`: Verify calculated duty applied to a small-engine vehicle vs a heavy equipment vehicle.

---

## Files in This Folder
- `routes.py` — Flask Blueprint (`tyrone_bp`) for `/pricing/estimate/<id>` and `/admin/pricing-rates`
- `pricing_engine.py` — Core FX + CC duty pricing algorithm
- `rates_service.py` — Read/update `FxRate` & `DutyTier` tables
- `templates/price_breakdown_partial.html` & `templates/manage_rates.html`
- `static/pricing.css` & `static/pricing_calc.js`
- `tests/test_f05_dynamic_pricing.py`
