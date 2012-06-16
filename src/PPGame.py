#!/usr/bin/python

import PPUtil

from gi.repository import Mx
from gi.repository import GObject
from gi.repository import Clutter

class PPGame(Mx.Application):
	""" PPGame - Main class of the game """

	def __init__(self):
		Mx.Application.__init__(self)
		self.application_name = "pill-popper"
		self.flags = Mx.ApplicationFlags.SINGLE_INSTANCE
		
		# Loads css styles file
		style = Mx.Style()
		style.load_from_file("pp.css")

		# Creates the window and set stage properties
		self.window = self.create_window()
		self.stage = self.window.get_clutter_stage()
		self.stage.set_color(PPUtil.PPColor.black())

		self.screen_box = None
		self.menu = self.create_menu()
		self.player = None
		self.score_label = None
		self.lives_box = None
		self.score = 0

		# Load the logo
		logo = Clutter.Texture()
		logo.set_from_file("logo.png")
		self.window.get_toolbar().add_actor(logo)

		layout = Clutter.BinLayout()
		layout.x_align = Clutter.BinAlignment.FILL
		layout.y_align = Clutter.BinAlignment.FILL

		self.screen_box = box = Clutter.Box()
		self.screen_box.layout_manager = layout
		box.layout_manager = layout

		# Add menu
		box.add_actor(self.menu)
		layout.set_alignment(self.menu, Clutter.BinAlignment.CENTER, Clutter.BinAlignment.CENTER)

		self.window.set_child(box)
		self.stage.show()

	def create_menu(self):
		layout = Mx.BoxLayout()
		layout.set_orientation(Mx.Orientation.VERTICAL)

		item = Mx.Button()
		item.set_label("New game")
		item.connect("clicked", self.new_game_cb)
		layout.add_actor(item, 0)

		item = Mx.Button()
		item.set_label("High-scores")
		item.connect("clicked", self.high_scores_cb)
		layout.add_actor(item, 0)

		item = Mx.Button()
		item.set_label("Quit")
		item.connect("clicked", self.quit_cb)
		layout.add_actor(item, 0)
		
		layout.set_style_class("Menu")

		return layout

	def quit_cb(self):
		Clutter.main_quit()

	def new_game_cb(self):
		pass

	def high_scores_cb(self):
		pass

	def set_menu_visible(self, visible):
		return self.menu
