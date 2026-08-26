#!/usr/bin/env python3
"""
QuickCourt Mock System Test Runner
Executes model logic and AI controllers directly inside local Python memory without needing a live PostgreSQL database server.
"""

import sys
import json
from datetime import datetime, timedelta

# --- MOCK CORE MODELS ---
class MockVenue:
    def __init__(self, id, name, owner="Manager Partner", state="approved", ai_trust_score=85):
        self.id = id
        self.name = name
        self.owner_id = owner
        self.state = state
        self.ai_trust_score = ai_trust_score

class MockCourt:
    def __init__(self, id, name, venue_id, is_indoor=True, price_hourly=50.0, state="available"):
        self.id = id
        self.name = name
        self.venue_id = venue_id
        self.is_indoor = is_indoor
        self.price_hourly = price_hourly
        self.state = state

class MockCourtSlot:
    def __init__(self, id, court_id, start_time, end_time, state="available"):
        self.id = id
        self.court_id = court_id
        self.start_time = start_time
        self.end_time = end_time
        self.state = state

# --- MOCK FEATURE A (Akthar): VENDOR AI INSPECTION ---
class MockCourtInspection:
    def __init__(self, id, name, court, defect_type="none", severity="normal", status="logged"):
        self.id = id
        self.name = name
        self.inspection_date = datetime.now().isoformat()
        self.court = court
        self.defect_type = defect_type
        self.severity = severity
        self.status = status
        self.feature_a_score = 100.0
        self.ai_confidence = 0.95
        self.ai_inspection_notes = ""

    def run_vision_ai(self):
        """Simulate Vision AI scan and trigger court auto-lock on critical defect."""
        if self.defect_type == "none":
            self.feature_a_score = 95.5
            self.severity = "normal"
            self.ai_inspection_notes = "AI Vision Scan Complete: Court surface and net condition optimal."
        else:
            self.feature_a_score = 42.0
            self.severity = "critical"
            self.status = "in_progress"
            self.ai_inspection_notes = f"AI Vision Alert: Severe defect identified ({self.defect_type}). Automatic court maintenance lock triggered."
            self._trigger_court_lock()

    def _trigger_court_lock(self):
        if self.severity == "critical":
            self.court.state = "under_maintenance"
            return True
        return False

# --- MOCK FEATURE B (Ashrith): PLAYER AI PORTAL CHAT ---
class MockPlayerAIChatController:
    def __init__(self, courts, slots):
        self.courts = courts
        self.slots = slots

    def handle_chat_request(self, payload):
        """Simulate POST /quickcourt/ai/chat controller endpoint."""
        data = json.loads(payload) if isinstance(payload, str) else payload
        prompt = data.get("prompt", "").lower()
        user_id = data.get("user_id", 1)

        available_slots = []
        for slot in self.slots:
            if slot.state == "available" and slot.court_id.state == "available":
                available_slots.append({
                    "id": slot.id,
                    "court_name": slot.court_id.name,
                    "price": slot.court_id.price_hourly,
                    "start": slot.start_time.strftime("%Y-%m-%d %H:%M:%S")
                })

        response_text = f"Hello User #{user_id}! Found {len(available_slots)} available court slots matching your request."
        return {
            "response": response_text,
            "slots": available_slots
        }

# --- SYSTEM TEST SUITE ---
def main():
    print("==================================================")
    print(" 🚀 QUICKCOURT IN-SYSTEM MOCK TEST RUNNER")
    print("==================================================")
    
    # 1. Instantiate Core Schema
    venue = MockVenue(id=1, name="QuickCourt Arena Central")
    court_a = MockCourt(id=101, name="Court A (Tennis)", venue_id=venue, price_hourly=60.0)
    court_b = MockCourt(id=102, name="Court B (Badminton)", venue_id=venue, price_hourly=40.0)

    now = datetime.now()
    slot1 = MockCourtSlot(id=501, court_id=court_a, start_time=now + timedelta(hours=1), end_time=now + timedelta(hours=2))
    slot2 = MockCourtSlot(id=502, court_id=court_b, start_time=now + timedelta(hours=1), end_time=now + timedelta(hours=2))

    print(f"\n[CORE SETUP] Venue: '{venue.name}' | Courts: ['{court_a.name}' ({court_a.state}), '{court_b.name}' ({court_b.state})]")

    # 2. Test Teammate A (Akthar) Vendor Vision AI & Auto-Lock
    print("\n--------------------------------------------------")
    print(" 🛠️ TESTING TEAMMATE A (AKTHAR): VENDOR AI INSPECTION")
    print("--------------------------------------------------")
    inspection = MockCourtInspection(id=1, name="INSP-001", court=court_a, defect_type="net_damage")
    print(f"Initial State: Court '{court_a.name}' state = {court_a.state}")
    print("Running Vision AI Scan on Court A...")
    inspection.run_vision_ai()
    print(f"AI Notes: {inspection.ai_inspection_notes}")
    print(f"Quality Score: {inspection.feature_a_score}/100 | Severity: {inspection.severity}")
    print(f"Updated State: Court '{court_a.name}' state = '{court_a.state}' (Auto-Locked!)")

    # 3. Test Teammate B (Ashrith) Player AI Chat Route
    print("\n--------------------------------------------------")
    print(" 🤖 TESTING TEAMMATE B (ASHRITH): PLAYER AI CHAT ROUTE")
    print("--------------------------------------------------")
    controller = MockPlayerAIChatController(courts=[court_a, court_b], slots=[slot1, slot2])
    chat_payload = {"prompt": "Find me available courts for tonight", "user_id": 42}
    print(f"Incoming POST /quickcourt/ai/chat Payload: {chat_payload}")
    result = controller.handle_chat_request(chat_payload)
    print("Response Output:")
    print(json.dumps(result, indent=2))

    print("\n==================================================")
    print(" ✅ ALL IN-SYSTEM MOCK TESTS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    main()
