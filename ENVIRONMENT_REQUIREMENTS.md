# QuickCourt Environment & System Requirements

To ensure zero database schema mismatches, dependency conflicts, or build failures when teammates (**Akthar** & **Ashrith**) and AI agents merge branches into `main`, all environments strictly support both **in-system Python mock execution** and standard Odoo ORM deployment.

---

### 1. Core Stack Specifications

| Component | Version Requirement | Notes / Usage |
| :--- | :--- | :--- |
| **Odoo Framework** | `Odoo 17.0` | Base framework (`hackathon_core`, `hackathon_feature_a`, `hackathon_feature_b`) |
| **Python Runtime** | `Python 3.10.x`+ | Required by Odoo 17.0 core ORM, mock runners, and AI integrations |
| **PostgreSQL / Standalone** | `PostgreSQL 15.x/16.x` or In-System Memory | System memory mock runner supported (`python3 run_mock_system.py`) |
| **Operating System** | `Linux (Ubuntu 22.04 LTS)` / `macOS 13+` / `WSL2` | POSIX environment standard |

---

### 2. In-System Mock Execution (No DB Setup Required)

For local mock testing directly inside system memory:
```bash
python3 run_mock_system.py
```
This executes:
- Teammate A (Akthar) Vendor AI inspection & automatic court maintenance locking.
- Teammate B (Ashrith) Player AI Chat controller route (`POST /quickcourt/ai/chat`).

---

### 3. PostgreSQL & Odoo Configuration (Full Production Deployment)

- **Database Host & Port:** `localhost:5432`
- **Standard Superuser / Role:** `odoo` (with `CREATEDB` privileges)
- **Standard Test Database Name:** `test_db`
- **Required PostgreSQL Extensions:** `unaccent`, `pg_trgm`

---

### 4. Teammate Module & In-System Sync Routine

Before committing or opening PRs:

1. **Run In-System Mock Test:**
   `python3 run_mock_system.py`

2. **Verify Odoo Module Compilation (If Running Odoo Server):**
   ```bash
   python3 odoo-bin -d test_db --db_user=odoo --db_password=odoo -u hackathon_core,hackathon_feature_a,hackathon_feature_b --stop-after-init
   ```
