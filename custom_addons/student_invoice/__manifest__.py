{
    'name': 'Student Invoice',
    'version': '1.0',
    'summary': 'Link students to invoices',
    'description': 'Adds a student field to invoices and links students to their invoices',
    'author': 'Nhlanhla Khosa',
    'category': 'Accounting',
    'depends': ['base', 'account', 'student'],
    'data': [
        'views/student_invoice_views.xml',
    ],
    'installable': True,
    'application': True,
}
