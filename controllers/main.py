# -*- coding: utf-8 -*-
import xmlrpc.client
import datetime
from odoo import http
from odoo.http import request
from collections import defaultdict
import requests
import json
from odoo import Command
import logging
_logger = logging.getLogger(__name__)
headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}
class CrmCustomerRequestController(http.Controller):
    @http.route('/leadcreate', auth='public')#, methods=['POST'], type='http')
    def lead_create(self, **kw):
        today = datetime.date.today().isoformat()
        # return today
        partner = request.env['res.partner'].search([], limit=1)
        # print(partner.id)
        products = request.env['product.template'].search([], limit=3)
        # print(products)
        JsonString = {
            'name': "TrangPTH test odoo",
            'type': "opportunity",
            'email_from': "trcheck api create in odoo",
            'partner_id': partner.id,
            'date_deadline': today,
            'description': "ghi chu noi bo",
            'request_ids': [Command.create(
                {
                    'product_id': rec.id,
                    'date': today, 
                    'qty': 1.0, 
                }) for rec in products
            ]
            
        }
        # return json.dumps(JsonString)
        try: 
            record = request.env['crm.lead'].create([JsonString])
            output = "<h2>CREATE CRM LEAD</h2><br>"
            output += "Partner: id = %s - name = %s" %(partner.id, partner.name)
            output += "Products:<ul>" 
            for rec in products:
                output += '<li>' + rec['name'] + '</li>'
            output += '</ul>'
            output += "done ===> opportunity_id : %s - name : %s" %(record.id, record.name)
            print(request.env['crm.lead'].search([('id', '=', record.id)]))
            return output
        except Exception as e:
            _logger.error("Error occurred: %s", str(e))
            return "Error occurred: Failed"

        # return {'id': record.id}
        # return json.dumps(JsonString)
        # return request.render("crm_customer_request.detail", {})
        # return {"id": record.id, "name": record.name}
        # return {'url': "/slides/%s" % (slug(lead))}

    # @route('/apipost', type='http', auth='user', website=True, methods=['POST'])
    # def deactivate_account(self, validation, password, **post):
