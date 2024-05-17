from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    date_of_birth = fields.Date(string='Date of Birth')
    active = fields.Boolean(string='Active', default=True)
