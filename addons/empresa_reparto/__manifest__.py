# -*- coding: utf-8 -*-
{
    'name': 'Empresa Reparto',
    'depends': ['base', 'web'],
'data': [
    'views/menu.xml',
    'views/empleado_views.xml',
    'views/vehiculo_views.xml',
    'views/cliente_views.xml',
    'wizard/reparto_wizard_view.xml',
    'report/reparto_report.xml',
    'security/ir.model.access.csv',

    ],
    'installable': True,
    'application': True,
}
