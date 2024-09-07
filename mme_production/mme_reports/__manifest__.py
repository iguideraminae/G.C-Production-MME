# -*- encoding: utf-8 -*-
{
    'name': 'Rapports MME',
    'category': 'Sales/Sales',
    'author': 'Tecpod',
    'website': 'https://tecpod.ma',
    "license": "AGPL-3",
    "version": "1.0",
    'depends': ['sale', 'mrp', 'project'],

    'description': """
    """,
    'data': [
        'views/sale_order.xml',
        'reports/header_footer_sale_order.xml',
        'reports/sale_order.xml',
        'reports/stock_picking.xml',
        'reports/header_footer_stock_picking.xml',

    ],
    'installable': True,
}
