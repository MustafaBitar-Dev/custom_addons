from odoo import models, fields, api
from odoo.exceptions import ValidationError

class GradeModel(models.Model):
    # Model Info
    _name = 'grade'
    _description = 'Grade model'
    _inherit = ['mail.thread'] 
    
    # Main Field
    number = fields.Integer('Grade Number')
    
    # Limit Fields
    disability_rate = fields.Float('Disability Rate')
    female_rate = fields.Float('Female Rate')
    max_benefit = fields.Integer('Max Benefit')
    ability_to_retire = fields.Boolean('Ability To Retire', default=False)
    
    # Allowances Fields
    education = fields.Float('Education Allowance')
    transport = fields.Float('Transport Allowance')
    medical = fields.Float('Medical Allowance')
    mobile = fields.Float('Mobile Allowance')
    housing = fields.Float('Housing Allowance')
    
    # Country Rates Fields
    egypt_rate = fields.Float('Egypt Rate')
    qatar_rate = fields.Float('Qatar Rate')
    other_country_rate = fields.Float('Other Countries Rate')
    
    
    # Constraints
    _sql_constraints = [('unique_grade', 'unique("number")', 'Grade Number Should Be Unique')]    
    
    @api.constrains('number')
    def _check_grade_number(self):
        for rec in self:
            if rec.number < 1:               
                raise ValidationError('Grade Number Should Be A Positive Integer')
    
    
    '''
    Because I have more than one fields has the same constrain
    I use a helper function which check the same condition and generate
    an error message based on the field name
    '''
    
    @api.constrains('disability_rate', 'female_rate', 
                    'egypt_rate', 'qatar_rate', 'other_country_rate')
    def _check_rate(self):
        def check_rate(attr):
            if rec[attr] < 0 or rec[attr] > 100:
                field_name = attr.replace('_', ' ').title()
                raise ValidationError( field_name + " Must Be Between 0 And 100")
        for rec in self:
            check_rate('disability_rate')
            check_rate('female_rate')
            check_rate('egypt_rate')
            check_rate('qatar_rate')
            check_rate('other_country_rate')

        
    @api.constrains('max_benefit', 'education', 'transport', 
                    'medical', 'mobile', 'housing')
    def _check_positive(self):
        def check_positive(attr):
            if rec[attr] < 0:
                field_name = attr.replace('_', ' ').title()
                raise ValidationError(field_name + ' Must Be Greater Than 0')
        for rec in self:
            check_positive('max_benefit')
            check_positive('education')
            check_positive('transport')
            check_positive('medical')
            check_positive('mobile')
            check_positive('housing')
            
  