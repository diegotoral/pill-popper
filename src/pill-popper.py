#!/usr/bin/python

import sys
import PPGuy

from gi.repository import Clutter

def collide_cb(collidee):
	print "collide_cb"

def main():
	Clutter.init(sys.argv)

	# Tests
	guy = PPGuy.PPGuy()
	guy.set_property("direction", 100)
	guy.connect("collide", collide_cb)
	print guy.get_property("direction")

	#Clutter.main()

if __name__ == "__main__":
    sys.exit(main())