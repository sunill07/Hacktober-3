# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "Chatter Logs",
    "version": "17.0.0.0",
    "category": "Chatter Logs",
    'summary': "",
    'description': """""",
    'author': "BrowseInfo",
    "website" : "https://www.browseinfo.com",
    "price": '',
    "currency": 'EUR',
    "depends": [
        'uom',
        'product',
        'mail',
        'base',
        'account',
        'analytic',
        'mrp',
    ],
    "data": [
        'views/uom_uom.xml',
        'views/uom_category.xml',
        'views/product_category.xml',
        'views/mail_template.xml',
        'views/res_currency.xml',
        'views/account_fiscal_position.xml',
        'views/account_group.xml',
        'views/account_analytic_plan.xml',
        'views/res_bank.xml',
        'views/product_attribute.xml',
        'views/product_supplierinfo.xml',
        'views/mrp_workcenter.xml',
        'views/mrp_routing_workcenter.xml',
        'views/res_lang.xml',
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": [""],
    "live_test_url": '',
    'license': 'OPL-1',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
