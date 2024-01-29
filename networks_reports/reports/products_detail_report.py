from odoo import _,api, fields, models
from odoo.exceptions import AccessError, UserError, ValidationError


class ProductsDetail(models.AbstractModel):
    _name = 'report.networks_reports.products_detail_template'
    _description = 'Products Detail QWeb PDF Reports'

    @api.model
    def _get_report_values(self, docids, data):
        if data['product_id']:
            doc = self.env['account.move'].search([('invoice_date', '>=', data['start_date']), ('invoice_date', '<=', data['end_date']), ('state', '=', 'posted'), ('move_type', '=', 'out_invoice')]).invoice_line_ids.filtered(lambda l: l.product_id.id == data['product_id'])
        else:
            doc = self.env['account.move'].search([('invoice_date', '>=', data['start_date']), ('invoice_date', '<=', data['end_date']), ('state', '=', 'posted'), ('move_type', '=', 'out_invoice')])
        if doc:
            return {
                'docs': doc,
            }
        else:
            raise ValidationError('No Invoice is available.')