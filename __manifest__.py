# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Customer Request Management',
    'version': '1.0',
    'category': 'CRM/Customer_Request',
    'depends': [
        'product',
        'crm',
        'sale',
    ],
    'data': [
        "security/ir.model.access.csv",
        # "views/crm_customer_request_templates.xml",
        "views/crm_lead_views.xml",
        "views/crm_customer_request_views.xml",
        "views/customer_request_menus.xml",
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
