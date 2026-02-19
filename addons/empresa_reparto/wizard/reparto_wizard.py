from odoo import models, fields

class RepartoWizard(models.TransientModel):
    _name = 'empresa_reparto.reparto_wizard'
    _description = 'Wizard para crear reparto'

    empleado_id = fields.Many2one('empresa_reparto.empleado', string="Empleado", required=True)
    vehiculo_id = fields.Many2one('empresa_reparto.vehiculo', string="Vehículo", required=True)
    cliente_id = fields.Many2one('empresa_reparto.cliente', string="Cliente", required=True)

    def crear_reparto(self):
        self.env['empresa_reparto.reparto'].create({
            'empleado_id': self.empleado_id.id,
            'vehiculo_id': self.vehiculo_id.id,
            'cliente_id': self.cliente_id.id,
            'fecha_recepcion': fields.Datetime.now(),
        })
        return {'type': 'ir.actions.act_window_close'}
