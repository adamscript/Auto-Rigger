from pymel.core import *
from pymel.core.nodetypes import *

#importlib.reload(guides)

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

        import gui
        progress_msg = "Creating Guides... (" + gui.progressnum(83) + "%) " + self.name + "_guide"
        print(progress_msg)
        progresswin.textbox.append(progress_msg)
        QApplication.processEvents()
        
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

        import gui
        progress_msg = "Creating Joints... (" + gui.progressnum(gui.prognum) + "%) " + self.name
        print(progress_msg)
        progresswin.textbox.append(progress_msg)
        QApplication.processEvents()

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
        
        import gui
        progress_msg = "Creating Joints... (" + gui.progressnum(gui.prognum) + "%) " + self.name
        print(progress_msg)
        progresswin.textbox.append(progress_msg)
        QApplication.processEvents()

    def createControl(self, r = 2, nr = "Y", fk = False):
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
        
        import gui
        progress_msg = "Creating Controllers... (" + gui.progressnum(gui.prognum) + "%) " + self.name + "_ctrl"
        print(progress_msg)
        progresswin.textbox.append(progress_msg)
        QApplication.processEvents()

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
        parent(self.name + "_ikpole_ctrl_connector", 'ikpole_ctrl_connector_offset')

        setAttr(self.name + "_ikpole_clusterHandle.visibility", 0)
        setAttr(self.name + "_ikpole_ctrl_clusterHandle.visibility", 0)

        #IK FK switch
        #Create IK FK switch
        self.ikswitch = MakeNurbPlane(w = 10, d = 1, ax = (0, 0, 1), n = self.name + "_ikfk_switch_ctrl")
        rename('makeNurbPlane1', self.name + "_ikfk_switch_ctrlInput")
        setAttr (self.name + "_ikfk_switch_ctrlInput.width", 10)
        setAttr (self.name + "_ikfk_switch_ctrl.overrideEnabled", 1)
        setAttr(self.name + '_ikfk_switch_ctrl.overrideShading', 0)
        setAttr(self.name + '_ikfk_switch_ctrl.overrideTexturing', 0)
        setAttr(self.name + '_ikfk_switch_ctrl.overridePlayback', 0)
        #Create IK FK switch Text
        self.iktext = textCurves(text = "IK", f = "Lucida Sans Unicode", n = self.name + "_IK_lttr")
        self.fktext = textCurves(text = "FK", f = "Lucida Sans Unicode", n = self.name + "_FK_lttr")
        xform(self.name + "_IK_lttrShape", t = (xform(self.name + "_ikfk_switch_ctrl", q = True, t = True, ws = True)), ws = True, cp = True)
        xform(self.name + "_FK_lttrShape", t = (xform(self.name + "_ikfk_switch_ctrl", q = True, t = True, ws = True)), ws = True, cp = True)
        xform(self.name + "_IK_lttrShape", s = (7, 7, 7))
        xform(self.name + "_FK_lttrShape", s = (7, 7, 7))
        setAttr(self.name + "_IK_lttrShape.overrideEnabled", 1)
        setAttr(self.name + "_FK_lttrShape.overrideEnabled", 1)
        setAttr(self.name + "_IK_lttrShape.overrideDisplayType", 2)
        setAttr(self.name + "_FK_lttrShape.overrideDisplayType", 2)
        
        parent(self.name + "_IK_lttrShape", self.name + "_ikfk_switch_ctrl")
        parent(self.name + "_FK_lttrShape", self.name + "_ikfk_switch_ctrl")
        
        #Create ikfk switch offset
        self.ikswitch_offset = group(n = self.name + "_ikfk_switch_ctrl_offset")
        parent(self.name + "_ikfk_switch_ctrl_offset", w = True)
        parent(self.name + "_ikfk_switch_ctrl", self.name + "_ikfk_switch_ctrl_offset")
        xform(self.name + "_ikfk_switch_ctrl_offset", t = (xform(ee, q = True, t = True, ws = True)))
        xform(self.name + "_ikfk_switch_ctrl_offset", t = (0, 10, -20), r = True)
        parent(self.name + "_ikfk_switch_ctrl_offset", 'grp_ctrl')
        pointConstraint(self.parent, self.name + "_ikfk_switch_ctrl_offset", mo = True)
        #Add ik fk switch attribute
        if(self.name == "l_arm" or self.name == "r_arm"):
            addAttr(self.name + "_ikfk_switch_ctrl", ln = "IK_FK_switch", k = True, min = 0, max = 1, dv = 0)
        elif(self.name == "l_leg" or self.name == "r_leg"):
            addAttr(self.name + "_ikfk_switch_ctrl", ln = "IK_FK_switch", k = True, min = 0, max = 1, dv = 1)
        #Connections
        connectAttr(self.name + '_ikfk_switch_ctrl.IK_FK_switch', sj + '_parentConstraint1.' + sj + '_ikW0', f = True)
        connectAttr(self.name + '_ikfk_switch_ctrl.IK_FK_switch', mj + '_parentConstraint1.' + mj + '_ikW0', f = True)
        connectAttr(self.name + '_ikfk_switch_ctrl.IK_FK_switch', ee + '_parentConstraint1.' + ee + '_ikW0', f = True)
        shadingNode('reverse', n = self.name + '_ikfk_switch', au = True)
        connectAttr(self.name + '_ikfk_switch_ctrl.IK_FK_switch', self.name + '_ikfk_switch.inputX', f = True)
        connectAttr(self.name + '_ikfk_switch.outputX', sj + '_parentConstraint1.' + sj + '_fkW1', f = True)
        connectAttr(self.name + '_ikfk_switch.outputX', mj + '_parentConstraint1.' + mj + '_fkW1', f = True)
        connectAttr(self.name + '_ikfk_switch.outputX', ee + '_parentConstraint1.' + ee + '_fkW1', f = True)
        connectAttr(self.name + '_ikfk_switch_ctrl.IK_FK_switch', self.name + '_ikpole_ctrl_offset.visibility', f = True)
        connectAttr(self.name + '_ikfk_switch_ctrl.IK_FK_switch', self.name + '_ik_ctrl_offset.visibility', f = True)
        connectAttr(self.name + '_ikfk_switch_ctrl.IK_FK_switch', self.name + '_ikpole_ctrl_connector.visibility', f = True)
        connectAttr(self.name + '_ikfk_switch_ctrl.IK_FK_switch', self.name + '_IK_lttrShape.visibility', f = True)
        connectAttr(self.name + '_ikfk_switch.outputX', self.name + '_FK_lttrShape.visibility', f = True)
        connectAttr(self.name + '_ikfk_switch.outputX', sj + '_fk_ctrl_offset.visibility', f = True)

        import gui
        progress_msg = "Creating IK Controls... (" + gui.progressnum(gui.prognum) + "%) " + self.name + "_ctrl"
        print(progress_msg)
        progresswin.textbox.append(progress_msg)
        QApplication.processEvents()

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

        select(self.parent + '_ikfk_switch_ctrl')
        addAttr(ln = "Heel_Twist", k = True)
        addAttr(ln = "Toes_Twist", k = True)
        addAttr(ln = "Toe_Tap", k = True)
        addAttr(ln = "Bank", k = True)
        addAttr(ln = "Roll", k = True, min = -30, max = 30, dv = 0)

        connectAttr(self.parent + '_ikfk_switch_ctrl.Heel_Twist', bj + '_rev.rotateY')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Toes_Twist', ee + '_rev.rotateY')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Toe_Tap', ee + '_tap.rotateX')

        shadingNode('condition', n = self.name + '_bank_condition', au = True)
        setAttr(self.name + '_bank_condition.operation', 2)
        connectAttr(self.parent + '_ikfk_switch_ctrl.Bank', self.name + '_bank_condition.colorIfFalseG')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Bank', self.name + '_bank_condition.colorIfTrueR')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Bank', self.name + '_bank_condition.firstTerm')
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
        connectAttr(self.parent + '_ikfk_switch_ctrl.Roll', bj + '_roll_condition.colorIfTrueR')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Roll', bj + '_roll_condition.firstTerm')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Roll', mj + '_roll_condition.colorIfTrueR')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Roll', mj + '_roll_condition.firstTerm')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Roll', self.name + '_roll_pma.input1D[0]')
        connectAttr(self.parent + '_ikfk_switch_ctrl.Roll', ee + '_roll_condition.firstTerm')
        connectAttr(self.name + '_roll_pma.output1D', ee + '_roll_condition.colorIfTrueR')
        connectAttr(bj + '_roll_condition.outColorR', self.name + '_roll_multi.input1X')
        connectAttr(mj + '_roll_condition.outColorR', self.name + '_roll_multi.input1Y')
        connectAttr(ee + '_roll_condition.outColorR', self.name + '_roll_multi.input1Z')
        connectAttr(self.name + '_roll_multi.outputX', bj + '_rev.rotateZ')
        connectAttr(self.name + '_roll_multi.outputY', mj + '_rev.rotateZ')
        connectAttr(self.name + '_roll_multi.outputZ', ee + '_rev.rotateZ')

        import gui
        progress_msg = "Creating Reverse Foot Controls... (" + gui.progressnum(gui.prognum) + "%) " + self.name + "_ctrl"
        print(progress_msg)
        progresswin.textbox.append(progress_msg)
        QApplication.processEvents()

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
l_finger_index_middlep = Rig("l_finger_index_middlep", t = (48.218, 90.448, 14.448), p = "l_finger_index_proximal")
l_finger_index_distal = Rig("l_finger_index_distal", t = (48.629, 87.937, 15.367), p = "l_finger_index_middlep")
l_finger_index_tip = Rig("l_finger_index_tip", t = (49, 86, 16), p = "l_finger_index_distal")
r_finger_index_metacarpal = Rig("r_finger_index_metacarpal", t = (-45.382, 101.311, 7.675), p = "r_wrist")
r_finger_index_proximal = Rig("r_finger_index_proximal", t = (-47.514, 93.318, 13.052), p = "r_finger_index_metacarpal")
r_finger_index_middlep = Rig("r_finger_index_middlep", t = (-48.218, 90.448, 14.448), p = "r_finger_index_proximal")
r_finger_index_distal = Rig("r_finger_index_distal", t = (-48.629, 87.937, 15.367), p = "r_finger_index_middlep")
r_finger_index_tip = Rig("r_finger_index_tip", t = (-49, 86, 16), p = "r_finger_index_distal")
#MIDDLE#
l_finger_middlef_metacarpal = Rig("l_finger_middlef_metacarpal", t = (46, 101.217, 6.603), p = "l_wrist")
l_finger_middlef_proximal = Rig("l_finger_middlef_proximal", t = (49, 92.83, 10.919), p = "l_finger_middlef_metacarpal")
l_finger_middlef_middlep = Rig("l_finger_middlef_middlep", t = (49.284, 89.204, 11.585), p = "l_finger_middlef_proximal")
l_finger_middlef_distal = Rig("l_finger_middlef_distal", t = (48.689, 86, 12), p = "l_finger_middlef_middlep")
l_finger_middlef_tip = Rig("l_finger_middlef_tip", t = (48.271, 84.081, 12.244), p = "l_finger_middlef_distal")
r_finger_middlef_metacarpal = Rig("r_finger_middlef_metacarpal", t = (-46, 101.217, 6.603), p = "r_wrist")
r_finger_middlef_proximal = Rig("r_finger_middlef_proximal", t = (-49, 92.83, 10.919), p = "r_finger_middlef_metacarpal")
r_finger_middlef_middlep = Rig("r_finger_middlef_middlep", t = (-49.284, 89.204, 11.585), p = "r_finger_middlef_proximal")
r_finger_middlef_distal = Rig("r_finger_middlef_distal", t = (-48.689, 86, 12), p = "r_finger_middlef_middlep")
r_finger_middlef_tip = Rig("r_finger_middlef_tip", t = (-48.271, 84.081, 12.244), p = "r_finger_middlef_distal")
#RING#
l_finger_ring_metacarpal = Rig("l_finger_ring_metacarpal", t = (46, 100.783, 5.433), p = "l_wrist")
l_finger_ring_proximal = Rig("l_finger_ring_proximal", t = (49.763, 93.155, 8.511), p = "l_finger_ring_metacarpal")
l_finger_ring_middlep = Rig("l_finger_ring_middlep", t = (49.312, 89.47, 8.796), p = "l_finger_ring_proximal")
l_finger_ring_distal = Rig("l_finger_ring_distal", t = (48.491, 86.937, 8.919), p = "l_finger_ring_middlep")
l_finger_ring_tip = Rig("l_finger_ring_tip", t = (48, 84.47, 9.081), p = "l_finger_ring_distal")
r_finger_ring_metacarpal = Rig("r_finger_ring_metacarpal", t = (-46, 100.783, 5.433), p = "r_wrist")
r_finger_ring_proximal = Rig("r_finger_ring_proximal", t = (-49.763, 93.155, 8.511), p = "r_finger_ring_metacarpal")
r_finger_ring_middlep = Rig("r_finger_ring_middlep", t = (-49.312, 89.47, 8.796), p = "r_finger_ring_proximal")
r_finger_ring_distal = Rig("r_finger_ring_distal", t = (-48.491, 86.937, 8.919), p = "r_finger_ring_middlep")
r_finger_ring_tip = Rig("r_finger_ring_tip", t = (-48, 84.47, 9.081), p = "r_finger_ring_distal")
#PINKY#
l_finger_pinky_metacarpal = Rig("l_finger_pinky_metacarpal", t = (46, 100.686, 4.506), p = "l_wrist")
l_finger_pinky_proximal = Rig("l_finger_pinky_proximal", t = (50, 93.654, 6.103), p = "l_finger_pinky_metacarpal")
l_finger_pinky_middlep = Rig("l_finger_pinky_middlep", t = (49.827, 90.743, 5.949), p = "l_finger_pinky_proximal")
l_finger_pinky_distal = Rig("l_finger_pinky_distal", t = (49, 89.103, 5.64), p = "l_finger_pinky_middlep")
l_finger_pinky_tip = Rig("l_finger_pinky_tip", t = (48, 87.794, 5.077), p = "l_finger_pinky_distal")
r_finger_pinky_metacarpal = Rig("r_finger_pinky_metacarpal", t = (-46, 100.686, 4.506), p = "r_wrist")
r_finger_pinky_proximal = Rig("r_finger_pinky_proximal", t = (-50, 93.654, 6.103), p = "r_finger_pinky_metacarpal")
r_finger_pinky_middlep = Rig("r_finger_pinky_middlep", t = (-49.827, 90.743, 5.949), p = "r_finger_pinky_proximal")
r_finger_pinky_distal = Rig("r_finger_pinky_distal", t = (-49, 89.103, 5.64), p = "r_finger_pinky_middlep")
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