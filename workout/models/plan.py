# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class Plan(models.Model):
    _name = 'workout.plan'
    _description = 'Workout Plan'
    _order = 'name'

    name = fields.Char('Name')
    days = fields.One2many('workout.plan.day', 'plan_id', 'Days')


class PlanDay(models.Model):
    _name = 'workout.plan.day'
    _description = 'Workout Plan'
    _order = 'day'

    name = fields.Char()
    plan_id = fields.Many2one('workout.plan', 'Plan', required=True)
    day = fields.Integer('Day', required=True)
    name = fields.Char('Name', compute='_compute_name')
    exercise_ids = fields.One2many('workout.plan.exercise', 'plan_day_id', 'Exercises')

    @api.depends('day')
    def _compute_name(self):
        for plan_day in self:
            plan_day.name = f'Day {plan_day.day}'


class PlanExercise(models.Model):
    _name = 'workout.plan.exercise'
    _description = 'Workout Plan Exercise'
    _order = 'sequence'

    sequence = fields.Integer('Sequence')
    plan_id = fields.Many2one('workout.plan', 'Plan', related='plan_day_id.plan_id')
    plan_day_id = fields.Many2one('workout.plan.day', 'Day', required=True)
    exercise_id = fields.Many2one('workout.exercise', 'Exercise', required=True)

    sets_number_min = fields.Integer('Sets (Min)')
    sets_number_max = fields.Integer('Sets (Max)')

    reps_number_min = fields.Integer('Reps (Min)')
    reps_number_max = fields.Integer('Reps (Max)')

    def action_add_log(self):
        self.ensure_one()
        view = self.env.ref('workout.workout_log_form')
        return {
            'name': _('Workout Log'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'workout.log',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': {
                'default_exercise_id': self.exercise_id.id
            }
        }
