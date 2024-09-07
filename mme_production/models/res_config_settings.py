# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_auto_generate = fields.Boolean(string='Auto Generate',
                                      help="Based on this selection it shows "
                                           "the fields for auto generating "
                                           "lot/serial number",
                                      config_parameter="auto_generate_lot_number.is_auto_generate")
    serial_number_type = fields.Selection(
        [('global', 'Global'), ('product', 'Product Wise')],
        default='global', string='Serial/lot Number',
        help="Generate the lot/serial number product wise or globally",
        config_parameter="auto_generate_lot_number.serial_number_type")
    prefix = fields.Char(string='Prefix',
                         help="Prefix value of the record for sequence",
                         config_parameter="auto_generate_lot_number.prefix")
    digits = fields.Integer(string='Digits',
                            help="Used to set number of digits contain in a "
                                 "sequence",
                            config_parameter="auto_generate_lot_number.digits")

    serial_selection = fields.Selection([('global', 'Global'),
                                         ('product_wise', 'Product Wise')],
                                        string="Choose Method",
                                        help="Select the method for generating"
                                             " serial numbers: global or "
                                             "product-wise.",
                                        config_parameter='serial_no_from_mo.'
                                                         'serial_selection')
    digit = fields.Integer(string="Number of Digits",
                           help="Specify the number of digits to use for the "
                                "serial numbers.",
                           config_parameter='serial_no_from_mo.digit', )
    is_serial_selection = fields.Boolean(string="Serial number Selection "
                                                "Method", help="Enable or "
                                                               "disable the"
                                                               " serial number"
                                                               " selection "
                                                               "method.",
                                         config_parameter='serial_no_from_mo.'
                                                          'is_serial_selection'
                                         )

    @api.onchange('is_auto_generate')
    def _onchange_auto_generate(self):
        self.env.company.check_auto_generate = False
        if self.is_auto_generate:
            self.env.company.check_auto_generate = True
