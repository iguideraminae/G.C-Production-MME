# -*- coding: utf-8 -*-
from odoo import fields, models

class SaleOrderMme(models.Model):
    _inherit = 'sale.order'

    lot = fields.Many2one('mrp.production', string="Lot")
    project_id = fields.Many2one('project.project', string="Projet")
    affectation = fields.Char(string='Affectation')
