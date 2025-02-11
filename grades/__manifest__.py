{
    'name': 'Grades',
    'depends': ['base', 'mail', 'hr'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/grades_grade_view.xml',
        'views/hr_employee_view.xml'
    ]
}