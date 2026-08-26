# QuickCourt Schema & Variable Registry

### 1. Model Hierarchy & Inheritance
quickcourt.venue (Core)
  └── quickcourt.court (Core)
        ├── court.slot (Core / calendar.event)
        │     └── (Inherited by: quickcourt_ai_player / hackathon_feature_b [Ashrith] for booking queries)
        ├── court.inspection (quickcourt_ai_vendor / hackathon_feature_a [Akthar])
        └── (Inherited by: quickcourt_ai_admin for trust score)

### 2. Standardized Field & Variable Names

| Model | Field Name | Type | Allowed Values / Format | Owner / Module | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `quickcourt.venue` | `name` | Char | String | Core (`hackathon_core`) | Venue Title |
| `quickcourt.venue` | `owner_id` | Many2one | `res.partner` | Core (`hackathon_core`) | Venue Manager/Owner |
| `quickcourt.venue` | `state` | Selection | `draft`, `pending`, `approved`, `rejected` | Core (`hackathon_core`) | Lifecycle stage |
| `quickcourt.venue` | `ai_trust_score` | Integer | `0` to `100` | Admin AI | Populated by Admin AI module |
| `quickcourt.court` | `name` | Char | String (e.g., "Court A") | Core (`hackathon_core`) | Court identifier |
| `quickcourt.court` | `venue_id` | Many2one | `quickcourt.venue` | Core (`hackathon_core`) | Parent venue link |
| `quickcourt.court` | `is_indoor` | Boolean | `True` / `False` | Core (`hackathon_core`) | Weather check flag |
| `quickcourt.court` | `price_hourly` | Float | Currency | Core (`hackathon_core`) | Base price per hour |
| `quickcourt.court` | `state` | Selection | `available`, `under_maintenance`, `decommissioned` | Core (`hackathon_core`) | Operating state |
| `court.slot` | `court_id` | Many2one | `quickcourt.court` | Core (`hackathon_core`) | Target court |
| `court.slot` | `start_time` | Datetime | UTC Timestamp | Core (`hackathon_core`) | Slot start time |
| `court.slot` | `end_time` | Datetime | UTC Timestamp | Core (`hackathon_core`) | Slot end time |
| `court.slot` | `state` | Selection | `available`, `booked`, `maintenance_locked` | Core (`hackathon_core`) | Reservation status |
| `court.inspection` | `court_id` | Many2one | `quickcourt.court` | Akthar (`hackathon_feature_a`) | Target court |
| `court.inspection` | `severity` | Selection | `normal`, `critical` | Akthar (`hackathon_feature_a`) | Critical triggers court lock |
| `court.inspection` | `status` | Selection | `logged`, `in_progress`, `resolved` | Akthar (`hackathon_feature_a`) | Inspection lifecycle |

### 3. API & Controller Contracts
- Player Chat Route: `POST /quickcourt/ai/chat` (Maintained by Teammate B: Ashrith)
  - Input JSON: `{"prompt": "string", "user_id": int}`
  - Output JSON: `{"response": "string", "slots": [{"id": int, "court_name": "string", "price": float, "start": "string"}]}`
