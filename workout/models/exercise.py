# -*- coding: utf-8 -*-
from odoo import models, fields


class Exercise(models.Model):
    _name = 'workout.exercise'
    _description = 'Exercise'
    _order = 'name'

    name = fields.Char('Name', required=True)
    muscle_ids = fields.Many2many(
        string='Muscles',
        comodel_name='workout.muscle',
        relation='workout_exercise_muscle_rel',
        column1='exercise_id',
        column2='muscle_id',
        required=True)

    additional_muscle_ids = fields.Many2many(
        string='Additional Muscles',
        comodel_name='workout.muscle',
        relation='workout_exercise_additional_muscle_rel',
        column1='exercise_id',
        column2='muscle_id')

    similar_exercise_ids = fields.Many2many(
        string='Similar Exercises',
        comodel_name='workout.exercise',
        relation='workout_exercise_similar_exercise_rel',
        column1='exercise_id',
        column2='muscle_id')
