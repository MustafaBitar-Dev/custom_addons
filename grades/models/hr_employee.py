from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = ['hr.employee']
    grade_id = fields.Many2one('grade')
    grade_number = fields.Integer(related='grade_id.number')
    
    contract_id = fields.Many2one('hr.contract', string="Contract")
    contract_wage = fields.Monetary(related='contract_id.wage')