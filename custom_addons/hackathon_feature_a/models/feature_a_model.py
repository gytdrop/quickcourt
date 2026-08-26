# Module: hackathon_feature_a / quickcourt_ai_vendor
# Teammate A: Akthar

from odoo import models, fields

class HackathonItemFeatureA(models.Model):
    _inherit = 'hackathon.item'  # Extends existing model without file conflicts

    feature_a_score = fields.Float(string='Feature A Score')


class CourtInspection(models.Model):
    """Vendor Inspection Model managed by Akthar (Teammate A).
    Automates vision inspection & court lock triggers.
    """
    _name = 'court.inspection'
    _description = 'Court Vision Inspection'

    court_id = fields.Many2one('quickcourt.court', string='Target Court', required=True, ondelete='cascade')
    severity = fields.Selection([
        ('normal', 'Normal'),
        ('critical', 'Critical')
    ], default='normal', string='Severity')
    status = fields.Selection([
        ('logged', 'Logged'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved')
    ], default='logged', string='Status')
