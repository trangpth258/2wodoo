from odoo import fields, models, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    #one2many
    request_ids = fields.One2many('crm.customer.request', 'opportunity_id', string='Customer Requests')
    requests_count = fields.Float(compute='_compute_customer_request_data', string="Expected Sales")
    requests_total = fields.Monetary(string="Expected Revenue", compute='_compute_customer_request_data', currency_field='currency_id')

    currency_id = fields.Many2one('res.currency', compute='_get_company_currency', readonly=True, string='Currency')

    @api.depends('request_ids.opportunity_id', 'request_ids.qty')
    def _compute_customer_request_data(self):
        for lead in self:
            lead.requests_count = sum(
                opp.qty for opp in lead.request_ids
            )
            lead.requests_total = sum(
                rec.qty * rec.product_id.list_price for rec in lead.request_ids
            )

    @api.model
    def _get_company_currency(self):
        for partner in self:
            if partner.company_id:
                partner.currency_id = partner.sudo().company_id.currency_id
            else:
                partner.currency_id = self.env.company.currency_id
    


    