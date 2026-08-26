# Git Workflow & Odoo Commit Guidelines

### 1. Branch Strategy
- Main Branch: `main` (Production/Evaluation ready - protected).
- Feature Branches:
  - Teammate A (Akthar): `feat/backend-vendor` (or `feat/akthar-backend-vendor`)
  - Teammate B (Ashrith): `feat/player-ai-portal` (or `feat/ashrith-player-ai-portal`)

### 2. Odoo Official Commit Standard
Format: `[TAG] module_name: short description in imperative present tense`

Allowed Tags:
- `[ADD]`: Addition of new models, views, or features.
- `[FIX]`: Bug fix, constraint correction, or typo fix.
- `[REF]`: Refactoring code without behavioral change.
- `[IMP]`: Improvement in performance or UI/UX.
- `[REM]`: Removal of deprecated code, models, or views.

Examples:
- `[ADD] quickcourt_core: implement court.slot model and overlap constraints`
- `[ADD] quickcourt_ai_vendor: add vision inspection model with auto-lock trigger`
- `[FIX] quickcourt_ai_player: handle timeout fallback in nlp chat controller`

### 3. Environment & Database Prerequisites
- **Odoo:** `17.0` | **Python:** `3.10` / `3.11` | **PostgreSQL:** `15.x` / `16.x`
- Full specifications documented in [ENVIRONMENT_REQUIREMENTS.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/ENVIRONMENT_REQUIREMENTS.md).

### 4. Sync & Merge Protocol
Before opening a PR or merging into main:
1. `git fetch origin`
2. `git rebase origin/main` (Resolve any local schema conflicts)
3. Run local test against PostgreSQL (`odoo` user, `5432` port):
   `python3 odoo-bin -d test_db --db_user=odoo --db_password=odoo -u hackathon_core,hackathon_feature_a,hackathon_feature_b --stop-after-init`
4. Push and merge clean linear history.
