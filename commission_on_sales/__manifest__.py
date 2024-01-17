# -- coding: utf-8 --
{
    # Module information
    'name': "Commission on Sales",
    'description': """
        Commission Module 
    """,
    'summary': """
        Calculate Commission on Sales
    """,
    'author': "Farooq Butt || 0301-5902110",
    'version': '16.0.1.0.0',
    'license': 'LGPL-3',
    # Dependencies
    'depends': ['base','contacts'],

    # Views
    'data': [
        'security/ir.model.access.csv',
        'views/commission_agent.xml',
        'views/res_partner_ext.xml',
        'views/commission_settlement.xml',
    ],

    # Technical
    "installable": True,
    "auto_install": False,
}
