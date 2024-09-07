from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    jauge_id = fields.Many2one('product.jauge', string="Barème de jaugeage")
    is_auto_generate = fields.Boolean(string="Is Auto Generate",
                                      compute='_compute_is_auto_generate',
                                      help="Used to hide and show the prefix "
                                           "and digit field based on the "
                                           "option that we choose in settings")
    prefix = fields.Char(string='Prefix',
                         help="Prefix value of the record for sequence")
    digits = fields.Integer(string='Digits',
                            help="Used to set number of digits contain in a "
                                 "sequence")
    number_next = fields.Integer(string='Next call', help="Next number that "
                                                          "will be used. This "
                                                          "number can be"
                                                          "incremented "
                                                          "frequently so the "
                                                          "displayed value "
                                                          "might"
                                                          "already be obsolete")

    digit = fields.Integer(string="Number of Digits",
                           help="Specify the desired number of digits.")


    @api.onchange('prefix', 'digits')
    def onchange_digits_prefix(self):
        self.number_next = 0

    def check_string_for_nine(self, string):
        return all(char == '9' for char in string)

    def _number_next_actual(self):
        if self.is_auto_generate:
            self.number_next += 1

            if len(str(self.digits)) == len(str(self.number_next)) and self.check_string_for_nine(
                    str(self.number_next)):
                self.digits += 1

            if self.digits - len(str(self.number_next)) <= 0:
                value = str(self.prefix)
            else:
                digits = "0" * (self.digits - len(str(self.number_next)))
                value = str(self.prefix) + digits

            return value + str(self.number_next)

    @api.depends('tracking')
    def _compute_is_auto_generate(self):
        for rec in self:
            rec.is_auto_generate = False
            product_type = rec.env['ir.config_parameter'].sudo().get_param(
                'auto_generate_lot_number.serial_number_type')
            auto_generate = rec.env['ir.config_parameter'].sudo().get_param(
                'auto_generate_lot_number.is_auto_generate')
            if product_type == 'product' and auto_generate:
                rec.is_auto_generate = True

    def write(self, values):
        res = super(ProductTemplate, self).write(values)
        if values.get('prefix') or values.get('digits'):
            self.number_next = 0
        return res


class ProductProduct(models.Model):
    _inherit = "product.product"

    jauge_id = fields.Many2one('product.jauge', string="Barème de jaugeage")