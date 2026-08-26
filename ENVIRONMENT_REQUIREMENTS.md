# QuickCourt Environment & System Requirements

To ensure zero database schema mismatches, dependency conflicts, or build failures when teammates (**Akthar** & **Ashrith**) and AI agents merge branches into `main`, all environments must strictly conform to these standardized specifications.

---

### 1. Core Stack Specifications

| Component | Version Requirement | Notes / Usage |
| :--- | :--- | :--- |
| **Odoo Framework** | `Odoo 17.0` | Base framework (`hackathon_core`, `hackathon_feature_a`, `hackathon_feature_b`) |
| **Python Runtime** | `Python 3.10.x` or `3.11.x` | Required by Odoo 17.0 core ORM and AI integrations |
| **PostgreSQL Database** | `PostgreSQL 15.x` or `16.x` | Relational DB engine with `unaccent` & `pg_trgm` extensions |
| **Operating System** | `Linux (Ubuntu 22.04 LTS)` / `macOS 13+` / `WSL2` | POSIX environment standard |

---

### 2. PostgreSQL Configuration

- **Database Host & Port:** `localhost:5432`
- **Standard Superuser / Role:** `odoo` (with `CREATEDB` and `NOSUPERUSER` privileges)
- **Standard Test Database Name:** `test_db` (or `quickcourt_dev`)
- **Required PostgreSQL Extensions:**
  ```sql
  CREATE EXTENSION IF NOT EXISTS unaccent;
  CREATE EXTENSION IF NOT EXISTS pg_trgm;
  ```
- **Connection Flags for CLI Execution:**
  `--db_host=localhost --db_port=5432 --db_user=odoo --db_password=odoo`

---

### 3. Python Package Dependencies

All Python packages must be installed in a virtual environment (`.venv`):

```text
# Base Odoo & Database Drivers
psycopg2-binary>=2.9.6
Werkzeug>=2.3.7
Jinja2>=3.1.2
requests>=2.31.0
Pillow>=10.0.0

# AI & Extension Dependencies (Used by Akthar & Ashrith)
pydantic>=2.0.0
google-generativeai>=0.3.0
```

Install via:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### 4. Teammate Module & Database Sync Routine

Before running Odoo module upgrades or merging branches:

1. **Verify PostgreSQL Connection:**
   `pg_isready -h localhost -p 5432 -U odoo`

2. **Execute Unified Module Update & Validation:**
   ```bash
   python3 odoo-bin -d test_db \
     --db_user=odoo \
     --db_password=odoo \
     -u hackathon_core,hackathon_feature_a,hackathon_feature_b \
     --stop-after-init
   ```
