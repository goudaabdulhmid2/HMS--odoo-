from odoo import models, fields, api

class Patient(models.Model):

    _name = 'hms.patient'

    first_name = fields.Char(required=True)

    last_name = fields.Char(required=True)

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

    age = fields.Integer()

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