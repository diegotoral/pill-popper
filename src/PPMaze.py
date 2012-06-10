#!/usr/bin/python

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
		type = GObject.TYPE_OBJECT,
		default = None,
		flags = GObject.PARAM_READWRITE
	)

	safe = GObject.property(
		type = GObject.TYPE_BOOLEAN,
		default = False,
		flags = GObject.PARAM_READWRITE
	)

	paused = GObject.property(
		type = GObject.TYPE_BOOLEAN,
		default = False,
		flags = GObject.PARAM_READWRITE
	)

	safe_lifetime = GObject.property(
		type = GObject.TYPE_OBJECT,
		default = None,
		flags = GObject.PARAM_READWRITE
	)

	guys = []

	def __init__(self):
		Clutter.Actor.__init__(self)

		self.color = PPColor.blue()
		self.maze_trace = []

		self.set_size(28, 31)
		self.set_maze(default_maze)

	def set_size(self, width, height):
		if self.width == width and self.height == height:
			return

		self.width = width
		self.height = height
		self.maze = maze_data

		Clutter.Actor.queue_redraw(maze)

	def set_maze(self, new_maze):
		self.maze = new_maze

	def paint(self):
		""" TODO """
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
		""" TODO """

	def unmap(self):
		""" TODO """

	def reset(self):
		""" TODO """

	def pause(self):
		""" TODO """

	def play(self):
		""" TODO """
