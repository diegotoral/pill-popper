

class PPlayer(Clutter.actor):

	direction = GObject.property(
		type = GObject.TYPE_INT,
		default = PPDirection.STATIONARY,
		flags = GObject.PARAM_READWRITE
	)


	def __init__(self):
		"""empty"""

	def do_get_property(self, prop):
		if (prop.name == "mouth":
			return self.mouth

	def do_set_property(self, prop, value):
		if (prop.name == "mouth"):
			mouth = value
			self.queue_redraw()

	def dispose():
		"""empty"""

	def finalize():
		"""empty"""

	def paint():
		"""empty"""

	def animate_mouth():
		"""empty"""

	def die():
		"""empty"""

	def is_dead():
		"""empty"""

	def spawn():
		"""empty"""

	def pass_through():
		"""empty"""

	def passing():
		"""empty"""

	def colide():
		"""empty"""

	def direction_notify():
		"""empty"""

	def new():
		"""empty"""
