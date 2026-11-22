# Karmanjahni Company Limited — Brand & UI Design Guide

All team members MUST import `/resources/design/theme.css` so that every feature looks like one cohesive Karmanjahni web application when fused.

---

## 1. Brand Identity
- **Company Name:** Karmanjahni Company Limited
- **Established:** Since 2006
- **Location:** Kingston, Jamaica (1 Perth Avenue / Maxfield Ave area)
- **Instagram:** https://www.instagram.com/karmanjahni_ja/?hl=en
- **FindYello Profile:** https://www.findyello.com/jamaica/karmanjahni-co-ltd/profile/
- **Logo Asset:** `resources/design/assets/karmanjahni-logo.jpg`
- **Brand Personality:** Premium, trustworthy Jamaican vehicle & heavy equipment importer known for unique colored, high-feature vehicles (sunroofs, rims, keyless entry).

---

## 2. Color Palette (Extracted from Official Crest Logo)

| Token | Hex | Usage |
| :--- | :--- | :--- |
| `--kj-navy-primary` | `#0A165E` | Primary headers, navbar, primary buttons, brand crest blue |
| `--kj-navy-dark` | `#060D38` | Deep sidebar/footer, dark hero accents |
| `--kj-gold-accent` | `#F2A922` | Call-to-action highlights, active nav underline, car crest gold |
| `--kj-gold-trim` | `#C8A26A` | Subtle card borders, metallic crest border accents |
| `--kj-cream` | `#FFF8E7` | Wordmark light tint, soft callout banners |
| `--kj-bg` | `#F4F6FA` | Page background |
| `--kj-surface` | `#FFFFFF` | Cards, forms, vehicle spec sheets |
| `--kj-text-dark` | `#0F172A` | Primary headings & body text |
| `--kj-text-muted` | `#475569` | Secondary labels & subtitles |

### Semantic Status Colors (Required by SRS F-01 & F-06)
| Status | Text Hex | Background Hex | CSS Class |
| :--- | :--- | :--- | :--- |
| **Delayed** (Visibly flagged per F-01 AC-2) | `#B91C1C` | `#FEE2E2` | `.badge-delayed` |
| **In Transit** | `#B45309` | `#FEF3C7` | `.badge-in-transit` |
| **Arrived / On Lot** | `#15803D` | `#DCFCE7` | `.badge-arrived` |

---

## 3. Responsive & Tablet Ergonomics (Required by SRS F-03)
- **Desktop:** `>= 1024px` (Purchasing Manager data entry & Admin rate management)
- **Tablet (Primary Lot Device):** `768px – 1023px` (Sales Staff standing on the car lot with customers)
- **Mobile:** `< 768px` (Customers browsing upcoming stock on phones)
- **Touch Targets:** All buttons, dropdowns, search fields, and gallery arrows MUST be at least `44px x 44px`.

---

## 4. How to Use in Your HTML Templates
Every template that extends `base_staff.html` or `base_public.html` automatically loads:
```html
<link rel="stylesheet" href="/resources/design/theme.css">
```
Use the CSS variables (e.g., `var(--kj-navy-primary)`, `var(--kj-gold-accent)`) in your module's `.css` file instead of hardcoding random colors.
