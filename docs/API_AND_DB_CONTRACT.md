# API & Database Contract (Shared Agreement)

All 5 team members build against the exact same database schema (`shared/models.py`) and URL route prefixes below so that fusing all Blueprints in `app.py` requires zero refactoring.

---

## 1. Route Ownership (URL Prefixes)

| Member | Blueprint | Route Prefix(es) | Public or Staff? |
| :--- | :--- | :--- | :--- |
| **Ashaya Watts (F-04)** | `ashaya_bp` | `/`, `/browse`, `/api/public/vehicles` | **Public** (strictly NO internal costs/BoL) |
| **Randre Fearon (F-01, F-02)** | `randre_bp` | `/tracking/*`, `/inventory/*` | **Staff** (Purchasing / Internal / Owner) |
| **Amanda Morgan (F-03)** | `amanda_bp` | `/tablet/*` | **Staff** (Sales Staff on Tablet / Owner) |
| **Tyrone Palmer (F-05)** | `tyrone_bp` | `/pricing/*`, `/admin/pricing-rates` | **Shared Service** (Price calc public-safe; rate editing Owner/Admin) |
| **Shakir Russell (F-06)** | `shakir_bp` | `/shipments/*`, `/staff/login`, `/staff/logout` | **Staff** (Authorized Staff / Purchasing / Owner) |

---

## 2. Core Database Tables (`shared/models.py`)

### `vehicles`
| Column | Type | Notes |
| :--- | :--- | :--- |
| `id` | Integer (PK) | Auto-increment |
| `make` | String(80) | e.g., Toyota, Honda, Caterpillar |
| `model` | String(100) | e.g., Tacoma Pickup, CR-V, Tractor |
| `year` | Integer | Model year |
| `category` | String(40) | `car`, `truck`, `bus`, `heavy_equipment`, `parts` |
| `color` | String(50) | e.g., Wine Red, Deep Blue, Black |
| `mileage_km` | Integer | Odometer reading |
| `engine_cc` | Integer | Used by F-05 duty calculator |
| `features` | Text | Comma-separated or JSON (e.g., `Sunroof, Keyless Entry, Alloy Rims`) |
| `origin_country` | String(50) | Japan, US, Singapore, Thailand, Europe |
| `photo_urls` | Text | JSON list of image paths/URLs |
| `base_foreign_price` | Numeric(12, 2) | **INTERNAL ONLY** — never expose in F-04 |
| `base_currency` | String(10) | `JPY`, `USD`, `SGD`, `THB`, `EUR` (**INTERNAL ONLY**) |
| `deposit_paid` | Boolean | **F-02 Gate:** must be `True` to activate unit |
| `is_deleted` | Boolean | **SRS §3.2 Soft Delete** (default `False`) |
| `deleted_at` | DateTime | Timestamp when soft-deleted |

### `shipments`
| Column | Type | Notes |
| :--- | :--- | :--- |
| `id` | Integer (PK) | Auto-increment |
| `vehicle_id` | Integer (FK -> `vehicles.id`) | Linked vehicle |
| `bill_of_lading` | String(100), Unique | **INTERNAL ONLY** — queried in F-01 & updated in F-06 |
| `status` | String(30) | `In Transit`, `Delayed`, `Arrived`, `Cleared` |
| `eta_date` | Date | Estimated Time of Arrival |
| `departure_date` | Date | Vessel departure date (optional) |
| `delay_reason` | String(255) | e.g., Tropical storm / port congestion |
| `updated_at` | DateTime | Last updated timestamp |
| `is_deleted` | Boolean | Soft delete flag (default `False`) |

### `fx_rates` (Managed by F-05 — SRS §3.3 Maintainability)
| Column | Type | Notes |
| :--- | :--- | :--- |
| `currency_code` | String(10), PK | `USD`, `JPY`, `SGD`, `THB`, `EUR` |
| `rate_to_jmd` | Numeric(12, 4) | Multiplier to Jamaican Dollars (JMD) |
| `updated_at` | DateTime | Last updated |

### `duty_tiers` (Managed by F-05 — SRS §3.3 Maintainability)
| Column | Type | Notes |
| :--- | :--- | :--- |
| `id` | Integer (PK) | Auto-increment |
| `label` | String(80) | e.g., `Small Engine (<= 1500cc)`, `Heavy Equipment` |
| `vehicle_category` | String(40) | `car`, `truck`, `bus`, `heavy_equipment` |
| `min_cc` | Integer | Minimum engine CC |
| `max_cc` | Integer | Maximum engine CC (nullable for no upper bound) |
| `duty_percentage` | Numeric(6, 2) | e.g., `45.00` for 45% |

### `users` (Staff Auth & RBAC — SRS §3.2 Security)
| Column | Type | Notes |
| :--- | :--- | :--- |
| `id` | Integer (PK) | Auto-increment |
| `username` | String(80), Unique | Login username |
| `email` | String(120), Unique | Staff email |
| `password_hash` | String(255) | Hashed via `werkzeug.security` |
| `role` | String(30) | `owner`, `purchasing_manager`, `sales_staff`, `internal_staff` |
| `is_active` | Boolean | Account status |

---

## 3. Public View Security Rule (SRS §1.5 & F-04 SR-3)

Any response rendered or returned to unauthenticated customers (**Ashaya's F-04**) **MUST ONLY** include safe fields:
- Allowed: `id`, `make`, `model`, `year`, `category`, `color`, `mileage_km`, `engine_cc`, `features`, `photo_urls`, `estimated_jmd_price` (from F-05), `public_availability_status` (`Available Now` / `Arriving Soon`), `estimated_arrival_window`.
- **FORBIDDEN in customer views:** `base_foreign_price`, `base_currency`, `bill_of_lading`, `deposit_paid`, supplier notes, internal purchase costs.
