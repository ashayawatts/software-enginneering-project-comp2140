# Final Integration & Code Fusion Checklist

Use this checklist when all 5 team members are ready to merge their branches into `main`:

1. **Pre-Merge Check (Each Member)**
   - [ ] `randre_fearon/tests/` passes (`F-01` & `F-02`)
   - [ ] `amanda_morgan/tests/` passes (`F-03`)
   - [ ] `ashaya_watts/tests/` passes (`F-04`)
   - [ ] `tyrone_palmer/tests/` passes (`F-05`)
   - [ ] `shakir_russell/tests/` passes (`F-06`)

2. **Fusion Steps**
   - [ ] Merge all 5 member branches (`member/randre`, `member/amanda`, `member/ashaya`, `member/tyrone`, `member/shakir`) into `main`.
   - [ ] Embed Tyrone's `price_breakdown_partial.html` / `calculate_estimated_jmd_price()` into Amanda's `vehicle_profile.html` (F-03) and Ashaya's `customer_vehicle_detail.html` (F-04).
   - [ ] Apply `@login_required` / `@role_required` from `shared/auth.py` to all internal routes (F-01, F-02, F-03, F-05 rate editor, F-06) while keeping Ashaya's F-04 storefront completely public and stripped of internal costs/BoL.
   - [ ] Run full test suite: `pytest` (including `integration/test_end_to_end.py`).
   - [ ] Verify tablet responsiveness on iPad/Android simulator (SRS F-03 TS-1).
   - [ ] Deploy fused app to Vercel (`vercel.json`) with production PostgreSQL `DATABASE_URL` and HTTPS enabled.
