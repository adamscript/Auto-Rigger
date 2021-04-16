##JOINTS##

# SPINE #
spine_joint = Joint("spine")
waist_joint = Joint("waist")
chest_joint = Joint("chest")
sternum_joint = Joint("sternum")
#Joint Orientation

# HEAD #
#Joint Orientation

# ARMS #
#Joint Orientation

# ARMS IK #
#Joint Orientation
#Parent Constraint

# ARMS FK #
#Joint Orientation
#Parent Constraint

# LEGS #
#Joint Orientation

# LEGS IK #
#Joint Orientation
#Parent Constraint

# LEGS FK #
#Joint Orientation
#Parent Constraint

# FOOT #
#Joint Orientation

# FOOT IK #
#Joint Orientation
#Parent Constraint
#Reverse Foot

# FOOT FK #
#Joint Orientation
#Parent Constraint

#Hide IK Joints
#Hide FK Joints

#IK FK Systems

# FINGERS #

#THUMB#
#Joint Orientation

#INDEX#
#Joint Orientation

#MIDDLE#
#Joint Orientation

#RING#
#Joint Orientation

#PINKY#
#Joint Orientation

class Joint:

	def __init__(self, name, parent):
		self.name = name
		self.parent = parent

	def create(self):
		self.guide = ls(self.name + "_guide")
		self.joint = joint(radius = 1, p = self.guide.translate.get(), n = self.name)
		self.joint.parent(self.parent)