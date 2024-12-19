# -*- coding: utf-8 -*-
# import xmlrpc.client
# import datetime
# from odoo import http, Command
import requests

from odoo import http
from odoo.http import request
import json

class LeadController(http.Controller):
    @http.route('/lead/create', type='json', auth='public', methods=['POST'])
    def create_lead(self, **kw):
        try:
            JsonString = request.get_json_data()
            if not JsonString.get('name'):
                return {'error': 'Missing required field: name'}
                
            print("=======trcheck import=======")
            env = http.request.env 
            user_id = env.user.id
            print(user_id) 

            lead = request.env['crm.lead'].sudo().create([JsonString])
            return {'message': 'Lead created successfully', 'lead_id': lead.id}

        except Exception as e:
            return {'error': str(e)}


# class CrmCustomerRequestController(http.Controller):
#     @http.route('/leadcreate', auth='public')#, methods=['POST'], type='http')
#     def lead_create(self, **kw):
#         today = datetime.date.today().isoformat()
#         # return today
#         partner = request.env['res.partner'].search([], limit=1)
#         # print(partner.id)
#         products = request.env['product.template'].search([], limit=3)
#         # print(products)
#         JsonString = {
#             'name': "TrangPTH test odoo",
#             'type': "opportunity",
#             'email_from': "trcheck api create in odoo",
#             'partner_id': partner.id,
#             'date_deadline': today,
#             'description': "ghi chu noi bo",
#             'request_ids': [Command.create(
#                 {
#                     'product_id': rec.id,
#                     'date': today, 
#                     'qty': 1.0, 
#                 }) for rec in products
#             ]
            
#         }
#         return json.dumps(JsonString)
#         try: 
#             record = request.env['crm.lead'].create([JsonString])
#             output = "<h2>CREATE CRM LEAD</h2><br>"
#             output += "Partner: id = %s - name = %s" %(partner.id, partner.name)
#             output += "Products:<ul>" 
#             for rec in products:
#                 output += '<li>' + rec['name'] + '</li>'
#             output += '</ul>'
#             output += "done ===> opportunity_id : %s - name : %s" %(record.id, record.name)
#             print(request.env['crm.lead'].search([('id', '=', record.id)]))
#             return output
#         except Exception as e:
#             _logger.error("Error occurred: %s", str(e))
#             return "Error occurred: Failed"

#         # return request.render("crm_customer_request.detail", {})
#         # return {"id": record.id, "name": record.name}

