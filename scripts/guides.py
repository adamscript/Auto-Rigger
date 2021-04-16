class Guide:

	def __init__(self, name, translate, scale, parent):
		self.name = name
		self.translate = translate
		self.scale = scale
		self.parent = parent

	def create(self):
		spaceLocator(n = self.name, p = self.translate)
		parent(self.name, self.parent)
		scale(self.name, self.scale, self.scale, self.scale)


