from odoo import models, fields

class HackathonBaseItem(models.Model):
    _name = 'hackathon.item'
    _description = 'Core Hackathon Entity'

    name = fields.Char(string='Item Name', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Completed')
    ], default='draft', string='Status')


class QuickcourtVenue(models.Model):
    _name = 'quickcourt.venue'
    _description = 'QuickCourt Venue'

    name = fields.Char(string='Venue Title', required=True)
    owner_id = fields.Many2one('res.partner', string='Venue Manager/Owner')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='draft', string='Lifecycle Stage')
    ai_trust_score = fields.Integer(string='AI Trust Score', default=0)


class QuickcourtCourt(models.Model):
    _name = 'quickcourt.court'
    _description = 'QuickCourt Court'

    name = fields.Char(string='Court Identifier', required=True)
    venue_id = fields.Many2one('quickcourt.venue', string='Parent Venue', required=True, ondelete='cascade')
    is_indoor = fields.Boolean(string='Is Indoor', default=False)
    price_hourly = fields.Float(string='Hourly Rate')
    state = fields.Selection([
        ('available', 'Available'),
        ('under_maintenance', 'Under Maintenance'),
        ('decommissioned', 'Decommissioned')
    ], default='available', string='Operating State')


class CourtSlot(models.Model):
    _name = 'court.slot'
    _description = 'Court Reservation Slot'

    court_id = fields.Many2one('quickcourt.court', string='Target Court', required=True, ondelete='cascade')
    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time', required=True)
    state = fields.Selection([
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('maintenance_locked', 'Maintenance Locked')
    ], default='available', string='Reservation Status')
