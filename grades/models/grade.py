from odoo import models, fields

class GradeModel(models.Model):
    _name = 'grade'
    _description = 'Grade model'
    _inherit = ['mail.thread'] 
    
    number = fields.Integer('Grade Number', required=True)
    disability_rate = fields.Float('Disability Rate')
    female_rate = fields.Float('Female Rate')
    max_benefit = fields.Integer('Max Benefit')
    education = fields.Float('Education Allowance', default=0)
    transport = fields.Float('Transport Allowance', default=0)
    medical = fields.Float('Medical Allowance', default=0)
    mobile = fields.Float('Mobile Allowance', default=0)
    housing = fields.Float('Housing Allowance', default=0)
    egypt_rate = fields.Float('Egypt Rate')
    qatar_rate = fields.Float('Qatar Rate')
    other_country_rate = fields.Float('Other Countries Rate')
    ability_to_retire = fields.Boolean('Ability To Retire', default=False)