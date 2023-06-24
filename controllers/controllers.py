# -*- coding: utf-8 -*-
# from odoo import http


# class MyPersonalExpense(http.Controller):
#     @http.route('/my_personal_expense/my_personal_expense', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_personal_expense/my_personal_expense/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_personal_expense.listing', {
#             'root': '/my_personal_expense/my_personal_expense',
#             'objects': http.request.env['my_personal_expense.my_personal_expense'].search([]),
#         })

#     @http.route('/my_personal_expense/my_personal_expense/objects/<model("my_personal_expense.my_personal_expense"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_personal_expense.object', {
#             'object': obj
#         })
