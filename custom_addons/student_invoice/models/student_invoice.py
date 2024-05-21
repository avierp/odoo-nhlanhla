from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    student_id = fields.Many2one('student.student', string='Student')

class Student(models.Model):
    _inherit = 'student.student'

    invoice_count = fields.Integer(
        string='Invoice Count',
        compute='_compute_invoice_count',
        default=0,
    )

    def _compute_invoice_count(self):
        for student in self:
            student.invoice_count = self.env['account.move'].search_count([('student_id', '=', student.id)])

    def action_view_student_invoices(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('student_id', '=', self.id)],
            'context': {'create': False, 'default_student_id': self.id},
        }
