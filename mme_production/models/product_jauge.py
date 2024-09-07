from odoo import api, fields, models


class ProductJauge(models.Model):
    _name = "product.jauge"

    name = fields.Char(String="Nom")
    volume_m3 = fields.Float(string="Volume nominal e m3")
    diametre_ext = fields.Float(string="Diamètre ext en mm")
    longeur_v = fields.Float(string="Longueur virole")
    longueur_t = fields.Float(string="Longueur totale")
    hauteur = fields.Float(string="Hauteur")
    bords = fields.Float(string="bords du fonds")
    values_ids = fields.One2many('jauge.values','jauge_id')

class Jauge_values(models.Model):
    _name = "jauge.values"

    hauteur = fields.Float('Hauteur H')
    volume = fields.Float('Volume')
    jauge_id = fields.Many2one('product.jauge')

