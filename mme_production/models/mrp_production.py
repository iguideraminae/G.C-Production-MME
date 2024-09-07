from odoo import api, fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    user_control_id = fields.Many2one('res.users', 'Responsable de Contrôle')
    trou = fields.Many2one('trou', 'Trou d’homme')
    entraxe = fields.Many2one('entraxe', 'Entraxe berceaux')
    norme = fields.Many2one('norme', 'Norme de construction')
    matiere = fields.Many2one('matiere', 'Matière')
    fonds = fields.Many2one('fonds', 'Fonds')
    revetement = fields.Many2one('revetement', 'Revêtement standard:')


    @api.depends("qc_inspections_ids")
    def _compute_created_inspections(self):
        for production in self:
            production.created_inspections = len(production.qc_inspections_ids)

    qc_inspections_ids = fields.One2many(
        comodel_name="qc.inspection",
        inverse_name="production_id",
        copy=False,
        string="Contrôle qualité",
        help="Inspections related to this production.",
    )
    created_inspections = fields.Integer(
        compute="_compute_created_inspections", string="Created inspections"
    )

    def action_confirm(self):
        parms = self.env['ir.config_parameter'].sudo()
        for rec in self:
            if rec.product_id.tracking in ['serial', 'lot']:
                if parms.get_param(
                        'serial_no_from_mo.serial_selection') == 'global':
                    digit = int(parms.get_param('serial_no_from_mo.digit'))
                    prefix = parms.get_param('serial_no_from_mo.prefix')
                    seq = self.env['ir.sequence'].sudo().search(
                        [('code', '=', 'mrp.production.sequence')])
                    if seq:
                        seq.write({
                            'prefix': prefix,
                            'padding': digit
                        })
                    if not seq:
                        self.env['ir.sequence'].create({
                            'name': 'Mrp Production',
                            'implementation': 'standard',
                            'code': 'mrp.production.sequence',
                            'prefix': prefix,
                            'padding': digit})
                    serial_id = self.env['stock.lot'].create({
                        'name': self.env['ir.sequence'].sudo().next_by_code(
                            'mrp.production.sequence'),
                        'product_id': rec.product_id.id,
                        'company_id': rec.company_id.id,
                    })
                else:
                    seq = self.env['ir.sequence'].sudo().search(
                        [('code', '=', rec.product_id.name)])
                    if seq:
                        seq.write({
                            'prefix': rec.product_id.product_tmpl_id.prefix,
                            'padding': rec.product_id.product_tmpl_id.digit,
                        })
                    if not seq:
                        self.env['ir.sequence'].create({
                            'name': 'Mrp Production',
                            'implementation': 'standard',
                            'code': rec.product_id.name,
                            'prefix': rec.product_id.product_tmpl_id.prefix,
                            'padding': rec.product_id.product_tmpl_id.digit})
                    serial_id = self.env['stock.lot'].create({
                        'name': self.env['ir.sequence'].sudo().next_by_code(
                            rec.product_id.name),
                        'product_id': rec.product_id.id,
                        'company_id': rec.company_id.id,
                    })
                rec.lot_producing_id = serial_id
        return super(MrpProduction, self).action_confirm()

class Trou(models.Model):
    _name = "trou"

    name = fields.Char("Nom")

class Entraxe(models.Model):
    _name = "entraxe"

    name = fields.Char("Nom")


class Norme(models.Model):
    _name = "norme"

    name = fields.Char("Nom")


class Matiere(models.Model):
    _name = "matiere"

    name = fields.Char("Nom")


class Fonds(models.Model):
    _name = "fonds"

    name = fields.Char("Nom")


class Revetement(models.Model):
    _name = "revetement"

    name = fields.Char("Nom")
