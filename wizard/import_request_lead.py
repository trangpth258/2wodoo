# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import _, api, fields, models
from odoo.exceptions import UserError
import xlrd
import openpyxl
from xlrd import open_workbook
import base64
import datetime
import odoo

from odoo.http import content_disposition

class ImportRequestLead(models.TransientModel):
    _name = 'import.request.lead'
    _description = 'Import Page Customer Request'
    # FIELD
    excel_file = fields.Binary(string='File Excel')
    
    #METHOD
    # @api.model
    @staticmethod
    def import_data(self):
        # print("==============check file excel import begin ==============")
        file_name = base64.b64decode(self.excel_file) #convert file_name
        workbook = xlrd.open_workbook(file_contents=file_name) #get book
        worksheet = workbook.sheet_by_index(0) #get sheet 1: index = 0

        opportunity_id = self.env.context.get('default_crm_lead_id')
        lead = self.env['crm.lead'].browse(opportunity_id)
        
        if lead.id:
            today = datetime.date.today().isoformat()
            default_products = [product.id for product in self.env['product.template'].search([])]

            for row_index in range(1, worksheet.nrows):
                row = worksheet.row_values(row_index)
                if row[0] in default_products:
                    lead.write({
                        'request_ids': [(0, 0, {
                            'product_id': row[0],
                            'date': today,
                            'qty': row[1]
                        })]
                    })

        # print("==============check file excel import end ==============")

        return {'type': 'ir.actions.act_window_close'}

    def action_download_template(self):
        # return [{
        #     'label': _('Import Template for Leads & Opportunities'),
        #     'template': '/crm_customer_request/static/xls/crm_lead.xls'
        # }]
        print("==============check file excel import ==============")
        
        return [{
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s/%s?download=true' % (
                self._name, '/crm_customer_request/static/xls/crm_lead.xls'),
            'target': 'new'
        }]

   

