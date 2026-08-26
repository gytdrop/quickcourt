# Module: hackathon_feature_b / quickcourt_ai_player
# Teammate B: Ashrith

from odoo import models, fields

class HackathonItemFeatureB(models.Model):
    _inherit = 'hackathon.item'  # Extends hackathon.item without touching core files

    ai_summary = fields.Text(string='AI Summary')

    def action_run_analysis(self):
        for record in self:
            record.ai_summary = f"Analysis generated for item: {record.name}"


class CourtSlotFeatureB(models.Model):
    """Player AI Portal Model extension managed by Ashrith (Teammate B).
    Inherits court.slot for NLP chat query processing and booking search.
    """
    _inherit = 'court.slot'

    player_notes = fields.Text(string='Player Booking Notes')
