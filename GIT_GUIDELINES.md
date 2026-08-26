# Git Workflow & Odoo Commit Guidelines

### 1. Branch Strategy
- Main Branch: `main` (Production/Evaluation ready - protected).
- Feature Branches:
  - Teammate A: `feat/backend-vendor`
  - Teammate B: `feat/player-ai-portal`

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

### 3. Sync & Merge Protocol
Before opening a PR or merging into main:
1. `git fetch origin`
2. `git rebase origin/main` (Resolve any local schema conflicts)
3. Run local test: `python3 odoo-bin -d test_db -u quickcourt_core,quickcourt_ai_vendor,quickcourt_ai_player --stop-after-init`
4. Push and merge clean linear history.
