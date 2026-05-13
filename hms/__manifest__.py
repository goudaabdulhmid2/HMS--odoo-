{
    'name': 'HMS Module',

    'summary': 'Hospital Management System',

    'description': """
        HMS Module
        Manage Patients Data
    """,

    'author': 'Abdulhamid',

    'category': 'Uncategorized',

    'version': '0.1',

    'depends': ['base', 'contacts'],

    'data': [

    'security/ir.model.access.csv',

    'views/patient_view.xml',

    'views/department_view.xml',
    
    'views/doctor_view.xml',

    'views/res_partner_view.xml',

    ],

    'installable': True,

    'application': True,
}