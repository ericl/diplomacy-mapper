#!/usr/bin/env python

from map import *

# EXAMPLE CODE BELOW

fleet_move_failed('eng', 'mao', ENGLAND)
fleet_move_failed('nth', 'bel', ENGLAND)
fleet_hold('nor', ENGLAND)
fleet_support_hold('nwg', 'nor', ENGLAND)
army_move('pic', 'bre', ENGLAND)
set('nor', ENGLAND)
set('bel', ENGLAND)
set('bre', ENGLAND)

set('tun', ITALY)
fleet_hold('tun', ITALY)
fleet_support_hold('tyr', 'tun', ITALY)
army_move('ven', 'pie', ITALY)
disband('mar')

army_move('bur', 'par', FRANCE)
fleet_move('lyo', 'mar', FRANCE)
army_move_failed('naf', 'tun', FRANCE)
army_support_move('spa', 'lyo', 'mar', FRANCE)
fleet_move_failed('wes', 'mao', FRANCE)
set('spa', FRANCE)
set('por', FRANCE)

fleet_move('bal', 'swe', GERMANY)
army_support_move('boh', 'trl', 'vie', GERMANY)
fleet_support_move('den', 'bal', 'swe', GERMANY)
army_move_failed('hol', 'bel', GERMANY)
army_move('trl', 'vie', GERMANY)
set('boh', GERMANY)
set('hol', GERMANY)
set('den', GERMANY)
set('vie', GERMANY)
set('swe', GERMANY)

army_move('gal', 'sil', RUSSIA)
fleet_move('rum', 'sev', RUSSIA)
army_move('stp', 'lvn', RUSSIA)
army_move('war', 'pru', RUSSIA)
army_support_move('bud', 'bul', 'ser', RUSSIA)
disband('swe')
disband('vie')
set('sil', RUSSIA)
set('gal', RUSSIA)
set('pru', RUSSIA)
set('bud', RUSSIA)
set('rum', RUSSIA)


fleet_support_move('alb', 'ser', 'gre', AUSTRIA)
army_move('ser', 'gre', AUSTRIA)
army_move_failed('tri', 'vie', AUSTRIA)
set('gre', AUSTRIA)
set('alb', AUSTRIA)

set('bul', TURKEY)
set('ser', TURKEY)
fleet_move('bla', 'con', TURKEY)
army_move('con', 'smy', TURKEY)
army_move('bul', 'ser', TURKEY)

done()
