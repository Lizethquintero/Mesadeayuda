# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    # _description = 'practica/sale_liz.practica/sale_liz'

    state = fields.Selection(('1','BORRADOR'),('2','COTIZACION'),('3','APROBACION 1'),('4','APROBACION 2'),('5','APROBACION 3'),('6','ORDEN DE VENTA')
                            ,('7','A FACTURAR'),('8','NOTA CREDITO'),('9','NOTA DEBITO'),('10','DOCUMENTO RFC'),('11','FACTURADO'),string='state')
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
