##CONTROLLERS##

# SPINE #
#Parent Constraint

# HEAD #
#Parent Constraint

# ARMS FK #
#Parent Constraint

# ARMS IK #
#Parent Constraint

# FINGERS #
#parent

# LEGS FK #
#Parent Constraint

# LEGS IK #
#Parent Constraint

# FOOT IK #
#Parent Constraint
#Reverse Foot

#IK FK Systems
#IK FK Toggle

#Pole Vector Constraint

#Connections

#Lock and Hide Attributes

#Colour Overrides

class Controller:

	def __init__(self, name, parent):
		self.name = name
		self.parent = parent

	def create(self, r = 10, nr = "Y"):
		self.guide = ls(self.name + "_guide")
		self.ctrl = MakeNurbCircle(r = r, n = self.name + "_ctrl")

		if(nr == "X" || nr == "x"):
			self.ctrl.setNormalX()
		else if(nr == "Y" || nr == "y"):
			self.ctrl.setNormalY()
		else if(nr == "Z" || nr == "z"):
			self.ctrl.setNormalZ()

		self.ctrl_offset = MakeGroup(self.name + "_ctrl", n = self.name + "_ctrl_offset")
		self.ctrl_offset.Transform().setTranslation(self.guide.getTranslation())
		self.ctrl_offset.Transform().setRotation(self.guide.getRotation())
		self.ctrl_offset.parent(self.parent + "_ctrl")

