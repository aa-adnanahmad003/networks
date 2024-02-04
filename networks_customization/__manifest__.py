# -- coding: utf-8 --
{
    # Module information
    'name': "Networks Customization",
    'description': """
        Networks Pvt. Ltd. Customization Module 
    """,
    'summary': """
        Networks Pvt. Ltd. Customization Module
    """,
    'author': "Farooq Butt || 0301-5902110",
    'version': '16.0.1.0.0',
    'license': 'LGPL-3',
    # Dependencies
    'depends': ['base', 'contacts'],

    # Views
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner_ext.xml',
    ],

    # Technical
    "installable": True,
    "auto_install": False,
}