from odoo import http

class RepartoController(http.Controller):

    @http.route('/estado/<codigo>', auth='public')
    def estado(self, codigo):
        reparto = http.request.env['reparto.reparto'].search([('codigo','=',codigo)])
        return reparto.estado
