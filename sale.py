# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2016 Apulia Software srl All Rights Reserved.
#                       www.apuliasoftware.it
#                       a.cometa@apuliasoftware.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, fields


class Sale(orm.Model):
    _inherit = "sale.order"

    def create(self, cr, uid, vals, context=None):
        if vals.get('name', '/') == '/':
            vals['name'] = self.pool['ir.sequence'].next_by_id(
                cr, uid, vals.get('sequence_id')) or '/'
        return super(Sale, self).create(cr, uid, vals, context=context)

    def copy(self, cr, uid, id, default=None, context=None):
        res = super(Sale, self).copy(cr, uid, id, default, context=context)
        new_seq = self.pool['ir.sequence'].next_by_id(
            cr, uid, self.read(cr, uid, id, ['sequence_id'])['sequence_id'][0])
        print default
        default.update({'name': new_seq})
        print default
        self.write(cr, uid, id, {'name': new_seq}, context=context)
        return res

    _columns = {
        'sequence_id': fields.many2one(
            'ir.sequence', "Sale sequence")
    }