#!/usr/bin/python

import PPGuy
from Util import PPColor

from gi.repository import GObject

class PPEnemy(PPGuy):
	""" PPEnemy """
	
	passed_barrier = False
	dead = False
	vulnerable = False

	__gsignals__ = {
		'targetting' : (GObject.SIGNAL_RUN_LAST, None, (int, int,))
	}

	def __init__(self):
		super(PPEnemy, self).__init__()

	def die(self):
		self.passed_barrier = False
		self.vulnerable = False
		self.dead = True

		self.set_speed(PPGuy.DEFAULT_SPEED / 2)

	def is_dead(self):
		return self.dead

	def paint(self):
		""" TODO """

	def is_vunerable(self):
		return self.vulnerable