from odoo import api, fields, models


class Patner(models.Model):
    _inherit = 'res.partner'

    is_karyawan = fields.Boolean(string='Karyawan', default= False)
    is_konsumen = fields.Boolean(string='Pelanggan',default=False)

    
    
    
    
    
