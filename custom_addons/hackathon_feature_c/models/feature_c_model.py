from odoo import models, fields

class HackathonItemFeatureC(models.Model):
    _inherit = 'hackathon.item'  # Extends hackathon.item without touching core files

    feature_c_notes = fields.Text(string='Feature C Notes')
