#!/usr/bin/python

import PPGuy
import PPTypes

from PPUtil import PPColor

from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Clutter

default_maze = [
	1,1,1,1,1,1,1,1,1,1,1,1,1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,
  	1,2,2,2,2,2,2,2,2,2,2,2,2, 1, 1,2,2,2,2,2,2,2,2,2,2,2,2,1,
  	1,2,1,1,1,1,2,1,1,1,1,1,2, 1, 1,2,1,1,1,1,1,2,1,1,1,1,2,1,
  	1,3,1,0,0,1,2,1,0,0,0,1,2, 1, 1,2,1,0,0,0,1,2,1,0,0,1,3,1,
  	1,2,1,1,1,1,2,1,1,1,1,1,2, 1, 1,2,1,1,1,1,1,2,1,1,1,1,2,1,
  	1,2,2,2,2,2,2,2,2,2,2,2,2, 2, 2,2,2,2,2,2,2,2,2,2,2,2,2,1,
  	1,2,1,1,1,1,2,1,1,2,1,1,1, 1, 1,1,1,1,2,1,1,2,1,1,1,1,2,1,
  	1,2,1,1,1,1,2,1,1,2,1,1,1, 0, 0,1,1,1,2,1,1,2,1,1,1,1,2,1,
  	1,2,2,2,2,2,2,1,1,2,2,2,2, 1, 1,2,2,2,2,1,1,2,2,2,2,2,2,1,
  	1,1,1,1,1,1,2,1,0,1,1,1,0, 1, 1,0,1,1,1,0,1,2,1,1,1,1,1,1,
  	0,0,0,0,0,1,2,1,0,1,1,1,0, 1, 1,0,1,1,1,0,1,2,1,0,0,0,0,0,
  	0,0,0,0,0,1,2,1,1,0,0,0,0, 0, 0,0,0,0,0,1,1,2,1,0,0,0,0,0,
  	0,0,0,0,0,1,2,1,1,0,1,1,1,10,10,1,1,1,0,1,1,2,1,0,0,0,0,0,
  	1,1,1,1,1,1,2,1,1,0,1,5,5, 0, 0,5,5,1,0,1,1,2,1,1,1,1,1,1,
  	0,0,0,0,0,0,2,0,0,0,1,0,6, 7, 8,9,0,1,0,0,0,2,0,0,0,0,0,0,
  	1,1,1,1,1,1,2,1,1,0,1,5,5, 5, 5,5,5,1,0,1,1,2,1,1,1,1,1,1,
  	0,0,0,0,0,1,2,1,1,0,1,1,1, 1, 1,1,1,1,0,1,1,2,1,0,0,0,0,0,
  	0,0,0,0,0,1,2,1,1,0,0,0,0,11,11,0,0,0,0,1,1,2,1,0,0,0,0,0,
  	0,0,0,0,0,1,2,1,1,0,1,1,1, 1, 1,1,1,1,0,1,1,2,1,0,0,0,0,0,
  	1,1,1,1,1,1,2,1,1,0,1,1,1, 0, 0,1,1,1,0,1,1,2,1,1,1,1,1,1,
  	1,2,2,2,2,2,2,2,2,2,2,2,2, 1, 1,2,2,2,2,2,2,2,2,2,2,2,2,1,
  	1,2,1,1,1,1,2,1,1,1,1,1,2, 1, 1,2,1,1,1,1,1,2,1,1,1,1,2,1,
  	1,2,1,1,0,1,2,1,1,1,1,1,2, 1, 1,2,1,1,1,1,1,2,1,0,1,1,2,1,
  	1,3,2,2,1,1,2,2,2,2,2,2,2, 4, 4,2,2,2,2,2,2,2,1,1,2,2,3,1,
  	1,1,1,2,1,1,2,1,1,2,1,1,1, 1, 1,1,1,1,2,1,1,2,1,1,2,1,1,1,
  	1,1,1,2,1,1,2,1,1,2,1,1,1, 0, 0,1,1,1,2,1,1,2,1,1,2,1,1,1,
  	1,2,2,2,2,2,2,1,1,2,2,2,2, 1, 1,2,2,2,2,1,1,2,2,2,2,2,2,1,
  	1,2,1,1,1,1,1,0,0,1,1,1,2, 1, 1,2,1,1,1,0,0,1,1,1,1,1,2,1,
  	1,2,1,1,1,1,1,1,1,1,1,1,2, 1, 1,2,1,1,1,1,1,1,1,1,1,1,2,1,
  	1,2,2,2,2,2,2,2,2,2,2,2,2, 2, 2,2,2,2,2,2,2,2,2,2,2,2,2,1,
  	1,1,1,1,1,1,1,1,1,1,1,1,1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1
]

class PPMaze(Clutter.Actor):
	""" PPMaze - represents the game board """

	width = GObject.property(
		type = GObject.TYPE_INT,
		default = 1,
		flags = GObject.PARAM_READWRITE
	)

	height = GObject.property(
		type = GObject.TYPE_INT,
		default = 1,
		flags = GObject.PARAM_READWRITE
	)

	color = GObject.property(
		type = Clutter.Color,
		default = PPColor.blue(),
		flags = GObject.PARAM_READWRITE
	)

	safe = GObject.property(
		type = GObject.TYPE_INT,
		default = 0,
		flags = GObject.PARAM_READWRITE
	)

	paused = GObject.property(
		type = GObject.TYPE_BOOLEAN,
		default = False,
		flags = GObject.PARAM_READWRITE
	)

	safe_lifetime = GObject.property(
		type = Clutter.Timeline,
		default = None,
		flags = GObject.PARAM_READWRITE
	)

	maze = []

	maze_trace = []

	guys = []

	def __init__(self):
		Clutter.Actor.__init__(self)

		self.set_size(28, 31)
		self.set_maze(default_maze)

	def do_property_get(self, prop):
		if prop.name == "width":
			return self.width
		elif prop.name == "height":
			return self.height
		elif prop.name == "color":
			return self.color
		elif prop.name == "safe":
			return self.safe_lifetime.get_duration() - self.safe_lifetime.get_elapsed_time()
		else:
			raise AttributeError, 'unknown property %s' % prop.name

	def do_property_set(self, prop, value):
		if prop.name == "width":
			self.set_size(value, self.height)
		elif prop.name == "height":
			self.set_size(self.width, value)
		elif prop.name == "color":
			self.color = value
			self.queue_redraw()
		elif prop.name == "safe":
			set_safe(value)
		else:
			raise AttributeError, 'unknown property %s' % prop.name

	def set_size(self, width, height):
		""" TODO: Finish this method """
		if self.width == width and self.height == height:
			return

		maze_data = []
		for x in self.maze:
			maze_data = x

		self.width = width
		self.height = height
		self.maze = maze_data
		self.maze_trace = []

		self.queue_redraw()

	def set_maze(self, new_maze):
		self.maze = new_maze

	def set_safe(self, msecs):
		""" TODO: Finish this method """
		if self.safe_lifetime is None:
			self.safe_lifetime = Clutter.Timeline(msecs)
			self.safe_lifetime.connect("new-frame", new_frame_cb)
			self.safe_lifetime.connect("completed", completed_cb)

		self.safe_lifetime.set_duration(msecs)
		self.safe_lifetime.rewind()
		self.safe_lifetime.start()

	def new_frame_cb(self, msecs):
		self.queue_redraw()

	def completed_cb(self):
		self.safe_lifetime = None
		self.notify("safe")

		self.queue_redraw()

	def paint(self):
		""" TODO: Finish this method """
		self.get_size(width, height)
		tile_width = width / self.width
		tile_height = height / self.height
		curve = min(tile_width / 4.0, tile_height / 4.0)
		xpadding = tile_width / 3.0
		ypadding = tile_height / 3.0

		for y in range(self.height):
			for x in range(sefl.width):
				value = self.maze[x*self.width+x]
				pill_radius = curve / 2.0

	def map(self):
		for x in self.guys:
			x.map()

	def unmap(self):
		for x in self.guys:
			x.unmap()

	def find_tile(self, code):
		""" TODO: Finish this method """
		for x in self.maze:
			if x == code:
				pass # Must return x and y coordinates

	def reset(self):
		for guy in self.guys:
			guy.reset()

		if self.safe_lifetime is not None:
			self.safe_lifetime = None

	def pause(self):
		self.paused = True

		for guy in self.guys:
			guy.pause()

		if self.safe_lifetime is not None:
			self.safe_lifetime.pause()

	def play(self):
		""" TODO """
