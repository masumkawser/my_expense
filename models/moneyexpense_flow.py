from odoo import api, fields, models, _

class MoneyFlow(models.Model):
    _name = 'money.expense'
    _description = 'moneyexpense for my personal'
    _order = 'issue_date desc'

    def _default_currency_id(self):
        return self.env.user.company_id.currency_id

    name = fields.Char(string='Expense Name', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self._default_currency_id())
    amount = fields.Float(string='Amount', digits=(16, 0), required=True)
    description = fields.Text(string='Description')
    money_type = fields.Selection(
        string='Money Type',
        selection=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('mobile_banking', 'Mobile_Banking')], required=True, default='cash')
    issue_date = fields.Datetime(string='Issue date', default=fields.Datetime.now, required=True)