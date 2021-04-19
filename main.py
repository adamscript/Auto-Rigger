from pymel.core import *
from pymel.core.nodetypes import *
#from rig.py import *

win = window(title="Awan's Auto Rigger")
layout = columnLayout()

#BUTTONS

guides_btn = button(l = "Create Guides", w = 200, p = layout)
mirrorguides_btn = button(l = "Mirror Guides", w = 200, p = layout)
deleteguides_btn = button(l = "Delete Guides", w = 200, p = layout)
separator()
displayaxes_btn = button(l = "Display Local Rotation Axes", w = 200, p = layout)
separator()
resetpose_btn = button(l = "Reset Pose", w = 200, p = layout)
separator()
humaniserig_btn = button(l = "Humanise Rig", w = 200, p = layout)
deleterig_btn = button(l = "Delete Rig", w = 200, p = layout)
separator()
autorig_btn = button(l = "Awto Rig!", w = 200, h = 150, p = layout)

def createGuides(*args):
	group(n = "guides")

	hips.createGuide(s = 10)
	waist.createGuide(s = 10)
	chest.createGuide(s = 10)
	sternum.createGuide(s = 10)
	l_clavicle.createGuide(s = 5)
	r_clavicle.createGuide(s = 5)

	neck.createGuide(s = 5)
	head.createGuide(s = 5)
	jaw.createGuide(s = 5)
	chin.createGuide(s = 5)
	l_eye.createGuide(s = 5)
	r_eye.createGuide(s = 5)

	l_shoulder.createGuide(s = 5)
	l_elbow.createGuide(s = 5)
	l_wrist.createGuide(s = 5)
	r_shoulder.createGuide(s = 5)
	r_elbow.createGuide(s = 5)
	r_wrist.createGuide(s = 5)
	
	l_finger_thumb_metacarpal.createGuide()
	l_finger_thumb_proximal.createGuide()
	l_finger_thumb_distal.createGuide()
	l_finger_thumb_tip.createGuide()
	r_finger_thumb_metacarpal.createGuide()
	r_finger_thumb_proximal.createGuide()
	r_finger_thumb_distal.createGuide()
	r_finger_thumb_tip.createGuide()
	
	l_finger_index_metacarpal.createGuide()
	l_finger_index_proximal.createGuide()
	l_finger_index_middle.createGuide()
	l_finger_index_distal.createGuide()
	l_finger_index_tip.createGuide()
	r_finger_index_metacarpal.createGuide()
	r_finger_index_proximal.createGuide()
	r_finger_index_middle.createGuide()
	r_finger_index_distal.createGuide()
	r_finger_index_tip.createGuide()
	
	l_finger_middle_metacarpal.createGuide()
	l_finger_middle_proximal.createGuide()
	l_finger_middle_middle.createGuide()
	l_finger_middle_distal.createGuide()
	l_finger_middle_tip.createGuide()
	r_finger_middle_metacarpal.createGuide()
	r_finger_middle_proximal.createGuide()
	r_finger_middle_middle.createGuide()
	r_finger_middle_distal.createGuide()
	r_finger_middle_tip.createGuide()
	
	l_finger_ring_metacarpal.createGuide()
	l_finger_ring_proximal.createGuide()
	l_finger_ring_middle.createGuide()
	l_finger_ring_distal.createGuide()
	l_finger_ring_tip.createGuide()
	r_finger_ring_metacarpal.createGuide()
	r_finger_ring_proximal.createGuide()
	r_finger_ring_middle.createGuide()
	r_finger_ring_distal.createGuide()
	r_finger_ring_tip.createGuide()
	
	l_finger_pinky_metacarpal.createGuide()
	l_finger_pinky_proximal.createGuide()
	l_finger_pinky_middle.createGuide()
	l_finger_pinky_distal.createGuide()
	l_finger_pinky_tip.createGuide()
	r_finger_pinky_metacarpal.createGuide()
	r_finger_pinky_proximal.createGuide()
	r_finger_pinky_middle.createGuide()
	r_finger_pinky_distal.createGuide()
	r_finger_pinky_tip.createGuide()

	l_thigh.createGuide(s = 5)
	l_knee.createGuide(s = 5)
	l_ankle.createGuide(s = 5)
	l_foot_ball.createGuide(s = 5)
	l_foot_toes.createGuide(s = 5)
	l_foot_heel.createGuide(s = 5)
	l_foot_inner.createGuide(s = 5)
	l_foot_outer.createGuide(s = 5)
	r_thigh.createGuide(s = 5)
	r_knee.createGuide(s = 5)
	r_ankle.createGuide(s = 5)
	r_foot_ball.createGuide(s = 5)
	r_foot_toes.createGuide(s = 5)
	r_foot_heel.createGuide(s = 5)
	r_foot_inner.createGuide(s = 5)
	r_foot_outer.createGuide(s = 5)
	
	print("Guides Created!")

def mirrorGuides(*args):
	print("Guides Mirrored!")

def deleteGuides(*args):
	allGuides = ls("guides")
	delete(allGuides)

	print("Guides Deleted!")

def displayAxes(*args):
	print("Axes Displayed!")

def resetPose(*args):
	print("Pose Resetted!")

def humaniseRig(*args):
	print("Rig Humanised!")

def deleteRig(*args):
	print("Rig Deleted!")

def createRig(*args):
	group(n = "rig")
	parent('rig', w = True)

	hips.createJoint(oj = False)
	waist.createJoint()
	chest.createJoint()
	sternum.createJoint()
	l_clavicle.createJoint()
	r_clavicle.createJoint()

	neck.createJoint()
	head.createJoint()
	jaw.createJoint()
	chin.createJoint(oj = False)
	l_eye.createJoint(oj = False)
	r_eye.createJoint(oj = False)

	l_shoulder.createJoint(ik = True)
	l_elbow.createJoint(ik = True)
	l_wrist.createJoint(oj = False, ik = True)
	r_shoulder.createJoint(ik = True)
	r_elbow.createJoint(ik = True)
	r_wrist.createJoint(oj = False, ik = True)
	
	l_finger_thumb_metacarpal.createJoint()
	l_finger_thumb_proximal.createJoint()
	l_finger_thumb_distal.createJoint()
	l_finger_thumb_tip.createJoint(oj = False)
	r_finger_thumb_metacarpal.createJoint()
	r_finger_thumb_proximal.createJoint()
	r_finger_thumb_distal.createJoint()
	r_finger_thumb_tip.createJoint(oj = False)
	
	l_finger_index_metacarpal.createJoint()
	l_finger_index_proximal.createJoint()
	l_finger_index_middle.createJoint()
	l_finger_index_distal.createJoint()
	l_finger_index_tip.createJoint(oj = False)
	r_finger_index_metacarpal.createJoint()
	r_finger_index_proximal.createJoint()
	r_finger_index_middle.createJoint()
	r_finger_index_distal.createJoint()
	r_finger_index_tip.createJoint(oj = False)
	
	l_finger_middle_metacarpal.createJoint()
	l_finger_middle_proximal.createJoint()
	l_finger_middle_middle.createJoint()
	l_finger_middle_distal.createJoint()
	l_finger_middle_tip.createJoint(oj = False)
	r_finger_middle_metacarpal.createJoint()
	r_finger_middle_proximal.createJoint()
	r_finger_middle_middle.createJoint()
	r_finger_middle_distal.createJoint()
	r_finger_middle_tip.createJoint(oj = False)
	
	l_finger_ring_metacarpal.createJoint()
	l_finger_ring_proximal.createJoint()
	l_finger_ring_middle.createJoint()
	l_finger_ring_distal.createJoint()
	l_finger_ring_tip.createJoint(oj = False)
	r_finger_ring_metacarpal.createJoint()
	r_finger_ring_proximal.createJoint()
	r_finger_ring_middle.createJoint()
	r_finger_ring_distal.createJoint()
	r_finger_ring_tip.createJoint(oj = False)
	
	l_finger_pinky_metacarpal.createJoint()
	l_finger_pinky_proximal.createJoint()
	l_finger_pinky_middle.createJoint()
	l_finger_pinky_distal.createJoint()
	l_finger_pinky_tip.createJoint(oj = False)
	r_finger_pinky_metacarpal.createJoint()
	r_finger_pinky_proximal.createJoint()
	r_finger_pinky_middle.createJoint()
	r_finger_pinky_distal.createJoint()
	r_finger_pinky_tip.createJoint(oj = False)

	l_thigh.createJoint(ik = True)
	l_knee.createJoint(ik = True)
	l_ankle.createJoint(oj = False, ik = True)
	l_foot_ball.createJoint(ik = True)
	l_foot_toes.createJoint(oj = False, ik = True)
	l_foot_heel.createJoint()
	l_foot_inner.createJoint()
	l_foot_outer.createJoint()
	r_thigh.createJoint(ik = True)
	r_knee.createJoint(ik = True)
	r_ankle.createJoint(oj = False, ik = True)
	r_foot_ball.createJoint(ik = True)
	r_foot_toes.createJoint(oj = False, ik = True)
	r_foot_heel.createJoint()
	r_foot_inner.createJoint()
	r_foot_outer.createJoint()

	print("Rig Created!")

#ADD COMMANDS TO BUTTONS WHEN PRESSED
guides_btn.setCommand(createGuides)
mirrorguides_btn.setCommand(mirrorGuides)
deleteguides_btn.setCommand(deleteGuides)
displayaxes_btn.setCommand(displayAxes)
resetpose_btn.setCommand(resetPose)
humaniserig_btn.setCommand(humaniseRig)
deleterig_btn.setCommand(deleteRig)
autorig_btn.setCommand(createRig)

win.show()

# RIG #

#GUIDES#

class Rig:

	def __init__(self, name, t = (0, 0, 0), p = ""):
		self.name = name
		self.translate = t
		self.parent = p

	def createGuide(self, s = 1):
		self.locator = spaceLocator(n = self.name + "_guide")
		self.locator.setTranslation(self.translate)
		self.locator.setScale([s, s, s])
		if (self.parent != ""):
			self.locator.setParent(self.parent + "_guide")

			self.guide_curve = NurbsCurve(p = [xform(self.name + "_guide", q = True, t = True, ws = True), xform(self.parent + "_guide", q = True, t = True, ws = True)], d = 1, n = self.name + "_guide_connector")
			cluster(self.name + "_guide_connector.cv[0]", n = self.name + "_guide_cluster")
			cluster(self.name + "_guide_connector.cv[1]", n = self.name + "_guide_parent_cluster")
			parent(self.name + "_guide_connector", "guides")
			parent(self.name + "_guide_clusterHandle", self.name + "_guide")
			parent(self.name + "_guide_parent_clusterHandle", self.parent + "_guide")
			setAttr(self.name + "_guide_connector.overrideEnabled", 1)
			setAttr(self.name + "_guide_connector.overrideDisplayType", 2)
			setAttr(self.name + "_guide_clusterHandleShape.visibility", 0)
			setAttr(self.name + "_guide_parent_clusterHandleShape.visibility", 0)
		else:
			self.locator.setParent("guides")

	def createJoint(self, oj = True, ik = False, rev = False):
		self.joint_pos = xform(ls(self.name + "_guide"), q = True, t = True, ws = True)
		print(self.joint_pos)
		self.joint = Joint(n = self.name, radius = 1, p = self.joint_pos)
		if(self.parent != ""):
			self.joint.setParent(self.parent)
		else:
			self.joint.setParent("rig")

		'''if oj:
			self.joint.orientJoint("yzx")
			self.joint.secondaryAxisOrient("zup")
		elif not oj:
			self.joint.orientJoint("none")'''

		if ik:
			self.jointIK = joint(radius = 1, p = self.joint_pos, n = self.name + "_ik")
			self.jointFK = joint(radius = 1, p = self.joint_pos, n = self.name + "_fk")

			self.jointIK.ParentConstraint(self.name)
			self.jointFK.ParentConstraint(self.name)

			#self.jointIK.hide()
			#self.jointFK.hide()
			print("ik")
		elif not ik:
			pass

		if rev:
			#self.jointrev = joint(radius = 1, p = self.joint_pos, n = self.name + "_rev")

			#self.jointrev.hide()
			print("rev")
		elif not rev:
			pass

# SPINE #
hips = Rig("hips", t = (0, 106.85, 2.652))
waist = Rig("waist", t = (0, 119.473, 5), p = "hips")
chest = Rig("chest", t = (0, 131.713, 5), p = "waist")
sternum = Rig("sternum", t = (0, 153.569, 1.886), p = "chest")
l_clavicle = Rig("l_clavicle", t = (3.107, 152.95, 4.807), p = "sternum")
r_clavicle = Rig("r_clavicle", t = (-3.107, 152.95, 4.807), p = "sternum")

# HEAD #
neck = Rig("neck", t = (0, 156.891, 1.886), p = "chest")
head = Rig("head", t = (0, 170.281, 3.69), p = "neck")
jaw = Rig("jaw", t = (0, 170.281, 7.175), p = "head")
chin = Rig("chin", t = (0, 163.448, 15.213), p = "jaw")
l_eye = Rig("l_eye", t = (3.125, 175.471, 12.969), p = "head")
r_eye = Rig("r_eye", t = (-3.125, 175.471, 12.969), p = "head")

# ARMS #
l_shoulder = Rig("l_shoulder", t = (19, 150.912, 0), p = "l_clavicle")
l_elbow = Rig("l_elbow", t = (31, 125, 0), p = "l_shoulder")
l_wrist = Rig("l_wrist", t = (45, 103, 6), p = "l_elbow")
r_shoulder = Rig("r_shoulder", t = (-19, 150.912, 0), p = "r_clavicle")
r_elbow = Rig("r_elbow", t = (-31, 125, 0), p = "r_shoulder")
r_wrist = Rig("r_wrist", t = (-45, 103, 6), p = "r_elbow")

# FINGERS #
#THUMB#
l_finger_thumb_metacarpal = Rig("l_finger_thumb_metacarpal", t = (45.382, 101.311, 7.675), p = "l_wrist")
l_finger_thumb_proximal = Rig("l_finger_thumb_proximal", t = (43.059, 97.395, 11.934), p = "l_finger_thumb_metacarpal")
l_finger_thumb_distal = Rig("l_finger_thumb_distal", t = (41.629, 94.984, 13.81), p = "l_finger_thumb_proximal")
l_finger_thumb_tip = Rig("l_finger_thumb_tip", t = (40.527, 92.962, 15.23), p = "l_finger_thumb_distal")
r_finger_thumb_metacarpal = Rig("r_finger_thumb_metacarpal", t = (-45.382, 101.311, 7.675), p = "r_wrist")
r_finger_thumb_proximal = Rig("r_finger_thumb_proximal", t = (-43.059, 97.395, 11.934), p = "r_finger_thumb_metacarpal")
r_finger_thumb_distal = Rig("r_finger_thumb_distal", t = (-41.629, 94.984, 13.81), p = "r_finger_thumb_proximal")
r_finger_thumb_tip = Rig("r_finger_thumb_tip", t = (-40.527, 92.962, 15.23), p = "r_finger_thumb_distal")
#INDEX#
l_finger_index_metacarpal = Rig("l_finger_index_metacarpal", t = (45.382, 101.311, 7.675), p = "l_wrist")
l_finger_index_proximal = Rig("l_finger_index_proximal", t = (47.514, 93.318, 13.052), p = "l_finger_index_metacarpal")
l_finger_index_middle = Rig("l_finger_index_middle", t = (48.218, 90.448, 14.448), p = "l_finger_index_proximal")
l_finger_index_distal = Rig("l_finger_index_distal", t = (48.629, 87.937, 15.367), p = "l_finger_index_middle")
l_finger_index_tip = Rig("l_finger_index_tip", t = (49, 86, 16), p = "l_finger_index_distal")
r_finger_index_metacarpal = Rig("r_finger_index_metacarpal", t = (-45.382, 101.311, 7.675), p = "r_wrist")
r_finger_index_proximal = Rig("r_finger_index_proximal", t = (-47.514, 93.318, 13.052), p = "r_finger_index_metacarpal")
r_finger_index_middle = Rig("r_finger_index_middle", t = (-48.218, 90.448, 14.448), p = "r_finger_index_proximal")
r_finger_index_distal = Rig("r_finger_index_distal", t = (-48.629, 87.937, 15.367), p = "r_finger_index_middle")
r_finger_index_tip = Rig("r_finger_index_tip", t = (-49, 86, 16), p = "r_finger_index_distal")
#MIDDLE#
l_finger_middle_metacarpal = Rig("l_finger_middle_metacarpal", t = (46, 101.217, 6.603), p = "l_wrist")
l_finger_middle_proximal = Rig("l_finger_middle_proximal", t = (49, 92.83, 10.919), p = "l_finger_middle_metacarpal")
l_finger_middle_middle = Rig("l_finger_middle_middle", t = (49.284, 89.204, 11.585), p = "l_finger_middle_proximal")
l_finger_middle_distal = Rig("l_finger_middle_distal", t = (48.689, 86, 12), p = "l_finger_middle_middle")
l_finger_middle_tip = Rig("l_finger_middle_tip", t = (48.271, 84.081, 12.244), p = "l_finger_middle_distal")
r_finger_middle_metacarpal = Rig("r_finger_middle_metacarpal", t = (-46, 101.217, 6.603), p = "r_wrist")
r_finger_middle_proximal = Rig("r_finger_middle_proximal", t = (-49, 92.83, 10.919), p = "r_finger_middle_metacarpal")
r_finger_middle_middle = Rig("r_finger_middle_middle", t = (-49.284, 89.204, 11.585), p = "r_finger_middle_proximal")
r_finger_middle_distal = Rig("r_finger_middle_distal", t = (-48.689, 86, 12), p = "r_finger_middle_middle")
r_finger_middle_tip = Rig("r_finger_middle_tip", t = (-48.271, 84.081, 12.244), p = "r_finger_middle_distal")
#RING#
l_finger_ring_metacarpal = Rig("l_finger_ring_metacarpal", t = (46, 100.783, 5.433), p = "l_wrist")
l_finger_ring_proximal = Rig("l_finger_ring_proximal", t = (49.763, 93.155, 8.511), p = "l_finger_ring_metacarpal")
l_finger_ring_middle = Rig("l_finger_ring_middle", t = (49.312, 89.47, 8.796), p = "l_finger_ring_proximal")
l_finger_ring_distal = Rig("l_finger_ring_distal", t = (48.491, 86.937, 8.919), p = "l_finger_ring_middle")
l_finger_ring_tip = Rig("l_finger_ring_tip", t = (48, 84.47, 9.081), p = "l_finger_ring_distal")
r_finger_ring_metacarpal = Rig("r_finger_ring_metacarpal", t = (-46, 100.783, 5.433), p = "r_wrist")
r_finger_ring_proximal = Rig("r_finger_ring_proximal", t = (-49.763, 93.155, 8.511), p = "r_finger_ring_metacarpal")
r_finger_ring_middle = Rig("r_finger_ring_middle", t = (-49.312, 89.47, 8.796), p = "r_finger_ring_proximal")
r_finger_ring_distal = Rig("r_finger_ring_distal", t = (-48.491, 86.937, 8.919), p = "r_finger_ring_middle")
r_finger_ring_tip = Rig("r_finger_ring_tip", t = (-48, 84.47, 9.081), p = "r_finger_ring_distal")
#PINKY#
l_finger_pinky_metacarpal = Rig("l_finger_pinky_metacarpal", t = (46, 100.686, 4.506), p = "l_wrist")
l_finger_pinky_proximal = Rig("l_finger_pinky_proximal", t = (50, 93.654, 6.103), p = "l_finger_pinky_metacarpal")
l_finger_pinky_middle = Rig("l_finger_pinky_middle", t = (49.827, 90.743, 5.949), p = "l_finger_pinky_proximal")
l_finger_pinky_distal = Rig("l_finger_pinky_distal", t = (49, 89.103, 5.64), p = "l_finger_pinky_middle")
l_finger_pinky_tip = Rig("l_finger_pinky_tip", t = (48, 87.794, 5.077), p = "l_finger_pinky_distal")
r_finger_pinky_metacarpal = Rig("r_finger_pinky_metacarpal", t = (-46, 100.686, 4.506), p = "r_wrist")
r_finger_pinky_proximal = Rig("r_finger_pinky_proximal", t = (-50, 93.654, 6.103), p = "r_finger_pinky_metacarpal")
r_finger_pinky_middle = Rig("r_finger_pinky_middle", t = (-49.827, 90.743, 5.949), p = "r_finger_pinky_proximal")
r_finger_pinky_distal = Rig("r_finger_pinky_distal", t = (-49, 89.103, 5.64), p = "r_finger_pinky_middle")
r_finger_pinky_tip = Rig("r_finger_pinky_tip", t = (-48, 87.794, 5.077), p = "r_finger_pinky_distal")

# LEGS #
l_thigh = Rig("l_thigh", t = (8.782, 101.69, 1.97), p = "hips")
l_knee = Rig("l_knee", t = (15, 54, 3), p = "l_thigh")
l_ankle = Rig("l_ankle", t = (18.901, 10, 0), p = "l_knee")
l_foot_ball = Rig("l_foot_ball", t = (21.058, 3.639, 14.117), p = "l_ankle")
l_foot_toes = Rig("l_foot_toes", t = (22.253, 3.639, 21.534), p = "l_foot_ball")
l_foot_heel = Rig("l_foot_heel", t = (18.406, 3.639, -4.419), p = "l_foot_toes")
l_foot_inner = Rig("l_foot_inner", t = (15.229, 3.639, 7.702), p = "l_foot_heel")
l_foot_outer = Rig("l_foot_outer", t = (25.864, 3.639, 7.702), p = "l_foot_heel")
r_thigh = Rig("r_thigh", t = (-8.782, 101.69, 1.97), p = "hips")
r_knee = Rig("r_knee", t = (-15, 54, 3), p = "r_thigh")
r_ankle = Rig("r_ankle", t = (-18.901, 10, 0), p = "r_knee")
r_foot_ball = Rig("r_foot_ball", t = (-21.058, 3.639, 14.117), p = "r_ankle")
r_foot_toes = Rig("r_foot_toes", t = (-22.253, 3.639, 21.534), p = "r_foot_ball")
r_foot_heel = Rig("r_foot_heel", t = (-18.406, 3.639, -4.419), p = "r_foot_toes")
r_foot_inner = Rig("r_foot_inner", t = (-15.229, 3.639, 7.702), p = "r_foot_heel")
r_foot_outer = Rig("r_foot_outer", t = (-25.864, 3.639, 7.702), p = "r_foot_heel")

#MAKE IK, HUMANISE, AND SKIN WEIGHT A CHECKBOX OPTION
#ADD MIRROR CONTROLS
#CREATE RIG UI