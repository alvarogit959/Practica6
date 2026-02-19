# -*- coding: utf-8 -*-
{
    'name': 'Gestión Empresa Reparto',
    'version': '1.0',
    'author': 'Tu Nombre',
    'category': 'Custom',
    'summary': 'Gestión de empleados, vehículos y repartos',
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
