# Execution & Agent Update Protocol

### The 4-Step "Post-Exec" Sync Routine:
Run this sequence after every completed model, view, or controller milestone:

1. **Verify Local Build (In-System or Odoo DB):**
   - In-System Standalone Test: `python3 run_mock_system.py`
   - (Optional Odoo DB): `python3 odoo-bin -d test_db --db_user=odoo --db_password=odoo -u <your_module> --stop-after-init`
   - Ensure zero Python syntax errors or XML XPath parsing exceptions.

2. **Update Registry on Change:**
   - Did you introduce a new field, selection key, or compute method?
   - **MANDATORY:** Immediately add it to `SCHEMA_REGISTRY.md` and commit.

3. **Active Teammate Execution Context:**

```text
Current Context:
- Role: Teammate A (Akthar)
- Module: quickcourt_ai_vendor (custom_addons/hackathon_feature_a)
- Branch: feat-backend-vendor
- Synced Commit: 57b6f67
- Referenced Schema: Read SCHEMA_REGISTRY.md and CONTRACT.md

Completed Task:
- Implemented court.inspection model, automated critical severity court lock, vision scan AI method, ir.model.access.csv security rules, and XML views/menus.

Next Task:
- Ready for next Vendor AI module feature (e.g. vision defect image attachment handler or vendor dashboard summary widget).
```

4. **Periodic Rebase:**
   - Every 2 hours, pull main into your feature branch to keep database schemas aligned across both teammates (Akthar & Ashrith).
