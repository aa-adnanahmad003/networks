from odoo import models, fields, api, _

class ResPartnerExt(models.Model):
    _inherit = 'res.partner'

    commission_agent_id = fields.Many2one('commission.agent', string='Commissioned Agent', ondelete='restrict')