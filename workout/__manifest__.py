# -*- coding: utf-8 -*-

{
    'name': 'Workout',
    'version': '1.0',
    'website': 'http://xfanis.ru',
    'category': 'Fitness',
    'sequence': 10,
    'summary': 'Workout Plans and Logs',
    'depends': [],
    'description': "",
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/main_menu.xml',
        'views/muscle.xml',
        'views/exercise.xml',
        'views/plan_manager.xml',
        'views/plan_user.xml',
        'views/log.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
