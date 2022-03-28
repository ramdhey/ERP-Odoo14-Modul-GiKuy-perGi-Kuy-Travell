# -*- coding: utf-8 -*-
# from odoo import http


# class Gikuy(http.Controller):
#     @http.route('/gikuy/gikuy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gikuy/gikuy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gikuy.listing', {
#             'root': '/gikuy/gikuy',
#             'objects': http.request.env['gikuy.gikuy'].search([]),
#         })

#     @http.route('/gikuy/gikuy/objects/<model("gikuy.gikuy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gikuy.object', {
#             'object': obj
#         })
