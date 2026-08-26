# QuickCourt Schema & Variable Registry

### 1. Model Hierarchy & Inheritance
quickcourt.venue (Core)
  └── quickcourt.court (Core)
        ├── court.slot (Core / calendar.event)
        │     └── (Inherited by: quickcourt_ai_player for booking queries)
        ├── court.inspection (quickcourt_ai_vendor)
        └── (Inherited by: quickcourt_ai_admin for trust score)

### 2. Standardized Field & Variable Names

| Model | Field Name | Type | Allowed Values / Format | Description |
| :--- | :--- | :--- | :--- | :--- |
| `quickcourt.venue` | `name` | Char | String | Venue Title |
| `quickcourt.venue` | `owner_id` | Many2one | `res.partner` | Venue Manager/Owner |
| `quickcourt.venue` | `state` | Selection | `draft`, `pending`, `approved`, `rejected` | Lifecycle stage |
| `quickcourt.venue` | `ai_trust_score` | Integer | `0` to `100` | Populated by Admin AI module |
| `quickcourt.court` | `name` | Char | String (e.g., "Court A") | Court identifier |
| `quickcourt.court` | `venue_id` | Many2one | `quickcourt.venue` | Parent venue link |
| `quickcourt.court` | `is_indoor` | Boolean | `True` / `False` | Weather check flag |
| `quickcourt.court` | `price_hourly` | Float | Currency | Base price per hour |
| `quickcourt.court` | `state` | Selection | `available`, `under_maintenance`, `decommissioned` | Operating state |
| `court.slot` | `court_id` | Many2one | `quickcourt.court` | Target court |
| `court.slot` | `start_time` | Datetime | UTC Timestamp | Slot start time |
| `court.slot` | `end_time` | Datetime | UTC Timestamp | Slot end time |
| `court.slot` | `state` | Selection | `available`, `booked`, `maintenance_locked` | Reservation status |
| `court.inspection` | `court_id` | Many2one | `quickcourt.court` | Target court |
| `court.inspection` | `severity` | Selection | `normal`, `critical` | Critical triggers court lock |
| `court.inspection` | `status` | Selection | `logged`, `in_progress`, `resolved` | Inspection lifecycle |

### 3. API & Controller Contracts
- Player Chat Route: `POST /quickcourt/ai/chat`
  - Input JSON: `{"prompt": "string", "user_id": int}`
  - Output JSON: `{"response": "string", "slots": [{"id": int, "court_name": "string", "price": float, "start": "string"}]}`
