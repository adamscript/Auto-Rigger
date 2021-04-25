from pymel.core import *
from pymel.core.nodetypes import *
import pymel.core as pm
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
	global prog
	prog = 1

	hip.createGuide(s = 10)
	waist.createGuide(s = 10)
	chest.createGuide(s = 10)
	collarbone.createGuide(s = 10)
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
	global prog
	prog = 1

	print("Guides Deleted!")

def displayAxes(*args):
	selectedJoints = ls(type = 'joint', sl = True)

	if not selectedJoints:
		allJoints = ls(type = 'joint')
		toggle(allJoints, la = True)
	else:
		print(selectedJoints)

		toggle(selectedJoints, la = True)
		print("Axes Displayed!")

def resetPose(*args):
	print("Pose Resetted!")

def humaniseRig(*args):
	print("Rig Humanised!")

def deleteRig(*args):
	allRig = ls("rig")
	delete(allRig)
	mel.eval('MLdeleteUnused;')
	global prog
	prog = 1

	print("Rig Deleted!")

def createRig(*args):
	group(n = "rig")
	parent('rig', w = True)

	root_ctrl = MakeNurbCircle(r = 50, n = "root_ctrl")
	root_ctrl.setNormalY(1)
	root_ctrl.setNormalZ(0)
	group('root_ctrl', n = "root_ctrl_offset")
	parent('root_ctrl_offset', 'rig')
	
	grp_ctrl = MakeNurbCircle(r = 30, n = "grp_ctrl")
	grp_ctrl.setNormalY(1)
	grp_ctrl.setNormalZ(0)
	group('grp_ctrl', n = "grp_ctrl_offset")
	xform('grp_ctrl_offset', t = xform("hip_guide", q = True, t = True, ws = True))
	parent('grp_ctrl_offset', 'root_ctrl')

	spine_ctrl = MakeNurbCircle(r = 25, n = "spine_ctrl")
	spine_ctrl.setNormalY(1)
	spine_ctrl.setNormalZ(0)
	group('spine_ctrl', n = "spine_ctrl_offset")
	xform('spine_ctrl_offset', t = xform("hip_guide", q = True, t = True, ws = True))
	parent('spine_ctrl_offset', 'grp_ctrl')

	group(n = "l_hand_ctrl", em = True)
	group("l_hand_ctrl", n = "l_hand_ctrl_offset")
	group(n = "r_hand_ctrl", em = True)
	group("r_hand_ctrl", n = "r_hand_ctrl_offset")
	
	global prog
	prog = 1

	# JOINTS #

	hip.createJoint()
	waist.createJoint()
	chest.createJoint()
	collarbone.createJoint()

	neck.createJoint()
	head.createJoint()
	jaw.createJoint()
	chin.createJoint()
	l_eye.createJoint()
	r_eye.createJoint()

	
	l_clavicle.createJoint()
	l_shoulder.createJoint(ik = True)
	l_elbow.createJoint(ik = True)
	l_wrist.createJoint(ik = True)
	r_clavicle.createJoint()
	r_shoulder.createJoint(ik = True)
	r_elbow.createJoint(ik = True)
	r_wrist.createJoint(ik = True)
	
	l_finger_thumb_metacarpal.createJoint()
	l_finger_thumb_proximal.createJoint()
	l_finger_thumb_distal.createJoint()
	l_finger_thumb_tip.createJoint()
	r_finger_thumb_metacarpal.createJoint()
	r_finger_thumb_proximal.createJoint()
	r_finger_thumb_distal.createJoint()
	r_finger_thumb_tip.createJoint()
	
	l_finger_index_metacarpal.createJoint()
	l_finger_index_proximal.createJoint()
	l_finger_index_middle.createJoint()
	l_finger_index_distal.createJoint()
	l_finger_index_tip.createJoint()
	r_finger_index_metacarpal.createJoint()
	r_finger_index_proximal.createJoint()
	r_finger_index_middle.createJoint()
	r_finger_index_distal.createJoint()
	r_finger_index_tip.createJoint()
	
	l_finger_middle_metacarpal.createJoint()
	l_finger_middle_proximal.createJoint()
	l_finger_middle_middle.createJoint()
	l_finger_middle_distal.createJoint()
	l_finger_middle_tip.createJoint()
	r_finger_middle_metacarpal.createJoint()
	r_finger_middle_proximal.createJoint()
	r_finger_middle_middle.createJoint()
	r_finger_middle_distal.createJoint()
	r_finger_middle_tip.createJoint()
	
	l_finger_ring_metacarpal.createJoint()
	l_finger_ring_proximal.createJoint()
	l_finger_ring_middle.createJoint()
	l_finger_ring_distal.createJoint()
	l_finger_ring_tip.createJoint()
	r_finger_ring_metacarpal.createJoint()
	r_finger_ring_proximal.createJoint()
	r_finger_ring_middle.createJoint()
	r_finger_ring_distal.createJoint()
	r_finger_ring_tip.createJoint()
	
	l_finger_pinky_metacarpal.createJoint()
	l_finger_pinky_proximal.createJoint()
	l_finger_pinky_middle.createJoint()
	l_finger_pinky_distal.createJoint()
	l_finger_pinky_tip.createJoint()
	r_finger_pinky_metacarpal.createJoint()
	r_finger_pinky_proximal.createJoint()
	r_finger_pinky_middle.createJoint()
	r_finger_pinky_distal.createJoint()
	r_finger_pinky_tip.createJoint()

	l_thigh.createJoint(ik = True)
	l_knee.createJoint(ik = True)
	l_ankle.createJoint(ik = True, rev = True)
	l_foot_ball.createJoint(ik = True, rev = True)
	l_foot_toes.createJoint(ik = True, rev = True)
	l_foot_heel.createJoint(rev = True)
	l_foot_inner.createJoint()
	l_foot_outer.createJoint()
	r_thigh.createJoint(ik = True)
	r_knee.createJoint(ik = True)
	r_ankle.createJoint(ik = True, rev = True)
	r_foot_ball.createJoint(ik = True, rev = True)
	r_foot_toes.createJoint(ik = True, rev = True)
	r_foot_heel.createJoint(rev = True)
	r_foot_inner.createJoint()
	r_foot_outer.createJoint()

	#Orient Joint
	hip.orientJoint()
	waist.orientJoint()
	chest.orientJoint()
	collarbone.orientJoint()

	neck.orientJoint()
	head.orientJoint()
	jaw.orientJoint()
	chin.orientJoint(oj = False)
	l_eye.orientJoint(oj = False)
	r_eye.orientJoint(oj = False)
	
	l_clavicle.orientJoint()
	l_shoulder.orientJoint(ik = True)
	l_elbow.orientJoint(ik = True)
	l_wrist.orientJoint(oj = False, ik = True)
	r_clavicle.orientJoint()
	r_shoulder.orientJoint(ik = True)
	r_elbow.orientJoint(ik = True)
	r_wrist.orientJoint(oj = False, ik = True)
	
	l_finger_thumb_metacarpal.orientJoint()
	l_finger_thumb_proximal.orientJoint()
	l_finger_thumb_distal.orientJoint()
	l_finger_thumb_tip.orientJoint(oj = False)
	r_finger_thumb_metacarpal.orientJoint()
	r_finger_thumb_proximal.orientJoint()
	r_finger_thumb_distal.orientJoint()
	r_finger_thumb_tip.orientJoint(oj = False)
	
	l_finger_index_metacarpal.orientJoint()
	l_finger_index_proximal.orientJoint()
	l_finger_index_middle.orientJoint()
	l_finger_index_distal.orientJoint()
	l_finger_index_tip.orientJoint(oj = False)
	r_finger_index_metacarpal.orientJoint()
	r_finger_index_proximal.orientJoint()
	r_finger_index_middle.orientJoint()
	r_finger_index_distal.orientJoint()
	r_finger_index_tip.orientJoint(oj = False)
	
	l_finger_middle_metacarpal.orientJoint()
	l_finger_middle_proximal.orientJoint()
	l_finger_middle_middle.orientJoint()
	l_finger_middle_distal.orientJoint()
	l_finger_middle_tip.orientJoint(oj = False)
	r_finger_middle_metacarpal.orientJoint()
	r_finger_middle_proximal.orientJoint()
	r_finger_middle_middle.orientJoint()
	r_finger_middle_distal.orientJoint()
	r_finger_middle_tip.orientJoint(oj = False)
	
	l_finger_ring_metacarpal.orientJoint()
	l_finger_ring_proximal.orientJoint()
	l_finger_ring_middle.orientJoint()
	l_finger_ring_distal.orientJoint()
	l_finger_ring_tip.orientJoint(oj = False)
	r_finger_ring_metacarpal.orientJoint()
	r_finger_ring_proximal.orientJoint()
	r_finger_ring_middle.orientJoint()
	r_finger_ring_distal.orientJoint()
	r_finger_ring_tip.orientJoint(oj = False)
	
	l_finger_pinky_metacarpal.orientJoint()
	l_finger_pinky_proximal.orientJoint()
	l_finger_pinky_middle.orientJoint()
	l_finger_pinky_distal.orientJoint()
	l_finger_pinky_tip.orientJoint(oj = False)
	r_finger_pinky_metacarpal.orientJoint()
	r_finger_pinky_proximal.orientJoint()
	r_finger_pinky_middle.orientJoint()
	r_finger_pinky_distal.orientJoint()
	r_finger_pinky_tip.orientJoint(oj = False)

	l_thigh.orientJoint(ik = True)
	l_knee.orientJoint(ik = True)
	l_ankle.orientJoint(oj = False, ik = True)
	l_foot_ball.orientJoint()
	l_foot_toes.orientJoint(oj = False)
	#l_foot_heel.orientJoint()
	#l_foot_inner.orientJoint()
	#l_foot_outer.orientJoint()
	r_thigh.orientJoint(ik = True)
	r_knee.orientJoint(ik = True)
	r_ankle.orientJoint(oj = False, ik = True)
	r_foot_ball.orientJoint()
	r_foot_toes.orientJoint(oj = False)
	#r_foot_heel.orientJoint()
	#r_foot_inner.orientJoint()
	#r_foot_outer.orientJoint()

	#IK FK SYSTEMS
        
	group('l_thigh_ik', 'l_thigh_fk', n =  'l_leg_ik_fk')
	group('l_shoulder_ik', 'l_shoulder_fk', n = 'l_arm_ik_fk')

	group('r_thigh_ik', 'r_thigh_fk', n =  'r_leg_ik_fk')
	group('r_shoulder_ik', 'r_shoulder_fk', n = 'r_arm_ik_fk')

	group('l_leg_ik_fk', 'l_arm_ik_fk', 'r_leg_ik_fk', 'r_arm_ik_fk', n = 'ik_fk_joints')
	parent('ik_fk_joints', 'root_ctrl')

	# CONTROLLERS #
	
	hip.createControl(r = 25)
	waist.createControl(r = 20)
	chest.createControl(r = 20)
	collarbone.createControl(r = 10)

	neck.createControl(r = 10)
	head.createControl(r = 15, nr = 'z')
	jaw.createControl(r = 2)
	#chin.createControl(r = 2)
	l_eye.createControl(r = 2)
	r_eye.createControl(r = 2)

	l_clavicle.createControl(r = 5)
	l_shoulder.createControl(r = 10, fk = True)
	l_elbow.createControl(r = 10, fk = True)
	l_wrist.createControl(r = 10, fk = True)
	r_clavicle.createControl(r = 5)
	r_shoulder.createControl(r = 10, fk = True)
	r_elbow.createControl(r = 10, fk = True)
	r_wrist.createControl(r = 10, fk = True)

	l_arm.createIKControl(sj = 'l_shoulder', ee = 'l_wrist', mj = 'l_elbow')
	r_arm.createIKControl(sj = 'r_shoulder', ee = 'r_wrist', mj = 'r_elbow')

	l_finger_thumb_metacarpal.createControl()
	l_finger_thumb_proximal.createControl()
	l_finger_thumb_distal.createControl()
	l_finger_thumb_tip.createControl()
	r_finger_thumb_metacarpal.createControl()
	r_finger_thumb_proximal.createControl()
	r_finger_thumb_distal.createControl()
	r_finger_thumb_tip.createControl()
	
	l_finger_index_metacarpal.createControl()
	l_finger_index_proximal.createControl()
	l_finger_index_middle.createControl()
	l_finger_index_distal.createControl()
	l_finger_index_tip.createControl()
	r_finger_index_metacarpal.createControl()
	r_finger_index_proximal.createControl()
	r_finger_index_middle.createControl()
	r_finger_index_distal.createControl()
	r_finger_index_tip.createControl()
	
	l_finger_middle_metacarpal.createControl()
	l_finger_middle_proximal.createControl()
	l_finger_middle_middle.createControl()
	l_finger_middle_distal.createControl()
	l_finger_middle_tip.createControl()
	r_finger_middle_metacarpal.createControl()
	r_finger_middle_proximal.createControl()
	r_finger_middle_middle.createControl()
	r_finger_middle_distal.createControl()
	r_finger_middle_tip.createControl()
	
	l_finger_ring_metacarpal.createControl()
	l_finger_ring_proximal.createControl()
	l_finger_ring_middle.createControl()
	l_finger_ring_distal.createControl()
	l_finger_ring_tip.createControl()
	r_finger_ring_metacarpal.createControl()
	r_finger_ring_proximal.createControl()
	r_finger_ring_middle.createControl()
	r_finger_ring_distal.createControl()
	r_finger_ring_tip.createControl()
	
	l_finger_pinky_metacarpal.createControl()
	l_finger_pinky_proximal.createControl()
	l_finger_pinky_middle.createControl()
	l_finger_pinky_distal.createControl()
	l_finger_pinky_tip.createControl()
	r_finger_pinky_metacarpal.createControl()
	r_finger_pinky_proximal.createControl()
	r_finger_pinky_middle.createControl()
	r_finger_pinky_distal.createControl()
	r_finger_pinky_tip.createControl()

	l_thigh.createControl(r = 15, fk = True)
	l_knee.createControl(r = 10, fk = True)
	l_ankle.createControl(r = 10, fk = True)
	l_foot_ball.createControl(r = 5)
	l_foot_toes.createControl(r = 5)
	#l_foot_heel.createControl()
	#l_foot_inner.createControl()
	#l_foot_outer.createControl()
	r_thigh.createControl(r = 15, fk = True)
	r_knee.createControl(r = 10, fk = True)
	r_ankle.createControl(r = 10, fk = True)
	r_foot_ball.createControl(r = 5)
	r_foot_toes.createControl(r = 5)
	#r_foot_heel.createControl()
	#r_foot_inner.createControl()
	#r_foot_outer.createControl()

	l_leg.createIKControl(sj = 'l_thigh', ee = 'l_ankle', mj = 'l_knee')
	r_leg.createIKControl(sj = 'r_thigh', ee = 'r_ankle', mj = 'r_knee')

	l_foot.createReverseControl(sj = 'l_ankle', ee = 'l_foot_toes', mj = 'l_foot_ball', bj = 'l_foot_heel')
	r_foot.createReverseControl(sj = 'r_ankle', ee = 'r_foot_toes', mj = 'r_foot_ball', bj = 'r_foot_heel')
	
	editControlShape()
	
	#IK FK SYSTEMS
        
	parentConstraint('hip_ctrl', 'l_leg_ik_fk', mo = True)

	parent("l_clavicle_ctrl_offset", 'collarbone_ctrl')
	parentConstraint('l_clavicle_ctrl', 'l_arm_ik_fk', mo = True)
	#parentConstraint('collarbone_ctrl', 'l_arm_ik_fk', mo = True)

	parentConstraint('hip_ctrl', 'r_leg_ik_fk', mo = True)

	parent("r_clavicle_ctrl_offset", 'collarbone_ctrl')
	parentConstraint('r_clavicle_ctrl', 'r_arm_ik_fk', mo = True)
	#parentConstraint('collarbone_ctrl', 'r_arm_ik_fk', mo = True)

	#lock and hide attributes

	offsetAttr = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']
	offsetGroup = ls('*_offset')
	ikfkToggle = ls('*ikfk_toggle_ctrl')
	
	for i in offsetGroup:
		for j in offsetAttr:
			setAttr(i + '.' + j, l = True, k = False, cb = False)

	for i in ikfkToggle:
		for j in offsetAttr:
			setAttr(i + '.' + j, l = True, k = False, cb = False)

	#colour overrides

	all_ctrl = ls('*ctrl')
	all_l_ctrl = ls('l_*ctrl')
	all_r_ctrl = ls('r_*ctrl')

	for i in all_ctrl:
		setAttr(i + ".overrideEnabled", 1)
		setAttr(i + ".overrideColor", 17)

	for i in all_l_ctrl:
		setAttr(i + ".overrideColor", 14)

	for i in all_r_ctrl:
		setAttr(i + ".overrideColor", 13)

	setAttr("grp_ctrl.overrideColor", 18)

	delete(ch = True, all = True)

	print("Rig Created!")

def progressNum(max):
	global prog
	prog+=1
	return str(int((prog/max)*100))

def editControlShape():
	#Eye_LookAt
	xform('l_eye_ctrl', t = (0, 15, 0), r = True)
	xform('r_eye_ctrl', t = (0, 15, 0), r = True)

	eyesLookAt_ctrl = MakeNurbCircle(r = 3, n = "eyesLookAt_ctrl")
	eyesLookAt_ctrl.setNormalY(1)
	eyesLookAt_ctrl.setNormalZ(0)
	group('eyesLookAt_ctrl', n = "eyesLookAt_ctrl_offset")
	xform("eyesLookAt_ctrl_offset", t = (0, (xform('l_eye_ctrl', q = True, t = True, ws = True))[1], (xform('l_eye_ctrl', q = True, t = True, ws = True))[2]), ro = xform('l_eye_ctrl_offset', q = True, ro = True, ws = True), ws = True)
	xform('eyesLookAt_ctrlShape.cv[0:8]', s = (3, 1, 2), r = True)

	parent('l_eye_ctrl_offset', 'eyesLookAt_ctrl')
	parent('r_eye_ctrl_offset', 'eyesLookAt_ctrl')
	parent('eyesLookAt_ctrl_offset', 'grp_ctrl')
	
	#Neck
	xform('neck_ctrl.rotatePivot', t = xform('neck_guide', q = True, t = True, ws = True), ws = True)
	
	#Collarbone
	xform('collarbone_ctrlShape.cv[0:8]', s = (2, 1, 1), r = True)
	xform('collarbone_ctrlShape.cv[1]', t = (0, -20, 0), r = True)
	xform('collarbone_ctrlShape.cv[5]', t = (0, -20, 0), r = True)

	#L_Clavicle
	xform('l_clavicle_ctrlShape.cv[0:8]', s = (1, 1, 0.5), r = True)
	xform('l_clavicle_ctrl.rotatePivot', t = xform('l_clavicle_guide', q = True, t = True, ws = True), ws = True)

	#R_Clavicle
	xform('r_clavicle_ctrlShape.cv[0:8]', s = (1, 1, 0.5), r = True)
	xform('r_clavicle_ctrl.rotatePivot', t = xform('r_clavicle_guide', q = True, t = True, ws = True), ws = True)

	#Hip
	l_thigh_pos = xform("l_thigh_guide", q = True, t = True, ws = True)
	r_thigh_pos = xform("r_thigh_guide", q = True, t = True, ws = True)
	l_knee_pos = xform("l_knee_guide", q = True, t = True, ws = True)
	r_knee_pos = xform("r_knee_guide", q = True, t = True, ws = True)

	xform('hip_ctrl.ep[0]', t = (0, -6, 0), r = True)
	xform('hip_ctrl.ep[4]', t = (0, -6, 0), r = True)
	xform('hip_ctrl.ep[5:7]', t = (0, 2, 0), r = True)
	xform('hip_ctrl.ep[1:3]', t = (0, 2, 0), r = True)
	xform('hip_ctrl.ep[6]', t = (0, 3.5, 0), r = True)
	xform('hip_ctrl.ep[2]', t = (0, 3.5, 0), r = True)
	xform('hip_ctrl.ep[0:8]', t = (0, (((l_thigh_pos[1] - l_knee_pos[1]) / 4) * -1), 0), s = (1, 1, 0.8), r = True)

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

		print("Creating Guides... (" + progressNum(83) + "%)")
		
	def createJoint(self, ik = False, rev = False):
		self.joint_pos = xform(self.name + "_guide", q = True, t = True, ws = True)
		self.joint = Joint(n = self.name, radius = 1, p = self.joint_pos)
		if (self.name.endswith("_foot_heel") or self.name.endswith("_foot_inner") or self.name.endswith("_foot_outer")):
			delete(self.name)
		elif(self.parent != ""):
			self.joint.setParent(self.parent)
		else:
			self.joint.setParent("root_ctrl")

		if ik:
			self.jointIK = Joint(n = self.name + "_ik", radius = 1, p = self.joint_pos)
			self.jointFK = Joint(n = self.name + "_fk", radius = 1, p = self.joint_pos)
			if(self.parent == "l_clavicle" or self.parent == "r_clavicle" or self.parent == "hip"):
				self.jointIK.setParent(self.parent)
				self.jointFK.setParent(self.parent)
			else:
				self.jointIK.setParent(self.parent + "_ik")
				self.jointFK.setParent(self.parent + "_fk")
		elif not ik:
			pass

		if rev:
			self.jointrev = Joint(radius = 1, p = self.joint_pos, n = self.name + "_rev")
			if (self.name == "l_ankle" or self.name == "r_ankle"):
				self.jointrev.setParent(self.parent)
			else:
				self.jointrev.setParent(self.parent + "_rev")
		elif not rev:
			pass
		
		hide (ls ('*_ik', type = 'joint'))
		hide (ls ('*_fk', type = 'joint'))
		hide (ls ('*_rev', type = 'joint'))

		print("Creating Joints... (" + progressNum(240) + "%)")

		return self
	
	def orientJoint(self, oj = True, ik = False):
		if oj:
			self.joint.orientJoint('yzx', sao = 'zup')
			if ik:
				self.jointIK.orientJoint('yzx', sao = 'zup')
				self.jointFK.orientJoint('yzx', sao = 'zup')

				parentConstraint(self.jointIK, self.joint, mo = False)
				parentConstraint(self.jointFK, self.joint, mo = False)
			elif not ik:
				pass
		elif not oj:
			self.joint.orientJoint('none')
			if ik:
				self.jointIK.orientJoint('none')
				self.jointFK.orientJoint('none')

				parentConstraint(self.jointIK, self.joint, mo = False)
				parentConstraint(self.jointFK, self.joint, mo = False)
			elif not ik:
				pass
		
		print("Creating Joints... (" + progressNum(240) + "%)")

	def createControl(self, r = 2, nr = "Y", fk = False):
		#Create circle
		#self.guide = ls(self.name + "_guide")

		if fk:
			self.ctrl = MakeNurbCircle(r = r, n = self.name + "_fk_ctrl")
		elif not fk:
			self.ctrl = MakeNurbCircle(r = r, n = self.name + "_ctrl")

		#Set the circle plane normal
		if(nr == "X" or nr == "x"):
			self.ctrl.setNormalX(1)
			self.ctrl.setNormalZ(0)
		elif(nr == "Y" or nr == "y"):
			self.ctrl.setNormalY(1)
			self.ctrl.setNormalZ(0)
		elif(nr == "Z" or nr == "z"):
			self.ctrl.setNormalZ(1)

		#Create control offset for each control
		if fk:
			self.ctrl_offset = group(em = True, n = self.name + "_fk_ctrl_offset")
			parent(self.name + "_fk_ctrl", self.name + "_fk_ctrl_offset")
		elif not fk:
			self.ctrl_offset = group(em = True, n = self.name + "_ctrl_offset")
			parent(self.name + "_ctrl", self.name + "_ctrl_offset")

		if(self.name == "collarbone"):
			xform(self.ctrl_offset, t = xform("neck_guide", q = True, t = True, ws = True), ro = xform("neck", q = True, ro = True, ws = True))
		elif(self.name == "neck"):
			self.neck_pos = xform("neck_guide", q = True, t = True, ws = True)
			self.head_pos = xform("head_guide", q = True, t = True, ws = True)
			xform(self.ctrl_offset, t = ((self.neck_pos[0], (self.neck_pos[1] + self.head_pos[1])/2, self.neck_pos[2])), ro = xform(self.name, q = True, ro = True, ws = True))
		elif(self.name.endswith("_clavicle")):
			self.clavicle_pos = xform(self.name + "_guide", q = True, t = True, ws = True)
			self.clavicle_rot = xform(self.name + "_guide", q = True, ro = True, ws = True)
			if(self.name.startswith("l_")):
				self.shoulder_pos = xform("l_shoulder_guide", q = True, t = True, ws = True)
			elif(self.name.startswith("r_")):
				self.shoulder_pos = xform("r_shoulder_guide", q = True, t = True, ws = True)
			xform(self.name + "_ctrl_offset", t = ((self.clavicle_pos[0] + self.shoulder_pos[0])/2, ((self.clavicle_pos[1] + self.shoulder_pos[1])/2) + 5, (self.clavicle_pos[2] + self.shoulder_pos[2])/2), ro = self.clavicle_rot, ws = True)
		elif(self.name == "jaw"):
			xform(self.ctrl_offset, t = xform("chin_guide", q = True, t = True, ws = True), ro = xform("chin", q = True, ro = True, ws = True))
			xform(self.name + "_ctrl.rotatePivot", t = xform("jaw_guide", q = True, t = True, ws = True), a = True, ws = True)
		else:
			xform(self.ctrl_offset, t = xform(self.name + "_guide", q = True, t = True, ws = True), ro = xform(self.name, q = True, ro = True, ws = True))

		if fk:
			if (self.parent.endswith("_clavicle") or self.parent == "hip"):
				parent(self.name + "_fk_ctrl_offset", self.parent + "_ctrl")
			else:
				parent(self.name + "_fk_ctrl_offset", self.parent + "_fk_ctrl")
		elif not fk:
			if (self.parent.endswith("_wrist")):
				if(self.name.startswith("l_")):
					parent('l_hand_ctrl_offset', 'grp_ctrl')
					parent(self.name + "_ctrl_offset", "l_hand_ctrl")
					parentConstraint(self.parent, 'l_hand_ctrl', mo = True)
				elif(self.name.startswith("r_")):
					parent('r_hand_ctrl_offset', 'grp_ctrl')
					parent(self.name + "_ctrl_offset", "r_hand_ctrl")
					parentConstraint(self.parent, 'r_hand_ctrl', mo = True)
			elif (self.parent.endswith("_ankle")):
				parent(self.name + "_ctrl_offset", "grp_ctrl")
				parentConstraint(self.parent, self.name + "_ctrl_offset", mo = True)
			elif (self.name == "hip" or self.name == "waist"):
				parent(self.name + "_ctrl_offset", "spine_ctrl")
			elif (self.parent != ""):
				parent(self.name + "_ctrl_offset", self.parent + "_ctrl")
			else:
				parent(self.name + "_ctrl_offset", "grp_ctrl")

		#Parent Constraint
		if fk:
			parentConstraint(self.name + "_fk_ctrl", self.name + "_fk", mo = False)
		elif not fk:
			if(self.name == "collarbone" or self.name.endswith("_clavicle")):
				pass
			elif(self.name == "jaw"):
				parentConstraint(self.name + "_ctrl", self.name, mo = True)
			elif(self.name.endswith("_eye")):
				aimConstraint(self.name + "_ctrl", self.name, aim = (0, 1, 0), u = (0, 0, 1) , mo = True)
			else:
				parentConstraint(self.name + "_ctrl", self.name, mo = False)
		
		print("Creating Controllers... (" + progressNum(240) + "%)")

	def createIKControl(self, sj, ee, mj, rev = False):
		#Get start joint and end effector position and rotation
		self.sj_pos = xform(sj, q = True, t = True, ws = True)
		self.ee_pos = xform(ee, q = True, t = True, ws = True)
		self.ee_rot = xform(mj, q = True, ro = True, ws = True)
		#Create IK Control Circle
		self.IKctrl = MakeNurbCircle(r = 10, n = self.name + "_ik_ctrl")
		self.IKctrl_offset = group(n = self.name + "_ik_ctrl_offset", em = True)
		self.IKctrl.setNormalY(1)
		self.IKctrl.setNormalZ(0)
		parent(self.name + "_ik_ctrl", self.name + "_ik_ctrl_offset")
		xform(self.name + "_ik_ctrl_offset", t = self.ee_pos, ro = self.ee_rot, ws = True)
		parent(self.name + "_ik_ctrl_offset", "grp_ctrl")
		orientConstraint(self.name + "_ik_ctrl", ee + "_ik")
		#Create IK Handle
		self.ikhandle = ikHandle(n = self.name + "_ikHandle", sj = sj + "_ik", ee = ee + "_ik")
		parent(self.name + "_ikHandle", self.name + "_ik_ctrl")
		#Create IK Pole
		self.ikpole = MakeNurbSphere(r = 3, n = self.name + "_ikpole_ctrl")
		rename('makeNurbSphere1', self.name + "_ikpole_ctrlInput")
		setAttr(self.name + '_ikpole_ctrlInput.sections', 4)
		setAttr(self.name + '_ikpole_ctrlInput.spans', 2)
		setAttr(self.name + '_ikpole_ctrl.overrideEnabled', 1)
		setAttr(self.name + '_ikpole_ctrl.overrideShading', 0)
		setAttr(self.name + '_ikpole_ctrl.overrideTexturing', 0)
		setAttr(self.name + '_ikpole_ctrl.overridePlayback', 0)

		self.ikpole_offset = group(n = self.name + "_ikpole_ctrl_offset", em = True)
		parent(self.name + "_ikpole_ctrl", self.name + "_ikpole_ctrl_offset")
		xform(self.name + "_ikpole_ctrl_offset", t = xform(mj, q = True, t = True, ws = True), ws = True)
		if(self.name == "l_arm" or self.name == "r_arm"):
			move(0, 0, -30, self.name + "_ikpole_ctrl_offset", ls = True, r = True)
		elif(self.name == "l_leg" or self.name == "r_leg"):
			move(0, 0, 30, self.name + "_ikpole_ctrl_offset", ls = True, r = True)
		makeIdentity(self.name + "_ikpole_ctrl", a = True, t = True)
		parent(self.name + "_ikpole_ctrl_offset", 'grp_ctrl')

		poleVectorConstraint(self.name + "_ikpole_ctrl", self.name + "_ikHandle")

		curve(p = [xform(mj, q = True, t = True, ws = True), xform(self.name + "_ikpole_ctrl", q = True, t = True, ws = True)], d = 1, ws = True, n = self.name + "_ikpole_ctrl_connector")
		cluster(self.name + '_ikpole_ctrl_connector.cv[0]', n = self.name + "_ikpole_cluster")
		cluster(self.name + '_ikpole_ctrl_connector.cv[1]', n = self.name + "_ikpole_ctrl_cluster")
		parent(self.name + "_ikpole_clusterHandle", mj)
		parent(self.name + "_ikpole_ctrl_clusterHandle", self.name + "_ikpole_ctrl")
		setAttr(self.name + "_ikpole_ctrl_connector.overrideEnabled", 1)
		setAttr(self.name + "_ikpole_ctrl_connector.overrideDisplayType", 2)
		parent(self.name + "_ikpole_ctrl_connector", self.name + '_ikpole_ctrl')
		setAttr(self.name + "_ikpole_clusterHandle.visibility", 0)
		setAttr(self.name + "_ikpole_ctrl_clusterHandle.visibility", 0)

		#IK FK Toggle
		#Create IK FK Toggle
		self.iktoggle = MakeNurbPlane(w = 10, d = 1, ax = (0, 0, 1), n = self.name + "_ikfk_toggle_ctrl")
		rename('makeNurbPlane1', self.name + "_ikfk_toggle_ctrlInput")
		setAttr (self.name + "_ikfk_toggle_ctrlInput.width", 10)
		setAttr (self.name + "_ikfk_toggle_ctrl.overrideEnabled", 1)
		setAttr(self.name + '_ikfk_toggle_ctrl.overrideShading', 0)
		setAttr(self.name + '_ikfk_toggle_ctrl.overrideTexturing', 0)
		setAttr(self.name + '_ikfk_toggle_ctrl.overridePlayback', 0)
		#Create IK FK Toggle Text
		self.iktext = textCurves(text = "IK", f = "Lucida Sans Unicode", n = self.name + "_IK_lttr")
		self.fktext = textCurves(text = "FK", f = "Lucida Sans Unicode", n = self.name + "_FK_lttr")
		xform(self.name + "_IK_lttrShape", t = (xform(self.name + "_ikfk_toggle_ctrl", q = True, t = True, ws = True)), ws = True, cp = True)
		xform(self.name + "_FK_lttrShape", t = (xform(self.name + "_ikfk_toggle_ctrl", q = True, t = True, ws = True)), ws = True, cp = True)
		xform(self.name + "_IK_lttrShape", s = (7, 7, 7))
		xform(self.name + "_FK_lttrShape", s = (7, 7, 7))
		setAttr(self.name + "_IK_lttrShape.overrideEnabled", 1)
		setAttr(self.name + "_FK_lttrShape.overrideEnabled", 1)
		setAttr(self.name + "_IK_lttrShape.overrideDisplayType", 2)
		setAttr(self.name + "_FK_lttrShape.overrideDisplayType", 2)
		
		parent(self.name + "_IK_lttrShape", self.name + "_ikfk_toggle_ctrl")
		parent(self.name + "_FK_lttrShape", self.name + "_ikfk_toggle_ctrl")
		
		#Create ikfk toggle offset
		self.iktoggle_offset = group(n = self.name + "_ikfk_toggle_ctrl_offset")
		parent(self.name + "_ikfk_toggle_ctrl_offset", w = True)
		parent(self.name + "_ikfk_toggle_ctrl", self.name + "_ikfk_toggle_ctrl_offset")
		xform(self.name + "_ikfk_toggle_ctrl_offset", t = (xform(ee, q = True, t = True, ws = True)))
		xform(self.name + "_ikfk_toggle_ctrl_offset", t = (0, 10, -20), r = True)
		parent(self.name + "_ikfk_toggle_ctrl_offset", 'grp_ctrl')
		pointConstraint(self.parent, self.name + "_ikfk_toggle_ctrl_offset", mo = True)
		#Add ik fk toggle attribute
		if(self.name == "l_arm" or self.name == "r_arm"):
			addAttr(self.name + "_ikfk_toggle_ctrl", ln = "IK_FK_Toggle", k = True, min = 0, max = 1, dv = 0)
		elif(self.name == "l_leg" or self.name == "r_leg"):
			addAttr(self.name + "_ikfk_toggle_ctrl", ln = "IK_FK_Toggle", k = True, min = 0, max = 1, dv = 1)
		#Connections
		connectAttr(self.name + '_ikfk_toggle_ctrl.IK_FK_Toggle', sj + '_parentConstraint1.' + sj + '_ikW0', f = True)
		connectAttr(self.name + '_ikfk_toggle_ctrl.IK_FK_Toggle', mj + '_parentConstraint1.' + mj + '_ikW0', f = True)
		connectAttr(self.name + '_ikfk_toggle_ctrl.IK_FK_Toggle', ee + '_parentConstraint1.' + ee + '_ikW0', f = True)
		shadingNode('reverse', n = self.name + '_ikfk_switch', au = True)
		connectAttr(self.name + '_ikfk_toggle_ctrl.IK_FK_Toggle', self.name + '_ikfk_switch.inputX', f = True)
		connectAttr(self.name + '_ikfk_switch.outputX', sj + '_parentConstraint1.' + sj + '_fkW1', f = True)
		connectAttr(self.name + '_ikfk_switch.outputX', mj + '_parentConstraint1.' + mj + '_fkW1', f = True)
		connectAttr(self.name + '_ikfk_switch.outputX', ee + '_parentConstraint1.' + ee + '_fkW1', f = True)
		connectAttr(self.name + '_ikfk_toggle_ctrl.IK_FK_Toggle', self.name + '_ikpole_ctrl_offset.visibility', f = True)
		connectAttr(self.name + '_ikfk_toggle_ctrl.IK_FK_Toggle', self.name + '_ik_ctrl_offset.visibility', f = True)
		connectAttr(self.name + '_ikfk_toggle_ctrl.IK_FK_Toggle', self.name + '_ikpole_ctrl_connector.visibility', f = True)
		connectAttr(self.name + '_ikfk_toggle_ctrl.IK_FK_Toggle', self.name + '_IK_lttrShape.visibility', f = True)
		connectAttr(self.name + '_ikfk_switch.outputX', self.name + '_FK_lttrShape.visibility', f = True)
		connectAttr(self.name + '_ikfk_switch.outputX', sj + '_fk_ctrl_offset.visibility', f = True)

		print("Creating IK Controls... (" + progressNum(240) + "%)")

	def createReverseControl(self, sj, ee, mj, bj):
		parent(sj + "_rev", self.parent + "_ik_ctrl")
		reroot(bj + "_rev")

		ikHandle(n = mj + '_ikHandle', sj = sj + '_ik', ee = mj + '_ik', sol = 'ikSCsolver')
		ikHandle(n = ee + '_ikHandle', sj = mj + '_ik', ee = ee + '_ik', sol = 'ikSCsolver')
		parent(mj + '_ikHandle', mj + '_rev')
		parent(ee + '_ikHandle', ee + '_rev')
		parent(self.parent + '_ikHandle', sj + '_rev')
		#parent(bj + '_rev', self.parent + '_ik_ctrl')

		group(ee + '_ikHandle', n = self.name + "_toes_tap")
		group(bj + '_rev', n = self.name + '_bank_inner')
		group(self.name + '_bank_inner', n = self.name + '_bank_outer')

		inner_pos = xform(self.name + '_inner_guide', q = True, t = True, ws = True)
		outer_pos = xform(self.name + '_outer_guide', q = True, t = True, ws = True)
		ball_pos = xform(self.name + '_ball_guide', q = True, t = True, ws = True)
		xform(ee + '_tap.rotatePivot', t = ball_pos, ws = True)
		xform(self.name + '_bank_inner.rotatePivot', t = inner_pos, ws = True)
		xform(self.name + '_bank_outer.rotatePivot', t = outer_pos, ws = True)

		select(self.parent + '_ikfk_toggle_ctrl')
		addAttr(ln = "Heel_Twist", k = True)
		addAttr(ln = "Toes_Twist", k = True)
		addAttr(ln = "Toe_Tap", k = True)
		addAttr(ln = "Bank", k = True)
		addAttr(ln = "Roll", k = True, min = -30, max = 30, dv = 0)

		connectAttr(self.parent + '_ikfk_toggle_ctrl.Heel_Twist', bj + '_rev.rotateY')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Toes_Twist', ee + '_rev.rotateY')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Toe_Tap', ee + '_tap.rotateX')

		shadingNode('condition', n = self.name + '_bank_condition', au = True)
		setAttr(self.name + '_bank_condition.operation', 2)
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Bank', self.name + '_bank_condition.colorIfFalseG')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Bank', self.name + '_bank_condition.colorIfTrueR')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Bank', self.name + '_bank_condition.firstTerm')
		connectAttr(self.name + '_bank_condition.outColorR', self.name + '_bank_inner.rotateZ')
		connectAttr(self.name + '_bank_condition.outColorG', self.name + '_bank_outer.rotateZ')

		shadingNode('condition', au = True, n = bj + '_roll_condition')
		shadingNode('condition', au = True, n = mj + '_roll_condition')
		shadingNode('condition', au = True, n = ee + '_roll_condition')
		shadingNode('multiplyDivide', au = True, n = self.name + '_roll_multi')
		shadingNode('plusMinusAverage', au = True, n = self.name + '_roll_pma')
		setAttr(bj + '_roll_condition.operation', 4)
		setAttr(mj + '_roll_condition.operation', 2)
		setAttr(ee + '_roll_condition.operation', 2)
		setAttr(ee + '_roll_condition.secondTerm', 10)
		setAttr(self.name + '_roll_multi.input2X', 1)
		setAttr(self.name + '_roll_multi.input2Y', 1)
		setAttr(self.name + '_roll_multi.input2Z', 1)
		setAttr(self.name + '_roll_pma.operation', 2)
		setAttr(self.name + '_roll_pma.input1D[1]', 10)
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Roll', bj + '_roll_condition.colorIfTrueR')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Roll', bj + '_roll_condition.firstTerm')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Roll', mj + '_roll_condition.colorIfTrueR')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Roll', mj + '_roll_condition.firstTerm')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Roll', self.name + '_roll_pma.input1D[0]')
		connectAttr(self.parent + '_ikfk_toggle_ctrl.Roll', ee + '_roll_condition.firstTerm')
		connectAttr(self.name + '_roll_pma.output1D', ee + '_roll_condition.colorIfTrueR')
		connectAttr(bj + '_roll_condition.outColorR', self.name + '_roll_multi.input1X')
		connectAttr(mj + '_roll_condition.outColorR', self.name + '_roll_multi.input1Y')
		connectAttr(ee + '_roll_condition.outColorR', self.name + '_roll_multi.input1Z')
		connectAttr(self.name + '_roll_multi.outputX', bj + '_rev.rotateZ')
		connectAttr(self.name + '_roll_multi.outputY', mj + '_rev.rotateZ')
		connectAttr(self.name + '_roll_multi.outputZ', ee + '_rev.rotateZ')

		print("Creating Reverse Foot Controls... (" + progressNum(240) + "%)")

# SPINE #
hip = Rig("hip", t = (0, 106.85, 2.652))
waist = Rig("waist", t = (0, 119.473, 5), p = "hip")
chest = Rig("chest", t = (0, 131.713, 5), p = "waist")
collarbone = Rig("collarbone", t = (0, 153.569, 1.886), p = "chest")

# HEAD #
neck = Rig("neck", t = (0, 156.891, 1.886), p = "collarbone")
head = Rig("head", t = (0, 170.281, 3.69), p = "neck")
jaw = Rig("jaw", t = (0, 170.281, 7.175), p = "head")
chin = Rig("chin", t = (0, 163.448, 15.213), p = "jaw")
l_eye = Rig("l_eye", t = (3.125, 175.471, 12.969), p = "head")
r_eye = Rig("r_eye", t = (-3.125, 175.471, 12.969), p = "head")

# ARMS #
l_clavicle = Rig("l_clavicle", t = (3.107, 152.95, 4.807), p = "collarbone")
l_shoulder = Rig("l_shoulder", t = (19, 150.912, 0), p = "l_clavicle")
l_elbow = Rig("l_elbow", t = (31, 125, 0), p = "l_shoulder")
l_wrist = Rig("l_wrist", t = (45, 103, 6), p = "l_elbow")
r_clavicle = Rig("r_clavicle", t = (-3.107, 152.95, 4.807), p = "collarbone")
r_shoulder = Rig("r_shoulder", t = (-19, 150.912, 0), p = "r_clavicle")
r_elbow = Rig("r_elbow", t = (-31, 125, 0), p = "r_shoulder")
r_wrist = Rig("r_wrist", t = (-45, 103, 6), p = "r_elbow")

l_arm = Rig("l_arm", p = "l_wrist")
r_arm = Rig("r_arm", p = "r_wrist")

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
l_thigh = Rig("l_thigh", t = (8.782, 101.69, 1.97), p = "hip")
l_knee = Rig("l_knee", t = (15, 54, 3), p = "l_thigh")
l_ankle = Rig("l_ankle", t = (18.901, 10, 0), p = "l_knee")
l_foot_ball = Rig("l_foot_ball", t = (21.058, 3.639, 14.117), p = "l_ankle")
l_foot_toes = Rig("l_foot_toes", t = (22.253, 3.639, 21.534), p = "l_foot_ball")
l_foot_heel = Rig("l_foot_heel", t = (18.406, 3.639, -4.419), p = "l_foot_toes")
l_foot_inner = Rig("l_foot_inner", t = (15.229, 3.639, 7.702), p = "l_foot_heel")
l_foot_outer = Rig("l_foot_outer", t = (25.864, 3.639, 7.702), p = "l_foot_heel")
r_thigh = Rig("r_thigh", t = (-8.782, 101.69, 1.97), p = "hip")
r_knee = Rig("r_knee", t = (-15, 54, 3), p = "r_thigh")
r_ankle = Rig("r_ankle", t = (-18.901, 10, 0), p = "r_knee")
r_foot_ball = Rig("r_foot_ball", t = (-21.058, 3.639, 14.117), p = "r_ankle")
r_foot_toes = Rig("r_foot_toes", t = (-22.253, 3.639, 21.534), p = "r_foot_ball")
r_foot_heel = Rig("r_foot_heel", t = (-18.406, 3.639, -4.419), p = "r_foot_toes")
r_foot_inner = Rig("r_foot_inner", t = (-15.229, 3.639, 7.702), p = "r_foot_heel")
r_foot_outer = Rig("r_foot_outer", t = (-25.864, 3.639, 7.702), p = "r_foot_heel")

l_leg = Rig("l_leg", p = "l_ankle")
r_leg = Rig("r_leg", p = "r_ankle")

l_foot = Rig("l_foot", p = "l_leg")
r_foot = Rig("r_foot", p = "r_leg")

#MAKE IK, HUMANISE, AND SKIN WEIGHT A CHECKBOX OPTION
#ADD MIRROR CONTROLS
#CREATE RIG UI