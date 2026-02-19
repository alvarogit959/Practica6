from odoo import models, fields, api


class Empleado(models.Model):
    _name = 'reparto.empleado'
    _description = 'Empleado'

    nombre = fields.Char(required=True)
    apellidos = fields.Char(required=True)
    dni = fields.Char(required=True)
    telefono = fields.Char()
    foto = fields.Binary()
    carnet_ciclomotor = fields.Boolean()
    carnet_furgoneta = fields.Boolean()

    reparto_ids = fields.One2many('reparto.reparto', 'empleado_id')
