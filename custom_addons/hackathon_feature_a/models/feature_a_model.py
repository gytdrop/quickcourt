# Module: hackathon_feature_a / quickcourt_ai_vendor
# Teammate A: Akthar

from odoo import models, fields, api

class HackathonItemFeatureA(models.Model):
    _inherit = 'hackathon.item'  # Extends existing model without file conflicts

    feature_a_score = fields.Float(string='Feature A Score')


class CourtInspection(models.Model):
    """Vendor Inspection Model managed by Akthar (Teammate A).
    Automates vision inspection & court lock triggers.
    """
    _name = 'court.inspection'
    _description = 'Court Vision Inspection'

    name = fields.Char(string='Inspection Reference', required=True, default='INSP-NEW')
    inspection_date = fields.Datetime(string='Inspection Date', default=fields.Datetime.now, required=True)
    court_id = fields.Many2one('quickcourt.court', string='Target Court', required=True, ondelete='cascade')
    defect_type = fields.Selection([
        ('none', 'No Defects Detected'),
        ('net_damage', 'Net Damage'),
        ('surface_crack', 'Surface Crack / Turf Damage'),
        ('lighting_failure', 'Lighting Hardware Failure'),
        ('line_marking', 'Faded Line Markings')
    ], default='none', string='Defect Type')
    severity = fields.Selection([
        ('normal', 'Normal'),
        ('critical', 'Critical')
    ], default='normal', string='Severity')
    status = fields.Selection([
        ('logged', 'Logged'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved')
    ], default='logged', string='Status')
    feature_a_score = fields.Float(string='Quality Score (0-100)', default=100.0)
    ai_confidence = fields.Float(string='AI Vision Confidence', default=0.95)
    ai_inspection_notes = fields.Text(string='AI Inspection Notes')

    @api.model_create_multi
    def create(self, vals_list):
        records = super(CourtInspection, self).create(vals_list)
        for record in records:
            record._check_critical_court_lock()
        return records

    def write(self, vals):
        res = super(CourtInspection, self).write(vals)
        for record in self:
            record._check_critical_court_lock()
        return res

    def _check_critical_court_lock(self):
        """Auto-lock court state to under_maintenance if severity is critical and inspection is active."""
        if self.severity == 'critical' and self.status in ['logged', 'in_progress']:
            if self.court_id and self.court_id.state != 'under_maintenance':
                self.court_id.write({'state': 'under_maintenance'})
                # Lock open reservation slots for this court
                slots = self.env['court.slot'].search([
                    ('court_id', '=', self.court_id.id),
                    ('state', '=', 'available')
                ])
                if slots:
                    slots.write({'state': 'maintenance_locked'})

    def action_run_vision_ai(self):
        """Simulate AI Vision Inspection processing on court image/data."""
        for record in self:
            if record.defect_type == 'none':
                record.feature_a_score = 95.5
                record.severity = 'normal'
                record.ai_inspection_notes = "AI Vision Scan Complete: Court surface and net condition optimal."
            else:
                record.feature_a_score = 42.0
                record.severity = 'critical'
                record.ai_inspection_notes = f"AI Vision Alert: Severe defect identified ({record.defect_type}). Automatic court maintenance lock triggered."
            record._check_critical_court_lock()

    def action_resolve_inspection(self):
        """Mark inspection as resolved and unlock court if no critical defects remain."""
        for record in self:
            record.write({'status': 'resolved'})
            # Check if court has remaining critical active inspections
            active_critical = self.search([
                ('court_id', '=', record.court_id.id),
                ('severity', '=', 'critical'),
                ('status', 'in', ['logged', 'in_progress']),
                ('id', '!=', record.id)
            ])
            if not active_critical and record.court_id:
                record.court_id.write({'state': 'available'})

    def action_lock_court(self):
        """Manually trigger court maintenance lock."""
        for record in self:
            record.write({'severity': 'critical', 'status': 'in_progress'})
            record._check_critical_court_lock()
