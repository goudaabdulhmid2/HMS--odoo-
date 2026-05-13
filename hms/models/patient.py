from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
from datetime import date


class Patient(models.Model):

    _name = 'hms.patient'

    first_name = fields.Char(required=True)

    last_name = fields.Char(required=True)

    email = fields.Char(required=True)

    birth_date = fields.Date()

    history = fields.Html()

    cr_ratio = fields.Float()

    blood_type = fields.Selection([
        ('a+', 'A+'),
        ('b+', 'B+'),
        ('o+', 'O+'),
    ])

    pcr = fields.Boolean()

    image = fields.Image()

    address = fields.Text()

    age = fields.Integer(
        compute='_compute_age'
    )

    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined')

    department_id = fields.Many2one(
        'hms.department'
    )

    department_capacity = fields.Integer(
        related='department_id.capacity'
    )

    doctor_ids = fields.Many2many(
        'hms.doctors'
    )


    @api.depends('birth_date')
    def _compute_age(self):

        today = date.today()

        for record in self:

            if record.birth_date:

                record.age = (
                    today.year - record.birth_date.year
                )

            else:

                record.age = 0


    @api.constrains('email')
    def _check_valid_email(self):

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        for record in self:

            if record.email:

                if not re.match(pattern, record.email):

                    raise ValidationError(
                        "Invalid Email"
                    )


    @api.constrains('email')
    def _check_unique_email(self):

        for record in self:

            duplicated_patient = self.search([
                ('email', '=', record.email),
                ('id', '!=', record.id)
            ], limit=1)

            if duplicated_patient:

                raise ValidationError(
                    'Email already exists!'
                )


    @api.constrains('age')
    def _check_age(self):

        for record in self:

            if record.age < 0:

                raise ValidationError(
                    "Age must be positive"
                )


    @api.onchange('age')
    def _onchange_age(self):

        if self.age and self.age < 30:

            self.pcr = True

            return {

                'warning': {

                    'title': 'Warning',

                    'message': 'PCR checked automatically'

                }

            }


    def set_good_state(self):

        self.state = 'good'


    def set_fair_state(self):

        self.state = 'fair'


    def set_serious_state(self):

        self.state = 'serious'