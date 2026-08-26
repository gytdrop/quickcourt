# QuickCourt Team Sync & In-System Development Guide

This tracked guide ensures all teammates (**Akthar - Team A**, **Ashrith - Team B**) and AI coding agents remain 100% synchronized across git branches without merge conflicts.

---

### 1. Local `EXEC_SYNC_LOOP.md` Isolation (Git Ignored)

> [!NOTE]
> `EXEC_SYNC_LOOP.md` is listed in `.gitignore` so each developer maintains their own local execution context without causing git merge conflicts.

When starting a session or feature branch, create your local `EXEC_SYNC_LOOP.md` using this template:

```text
Current Context:
- Role: [Teammate A (Akthar) | Teammate B (Ashrith)]
- Module: [quickcourt_ai_vendor | quickcourt_ai_player]
- Branch: [feat-backend-vendor | feat-player-ai-portal]
- Synced Commit: [Latest commit SHA from origin/main]
- Schema & Contracts: Refer to SCHEMA_REGISTRY.md and CONTRACT.md

Next Task:
[Describe next specific feature to implement]
```

---

### 2. Standalone In-System Mock Execution (No Live Database Required)

All models and AI routes are tested directly inside system memory without needing a live external PostgreSQL server.

Run the test suite in terminal:
```bash
python3 run_mock_system.py
```

This validates:
- **Teammate A (Akthar):** `court.inspection` creation, Vision AI defect scoring, and automatic court maintenance locking.
- **Teammate B (Ashrith):** `POST /quickcourt/ai/chat` Player AI route filtering available slots.

---

### 3. Teammate Module Ownership & Branches

| Teammate | Role / Feature | Module Directory | Branch Name |
| :--- | :--- | :--- | :--- |
| **Akthar (Team A)** | Vendor AI Inspection & Auto-Lock | `custom_addons/hackathon_feature_a` | `feat-backend-vendor` |
| **Ashrith (Team B)** | Player AI Portal & Chat Route | `custom_addons/hackathon_feature_b` | `feat-player-ai-portal` |
| **Core Layer** | Shared Core Models (`venue`, `court`, `slot`) | `custom_addons/hackathon_core` | `main` (Frozen) |

---

### 4. Official Odoo Commit Tags

All commits pushed to GitHub must follow the official standard:
Format: `[TAG] module_name: short description in imperative present tense`

- `[ADD]`: New models, views, controllers, or features.
- `[FIX]`: Bug fixes or constraint corrections.
- `[REF]`: Refactoring code without behavioral change.
- `[IMP]`: Improvements in performance or UI/UX.

Examples:
- `[ADD] quickcourt_ai_vendor: implement court.inspection model, vision scan AI, and auto court lock`
- `[ADD] quickcourt_ai_player: implement POST /quickcourt/ai/chat controller route`

---

### 5. Single-Source-of-Truth Reference Files
- [AGENTS.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/AGENTS.md) – Project guidelines & rules
- [SCHEMA_REGISTRY.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/SCHEMA_REGISTRY.md) – Shared model hierarchies & fields
- [CONTRACT.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/CONTRACT.md) – Technical field & API agreements
- [GIT_GUIDELINES.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/GIT_GUIDELINES.md) – Git workflow protocols
- [ENVIRONMENT_REQUIREMENTS.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/ENVIRONMENT_REQUIREMENTS.md) – System specs & dependencies
