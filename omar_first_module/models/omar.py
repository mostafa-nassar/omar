from datetime import date
from datetime import datetime
from odoo import api, _
from odoo import exceptions
from odoo import fields
from odoo import models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.tools import pytz
# from odoo.tools import timedelta
from datetime import timedelta
# from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class omar_module(models.Model):
    _name = 'employee.list'
    # _inherits = {'calendar.event': "event_id"} # Delegation
    # _inherit = ['mail.thread']

    name = fields.Char()
    birth_date = fields.Date()
    phone = fields.Integer()
