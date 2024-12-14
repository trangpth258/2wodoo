# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    #=== FIELDS ===#

    #=== METHODS ===#

    @api.onchange('opportunity_id')
    def _onchange_opportunity_id(self):
        if self.opportunity_id:
            if not self.order_line:
                #Query
                query = """
                    select product_id, sum(qty) as qty_total 
                        from crm_customer_request 
                            where opportunity_id = %s
                                group by product_id 
                        """ % (self.opportunity_id.id)
                self._cr.execute(query)
                result = self.env.cr.dictfetchall()
                # Fill data to order_line
                default_products = [product.id for product in self.env['product.product'].search([])]
                for record in result:
                    if record['product_id'] in default_products:
                        self.order_line = [(0, 0, {
                            'product_id': record['product_id'],
                            'product_uom_qty': record['qty_total']
                        })]
    def default_get(self, fields):
        res = super(SaleOrder, self).default_get(fields)
        # res['client_order_ref'] = res['opportunity_id']
        print(res)
        return res