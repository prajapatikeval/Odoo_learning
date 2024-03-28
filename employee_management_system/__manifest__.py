# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Employee Management System',
    'version' : '15',
    'summary': 'Employee Management System',
    'sequence': 10,
    'description': """
Employee Management System
====================
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.google.com',
    'depends' : ['base_setup', 'product', 'analytic', 'portal', 'digest'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/base_template.xml',
        'views/Dashboard.xml',
        'views/Client.xml',
        'views/Manager.xml',
        'views/Employee.xml',
        'views/Projects.xml',
        'views/menus.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    'license': 'LGPL-3',
}