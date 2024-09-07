# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class Project(models.Model):
    _inherit = 'project.project'

    sale_order_ids = fields.One2many('sale.order','projects_id',string='Sale order')
