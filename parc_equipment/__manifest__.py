# -*- coding: utf-8 -*-
##############################################################################
#
# This module is developed by Idealis Consulting SPRL
# Copyright (C) 2020 Idealis Consulting SPRL (<https://idealisconsulting.com>).
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Trane Parc Equipment',
    'category': 'Maintenace',
    'website': 'https://www.idealisconsulting.com/',
    'summary': 'Custom Maintenance module',
    'version': '15.0',
    'description': """
        """,
    'author': 'Idealis Consulting',
    'depends': [
        'maintenance',
        'stock',
        'account',
        'stock_enterprise',
        'documents',
    ],
    'data': [
        'views/equipment.xml',
        'views/stock_picking.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
