from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import*

import maya.OpenMayaUI as OpenMayaUI
from pymel.core import *

import maya.OpenMaya as om
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

scriptJob(ka = True)

picker_bg = QLabel()

namespace_label = QLabel()
namespace_label.setText("Namespace :")
namespace_label.setAlignment(Qt.AlignRight)

namespace_sel = QComboBox()

class PickerWindow(MayaQWidgetDockableMixin, QDialog):
    def __init__(self):
        super(PickerWindow, self).__init__()
        
        # It is crucial we set a unique object name as this is used internally by Maya
        self.setWindowTitle("Awan's Character Rig Picker GUI")
        
        self.setFixedWidth(470)
        self.setFixedHeight(560)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.header_layout = QHBoxLayout()
        self.footer_layout = QHBoxLayout()
    
    def addLayout(self, layout):
        self.layout.addLayout(layout)

pickerwin = PickerWindow()

def setNamespace():
    if ls("*guiData", r = True):
        spine_gui.show().move(offsetX = -60)
        
        hip_gui.show().move()
        waist_gui.show().move()
        chest_gui.show().move()
        collarbone_gui.show().move()

        head_gui.show().move(offsetX = -70)
        jaw_gui.show().move()

        l_eye_gui.show()
        r_eye_gui.show()
        eyesLookAt_gui.show()

        l_clavicle_gui.show().move()
        r_clavicle_gui.show().move()

        l_fingers_thumb_gui.show()
        l_fingers_index_gui.show()
        l_fingers_middlef_gui.show()
        l_fingers_ring_gui.show()
        l_fingers_pinky_gui.show()

        l_fingers_metacarpal_gui.show()
        l_fingers_proximal_gui.show()
        l_fingers_middlep_gui.show()
        l_fingers_distal_gui.show()
        l_fingers_tip_gui.show()

        l_finger_thumb_metacarpal_gui.show()
        l_finger_thumb_proximal_gui.show()
        l_finger_thumb_distal_gui.show()
        l_finger_thumb_tip_gui.show()

        l_finger_index_metacarpal_gui.show()
        l_finger_index_proximal_gui.show()
        l_finger_index_middlep_gui.show()
        l_finger_index_distal_gui.show()
        l_finger_index_tip_gui.show()

        l_finger_middlef_metacarpal_gui.show()
        l_finger_middlef_proximal_gui.show()
        l_finger_middlef_middlep_gui.show()
        l_finger_middlef_distal_gui.show()
        l_finger_middlef_tip_gui.show()

        l_finger_ring_metacarpal_gui.show()
        l_finger_ring_proximal_gui.show()
        l_finger_ring_middlep_gui.show()
        l_finger_ring_distal_gui.show()
        l_finger_ring_tip_gui.show()

        l_finger_pinky_metacarpal_gui.show()
        l_finger_pinky_proximal_gui.show()
        l_finger_pinky_middlep_gui.show()
        l_finger_pinky_distal_gui.show()
        l_finger_pinky_tip_gui.show()

        r_fingers_thumb_gui.show()
        r_fingers_index_gui.show()
        r_fingers_middlef_gui.show()
        r_fingers_ring_gui.show()
        r_fingers_pinky_gui.show()

        r_fingers_metacarpal_gui.show()
        r_fingers_proximal_gui.show()
        r_fingers_middlep_gui.show()
        r_fingers_distal_gui.show()
        r_fingers_tip_gui.show()

        r_finger_thumb_metacarpal_gui.show()
        r_finger_thumb_proximal_gui.show()
        r_finger_thumb_distal_gui.show()
        r_finger_thumb_tip_gui.show()

        r_finger_index_metacarpal_gui.show()
        r_finger_index_proximal_gui.show()
        r_finger_index_middlep_gui.show()
        r_finger_index_distal_gui.show()
        r_finger_index_tip_gui.show()

        r_finger_middlef_metacarpal_gui.show()
        r_finger_middlef_proximal_gui.show()
        r_finger_middlef_middlep_gui.show()
        r_finger_middlef_distal_gui.show()
        r_finger_middlef_tip_gui.show()

        r_finger_ring_metacarpal_gui.show()
        r_finger_ring_proximal_gui.show()
        r_finger_ring_middlep_gui.show()
        r_finger_ring_distal_gui.show()
        r_finger_ring_tip_gui.show()

        r_finger_pinky_metacarpal_gui.show()
        r_finger_pinky_proximal_gui.show()
        r_finger_pinky_middlep_gui.show()
        r_finger_pinky_distal_gui.show()
        r_finger_pinky_tip_gui.show()

        l_foot_ankle_gui.show()
        r_foot_ankle_gui.show()

        l_foot_ankle_fk_gui.show()
        l_foot_ball_gui.show()
        l_foot_toes_gui.show()
        r_foot_ankle_fk_gui.show()
        r_foot_ball_gui.show()
        r_foot_toes_gui.show()

        namespaceik = ls("*" + namespace_sel.currentText() + ":guiData", r = True)
        for i in namespaceik:
            if getAttr(i + ".isIK"):
                l_shoulder_fk_gui.show().move()
                l_elbow_fk_gui.show().move()
                l_wrist_fk_gui.show().move()
                r_shoulder_fk_gui.show().move()
                r_elbow_fk_gui.show().move()
                r_wrist_fk_gui.show().move()

                l_arm_ikpole_gui.show().move()
                l_arm_ik_gui.show().move()
                r_arm_ikpole_gui.show().move()
                r_arm_ik_gui.show().move()

                l_thigh_fk_gui.show().move()
                l_knee_fk_gui.show().move()
                l_ankle_fk_gui.show().move()
                r_thigh_fk_gui.show().move()
                r_knee_fk_gui.show().move()
                r_ankle_fk_gui.show().move()

                l_leg_ikpole_gui.show().move()
                l_leg_ik_gui.show().move()
                r_leg_ikpole_gui.show().move()
                r_leg_ik_gui.show().move()

                l_foot_ankle_fk_gui.show()
                r_foot_ankle_fk_gui.show()

                l_arm_ikfk_switch_gui.show()
                r_arm_ikfk_switch_gui.show()
                l_leg_ikfk_switch_gui.show()
                r_leg_ikfk_switch_gui.show()

                l_leg_ikfk_switch_select_gui.show()
                r_leg_ikfk_switch_select_gui.show()

                l_shoulder_gui.hide()
                l_elbow_gui.hide()
                l_wrist_gui.hide()
                r_shoulder_gui.hide()
                r_elbow_gui.hide()
                r_wrist_gui.hide()

                l_thigh_gui.hide()
                l_knee_gui.hide()
                l_ankle_gui.hide()
                r_thigh_gui.hide()
                r_knee_gui.hide()
                r_ankle_gui.hide()

                ikfkuichange()
            elif not getAttr(i + ".isIK"):
                l_shoulder_gui.show().move()
                l_elbow_gui.show().move()
                l_wrist_gui.show().move()
                r_shoulder_gui.show().move()
                r_elbow_gui.show().move()
                r_wrist_gui.show().move()

                l_thigh_gui.show().move()
                l_knee_gui.show().move()
                l_ankle_gui.show().move()
                r_thigh_gui.show().move()
                r_knee_gui.show().move()
                r_ankle_gui.show().move()

                l_shoulder_fk_gui.hide()
                l_elbow_fk_gui.hide()
                l_wrist_fk_gui.hide()
                r_shoulder_fk_gui.hide()
                r_elbow_fk_gui.hide()
                r_wrist_fk_gui.hide()

                l_arm_ikpole_gui.hide()
                l_arm_ik_gui.hide()
                r_arm_ikpole_gui.hide()
                r_arm_ik_gui.hide()

                l_thigh_fk_gui.hide()
                l_knee_fk_gui.hide()
                l_ankle_fk_gui.hide()
                r_thigh_fk_gui.hide()
                r_knee_fk_gui.hide()
                r_ankle_fk_gui.hide()

                l_leg_ikpole_gui.hide()
                l_leg_ik_gui.hide()
                r_leg_ikpole_gui.hide()
                r_leg_ik_gui.hide()

                l_foot_ankle_fk_gui.hide()
                r_foot_ankle_fk_gui.hide()

                l_arm_ikfk_switch_gui.hide()
                r_arm_ikfk_switch_gui.hide()
                l_leg_ikfk_switch_gui.hide()
                r_leg_ikfk_switch_gui.hide()

                l_leg_ikfk_switch_select_gui.hide()
                r_leg_ikfk_switch_select_gui.hide()

        picker_bg.setPixmap(workspace(q = True, rd = True) + "images/" + namespace_sel.currentText() +'_pb.1.jpg')
    elif not ls("*guiData", r = True):
        print("NO GUI DATA")
        
        spine_gui.hide()
        
        hip_gui.hide()
        waist_gui.hide()
        chest_gui.hide()
        collarbone_gui.hide()

        root_gui.hide()
        ctrlgrp_gui.hide()

        head_gui.hide()
        jaw_gui.hide()

        l_eye_gui.hide()
        r_eye_gui.hide()
        eyesLookAt_gui.hide()

        l_clavicle_gui.hide()
        r_clavicle_gui.hide()
        
        l_shoulder_gui.hide()
        l_elbow_gui.hide()
        l_wrist_gui.hide()
        r_shoulder_gui.hide()
        r_elbow_gui.hide()
        r_wrist_gui.hide()

        l_thigh_gui.hide()
        l_knee_gui.hide()
        l_ankle_gui.hide()
        r_thigh_gui.hide()
        r_knee_gui.hide()
        r_ankle_gui.hide()

        l_shoulder_fk_gui.hide()
        l_elbow_fk_gui.hide()
        l_wrist_fk_gui.hide()
        r_shoulder_fk_gui.hide()
        r_elbow_fk_gui.hide()
        r_wrist_fk_gui.hide()

        l_fingers_thumb_gui.hide()
        l_fingers_index_gui.hide()
        l_fingers_middlef_gui.hide()
        l_fingers_ring_gui.hide()
        l_fingers_pinky_gui.hide()

        l_fingers_metacarpal_gui.hide()
        l_fingers_proximal_gui.hide()
        l_fingers_middlep_gui.hide()
        l_fingers_distal_gui.hide()
        l_fingers_tip_gui.hide()

        l_finger_thumb_metacarpal_gui.hide()
        l_finger_thumb_proximal_gui.hide()
        l_finger_thumb_distal_gui.hide()
        l_finger_thumb_tip_gui.hide()

        l_finger_index_metacarpal_gui.hide()
        l_finger_index_proximal_gui.hide()
        l_finger_index_middlep_gui.hide()
        l_finger_index_distal_gui.hide()
        l_finger_index_tip_gui.hide()

        l_finger_middlef_metacarpal_gui.hide()
        l_finger_middlef_proximal_gui.hide()
        l_finger_middlef_middlep_gui.hide()
        l_finger_middlef_distal_gui.hide()
        l_finger_middlef_tip_gui.hide()

        l_finger_ring_metacarpal_gui.hide()
        l_finger_ring_proximal_gui.hide()
        l_finger_ring_middlep_gui.hide()
        l_finger_ring_distal_gui.hide()
        l_finger_ring_tip_gui.hide()

        l_finger_pinky_metacarpal_gui.hide()
        l_finger_pinky_proximal_gui.hide()
        l_finger_pinky_middlep_gui.hide()
        l_finger_pinky_distal_gui.hide()
        l_finger_pinky_tip_gui.hide()

        r_fingers_thumb_gui.hide()
        r_fingers_index_gui.hide()
        r_fingers_middlef_gui.hide()
        r_fingers_ring_gui.hide()
        r_fingers_pinky_gui.hide()

        r_fingers_metacarpal_gui.hide()
        r_fingers_proximal_gui.hide()
        r_fingers_middlep_gui.hide()
        r_fingers_distal_gui.hide()
        r_fingers_tip_gui.hide()

        r_finger_thumb_metacarpal_gui.hide()
        r_finger_thumb_proximal_gui.hide()
        r_finger_thumb_distal_gui.hide()
        r_finger_thumb_tip_gui.hide()

        r_finger_index_metacarpal_gui.hide()
        r_finger_index_proximal_gui.hide()
        r_finger_index_middlep_gui.hide()
        r_finger_index_distal_gui.hide()
        r_finger_index_tip_gui.hide()

        r_finger_middlef_metacarpal_gui.hide()
        r_finger_middlef_proximal_gui.hide()
        r_finger_middlef_middlep_gui.hide()
        r_finger_middlef_distal_gui.hide()
        r_finger_middlef_tip_gui.hide()

        r_finger_ring_metacarpal_gui.hide()
        r_finger_ring_proximal_gui.hide()
        r_finger_ring_middlep_gui.hide()
        r_finger_ring_distal_gui.hide()
        r_finger_ring_tip_gui.hide()

        r_finger_pinky_metacarpal_gui.hide()
        r_finger_pinky_proximal_gui.hide()
        r_finger_pinky_middlep_gui.hide()
        r_finger_pinky_distal_gui.hide()
        r_finger_pinky_tip_gui.hide()

        l_arm_ikpole_gui.hide()
        l_arm_ik_gui.hide()
        r_arm_ikpole_gui.hide()
        r_arm_ik_gui.hide()

        l_thigh_fk_gui.hide()
        l_knee_fk_gui.hide()
        l_ankle_fk_gui.hide()
        r_thigh_fk_gui.hide()
        r_knee_fk_gui.hide()
        r_ankle_fk_gui.hide()

        l_leg_ikpole_gui.hide()
        l_leg_ik_gui.hide()
        r_leg_ikpole_gui.hide()
        r_leg_ik_gui.hide()

        l_foot_ankle_fk_gui.hide()
        r_foot_ankle_fk_gui.hide()

        l_arm_ikfk_switch_gui.hide()
        r_arm_ikfk_switch_gui.hide()
        l_leg_ikfk_switch_gui.hide()
        r_leg_ikfk_switch_gui.hide()

        l_leg_ikfk_switch_select_gui.hide()
        r_leg_ikfk_switch_select_gui.hide()

        l_foot_ankle_gui.hide()
        r_foot_ankle_gui.hide()

        l_foot_ankle_fk_gui.hide()
        l_foot_ball_gui.hide()
        l_foot_toes_gui.hide()
        r_foot_ankle_fk_gui.hide()
        r_foot_ball_gui.hide()
        r_foot_toes_gui.hide()

        picker_bg.setPixmap(None)

def ikfkuichange():
    for x in ls("*" + namespace_sel.currentText() + ":*_ikfk_switch_ctrl"):
        if((str(x).partition(namespace_sel.currentText() + ':')[2]).startswith("l_arm")):
            if(getAttr('*' + namespace_sel.currentText() + ':l_arm_ikfk_switch_ctrl.IK_FK_switch') == 0):
                l_arm_ikfk_switch_gui.setText("FK")
                l_shoulder_fk_gui.show()
                l_elbow_fk_gui.show()
                l_wrist_fk_gui.show()
                l_arm_ikpole_gui.hide()
                l_arm_ik_gui.hide()
            elif(getAttr('*' + namespace_sel.currentText() + ':l_arm_ikfk_switch_ctrl.IK_FK_switch') == 1):
                l_arm_ikfk_switch_gui.setText("IK")
                l_shoulder_fk_gui.hide()
                l_elbow_fk_gui.hide()
                l_wrist_fk_gui.hide()
                l_arm_ikpole_gui.show()
                l_arm_ik_gui.show()
        elif((str(x).partition(namespace_sel.currentText() + ':')[2]).startswith("r_arm")):
            if(getAttr('*' + namespace_sel.currentText() + ':r_arm_ikfk_switch_ctrl.IK_FK_switch') == 0):
                r_arm_ikfk_switch_gui.setText("FK")
                r_shoulder_fk_gui.show()
                r_elbow_fk_gui.show()
                r_wrist_fk_gui.show()
                r_arm_ikpole_gui.hide()
                r_arm_ik_gui.hide()
            elif(getAttr('*' + namespace_sel.currentText() + ':r_arm_ikfk_switch_ctrl.IK_FK_switch') == 1):
                r_arm_ikfk_switch_gui.setText("IK")
                r_shoulder_fk_gui.hide()
                r_elbow_fk_gui.hide()
                r_wrist_fk_gui.hide()
                r_arm_ikpole_gui.show()
                r_arm_ik_gui.show()
        elif((str(x).partition(namespace_sel.currentText() + ':')[2]).startswith("l_leg")):
            if(getAttr('*' + namespace_sel.currentText() + ':l_leg_ikfk_switch_ctrl.IK_FK_switch') == 0):
                l_leg_ikfk_switch_gui.setText("FK")
                l_thigh_fk_gui.show()
                l_knee_fk_gui.show()
                l_ankle_fk_gui.show()
                l_leg_ikpole_gui.hide()
                l_leg_ik_gui.hide()
            elif(getAttr('*' + namespace_sel.currentText() + ':l_leg_ikfk_switch_ctrl.IK_FK_switch') == 1):
                l_leg_ikfk_switch_gui.setText("IK")
                l_thigh_fk_gui.hide()
                l_knee_fk_gui.hide()
                l_ankle_fk_gui.hide()
                l_leg_ikpole_gui.show()
                l_leg_ik_gui.show()
        elif((str(x).partition(namespace_sel.currentText() + ':')[2]).startswith("r_leg")):
            if(getAttr('*' + namespace_sel.currentText() + ':r_leg_ikfk_switch_ctrl.IK_FK_switch') == 0):
                r_leg_ikfk_switch_gui.setText("FK")
                r_thigh_fk_gui.show()
                r_knee_fk_gui.show()
                r_ankle_fk_gui.show()
                r_leg_ikpole_gui.hide()
                r_leg_ik_gui.hide()
            elif(getAttr('*' + namespace_sel.currentText() + ':r_leg_ikfk_switch_ctrl.IK_FK_switch') == 1):
                r_leg_ikfk_switch_gui.setText("IK")
                r_thigh_fk_gui.hide()
                r_knee_fk_gui.hide()
                r_ankle_fk_gui.hide()
                r_leg_ikpole_gui.show()
                r_leg_ik_gui.show()

namespaceik = ls("*" + namespace_sel.currentText() + ":guiData", r = True)
for i in namespaceik:
    if getAttr(i + ".isIK"):
        for i in ls("*_ikfk_switch_ctrl", r = True):
            scriptJob(ac = [i + '.IK_FK_switch', ikfkuichange])
    elif not getAttr(i + ".isIK"):
        pass

def getNamespace_list():
    namespace_sel.clear()
    namespace_list = ls("*guiData", r = True)
    for i in namespace_list:
        namespace_sel.addItem(getAttr(i + ".name"))

getNamespace_list()
namespace_sel.activated.connect(setNamespace)

pickerwin.header_layout.addWidget(namespace_label)
pickerwin.header_layout.addWidget(namespace_sel)

pickerwin.layout.addLayout(pickerwin.header_layout)
pickerwin.layout.addWidget(picker_bg)
pickerwin.layout.addLayout(pickerwin.footer_layout)

class GUI():

    def __init__(self, name, shape, p = (0, 0), radius = 1, width = 1, height = 1, color = "", text = "", selections = ""):
        self.name = name
        self.shape = shape
        self.pos = p
        self.radius = radius
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.selections = selections

    def drawUIButton(self, command, txt = ""):
        self.button = QPushButton()
        self.button.setText(txt)
        self.button.clicked.connect(command)
        pickerwin.footer_layout.addWidget(self.button)

    def drawSelectionButton(self, posX = 0, posY = 0):
        if (self.shape == "square"):
            self.button = QPushButton(pickerwin)
            self.button.setText(self.text)
            self.button.setGeometry(posX - (self.radius/2), posY - (self.radius/2), self.radius, self.radius)
            self.button.setStyleSheet("background-color: " + self.color + ";")
            self.button.clicked.connect(self.selection)
        elif(self.shape == "rect"):
            self.button = QPushButton(pickerwin)
            self.button.setText(self.text)
            self.button.setGeometry(posX - (self.width/2), posY - (self.height/2), self.width, self.height)
            self.button.setStyleSheet("background-color: " + self.color + ";")
            self.button.clicked.connect(self.selection)
        elif(self.shape == "circle"):
            self.button = QPushButton(pickerwin)
            self.button.setText(self.text)
            self.button.setGeometry(posX - (self.radius/2), posY - (self.radius/2), self.radius, self.radius)
            self.button.setStyleSheet("background-color: " + self.color + "; border-radius: " + str(self.radius/2) + "px;")
            self.button.clicked.connect(self.selection)

    def drawMultipleSelectionButton(self, posX = 0, posY = 0):
        self.button = QPushButton(pickerwin)
        self.button.setText(self.text)
        self.button.setGeometry(posX - (self.radius/2), posY - (self.radius/2), self.radius, self.radius)
        self.button.setStyleSheet("background-color: " + self.color + "; border-radius: " + str(self.radius/2) + "px;")
        self.button.clicked.connect(self.multipleSelection)

    def drawToggleButton(self, posX = 0, posY = 0):
        self.button = QPushButton(pickerwin)
        self.button.setText(self.text)
        self.button.setGeometry(posX - (self.radius/2), posY - (self.radius/2), self.radius, self.radius)
        self.button.setStyleSheet("background-color: " + self.color + "; font-size : 15px; font-weight : bold;")
        self.button.clicked.connect(self.toggle)

    def selection(self):
        if (self.name.startswith("l_finger_") or self.name.startswith("r_finger_")):
            self.select = ls("*" + namespace_sel.currentText() + ":" + self.name + "_ctrl", r = True)
            for i in self.select:
                select(i, add = True)
        else:
            self.select = ls("*" + namespace_sel.currentText() + ":" + self.name + "_ctrl", r = True)
            for i in self.select:
                select(i)
        print(self.name + " clicked!")

    def multipleSelection(self):
        selects = ls("*" + namespace_sel.currentText() + ":" + self.name.partition(self.selections)[0] + "*" + self.name.partition(self.selections)[1] + "*_ctrl")
        for x in selects:   
            select(x, add = True)
            print(x)

    def toggle(self):
        if(getAttr("*" + namespace_sel.currentText() + ":" + self.name + "_ctrl.IK_FK_switch") == 0):
            setAttr("*" + namespace_sel.currentText() + ":" + self.name + "_ctrl.IK_FK_switch", 1)
        elif(getAttr("*" + namespace_sel.currentText() + ":" + self.name + "_ctrl.IK_FK_switch") == 1):
            setAttr("*" + namespace_sel.currentText() + ":" + self.name + "_ctrl.IK_FK_switch", 0)
        ikfkuichange()
        select("*" + namespace_sel.currentText() + ":" + self.name + "_ctrl")

    def move(self, offsetX = 0, offsetY = 0):
        self.namespace = ls("*" + namespace_sel.currentText() + ":guiData", r = True)
        for i in self.namespace:
            if(self.shape != "rect"):
                self.button.move((getAttr(i + "." + self.name + "_ctrl_guiDataX")) - (self.radius/2) + offsetX, (getAttr(i + "." + self.name + "_ctrl_guiDataY")) - (self.radius/2) + offsetY)
            else:
                self.button.move((getAttr(i + "." + self.name + "_ctrl_guiDataX")) - (self.width/2) + offsetX, (getAttr(i + "." + self.name + "_ctrl_guiDataY")) - (self.height/2) + offsetY)
        
    def setText(self, txt = ""):
        self.button.setText(txt)

    def hide(self):
        self.button.hide()
        return self
    
    def show(self):
        self.button.show()
        return self

# UI #

def key_cmd():
    if not ls(sl = True, r = True):
        om.MGlobal.displayError("There is no object to key!")
    else:
        setKeyframe()

def keyall_cmd():
    for i in ls("*" + namespace_sel.currentText() + ":*ctrl", r = True):
        select(i)
        setKeyframe()

def resetpose_cmd():
    for i in ls("*" + namespace_sel.currentText() + ":*ctrl", r = True):
        xform(i, t = (0, 0, 0), ro = (0, 0, 0), s = (1, 1, 1), os = True)

def deselectall_cmd():
    select(cl = True)

key_btn = GUI("key", "rect")
keyall_btn = GUI("keyall", "rect")
resetpose_btn = GUI("resetpose", "rect")
deselectall_btn = GUI("deselectall", "rect")

key_btn.drawUIButton(key_cmd, txt = "Key")
keyall_btn.drawUIButton(keyall_cmd, txt = "Key All")
resetpose_btn.drawUIButton(resetpose_cmd, txt = "Reset Pose")
deselectall_btn.drawUIButton(deselectall_cmd, txt = "Deselect All")

# ROOT #

root_gui = GUI("root", "rect", width = 150, height = 10, color = "#3696d9")
ctrlgrp_gui = GUI("grp", "rect", width = 50, height = 10, color = "#3696d9")

root_gui.drawSelectionButton(235, 505)
ctrlgrp_gui.drawSelectionButton(235, 490)

# SPINE #
spine_gui = GUI("spine", "square", radius = 20, color = "#cad936")

hip_gui = GUI("hip", "rect", width = 80, height = 10, color = "#cad936")
waist_gui = GUI("waist", "rect", width = 60, height = 10, color = "#cad936")
chest_gui = GUI("chest", "rect", width = 60, height = 10, color = "#cad936")
collarbone_gui = GUI("collarbone", "square", radius = 18, color = "#cad936")

spine_gui.drawSelectionButton()

hip_gui.drawSelectionButton()
waist_gui.drawSelectionButton()
chest_gui.drawSelectionButton()
collarbone_gui.drawSelectionButton()

# HEAD #
head_gui = GUI("head", "square", radius = 50, color = "#cad936")
jaw_gui = GUI("jaw", "circle", radius = 10, color = "#cad936")
l_eye_gui = GUI("l_eye", "circle", radius = 16, color = "#3d9b2f")
r_eye_gui = GUI("r_eye", "circle", radius = 16, color = "#9b3b2f")
eyesLookAt_gui = GUI("eyesLookAt", "rect", width = 50, height = 7, color = "#cad936")

head_gui.drawSelectionButton()
jaw_gui.drawSelectionButton()
l_eye_gui.drawSelectionButton(340, 90)
r_eye_gui.drawSelectionButton(316, 90)
eyesLookAt_gui.drawSelectionButton(328, 110)

# ARMS #
l_clavicle_gui = GUI("l_clavicle", "square", radius = 12, color = "#3d9b2f")
r_clavicle_gui = GUI("r_clavicle", "square", radius = 12, color = "#9b3b2f")

l_shoulder_gui = GUI("l_shoulder", "circle", radius = 20, color = "#3d9b2f")
l_elbow_gui = GUI("l_elbow", "circle", radius = 20, color = "#3d9b2f")
l_wrist_gui = GUI("l_wrist", "circle", radius = 20, color = "#3d9b2f")
r_shoulder_gui = GUI("r_shoulder", "circle", radius = 20, color = "#9b3b2f")
r_elbow_gui = GUI("r_elbow", "circle", radius = 20, color = "#9b3b2f")
r_wrist_gui = GUI("r_wrist", "circle", radius = 20, color = "#9b3b2f")

l_shoulder_fk_gui = GUI("l_shoulder_fk", "circle", radius = 20, color = "#3d9b2f")
l_elbow_fk_gui = GUI("l_elbow_fk", "circle", radius = 20, color = "#3d9b2f")
l_wrist_fk_gui = GUI("l_wrist_fk", "circle", radius = 20, color = "#3d9b2f")
r_shoulder_fk_gui = GUI("r_shoulder_fk", "circle", radius = 20, color = "#9b3b2f")
r_elbow_fk_gui = GUI("r_elbow_fk", "circle", radius = 20, color = "#9b3b2f")
r_wrist_fk_gui = GUI("r_wrist_fk", "circle", radius = 20, color = "#9b3b2f")

l_arm_ikpole_gui = GUI("l_arm_ikpole", "circle", radius = 14, color = "#3d9b2f")
l_arm_ik_gui = GUI("l_arm_ik", "square", radius = 20, color = "#3d9b2f")
r_arm_ikpole_gui = GUI("r_arm_ikpole", "circle", radius = 14, color = "#9b3b2f")
r_arm_ik_gui = GUI("r_arm_ik", "square", radius = 20, color = "#9b3b2f")

l_clavicle_gui.drawSelectionButton()
r_clavicle_gui.drawSelectionButton()

l_shoulder_gui.drawSelectionButton()
l_elbow_gui.drawSelectionButton()
l_wrist_gui.drawSelectionButton()
r_shoulder_gui.drawSelectionButton()
r_elbow_gui.drawSelectionButton()
r_wrist_gui.drawSelectionButton()

l_shoulder_fk_gui.drawSelectionButton()
l_elbow_fk_gui.drawSelectionButton()
l_wrist_fk_gui.drawSelectionButton()
r_shoulder_fk_gui.drawSelectionButton()
r_elbow_fk_gui.drawSelectionButton()
r_wrist_fk_gui.drawSelectionButton()

l_arm_ikpole_gui.drawSelectionButton()
l_arm_ik_gui.drawSelectionButton()
r_arm_ikpole_gui.drawSelectionButton()
r_arm_ik_gui.drawSelectionButton()

# L FINGERS #
#THUMB#
l_finger_thumb_metacarpal_gui = GUI("l_finger_thumb_metacarpal", "rect", width = 15, height = 25, color = "#3d9b2f")
l_finger_thumb_proximal_gui = GUI("l_finger_thumb_proximal", "rect", width = 15, height = 10, color = "#3d9b2f")
l_finger_thumb_distal_gui = GUI("l_finger_thumb_distal", "rect", width = 15, height = 10, color = "#3d9b2f")
l_finger_thumb_tip_gui = GUI("l_finger_thumb_tip", "rect", width = 15, height = 10, color = "#3d9b2f")
#INDEX#
l_finger_index_metacarpal_gui = GUI("l_finger_index_metacarpal", "rect", width = 10, height = 25, color = "#3d9b2f")
l_finger_index_proximal_gui = GUI("l_finger_index_proximal", "square", radius = 10, color = "#3d9b2f")
l_finger_index_middlep_gui = GUI("l_finger_index_middlep", "square", radius = 10, color = "#3d9b2f")
l_finger_index_distal_gui = GUI("l_finger_index_distal", "square", radius = 10, color = "#3d9b2f")
l_finger_index_tip_gui = GUI("l_finger_index_tip", "square", radius = 10, color = "#3d9b2f")
#MIDDLE#
l_finger_middlef_metacarpal_gui = GUI("l_finger_middlef_metacarpal", "rect", width = 10, height = 25, color = "#3d9b2f")
l_finger_middlef_proximal_gui = GUI("l_finger_middlef_proximal", "square", radius = 10, color = "#3d9b2f")
l_finger_middlef_middlep_gui = GUI("l_finger_middlef_middlep", "square", radius = 10, color = "#3d9b2f")
l_finger_middlef_distal_gui = GUI("l_finger_middlef_distal", "square", radius = 10, color = "#3d9b2f")
l_finger_middlef_tip_gui = GUI("l_finger_middlef_tip", "square", radius = 10, color = "#3d9b2f")
#RING#
l_finger_ring_metacarpal_gui = GUI("l_finger_ring_metacarpal", "rect", width = 10, height = 25, color = "#3d9b2f")
l_finger_ring_proximal_gui = GUI("l_finger_ring_proximal", "square", radius = 10, color = "#3d9b2f")
l_finger_ring_middlep_gui = GUI("l_finger_ring_middlep", "square", radius = 10, color = "#3d9b2f")
l_finger_ring_distal_gui = GUI("l_finger_ring_distal", "square", radius = 10, color = "#3d9b2f")
l_finger_ring_tip_gui = GUI("l_finger_ring_tip", "square", radius = 10, color = "#3d9b2f")
#PINKY#
l_finger_pinky_metacarpal_gui = GUI("l_finger_pinky_metacarpal", "rect", width = 10, height = 25, color = "#3d9b2f")
l_finger_pinky_proximal_gui = GUI("l_finger_pinky_proximal", "square", radius = 10, color = "#3d9b2f")
l_finger_pinky_middlep_gui = GUI("l_finger_pinky_middlep", "square", radius = 10, color = "#3d9b2f")
l_finger_pinky_distal_gui = GUI("l_finger_pinky_distal", "square", radius = 10, color = "#3d9b2f")
l_finger_pinky_tip_gui = GUI("l_finger_pinky_tip", "square", radius = 10, color = "#3d9b2f")
#EXTRA CONTROLS
l_fingers_thumb_gui = GUI("l_finger_thumb", "circle", radius = 12, color = "#3d9b2f", selections = "thumb")
l_fingers_index_gui = GUI("l_finger_index", "circle", radius = 12, color = "#3d9b2f", selections = "index")
l_fingers_middlef_gui = GUI("l_finger_middlef", "circle", radius = 12, color = "#3d9b2f", selections = "middlef")
l_fingers_ring_gui = GUI("l_finger_ring", "circle", radius = 12, color = "#3d9b2f", selections = "ring")
l_fingers_pinky_gui = GUI("l_finger_pinky", "circle", radius = 12, color = "#3d9b2f", selections = "pinky")

l_fingers_metacarpal_gui = GUI("l_finger_metacarpal", "circle", radius = 12, color = "#3d9b2f", selections = "metacarpal")
l_fingers_proximal_gui = GUI("l_finger_proximal", "circle", radius = 12, color = "#3d9b2f", selections = "proximal")
l_fingers_middlep_gui = GUI("l_finger_middlep", "circle", radius = 12, color = "#3d9b2f", selections = "middlep")
l_fingers_distal_gui = GUI("l_finger_distal", "circle", radius = 12, color = "#3d9b2f", selections = "distal")
l_fingers_tip_gui = GUI("l_finger_tip", "circle", radius = 12, color = "#3d9b2f", selections = "tip")

l_fingers_thumb_gui.drawMultipleSelectionButton(posX = 370, posY = 420)
l_fingers_index_gui.drawMultipleSelectionButton(posX = 385, posY = 420)
l_fingers_middlef_gui.drawMultipleSelectionButton(posX = 400, posY = 420)
l_fingers_ring_gui.drawMultipleSelectionButton(posX = 415, posY = 420)
l_fingers_pinky_gui.drawMultipleSelectionButton(posX = 430, posY = 420)

l_fingers_metacarpal_gui.drawMultipleSelectionButton(posX = 445, posY = 345)
l_fingers_proximal_gui.drawMultipleSelectionButton(posX = 445, posY = 360)
l_fingers_middlep_gui.drawMultipleSelectionButton(posX = 445, posY = 375)
l_fingers_distal_gui.drawMultipleSelectionButton(posX = 445, posY = 390)
l_fingers_tip_gui.drawMultipleSelectionButton(posX = 445, posY = 405)

l_finger_thumb_metacarpal_gui.drawSelectionButton(posX = 370, posY = 340)
l_finger_thumb_proximal_gui.drawSelectionButton(posX = 370, posY = 360)
l_finger_thumb_distal_gui.drawSelectionButton(posX = 370, posY = 375)
l_finger_thumb_tip_gui.drawSelectionButton(posX = 370, posY = 390)

l_finger_index_metacarpal_gui.drawSelectionButton(posX = 385, posY = 340)
l_finger_index_proximal_gui.drawSelectionButton(posX = 385, posY = 360)
l_finger_index_middlep_gui.drawSelectionButton(posX = 385, posY = 375)
l_finger_index_distal_gui.drawSelectionButton(posX = 385, posY = 390)
l_finger_index_tip_gui.drawSelectionButton(posX = 385, posY = 405)

l_finger_middlef_metacarpal_gui.drawSelectionButton(posX = 400, posY = 340)
l_finger_middlef_proximal_gui.drawSelectionButton(posX = 400, posY = 360)
l_finger_middlef_middlep_gui.drawSelectionButton(posX = 400, posY = 375)
l_finger_middlef_distal_gui.drawSelectionButton(posX = 400, posY = 390)
l_finger_middlef_tip_gui.drawSelectionButton(posX = 400, posY = 405)

l_finger_ring_metacarpal_gui.drawSelectionButton(posX = 415, posY = 340)
l_finger_ring_proximal_gui.drawSelectionButton(posX = 415, posY = 360)
l_finger_ring_middlep_gui.drawSelectionButton(posX = 415, posY = 375)
l_finger_ring_distal_gui.drawSelectionButton(posX = 415, posY = 390)
l_finger_ring_tip_gui.drawSelectionButton(posX = 415, posY = 405)

l_finger_pinky_metacarpal_gui.drawSelectionButton(posX = 430, posY = 340)
l_finger_pinky_proximal_gui.drawSelectionButton(posX = 430, posY = 360)
l_finger_pinky_middlep_gui.drawSelectionButton(posX = 430, posY = 375)
l_finger_pinky_distal_gui.drawSelectionButton(posX = 430, posY = 390)
l_finger_pinky_tip_gui.drawSelectionButton(posX = 430, posY = 405)

# R FINGERS #
#THUMB#
r_finger_thumb_metacarpal_gui = GUI("r_finger_thumb_metacarpal", "rect", width = 15, height = 25, color = "#9b3b2f")
r_finger_thumb_proximal_gui = GUI("r_finger_thumb_proximal", "rect", width = 15, height = 10, color = "#9b3b2f")
r_finger_thumb_distal_gui = GUI("r_finger_thumb_distal", "rect", width = 15, height = 10, color = "#9b3b2f")
r_finger_thumb_tip_gui = GUI("r_finger_thumb_tip", "rect", width = 15, height = 10, color = "#9b3b2f")
#INDEX#
r_finger_index_metacarpal_gui = GUI("r_finger_index_metacarpal", "rect", width = 10, height = 25, color = "#9b3b2f")
r_finger_index_proximal_gui = GUI("r_finger_index_proximal", "square", radius = 10, color = "#9b3b2f")
r_finger_index_middlep_gui = GUI("r_finger_index_middlep", "square", radius = 10, color = "#9b3b2f")
r_finger_index_distal_gui = GUI("r_finger_index_distal", "square", radius = 10, color = "#9b3b2f")
r_finger_index_tip_gui = GUI("r_finger_index_tip", "square", radius = 10, color = "#9b3b2f")
#MIDDLE#
r_finger_middlef_metacarpal_gui = GUI("r_finger_middlef_metacarpal", "rect", width = 10, height = 25, color = "#9b3b2f")
r_finger_middlef_proximal_gui = GUI("r_finger_middlef_proximal", "square", radius = 10, color = "#9b3b2f")
r_finger_middlef_middlep_gui = GUI("r_finger_middlef_middlep", "square", radius = 10, color = "#9b3b2f")
r_finger_middlef_distal_gui = GUI("r_finger_middlef_distal", "square", radius = 10, color = "#9b3b2f")
r_finger_middlef_tip_gui = GUI("r_finger_middlef_tip", "square", radius = 10, color = "#9b3b2f")
#RING#
r_finger_ring_metacarpal_gui = GUI("r_finger_ring_metacarpal", "rect", width = 10, height = 25, color = "#9b3b2f")
r_finger_ring_proximal_gui = GUI("r_finger_ring_proximal", "square", radius = 10, color = "#9b3b2f")
r_finger_ring_middlep_gui = GUI("r_finger_ring_middlep", "square", radius = 10, color = "#9b3b2f")
r_finger_ring_distal_gui = GUI("r_finger_ring_distal", "square", radius = 10, color = "#9b3b2f")
r_finger_ring_tip_gui = GUI("r_finger_ring_tip", "square", radius = 10, color = "#9b3b2f")
#PINKY#
r_finger_pinky_metacarpal_gui = GUI("r_finger_pinky_metacarpal", "rect", width = 10, height = 25, color = "#9b3b2f")
r_finger_pinky_proximal_gui = GUI("r_finger_pinky_proximal", "square", radius = 10, color = "#9b3b2f")
r_finger_pinky_middlep_gui = GUI("r_finger_pinky_middlep", "square", radius = 10, color = "#9b3b2f")
r_finger_pinky_distal_gui = GUI("r_finger_pinky_distal", "square", radius = 10, color = "#9b3b2f")
r_finger_pinky_tip_gui = GUI("r_finger_pinky_tip", "square", radius = 10, color = "#9b3b2f")
#EXTRA CONTROLS
r_fingers_thumb_gui = GUI("r_finger_thumb", "circle", radius = 12, color = "#9b3b2f", selections = "thumb")
r_fingers_index_gui = GUI("r_finger_index", "circle", radius = 12, color = "#9b3b2f", selections = "index")
r_fingers_middlef_gui = GUI("r_finger_middlef", "circle", radius = 12, color = "#9b3b2f", selections = "middlef")
r_fingers_ring_gui = GUI("r_finger_ring", "circle", radius = 12, color = "#9b3b2f", selections = "ring")
r_fingers_pinky_gui = GUI("r_finger_pinky", "circle", radius = 12, color = "#9b3b2f", selections = "pinky")

r_fingers_metacarpal_gui = GUI("r_finger_metacarpal", "circle", radius = 12, color = "#9b3b2f", selections = "metacarpal")
r_fingers_proximal_gui = GUI("r_finger_proximal", "circle", radius = 12, color = "#9b3b2f", selections = "proximal")
r_fingers_middlep_gui = GUI("r_finger_middlep", "circle", radius = 12, color = "#9b3b2f", selections = "middlep")
r_fingers_distal_gui = GUI("r_finger_distal", "circle", radius = 12, color = "#9b3b2f", selections = "distal")
r_fingers_tip_gui = GUI("r_finger_tip", "circle", radius = 12, color = "#9b3b2f", selections = "tip")

r_fingers_thumb_gui.drawMultipleSelectionButton(posX = 100, posY = 420)
r_fingers_index_gui.drawMultipleSelectionButton(posX = 85, posY = 420)
r_fingers_middlef_gui.drawMultipleSelectionButton(posX = 70, posY = 420)
r_fingers_ring_gui.drawMultipleSelectionButton(posX = 55, posY = 420)
r_fingers_pinky_gui.drawMultipleSelectionButton(posX = 40, posY = 420)

r_fingers_metacarpal_gui.drawMultipleSelectionButton(posX = 25, posY = 345)
r_fingers_proximal_gui.drawMultipleSelectionButton(posX = 25, posY = 360)
r_fingers_middlep_gui.drawMultipleSelectionButton(posX = 25, posY = 375)
r_fingers_distal_gui.drawMultipleSelectionButton(posX = 25, posY = 390)
r_fingers_tip_gui.drawMultipleSelectionButton(posX = 25, posY = 405)

r_finger_thumb_metacarpal_gui.drawSelectionButton(posX = 100, posY = 340)
r_finger_thumb_proximal_gui.drawSelectionButton(posX = 100, posY = 360)
r_finger_thumb_distal_gui.drawSelectionButton(posX = 100, posY = 375)
r_finger_thumb_tip_gui.drawSelectionButton(posX = 100, posY = 390)

r_finger_index_metacarpal_gui.drawSelectionButton(posX = 85, posY = 340)
r_finger_index_proximal_gui.drawSelectionButton(posX = 85, posY = 360)
r_finger_index_middlep_gui.drawSelectionButton(posX = 85, posY = 375)
r_finger_index_distal_gui.drawSelectionButton(posX = 85, posY = 390)
r_finger_index_tip_gui.drawSelectionButton(posX = 85, posY = 405)

r_finger_middlef_metacarpal_gui.drawSelectionButton(posX = 70, posY = 340)
r_finger_middlef_proximal_gui.drawSelectionButton(posX = 70, posY = 360)
r_finger_middlef_middlep_gui.drawSelectionButton(posX = 70, posY = 375)
r_finger_middlef_distal_gui.drawSelectionButton(posX = 70, posY = 390)
r_finger_middlef_tip_gui.drawSelectionButton(posX = 70, posY = 405)

r_finger_ring_metacarpal_gui.drawSelectionButton(posX = 55, posY = 340)
r_finger_ring_proximal_gui.drawSelectionButton(posX = 55, posY = 360)
r_finger_ring_middlep_gui.drawSelectionButton(posX = 55, posY = 375)
r_finger_ring_distal_gui.drawSelectionButton(posX = 55, posY = 390)
r_finger_ring_tip_gui.drawSelectionButton(posX = 55, posY = 405)

r_finger_pinky_metacarpal_gui.drawSelectionButton(posX = 40, posY = 340)
r_finger_pinky_proximal_gui.drawSelectionButton(posX = 40, posY = 360)
r_finger_pinky_middlep_gui.drawSelectionButton(posX = 40, posY = 375)
r_finger_pinky_distal_gui.drawSelectionButton(posX = 40, posY = 390)
r_finger_pinky_tip_gui.drawSelectionButton(posX = 40, posY = 405)

# LEGS #

l_thigh_gui = GUI("l_thigh", "circle", radius = 20, color = "#3d9b2f")
l_knee_gui = GUI("l_knee", "circle", radius = 20, color = "#3d9b2f")
l_ankle_gui = GUI("l_ankle", "circle", radius = 20, color = "#3d9b2f")
r_thigh_gui = GUI("r_thigh", "circle", radius = 20, color = "#9b3b2f")
r_knee_gui = GUI("r_knee", "circle", radius = 20, color = "#9b3b2f")
r_ankle_gui = GUI("r_ankle", "circle", radius = 20, color = "#9b3b2f")

l_thigh_fk_gui = GUI("l_thigh_fk", "circle", radius = 20, color = "#3d9b2f")
l_knee_fk_gui = GUI("l_knee_fk", "circle", radius = 20, color = "#3d9b2f")
l_ankle_fk_gui = GUI("l_ankle_fk", "circle", radius = 20, color = "#3d9b2f")
r_thigh_fk_gui = GUI("r_thigh_fk", "circle", radius = 20, color = "#9b3b2f")
r_knee_fk_gui = GUI("r_knee_fk", "circle", radius = 20, color = "#9b3b2f")
r_ankle_fk_gui = GUI("r_ankle_fk", "circle", radius = 20, color = "#9b3b2f")

l_leg_ikpole_gui = GUI("l_leg_ikpole", "circle", radius = 14, color = "#3d9b2f")
l_leg_ik_gui = GUI("l_leg_ik", "square", radius = 20, color = "#3d9b2f")
r_leg_ikpole_gui = GUI("r_leg_ikpole", "circle", radius = 14, color = "#9b3b2f")
r_leg_ik_gui = GUI("r_leg_ik", "square", radius = 20, color = "#9b3b2f")

l_thigh_gui.drawSelectionButton()
l_knee_gui.drawSelectionButton()
l_ankle_gui.drawSelectionButton()
r_thigh_gui.drawSelectionButton()
r_knee_gui.drawSelectionButton()
r_ankle_gui.drawSelectionButton()

l_thigh_fk_gui.drawSelectionButton()
l_knee_fk_gui.drawSelectionButton()
l_ankle_fk_gui.drawSelectionButton()
r_thigh_fk_gui.drawSelectionButton()
r_knee_fk_gui.drawSelectionButton()
r_ankle_fk_gui.drawSelectionButton()

l_leg_ikpole_gui.drawSelectionButton()
l_leg_ik_gui.drawSelectionButton()
r_leg_ikpole_gui.drawSelectionButton()
r_leg_ik_gui.drawSelectionButton()

# FOOT #

l_foot_ankle_gui = GUI("l_ankle", "rect", width = 55, height = 20, color = "#3d9b2f")
r_foot_ankle_gui = GUI("r_ankle", "rect", width = 55, height = 20, color = "#9b3b2f")

l_foot_ankle_fk_gui = GUI("l_ankle_fk", "rect", width = 55, height = 20, color = "#3d9b2f")
l_foot_ball_gui = GUI("l_foot_ball", "rect", width = 15, height = 15, color = "#3d9b2f")
l_foot_toes_gui = GUI("l_foot_toes", "rect", width = 20, height = 10, color = "#3d9b2f")
r_foot_ankle_fk_gui = GUI("r_ankle_fk", "rect", width = 55, height = 20, color = "#9b3b2f")
r_foot_ball_gui = GUI("r_foot_ball", "rect", width = 15, height = 15, color = "#9b3b2f")
r_foot_toes_gui = GUI("r_foot_toes", "rect", width = 20, height = 10, color = "#9b3b2f")

l_foot_ankle_gui.drawSelectionButton(370, 489)
r_foot_ankle_gui.drawSelectionButton(100, 489)

l_foot_ankle_fk_gui.drawSelectionButton(370, 489)
l_foot_ball_gui.drawSelectionButton(408, 492)
l_foot_toes_gui.drawSelectionButton(428, 494)
r_foot_ankle_fk_gui.drawSelectionButton(100, 489)
r_foot_ball_gui.drawSelectionButton(62, 492)
r_foot_toes_gui.drawSelectionButton(42, 494)

# IK FK #

l_arm_ikfk_switch_gui = GUI("l_arm_ikfk_switch", "square", radius = 30, color = "#3d9b2f")
r_arm_ikfk_switch_gui = GUI("r_arm_ikfk_switch", "square", radius = 30, color = "#9b3b2f")
l_leg_ikfk_switch_gui = GUI("l_leg_ikfk_switch", "square", radius = 30, color = "#3d9b2f")
r_leg_ikfk_switch_gui = GUI("r_leg_ikfk_switch", "square", radius = 30, color = "#9b3b2f")

l_leg_ikfk_switch_select_gui = GUI("l_leg_ikfk_switch", "rect", width = 30, height = 9, color = "#3d9b2f")
r_leg_ikfk_switch_select_gui = GUI("r_leg_ikfk_switch", "rect", width = 30, height = 9, color = "#9b3b2f")

l_arm_ikfk_switch_gui.drawToggleButton(420, 300)
r_arm_ikfk_switch_gui.drawToggleButton(55, 300)
l_leg_ikfk_switch_gui.drawToggleButton(360, 450)
r_leg_ikfk_switch_gui.drawToggleButton(110, 450)

l_leg_ikfk_switch_select_gui.drawSelectionButton(360, 472)
r_leg_ikfk_switch_select_gui.drawSelectionButton(110, 472)

#print(pickerwin.frameGeometry().width())
setNamespace()
ikfkuichange()

#pickerwin.show(dockable=True)

def helloitsme():
    print("hello from the other side")