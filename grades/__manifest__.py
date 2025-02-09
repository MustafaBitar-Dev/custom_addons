{
    'name': 'Grades',
    'depends': ['base', 'mail'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/grades_grade_view.xml'
    ]
}