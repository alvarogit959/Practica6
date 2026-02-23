# -*- coding: utf-8 -*-
{
    'name': 'Empresa Reparto',
    'depends': ['base', 'web'],
'data': [
    'security/ir.model.access.csv',
    'views/menu.xml',
    'views/empleado_views.xml',
    'views/vehiculo_views.xml',
    'views/cliente_views.xml',
    'views/reparto_views.xml',
    'wizard/reparto_wizard.xml',
    'report/reparto_report.xml',
    
    
],
    'installable': True,
    'application': True,
}
