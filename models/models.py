# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class my_personal_expense(models.Model):
#     _name = 'my_personal_expense.my_personal_expense'
#     _description = 'my_personal_expense.my_personal_expense'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
