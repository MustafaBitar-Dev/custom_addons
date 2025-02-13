from odoo import models, fields, api
from datetime import timedelta

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
    
    visa_status = fields.Selection([
    ('valid', "Valid"),
    ('soon', "Expiring Soon"),
    ('expired', "Expired")], default='valid')
    
    
    ref = fields.Char(default='New', readonly=True)
    
    @api.depends('grade_education','grade_transport','grade_medical','grade_mobile','grade_housing')
    def _compute_total(self):
        for record in self:
            if record.gender == 'female':
                record.grade_education *= record.female_rate
            allowances = record.grade_education + record.grade_transport + record.grade_medical + record.grade_mobile + record.grade_housing
            if record.disability:
                allowances *= record.disability_rate
            record.total = allowances + record.contract_wage
            
            
    def check_visa_expiration_date(self):
        employee_ids = self.search([])  
        for rec in employee_ids:           
            if rec.visa_expire:
                if rec.visa_expire < fields.date.today():
                    rec.visa_status = 'expired'              
                elif rec.visa_expire - timedelta(30) < fields.date.today():
                    rec.visa_status = 'soon'
                else:
                    rec.visa_status = 'valid'           
    
    @api.model
    def create(self, vals):
        res = super(HrEmployee, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('emplooye_seq')
        return res