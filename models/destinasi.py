from odoo import api, fields, models


class destinasi(models.Model):
    _name = 'gikuy.destinasi'
    _description = 'Destinasi Wisata'

    
    
   
    name = fields.Selection(string='Nama Daerah', selection=[('bali', 'Bali 1'), ('blii', 'Bali 2'),('bliii', 'Bali 3'),('bdg', 'Bandung 1'),('bdgg', 'Bandung 2'),('jgj', 'Jogja 1'),('jgjj', 'Jogja 2'),('smg', 'Semarang'),('pls', 'Bromo + Bali 1'),('plss', 'Bandung + Jogja'),('ppls', 'Jogja + Bromo + Bali 2'),('tmbh', 'Bandung 2 + Bromo + Bali 3')])
    harga = fields.Integer(string='Harga')
    detail = fields.Char(string='Detail Tempat dan Acara')
    
    

    
