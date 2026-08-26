# Odoo Hackathon Project Guidelines & Agent Context

This repository follows a strict **modular Odoo architecture** to prevent git merge conflicts and ensure clear feature isolation across team members (**Akthar** & **Ashrith**) and AI coding assistants.

---

## 1. Project Structure

Custom modules live under `custom_addons/`:

```
custom_addons/
├── hackathon_core/          # Core models, security CSVs, and primary views
├── hackathon_feature_a/     # Teammate A (Akthar): Vendor AI Inspection module (quickcourt_ai_vendor)
├── hackathon_feature_b/     # Teammate B (Ashrith): Player AI Portal & Chat module (quickcourt_ai_player)
└── hackathon_feature_c/     # Teammate C's feature module
```

---

## 2. Standard Environment & Database Stack

To ensure seamless merging and schema synchronization, all teammates and agents must develop on:
- **Odoo Framework:** `17.0` (Community / Enterprise)
- **Python Runtime:** `Python 3.10` or `3.11`
- **PostgreSQL Database:** `PostgreSQL 15.x` or `16.x` (DB user: `odoo`, Port: `5432`, Target DB: `test_db`)
- **Extensions:** `unaccent`, `pg_trgm`
- **Full Specs & Packages:** See [ENVIRONMENT_REQUIREMENTS.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/ENVIRONMENT_REQUIREMENTS.md) and [requirements.txt](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/requirements.txt).

---

## 3. Strict Rules for Developers & AI Agents

1. **NEVER modify `hackathon_core` for feature-specific needs**:
   - `hackathon_core` is frozen after setup.
   - If your feature requires new fields or logic on existing models, extend them inside your feature module using `_inherit`.

2. **Use Python Model Inheritance (`_inherit`)**:
   ```python
   class HackathonItemFeatureA(models.Model):
       _inherit = 'hackathon.item'
       feature_a_score = fields.Float(string='Feature A Score')
   ```

3. **Use View Inheritance (`inherit_id`)**:
   - Extend XML views via `<xpath>` in your feature module's view files instead of editing `base_views.xml`.

4. **Consult & Update `CONTRACT.md` & `SCHEMA_REGISTRY.md` First**:
   - Before introducing new field names, model names, or method signatures, check `CONTRACT.md` to prevent duplication.

5. **Python & Odoo Conventions**:
   - Use snake_case for field names (`feature_a_score`, `ai_summary`).
   - Use dot notation for model names (`quickcourt.venue`, `quickcourt.court`, `court.slot`, `court.inspection`).
   - Ensure every addon folder has `__init__.py` and `__manifest__.py`.
