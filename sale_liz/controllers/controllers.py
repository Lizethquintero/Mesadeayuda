# -*- coding: utf-8 -*-
# from odoo import http


# class Practica/saleLiz(http.Controller):
#     @http.route('/practica/sale_liz/practica/sale_liz/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practica/sale_liz/practica/sale_liz/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practica/sale_liz.listing', {
#             'root': '/practica/sale_liz/practica/sale_liz',
#             'objects': http.request.env['practica/sale_liz.practica/sale_liz'].search([]),
#         })

#     @http.route('/practica/sale_liz/practica/sale_liz/objects/<model("practica/sale_liz.practica/sale_liz"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practica/sale_liz.object', {
#             'object': obj
#         })
