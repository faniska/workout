# -*- coding: utf-8 -*-
from odoo import models, fields


class WorkoutLog(models.Model):
    _name = 'workout.log'
    _description = 'Workout Log'
    _order = 'id desc'

    exercise_id = fields.Many2one('workout.exercise', 'Exercise', required=True)
    date = fields.Date('Date', default=fields.Date.today)
    reps = fields.Integer('Reps')
    weight = fields.Integer('Weight')
