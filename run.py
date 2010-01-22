#!/usr/bin/env python

from map import *

# EXAMPLE CODE BELOW

fleet_move('nor', 'nwy', ENGLAND)
set('nwy', ENGLAND)
fleet_move_failed('nth', 'bel', ENGLAND)
army_hold('yor', ENGLAND)
fleet_support_hold('iri', 'nao', ENGLAND)
fleet_support_hold('nao', 'iri', ENGLAND)

fleet_move('mao', 'por', FRANCE)
set('por', FRANCE)
set('spa', FRANCE)
army_move('gas', 'mar', FRANCE)

army_move('stp', 'mos', RUSSIA)
army_support_move('lvn', 'stp', 'mos', RUSSIA)
disband('mos')
fleet_create('spa_sc', ITALY)
fleet_create('spa_nc', ITALY)

army_support_hold('pie', 'ven', ITALY)
army_hold('ven', ITALY)
fleet_move('ion', 'tun', ITALY)
set('tun', ITALY)

army_move('bul', 'gre', TURKEY)
set('gre', TURKEY)
army_move('con', 'bul', TURKEY)
set('bul', TURKEY)
fleet_move_failed('bla', 'sev', TURKEY)

army_move_failed('ukr', 'sev', RUSSIA)
fleet_hold('rum', RUSSIA)
set('rum', RUSSIA)
army_retreat('gal', 'vie', RUSSIA)
set('vie', RUSSIA)

army_move_failed('trl', 'ven', AUSTRIA)
fleet_support_move('tri', 'trl', 'ven', AUSTRIA)
army_move('ser', 'bud', AUSTRIA)
fleet_create('ank', TURKEY)
army_create('war', RUSSIA)

army_move_failed('ruh', 'bel', GERMANY)
fleet_hold('den', GERMANY)
set('den', GERMANY)
army_move('ber', 'kie', GERMANY)

fleet_convoy('wes', 'tyr', FRANCE)
fleet_convoy('tyr', 'nap', FRANCE)
army_convoy('spa', 'wes', 'nap', FRANCE)
set('nap', FRANCE)

done()
