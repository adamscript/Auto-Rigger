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

	def create(self, r = 10, nr = "Y", p = self.parent + "_ctrl", *pc = self.name, ik = False):
		#Create circle
		self.guide = ls(self.name + "_guide")
		self.ctrl = MakeNurbCircle(r = r, n = self.name + "_ctrl")

		#Set the circle plane normal
		if(nr == "X" || nr == "x"):
			self.ctrl.setNormalX()
		else if(nr == "Y" || nr == "y"):
			self.ctrl.setNormalY()
		else if(nr == "Z" || nr == "z"):
			self.ctrl.setNormalZ()

		#Create control offset for each control
		self.ctrl_offset = MakeGroup(self.name + "_ctrl", n = self.name + "_ctrl_offset")
		self.ctrl_offset.Transform().setTranslation(self.guide.getTranslation())
		self.ctrl_offset.Transform().setRotation(self.guide.getRotation())
		self.ctrl_offset.parent(p)

		#Edit control

		#COLLARBONE
		if(self.name == "l_collarbone" || self.name == "r_collarbone"):
			#Shape Vertex
			scale(1, 1, 0.5, self.name + "_ctrlShape.cv[0:8]", r = True)
			#Put collarbone ctrl between clavicle and shoulder
			if(self.name == "l_collarbone"):
				self.clavicle_pos = Transform().getTranslation(ls(l_clavicle_guide))
				self.shoulder_pos = Transform().getTranslation(ls(l_shoulder_guide))
			else if(self.name == "r_collarbone"):
				self.clavicle_pos = Transform().getTranslation(ls(r_clavicle_guide))
				self.shoulder_pos = Transform().getTranslation(ls(r_shoulder_guide))

			self.ctrl_offset.Transform().setTranslationX((self.clavicle_pos[0] + self.shoulder_pos[0]) / 2)
			self.ctrl_offset.Transform().setTranslationY(((self.clavicle_pos[1] + self.shoulder_pos[1]) / 2) + 5)
			self.ctrl_offset.Transform().setTranslationZ((self.clavicle_pos[2] + self.shoulder_pos[2]) / 2)
			#Rotate Pivot
			self.ctrlRotatePivot = self.name + "_ctrl.rotatePivot"
			self.ctrlRotatePivot.setTranslation(self.guide.getTranslation())
			#Parent Constraint to IK
			if(self.name == "l_collarbone"):
				self.ctrl.ParentConstraint('l_shoulder_ik')
			else if(self.name == "r_collarbone"):
				self.ctrl.ParentConstraint('r_shoulder_ik')
		else:
			pass

		#HIP
		if(self.name == "hip"):
			#Shape Vertex
			move(0, -6, 0, 'hip_ctrl.ep[0]', 'hip_ctrl.ep[4]', r = True)
        	move(0, 2, 0, 'hip_ctrl.ep[5:7]', 'hip_ctrl.ep[1:3]', r= True)
        	move(0, 3.5, 0, 'hip_ctrl.ep[6]', 'hip_ctrl.ep[2]', r = True)
        	scale(1, 1, 0.8, 'hip_ctrl.ep[0:8]', r = True)
        	#Move hip ctrl higher
        	self.thigh_pos = Transform().getTranslation(ls(l_thigh_guide))
        	self.knee_pos = Transform().getTranslation(ls(l_knee_guide))
        	move(0, (((l_thigh_pos[1] - l_knee_pos[1]) / 4) * -1), 0, 'self.hip_ctrl', ls = True)
        	makeIdentity('self.hip_ctrl')
        	#Rotate Pivot
        	self.ctrlRotatePivot = self.name + "hip_ctrl.rotatePivot"
        	self.waist_pos = ls('waist_guide')
        	self.ctrlRotatePivot.Transform.setTranslation(self.waist_pos)
        	#Parent Constraint to IK
        	self.ctrl.ParentConstraint(ls('l_thigh_ik'))
        	self.ctrl.ParentConstraint(ls('r_thigh_ik'))
        else:
        	pass

        #End of editing

        #Parent Constraint
        self.ctrl.ParentConstraint(pc)
