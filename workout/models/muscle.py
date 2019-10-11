# -*- coding: utf-8 -*-

from odoo import fields, models


class MuscleGroup(models.Model):
    _name = 'workout.muscle.group'
    _description = 'Muscle Group'
    _order = 'name'

    name = fields.Char('Name', required=True)
    muscle_ids = fields.One2many('workout.muscle', 'group_id', 'Muscles')


class Muscle(models.Model):
    _name = 'workout.muscle'
    _description = 'Muscle'
    _order = 'name'

    name = fields.Char('Name', required=True)
    group_id = fields.Many2one('workout.muscle.group', 'Group')
