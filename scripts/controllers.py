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

	def createControl(self, r = 10, nr = "Y", p = self.parent + "_ctrl", pc = self.name, fk = False):
		#Create circle
		self.guide = ls(self.name + "_guide")

		if(fk == True):
			self.ctrl = MakeNurbCircle(r = r, n = self.name + "_fk_ctrl")
		else if(fk == False):
			self.ctrl = MakeNurbCircle(r = r, n = self.name + "_ctrl")

		#Set the circle plane normal
		if(nr == "X" || nr == "x"):
			self.ctrl.setNormalX()
		else if(nr == "Y" || nr == "y"):
			self.ctrl.setNormalY()
		else if(nr == "Z" || nr == "z"):
			self.ctrl.setNormalZ()

		#Create control offset for each control
		if(fk == True):
			self.ctrl_offset = MakeGroup(self.name + "_fk_ctrl", n = self.name + "_fk_ctrl_offset")
		else if(fk == False):
			self.ctrl_offset = MakeGroup(self.name + "_ctrl", n = self.name + "_ctrl_offset")
		
		self.ctrl_offset.Transform().setTranslation(self.guide.getTranslation())
		self.ctrl_offset.Transform().setRotation(self.guide.getRotation())

		self.ctrl_offset.Parent(p)

		#Parent Constraint
        self.ctrl.ParentConstraint(pc)

    def createIKControl(self, sj, ee, mj):
    	self.sj_pos = Transform().getTranslation(ls(sj))
    	self.ee_pos = Transform().getTranslation(ls(ee))
    	self.ee_rot = Transform().getRotation(ls(ee))

    	self.ctrl = MakeNurbCircle(r = 10, n = self.name + "_ik_ctrl")
    	self.ctrl_offset = MakeGroup(self.name + "_ctrl", n = self.name + "_ctrl_offset", em = True)
    	self.ctrl_offset.Transform().setTranslation(self.ee_pos)
    	self.ctrl_offset.Transform().setRotation(self.ee_rot)

    	self.ctrl_offset.Parent(self.parent)

    	self.ikhandle = IkHandle(n = self.name + "_ikHandle", sj = sj, ee = ee)
    	self.ikhandle.Parent(self.parent)

    	self.ikpole = MakeNurbSphere(r = 3, n = self.name + "_ikPole")
    	self.ikpole.Attribute().setAttr('makeNurbSphere1.sections', 4)
        self.ikpole.Attribute().setAttr('makeNurbSphere1.spans', 2)
        self.ikpole.Attribute().setAttr(self.name + '_ik_ctrl.overrideEnabled', 1)
        self.ikpole.Attribute().setAttr(self.name + '_ik_ctrl.overrideShading', 0)
        self.ikpole.Attribute().setAttr(self.name + '_ik_ctrl.overrideTexturing', 0)
        self.ikpole.Attribute().setAttr(self.name + '_ik_ctrl.overridePlayback', 0)

        self.ikpole_offset = MakeGroup(self.name + "_ik_ctrl", n = self.name + "_ik_ctrl_offset")
        self.ikpole_offset.Transform().setTranslationX((sj_pos[0] + ee_pos[0]) / 2)
        self.ikpole_offset.Transform().setTranslationY((sj_pos[1] + ee_pos[1]) / 2)
        self.ikpole_offset.Transform().setTranslationZ(-30, ls = True, r = True)
        self.ikpole_offset.MakeIdentity()
        self.ikpole_offset.Parent(self.parent)

        self.ikpole_curve = NurbsCurve(p = [Transform().getTranslation(ls(mj))], [Transform().getTranslation(self.ikpole)], d = 1, n = self.name + "_ik_ctrl_connector")
        self.ikpole_cluster = Cluster(self.name + "_ik_ctrl_connector.cv[1]", n = self.name + "_ik_ctrl_cluster")
        self.middlejoint_cluster = Cluster(self.name + "_ik_ctrl_connector.cv[0]", n = self.name + "_ik_ctrl_cluster")
        self.ikpole_cluster.Parent(self.ikpole)
        self.middlejoint_cluster.Parent(mj)
        self.ikpole_curve.Attribute().setAttr(self.name + "_ik_ctrl_connector.overrideEnable", 1)
        self.ikpole_curve.Attribute().setAttr(self.name + "_ik_ctrl_connector.overrideDisplayType", 2)

        self.ctrl.OrientConstraint(ee + "_ik")

	def edit()
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
