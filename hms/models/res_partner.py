from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):

    _inherit = 'res.partner'

    related_patient_id = fields.Many2one(
        'hms.patient',
        string='Related Patient'
    )

    vat = fields.Char(required=True)

    @api.constrains('related_patient_id')
    def _check_related_patient(self):

        for record in self:

            if not record.related_patient_id:
                continue

            duplicated_partner = self.env['res.partner'].search([
                ('related_patient_id', '=', record.related_patient_id.id),
                ('id', '!=', record.id)
            ], limit=1)

            if duplicated_partner:
                raise ValidationError(
                    'This patient is already linked to another customer!'
                )