from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = ['hr.employee']
    grade_id = fields.Many2one('grade')
    grade_number = fields.Integer(related='grade_id.number')
    
    grade_education = fields.Float(related='grade_id.education')
    grade_transport = fields.Float(related='grade_id.transport')
    grade_medical = fields.Float(related='grade_id.medical')
    grade_mobile = fields.Float(related='grade_id.mobile')
    grade_housing = fields.Float(related='grade_id.housing')
    
    disability_rate = fields.Float(related='grade_id.disability_rate')
    female_rate = fields.Float(related='grade_id.female_rate')
    max_benefit = fields.Integer(related='grade_id.max_benefit')
    ability_to_retire = fields.Boolean(related='grade_id.ability_to_retire')
    
    egypt_rate = fields.Float(related='grade_id.egypt_rate')
    qatar_rate = fields.Float(related='grade_id.qatar_rate')
    other_country_rate = fields.Float(related='grade_id.other_country_rate')
    
    contract_id = fields.Many2one('hr.contract', string='Contract')
    contract_wage = fields.Monetary(related='contract_id.wage')
    
    disability = fields.Boolean(default=False)
    
    total = fields.Float('Total', compute='_compute_total')
    
    
    
    @api.depends('grade_education','grade_transport','grade_medical','grade_mobile','grade_housing')
    def _compute_total(self):
        for record in self:
            if record.gender == 'female':
                record.grade_education *= record.female_rate
            allowances = record.grade_education + record.grade_transport + record.grade_medical + record.grade_mobile + record.grade_housing
            if record.disability:
                allowances *= record.disability_rate
            record.total = allowances + record.contract_wage