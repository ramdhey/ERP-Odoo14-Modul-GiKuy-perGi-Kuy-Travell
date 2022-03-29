from odoo import http, fields, models
from odoo.http import request
import json


class KursiTamuCon(http.Controller):
    @http.route('/funtrip', auth='public', methods=['GET'])
    def getRincianOrderan(self, **kwargs):
        funtrip = request.env['gikuy.funtrip'].search([])
        value = []
        for k in funtrip:
                value.append({"namapaketfunTrip" : k.name,
                            "detail" : k.detail,
                            "harga" : k.harga,})
        return json.dumps(value)

    @http.route(['/funtrip','/funtrip/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getRincianOrderan(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            funtrip = request.env['gikuy.funtrip'].search([])            
            for k in funtrip:
                value.append({"id": k.id,
                            "namapaketfunTrip" : k.name,
                            "detail" : k.detail,
                            "harga" : k.harga})
            return json.dumps(value)
        else:
            kursiid = request.env['gikuy.orderrinci'].search([('id','=',idnya)])
            for k in kursiid:
                value.append({"id": k.id,
                            "hargaperunit" : k.hargaperunit,
                            "ava" : k.ava})
            return json.dumps(value)
    
    @http.route('/createfuntrip',auth='user', type='json', methods=['POST'])
    def createFuntrip(self, **kw):    
        if request.jsonrequest:    
            if kw['name']:
                vals={
                    'name': kw['name'], 
                    'detail' : kw['detail'],
                    'ava' : kw['ava'],
                    'harga' : kw['harga'],
                }
                newfuntrip = request.env['gikuy.funtrip'].create(vals)
                args = {'success': True, 'ID':newfuntrip.id}
                return args