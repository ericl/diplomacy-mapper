#!/usr/bin/env python

from map import *

# EXAMPLE CODE BELOW

fleet_create('lon', ENGLAND)
fleet_create('edi', ENGLAND)
fleet_create('mar', FRANCE)
army_create('par', FRANCE)
army_create('mun', GERMANY)
army_create('ber', GERMANY)
fleet_create('smy', TURKEY)
army_create('stp', RUSSIA)
army_create('war', RUSSIA)
fleet_create('sev', RUSSIA)
fleet_create('rom', ITALY)

fleet_move('nwg', 'nor', ENGLAND)
set('nor', ENGLAND)
fleet_convoy('nth', 'yor', 'bel', ENGLAND)
army_move('yor', 'bel', ENGLAND)
set('bel', ENGLAND)

fleet_move('ion', 'tun', ITALY)
set('tun', ITALY)
army_hold('ven', ITALY)
army_support_hold('pie', 'ven', ITALY)

army_move('gas', 'spa', FRANCE)
army_move('spa', 'por', FRANCE)
fleet_move('mao', 'wes', FRANCE)
set('spa', FRANCE)
set('por', FRANCE)

army_move('ruh', 'hol', GERMANY)
set('hol', GERMANY)
army_move('ber', 'sil', GERMANY)
fleet_hold('den', GERMANY)
set('den', GERMANY)

fleet_move('fin', 'swe', RUSSIA)
army_move('gal', 'bud', RUSSIA)
fleet_hold('rum', RUSSIA)
army_move('ukr', 'gal', RUSSIA)
set('gal', RUSSIA)
set('bud', RUSSIA)
set('swe', RUSSIA)
set('rum', RUSSIA)

fleet_move_failed('tri', 'ven', AUSTRIA)
army_move_failed('ser', 'bul', AUSTRIA)
army_support_move('trl', 'tri', 'ven', AUSTRIA)
set('ser', AUSTRIA)

fleet_hold('bla', TURKEY)
army_move_failed('bul', 'ser', TURKEY)
army_move_failed('con', 'bul', TURKEY)
set('bul', TURKEY)

done()
