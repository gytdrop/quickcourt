# QuickCourt - Modular Odoo Hackathon Project

QuickCourt is a modular Odoo 17.0 application built for smart court venue management, vendor AI vision inspections, and player AI portal chat bookings.

---

### 👥 Team Assignments & Modules
- **Akthar (Teammate A):** Vendor AI Inspection System (`custom_addons/hackathon_feature_a` / `quickcourt_ai_vendor`) | Branch: `feat-backend-vendor`
- **Ashrith (Teammate B):** Player AI Portal & Chat Route (`custom_addons/hackathon_feature_b` / `quickcourt_ai_player`) | Branch: `feat-player-ai-portal`

---

### 📖 Single-Source-of-Truth GitHub Guides
- [TEAM_SYNC_GUIDE.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/TEAM_SYNC_GUIDE.md) – **Start Here!** Full team sync & onboarding instructions.
- [AGENTS.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/AGENTS.md) – Project architecture guidelines & constraints.
- [SCHEMA_REGISTRY.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/SCHEMA_REGISTRY.md) – Shared model hierarchy & variable registry.
- [CONTRACT.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/CONTRACT.md) – Model fields & API endpoint contracts.
- [GIT_GUIDELINES.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/GIT_GUIDELINES.md) – Official Odoo commit standards & rebase workflow.
- [ENVIRONMENT_REQUIREMENTS.md](file:///home/gytdrop/Documents/HACKATHONS/2026/odoo%20hackathon/odoo%20mock/quickcourt/ENVIRONMENT_REQUIREMENTS.md) – System stack & standalone mock execution.

---

### ⚡ Quick In-System Test Run
Run standalone mock tests directly in system memory without a live database:
```bash
python3 run_mock_system.py
```
