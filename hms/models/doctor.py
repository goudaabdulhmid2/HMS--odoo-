from odoo import models, fields


class Doctors(models.Model):

    _name = 'hms.doctors'

    first_name = fields.Char()

    last_name = fields.Char()

    image = fields.Image()