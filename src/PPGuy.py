#!/usr/bin/python

import PPMaze

from gi.repository import GObject
from gi.repository import Clutter

class PPDirection:
	""" PPDirection - PPGuy direction values """
	
	STATIONARY = 0
	UP = 1
	DOWN = 2
	LEFT = 3
	RIGHT = 4

class PPGuy(Clutter.Actor):
	""" PPGuy class - base class for some entities of the game """

	DEFAULT_SPEED = 100

	direction = GObject.property(
		type = GObject.TYPE_INT,
		default = PPDirection.STATIONARY,
		flags = GObject.PARAM_READWRITE
	)

	movement = GObject.property(
		type = GObject.TYPE_FLOAT,
		default = 0,
		flags = GObject.PARAM_READWRITE
	)

	speed = GObject.property(
		type = GObject.TYPE_INT,
		default = DEFAULT_SPEED,
		flags = GObject.PARAM_READWRITE
	)

	maze = GObject.property(
		type = GObject.TYPE_OBJECT,
		default = None,
		flags = GObject.PARAM_READWRITE
	)

	__gsignals__ = {
		'collide' : (GObject.SIGNAL_RUN_LAST, None, (GObject.TYPE_OBJECT,)),
		'die' : (GObject.SIGNAL_RUN_LAST, None, (GObject.TYPE_OBJECT,)),
		'spawn' : (GObject.SIGNAL_RUN_LAST, None, (int,)),
		'passing' : (GObject.SIGNAL_RUN_LAST, None, (int,)),
		'maze_set' : (GObject.SIGNAL_RUN_LAST, None, (GObject.TYPE_OBJECT, GObject.TYPE_OBJECT,))
	}

	def __init__(self):
		Clutter.Actor.__init__(self)

		self.spawn_point = 0
		self.x = self.y = 0
		self.timeline = None

		self.connect("parent-set", self.parent_set_cb)

	def do_collide(self, collidee):
		""" Empty """
		
	def do_die(self):
		""" Empty """

	def do_spawn(self):
		""" Empty """

	def do_passing(self, code):
		return (not code == PPMaze.PPPieces.WALL)

	def do_get_property(self, prop):
		if prop.name == "direction":
			return self.direction
		elif prop.name == "movement":
			return self.movement
		elif prop.name == "speed":
			return self.speed
		elif prop.name == "maze":
			return self.maze
		else:
			raise AttributeError, 'unknown property %s' % prop.name

	def do_set_property(self, prop, value):
		if prop.name == "direction":
			if self.direction <> value:
				self.direction = value
				self.queue_relayout()
		elif prop.name == "movement":
			if self.movement <> value:
				self.movement = value
				self.queue_redraw()
		elif prop.name == "speed":
			self.speed = value
		else:
			raise AttributeError, 'unknown property %s' % prop.name
		
	def pause(self):
		if self.timeline is not None:
			self.timeline.pause()

	def reset(self):
		# Get spawn coordinates
		self.maze.find_tile(self.spawn_point)
		
		if self.timeline is not None:
			self.timeline = None

		self.x = x
		self.y = y
		self.movement = 0.0
		self.spawn()

	def die(self):
		self.emit("die")

	def decide(self):
		pass

	def spawn(self):
		self.emit("spawn")

	def passing(self, code):
		self.emit("passing", code)

	def collide(self, collidee):
		self.emit("collide", collidee)

	def pass_through(self, code):
		pass

	def parent_set_cb(self):
		new_maze = None
		parent = self.get_parent()

		if isinstance(parent, PPMaze):
			new_maze = parent

		self.emit("maze_set", new_maze, self.maze)

		self.maze = new_maze