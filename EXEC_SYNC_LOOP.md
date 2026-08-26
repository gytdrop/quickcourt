# Execution & Agent Update Protocol

### The 4-Step "Post-Exec" Sync Routine:
Run this sequence after every completed model, view, or controller milestone:

1. **Verify Local Build:**
   - Execute: `python3 odoo-bin -d test_db -u <your_module> --stop-after-init`
   - Ensure zero Python syntax errors or XML XPath parsing exceptions.

2. **Update Registry on Change:**
   - Did you introduce a new field, selection key, or compute method?
   - **MANDATORY:** Immediately add it to `SCHEMA_REGISTRY.md` and commit.

3. **Feed Context to Your Agent for the Next Prompt:**
   When starting the next task, prepend this prompt block:
   ```text
   Current Context:
   - Module: [quickcourt_core | quickcourt_ai_vendor | quickcourt_ai_player]
   - Synced Commit: [Latest commit SHA from origin/main]
   - Referenced Schema: Read SCHEMA_REGISTRY.md.
   
   Next Task:
   [Describe next specific feature to implement]
   ```

4. **Periodic Rebase:**
   - Every 2 hours, pull main into your feature branch to keep database schemas aligned across both teammates.
