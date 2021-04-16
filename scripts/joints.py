class Joint:

	def __init__(self, name, parent):
		self.name = name
		self.parent = parent

	def create(self):
		self.guide = ls(self.name + "_guide")
		self.joint = joint(radius = 1, p = self.guide.translate.get(), n = self.name)
		self.joint.parent(self.parent)

# SPINE #

spine_joint = Joint("spine")
waist_joint = Joint("waist")
chest_joint = Joint("chest")
sternum_joint = Joint("sternum")