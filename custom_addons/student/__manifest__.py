{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Module to manage students',
    'description': 'A module to manage student records',
    'author': 'Nhlanhla Khosa',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
}
