##JOINTS##

# SPINE #
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

	def createJoint(self, oj = True, ik = False, rev = False):
		self.guide = ls(self.name + "_guide")
		self.joint = joint(radius = 1, p = self.guide.getTranslation(), n = self.name)
		self.joint.parent(self.parent)

		if(oj == True):
			self.joint.orientJoint('yzx')
			self.joint.secondaryAxisOrient('zup')
		else if(oj == False):
			self.joint.orientJoint('none')

		if(ik == True):
			self.jointIK = joint(radius = 1, p = self.guide.getTranslation(), n = self.name + "_ik")
			self.jointFK = joint(radius = 1, p = self.guide.getTranslation(), n = self.name + "_fk")

			self.jointIK.ParentConstraint(self.name)
			self.jointFK.ParentConstraint(self.name)

			self.jointIK.hide()
			self.jointFK.hide()
		else if(ik == False):
			pass

		if(rev == True):
			self.jointrev = joint(radius = 1, p = self.guide.getTranslation(), n = self.name + "_rev")

			self.jointrev.hide()
		else if(rev == False):
			pass