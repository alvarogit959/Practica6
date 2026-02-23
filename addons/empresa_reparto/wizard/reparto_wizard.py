from odoo import models, fields

class RepartoWizard(models.TransientModel):
    _name = 'reparto.reparto_wizard'

    empleado_id = fields.Many2one('reparto.empleado', string="Empleado", required=True)
    vehiculo_id = fields.Many2one('reparto.vehiculo', string="Vehículo", required=True)
    cliente_id = fields.Many2one('reparto.cliente', string="Cliente", required=True)

    def crear_reparto(self):
        self.env['reparto.reparto'].create({
            'empleado_id': self.empleado_id.id,
            'vehiculo_id': self.vehiculo_id.id,
            'cliente_id': self.cliente_id.id,
            'fecha_recepcion': fields.Datetime.now(),
        })
        return {'type': 'ir.actions.act_window_close'}
