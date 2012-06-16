#!/usr/bin/python

import sys
import PPGuy, PPMaze, PPGame

from gi.repository import Mx
from gi.repository import GObject
from gi.repository import Clutter

def collide_cb(actor, collidee):
	collidee.set_property("direction", 69)
	print collidee.get_property("direction")

def main():
	Clutter.init(sys.argv)

	# Tests
	guy = PPGuy.PPGuy()
	guy.set_property("direction", 100)
	guy.connect("collide", collide_cb)
	print guy.get_property("direction")

	maze = PPMaze.PPMaze()
	print maze.get_property("width")
	print maze.get_property("height")

	guy.emit("collide", PPGuy.PPGuy())

	game = PPGame.PPGame()
	Mx.Application.run(game)

if __name__ == "__main__":
    sys.exit(main())