{
    'name': 'Student Invoice',
    'version': '1.0',
    'summary': 'Add student field to invoices',
    'author': 'Nhlanhla Khosa',
    'depends': ['account', 'student'],
    'data': [
        'views/student_invoice_views.xml',
    ],
    'installable': True,
    'application': False,
}
