from odoo import  fields, models

class TrainingLesson(models.Model):
    _name = 'pscloud.training.lesson'
    _description = "课程信息"

    name = fields.Char(string='Name')
    teacher_id = fields.Many2one('res.partner', string='老师')
    student_ids = fields.Many2many('res.partner', string='学生', readonly=True)
    start_date = fields.Date(string='开始时间')
    end_date = fields.Date(string='结束时间')