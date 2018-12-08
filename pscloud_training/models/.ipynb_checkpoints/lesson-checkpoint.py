class TrainingLesson(models.Model):
    _name = 'pscloud.training.lesson'
    _description = "课程信息"

    name = fields.Char(string='Name')