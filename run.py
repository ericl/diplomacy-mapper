#!/usr/bin/env python

from map import *

# EXAMPLE CODE BELOW

fleet_move('nwg', 'nor', ENGLAND)
set('nor', ENGLAND)
fleet_convoy('nth', 'yor', 'bel', ENGLAND)
army_move('yor', 'bel', ENGLAND)
fleet_support_hold('iri', 'nao', ENGLAND)
fleet_support_hold('nao', 'iri', ENGLAND)

fleet_move('mao', 'por', FRANCE)
set('por', FRANCE)
set('spa', FRANCE)
army_move('gas', 'mar', FRANCE)
army_hold('ser', FRANCE)

army_move('stp', 'mos', RUSSIA)
army_support_move('lvn', 'stp', 'mos', RUSSIA)
disband('mos')
fleet_create('spa_nc', ITALY)

army_support_hold('pie', 'ven', ITALY)
army_hold('ven', ITALY)

army_move('bul', 'gre', TURKEY)
set('gre', TURKEY)
army_move('con', 'bul', TURKEY)
set('bul', TURKEY)
fleet_move_failed('bla', 'sev', TURKEY)

army_move_failed('ukr', 'sev', RUSSIA)
fleet_hold('rum', RUSSIA)
set('rum', RUSSIA)
army_move('gal', 'vie', RUSSIA)
set('vie', RUSSIA)

army_move_failed('trl', 'ven', AUSTRIA)
fleet_support_move('tri', 'trl', 'ven', AUSTRIA)
army_move('ser', 'bud', AUSTRIA)
fleet_create('ank', TURKEY)
army_create('war', RUSSIA)

army_move('ruh', 'hol', GERMANY)
set('hol', GERMANY)
set('bel', ENGLAND)
fleet_hold('den', GERMANY)
fleet_move_failed('tun', 'tyr', ITALY)
set('den', GERMANY)
army_move('ber', 'kie', GERMANY)

army_support_move('rom', 'spa', 'nap', TURKEY)
fleet_support_move('ion', 'spa', 'nap', FRANCE)
army_retreat('nap', 'apu', FRANCE)

fleet_convoy('wes', 'spa', 'nap', FRANCE)
fleet_convoy('tyr', 'spa', 'nap', FRANCE)
army_move('spa', 'nap', FRANCE)
set('nap', FRANCE)

done()
