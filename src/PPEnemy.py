#!/usr/bin/python

import PPGuy
from PPUtil import PPColor

from gi.repository import Cogl
from gi.repository import GObject
from gi.repository import Clutter

class PPEnemy(PPGuy.PPGuy):
	""" PPEnemy """
	
	color = GObject.property(
		type = Clutter.Color,
		default = None,
		flags = GObject.PARAM_READWRITE
	)

	__gsignals__ = {
		'targetting' : (GObject.SIGNAL_RUN_LAST, None, (int, int,))
	}

	passed_barrier = False
	dead = False
	vulnerable = False

	def __init__(self):
		super(PPEnemy, self).__init__()

	def do_property_get(self, prop):
		if prop.name == "color":
			return self.color
		else:
			raise AttributeError, 'unknown property %s' % prop.name

	def do_property_set(self, prop, value):
		if porp.name == "color":
			self.color = value
			self.queue_redraw()
		else:
			raise AttributeError, 'unknown property %s' % prop.name
			
	def die(self):
		self.passed_barrier = False
		self.vulnerable = False
		self.dead = True

		self.set_speed(PPGuy.DEFAULT_SPEED / 2)

	def is_dead(self):
		return self.dead

	def paint(self):
		if not is_dead:
			# TODO: Determine color and secondary color

			Cogl.set_source_color(color)

			path = Cogl.Path

			# Draw head arc
			path.move_to(0.0, 0.5)
			path.arc(0.5, 0.5, 0.5, 0.5, 180, 360)

			# Side line
			path.line_to(1.0, 1.0)

			# Zig-zag
			for i in range(3,0):
				path.line_to(i/4.0 + 1/8.0, 0.9)
				path.line_to(i/4.0, 1.0)

			# Other side
			path.close()
			path.fill()

		# Eyeball
		Cogl.set_source_color(sec_color)

		path = Cogl.Path
		
		# Left
		path.arc(1/4.0, 0.4, 1/6.0, 1/6.0, 0, 360)
		path.fill()

		# Right
		path.arc(1.0 - 1/4.0, 0.4, 1/6.0, 1/6.0, 0, 360)
		path.fill()

		if is_vunerable and not is_dead:
			path.move_to(0, 0.70)
			for i in range(1,3):
				path.line_to(i/3.0 - 1/6.0, 0.80)
				path.line_to(i/3.0, 0.70)
			path.stroke()
		else:
			# Pupil
			offset_x = offset_y = 0.0

			if self.direction == PPDirection.UP:
				offset_y -= 1/8.0
			elif self.direction == PPDirection.RIGHT:
				offset_x += 1/8.0
			elif self.direction == PPDirection.DOWN:
				offset_y += 1/8.0
			elif self.direction == PPDirection.LEFT:
				offset_x -= 1/8.0

			Cogl.set_source_color(PPColor.blue())

			path.arc(1/4.0 + offset_x, 0.4 + offset_y, 1/9.0, 1/9.0, 0, 360)
			path.fill()

			path.arc(1.0 - 1/4.0 + offset_x, 0.4 + offset_y, 1/9.0, 1/9.0, 0, 360)
			path.fill()

	def is_vunerable(self):
		return self.vulnerable

	def collide(self, collidee):
		if not collidee.is_enemy and self.is_vunerable() and not collidee.is_dead() and not self.is_dead()
			self.die()