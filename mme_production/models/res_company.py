# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    check_auto_generate = fields.Boolean(string='Auto Generate',
                                         help="Used for setting the sequence "
                                              "number based on the company")
