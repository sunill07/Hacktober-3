# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, tools, models, _


class ProductAttribute(models.Model):
    _name = "product.attribute"
    _inherit = ['product.attribute' ,'mail.thread', 'mail.activity.mixin']

    def init(self):
        for field in self._fields.values():
            if isinstance(field, fields.Text) or \
                isinstance(field, fields.Char) or \
                isinstance(field, fields.Integer) or \
                isinstance(field, fields.Float) or \
                isinstance(field, fields.Monetary) or \
                isinstance(field, fields.Date) or \
                isinstance(field, fields.Datetime) or \
                isinstance(field, fields.Boolean) or \
                isinstance(field, fields.Selection) or \
                isinstance(field, fields.Image) or \
                isinstance(field, fields.Binary) or \
                isinstance(field, fields.Many2one) or \
                isinstance(field, fields.Many2many) or \
                isinstance(field, fields.One2many):
                field.tracking = True
                