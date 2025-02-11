from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    grade_id = fields.Many2one('grade')
    grade_number = fields.Integer(related='grade_id.number')