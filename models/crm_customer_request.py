from odoo import fields, models, api

class CrmCustomerRequest(models.Model):
    _name = "crm.customer.request"
    _description = "Customer Request"
    _rec_name = "opportunity_id"
    # khai bao cac truong trong bang
    # product.template
    product_id = fields.Many2one('product.template', string="Product", required = True)
    # crm.lead
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity", required = True)
    # date, default = today
    date = fields.Date(string = "Date", default = fields.Date.today(), required = True)
    # description
    description = fields.Char(string = "Description")
    # qty default = 1
    qty = fields.Float(string = "Quantity", default = 1)

    @api.model
    def name_get(self):
        res =[]
        for record in self:
            res.append((record.id, '%s - %s' % (record.product_id.name, record.opportunity_id.name)))
        return res
