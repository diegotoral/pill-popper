#!/usr/bin/python

from gi.repository import GObject
from gi.repository import Clutter

class PPColor(GObject.GObject):
	""" PPColor - Colors factory """

	@staticmethod
	def red():
		return Clutter.Color.new (0xff, 0x00, 0x00, 0xff)
	
	@staticmethod
	def white():
		return Clutter.Color.new(0xff, 0xff, 0xff, 0xff)

	@staticmethod
	def blue():
		return Clutter.Color.new(0x21, 0x21, 0xde, 0xff)

	@staticmethod
	def black():
		return Clutter.Color.new(0x00, 0x00, 0x00, 0xff)

	@staticmethod
	def pill_color():
		return Clutter.Color.new(0xff, 0xb8, 0x97, 0xff)