#-*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    
    _inherit = 'sale.order'
    _description = 'Sale order qweb'

    qweb_note = fields.Char(string="Notas: ")
    qweb_presentation = fields.Html(string="Presentacion: ", sanitize=False)
    qweb_control = fields.Html(string="Constrol Revisiones: ", sanitize=False)
    qweb_company = fields.Html(string="Nuestra Empresa: ", sanitize=False, compute='_compute_our_company')
    qweb_summary = fields.Html(string="Resumen Solicitud: ", sanitize=False)
    qweb_description = fields.Html(string="Descripcion de servicio propuesto: ", sanitize=False)
    qweb_solution = fields.Html(string="Solucion Propuesta: ", sanitize=False)
    qweb_wbs = fields.Html(string="Wbs: ", sanitize=False)

    def _compute_our_company(self):
        templates = self.env['sale.order.template']
        html = templates.search([('our_company_template','!=',False)])
        for record in self:
            if record.qweb_company == False:
                record.qweb_company = html.our_company_template
        
    