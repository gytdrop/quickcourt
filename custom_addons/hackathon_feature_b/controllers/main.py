# Module: hackathon_feature_b / quickcourt_ai_player
# Teammate B: Ashrith

from odoo import http
from odoo.http import request
import json

class QuickCourtWebsiteController(http.Controller):

    @http.route('/quickcourt', type='http', auth='public', website=True)
    def quickcourt_portal_page(self, **kw):
        """Render main player portal page listing sports venues and available courts."""
        venues = request.env['quickcourt.venue'].sudo().search([('state', '=', 'approved')])
        courts = request.env['quickcourt.court'].sudo().search([('state', '=', 'available')])
        slots = request.env['court.slot'].sudo().search([('state', '=', 'available')], limit=10)

        values = {
            'venues': venues,
            'courts': courts,
            'slots': slots,
        }
        return request.render('hackathon_feature_b.player_portal_page', values)

    @http.route('/quickcourt/ai/chat', type='json', auth='public', website=True, methods=['POST'], csrf=False)
    def quickcourt_ai_chat_endpoint(self, **post):
        """Strict JSON contract endpoint for player AI natural language court search."""
        data = request.get_json_data() or {}
        prompt = data.get('prompt', '').lower()
        
        # Query available court slots
        available_slots = request.env['court.slot'].sudo().search([
            ('state', '=', 'available'),
            ('court_id.state', '=', 'available')
        ], limit=5)

        matched_slots = []
        for slot in available_slots:
            matched_slots.append({
                'slot_id': slot.id,
                'court_name': slot.court_id.name,
                'time_range': f"{slot.start_time.strftime('%H:%M')} - {slot.end_time.strftime('%H:%M')}" if slot.start_time and slot.end_time else "18:00 - 19:00",
                'price': slot.court_id.price_hourly or 50.0,
                'weather_warning': not slot.court_id.is_indoor
            })

        message = f"Found {len(matched_slots)} available courts matching your request!"
        if 'indoor' in prompt:
            matched_slots = [s for s in matched_slots if not s['weather_warning']]
            message = f"Filtered {len(matched_slots)} indoor courts matching your criteria."

        return {
            'assistant_message': message,
            'matched_slots': matched_slots
        }
