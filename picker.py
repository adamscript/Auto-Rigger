from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import*

import math
import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI
from pymel.core import *

import maya.OpenMaya as om
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

scriptJob(ka = True)

picker_bg = QLabel()

namespace_label = QLabel()
namespace_label.setText("Namespace :")
namespace_label.setAlignment(Qt.AlignRight)

class Window(MayaQWidgetDockableMixin, QDialog):
    def __init__(self):
        super(Window, self).__init__()
        
        # It is crucial we set a unique object name as this is used internally by Maya
        self.setWindowTitle("Awan's Character Rig Picker GUI")
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.header_layout = QHBoxLayout()
        self.footer_layout = QHBoxLayout()
    
    def addLayout(self, layout):
        self.layout.addLayout(layout)

if __name__ == "__main__":
    window = Window()
    window.setFixedWidth(470)
    window.setFixedHeight(560)
    window.setWindowFlags(Qt.WindowStaysOnTopHint)

def setNamespace():
    spine.move(offsetX = -60)
    
    hip.move()
    waist.move()
    chest.move()
    collarbone.move()

    head.move(offsetX = -70)
    jaw.move()

    l_clavicle.move()
    r_clavicle.move()

    namespaceik = ls("*" + namespace_sel.currentText() + ":guiData", r = True)
    for i in namespaceik:
        if getAttr(i + ".isIK"):
            l_shoulder_fk.show().move()
            l_elbow_fk.show().move()
            l_wrist_fk.show().move()
            r_shoulder_fk.show().move()
            r_elbow_fk.show().move()
            r_wrist_fk.show().move()

            l_arm_ikpole.show().move()
            l_arm_ik.show().move()
            r_arm_ikpole.show().move()
            r_arm_ik.show().move()

            l_thigh_fk.show().move()
            l_knee_fk.show().move()
            l_ankle_fk.show().move()
            r_thigh_fk.show().move()
            r_knee_fk.show().move()
            r_ankle_fk.show().move()

            l_leg_ikpole.show().move()
            l_leg_ik.show().move()
            r_leg_ikpole.show().move()
            r_leg_ik.show().move()

            l_foot_ankle_fk.show()
            r_foot_ankle_fk.show()

            l_arm_ikfk_switch.show()
            r_arm_ikfk_switch.show()
            l_leg_ikfk_switch.show()
            r_leg_ikfk_switch.show()

            l_leg_ikfk_switch_select.show()
            r_leg_ikfk_switch_select.show()

            l_shoulder.hide()
            l_elbow.hide()
            l_wrist.hide()
            r_shoulder.hide()
            r_elbow.hide()
            r_wrist.hide()

            l_thigh.hide()
            l_knee.hide()
            l_ankle.hide()
            r_thigh.hide()
            r_knee.hide()
            r_ankle.hide()

            ikfkuichange()
        elif not getAttr(i + ".isIK"):
            l_shoulder.show().move()
            l_elbow.show().move()
            l_wrist.show().move()
            r_shoulder.show().move()
            r_elbow.show().move()
            r_wrist.show().move()

            l_thigh.show().move()
            l_knee.show().move()
            l_ankle.show().move()
            r_thigh.show().move()
            r_knee.show().move()
            r_ankle.show().move()

            l_shoulder_fk.hide()
            l_elbow_fk.hide()
            l_wrist_fk.hide()
            r_shoulder_fk.hide()
            r_elbow_fk.hide()
            r_wrist_fk.hide()

            l_arm_ikpole.hide()
            l_arm_ik.hide()
            r_arm_ikpole.hide()
            r_arm_ik.hide()

            l_thigh_fk.hide()
            l_knee_fk.hide()
            l_ankle_fk.hide()
            r_thigh_fk.hide()
            r_knee_fk.hide()
            r_ankle_fk.hide()

            l_leg_ikpole.hide()
            l_leg_ik.hide()
            r_leg_ikpole.hide()
            r_leg_ik.hide()

            l_foot_ankle_fk.hide()
            r_foot_ankle_fk.hide()

            l_arm_ikfk_switch.hide()
            r_arm_ikfk_switch.hide()
            l_leg_ikfk_switch.hide()
            r_leg_ikfk_switch.hide()

            l_leg_ikfk_switch_select.hide()
            r_leg_ikfk_switch_select.hide()

    picker_bg.setPixmap(workspace(q = True, rd = True) + "images/" + namespace_sel.currentText() +'_pb.1.jpg')

def ikfkuichange():
    for x in ls("*" + namespace_sel.currentText() + ":*_ikfk_switch_ctrl"):
        if((str(x).partition(namespace_sel.currentText() + ':')[2]).startswith("l_arm")):
            if(getAttr('*' + namespace_sel.currentText() + ':l_arm_ikfk_switch_ctrl.IK_FK_switch') == 0):
                l_arm_ikfk_switch.setText("FK")
                l_shoulder_fk.show()
                l_elbow_fk.show()
                l_wrist_fk.show()
                l_arm_ikpole.hide()
                l_arm_ik.hide()
            elif(getAttr('*' + namespace_sel.currentText() + ':l_arm_ikfk_switch_ctrl.IK_FK_switch') == 1):
                l_arm_ikfk_switch.setText("IK")
                l_shoulder_fk.hide()
                l_elbow_fk.hide()
                l_wrist_fk.hide()
                l_arm_ikpole.show()
                l_arm_ik.show()
        elif((str(x).partition(namespace_sel.currentText() + ':')[2]).startswith("r_arm")):
            if(getAttr('*' + namespace_sel.currentText() + ':r_arm_ikfk_switch_ctrl.IK_FK_switch') == 0):
                r_arm_ikfk_switch.setText("FK")
                r_shoulder_fk.show()
                r_elbow_fk.show()
                r_wrist_fk.show()
                r_arm_ikpole.hide()
                r_arm_ik.hide()
            elif(getAttr('*' + namespace_sel.currentText() + ':r_arm_ikfk_switch_ctrl.IK_FK_switch') == 1):
                r_arm_ikfk_switch.setText("IK")
                r_shoulder_fk.hide()
                r_elbow_fk.hide()
                r_wrist_fk.hide()
                r_arm_ikpole.show()
                r_arm_ik.show()
        elif((str(x).partition(namespace_sel.currentText() + ':')[2]).startswith("l_leg")):
            if(getAttr('*' + namespace_sel.currentText() + ':l_leg_ikfk_switch_ctrl.IK_FK_switch') == 0):
                l_leg_ikfk_switch.setText("FK")
                l_thigh_fk.show()
                l_knee_fk.show()
                l_ankle_fk.show()
                l_leg_ikpole.hide()
                l_leg_ik.hide()
            elif(getAttr('*' + namespace_sel.currentText() + ':l_leg_ikfk_switch_ctrl.IK_FK_switch') == 1):
                l_leg_ikfk_switch.setText("IK")
                l_thigh_fk.hide()
                l_knee_fk.hide()
                l_ankle_fk.hide()
                l_leg_ikpole.show()
                l_leg_ik.show()
        elif((str(x).partition(namespace_sel.currentText() + ':')[2]).startswith("r_leg")):
            if(getAttr('*' + namespace_sel.currentText() + ':r_leg_ikfk_switch_ctrl.IK_FK_switch') == 0):
                r_leg_ikfk_switch.setText("FK")
                r_thigh_fk.show()
                r_knee_fk.show()
                r_ankle_fk.show()
                r_leg_ikpole.hide()
                r_leg_ik.hide()
            elif(getAttr('*' + namespace_sel.currentText() + ':r_leg_ikfk_switch_ctrl.IK_FK_switch') == 1):
                r_leg_ikfk_switch.setText("IK")
                r_thigh_fk.hide()
                r_knee_fk.hide()
                r_ankle_fk.hide()
                r_leg_ikpole.show()
                r_leg_ik.show()

namespaceik = ls("*" + namespace_sel.currentText() + ":guiData", r = True)
for i in namespaceik:
    if getAttr(i + ".isIK"):
        for i in ls("*_ikfk_switch_ctrl", r = True):
            scriptJob(ac = [i + '.IK_FK_switch', ikfkuichange])
    elif not getAttr(i + ".isIK"):
        pass

namespace_sel = QComboBox()
namespace_list = ls("*guiData", r = True)
for i in namespace_list:
    namespace_sel.addItem(getAttr(i + ".name"))
namespace_sel.activated.connect(setNamespace)

window.header_layout.addWidget(namespace_label)
window.header_layout.addWidget(namespace_sel)

window.layout.addLayout(window.header_layout)
window.layout.addWidget(picker_bg)
window.layout.addLayout(window.footer_layout)

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
        window.footer_layout.addWidget(self.button)

    def drawSelectionButton(self, posX = 0, posY = 0):
        if (self.shape == "square"):
            self.button = QPushButton(window)
            self.button.setText(self.text)
            self.button.setGeometry(posX - (self.radius/2), posY - (self.radius/2), self.radius, self.radius)
            self.button.setStyleSheet("background-color: " + self.color + ";")
            self.button.clicked.connect(self.selection)
        elif(self.shape == "rect"):
            self.button = QPushButton(window)
            self.button.setText(self.text)
            self.button.setGeometry(posX - (self.width/2), posY - (self.height/2), self.width, self.height)
            self.button.setStyleSheet("background-color: " + self.color + ";")
            self.button.clicked.connect(self.selection)
        elif(self.shape == "circle"):
            self.button = QPushButton(window)
            self.button.setText(self.text)
            self.button.setGeometry(posX - (self.radius/2), posY - (self.radius/2), self.radius, self.radius)
            self.button.setStyleSheet("background-color: " + self.color + "; border-radius: " + str(self.radius/2) + "px;")
            self.button.clicked.connect(self.selection)

    def drawMultipleSelectionButton(self, posX = 0, posY = 0):
        self.button = QPushButton(window)
        self.button.setText(self.text)
        self.button.setGeometry(posX - (self.radius/2), posY - (self.radius/2), self.radius, self.radius)
        self.button.setStyleSheet("background-color: " + self.color + "; border-radius: " + str(self.radius/2) + "px;")
        self.button.clicked.connect(self.multipleSelection)

    def drawToggleButton(self, posX = 0, posY = 0):
        self.button = QPushButton(window)
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

root = GUI("root", "rect", width = 150, height = 10, color = "#3696d9")
ctrlgrp = GUI("grp", "rect", width = 50, height = 10, color = "#3696d9")

root.drawSelectionButton(235, 505)
ctrlgrp.drawSelectionButton(235, 490)

# SPINE #
spine = GUI("spine", "square", radius = 20, color = "#cad936")

hip = GUI("hip", "rect", width = 80, height = 10, color = "#cad936")
waist = GUI("waist", "rect", width = 60, height = 10, color = "#cad936")
chest = GUI("chest", "rect", width = 60, height = 10, color = "#cad936")
collarbone = GUI("collarbone", "square", radius = 18, color = "#cad936")

spine.drawSelectionButton()

hip.drawSelectionButton()
waist.drawSelectionButton()
chest.drawSelectionButton()
collarbone.drawSelectionButton()

# HEAD #
head = GUI("head", "square", radius = 50, color = "#cad936")
jaw = GUI("jaw", "circle", radius = 10, color = "#cad936")
l_eye = GUI("l_eye", "circle", radius = 16, color = "#3d9b2f")
r_eye = GUI("r_eye", "circle", radius = 16, color = "#9b3b2f")
eyesLookAt = GUI("eyesLookAt", "rect", width = 50, height = 7, color = "#cad936")

head.drawSelectionButton()
jaw.drawSelectionButton()
l_eye.drawSelectionButton(340, 90)
r_eye.drawSelectionButton(316, 90)
eyesLookAt.drawSelectionButton(328, 110)

# ARMS #
l_clavicle = GUI("l_clavicle", "square", radius = 12, color = "#3d9b2f")
r_clavicle = GUI("r_clavicle", "square", radius = 12, color = "#9b3b2f")

l_shoulder = GUI("l_shoulder", "circle", radius = 20, color = "#3d9b2f")
l_elbow = GUI("l_elbow", "circle", radius = 20, color = "#3d9b2f")
l_wrist = GUI("l_wrist", "circle", radius = 20, color = "#3d9b2f")
r_shoulder = GUI("r_shoulder", "circle", radius = 20, color = "#9b3b2f")
r_elbow = GUI("r_elbow", "circle", radius = 20, color = "#9b3b2f")
r_wrist = GUI("r_wrist", "circle", radius = 20, color = "#9b3b2f")

l_shoulder_fk = GUI("l_shoulder_fk", "circle", radius = 20, color = "#3d9b2f")
l_elbow_fk = GUI("l_elbow_fk", "circle", radius = 20, color = "#3d9b2f")
l_wrist_fk = GUI("l_wrist_fk", "circle", radius = 20, color = "#3d9b2f")
r_shoulder_fk = GUI("r_shoulder_fk", "circle", radius = 20, color = "#9b3b2f")
r_elbow_fk = GUI("r_elbow_fk", "circle", radius = 20, color = "#9b3b2f")
r_wrist_fk = GUI("r_wrist_fk", "circle", radius = 20, color = "#9b3b2f")

l_arm_ikpole = GUI("l_arm_ikpole", "circle", radius = 14, color = "#3d9b2f")
l_arm_ik = GUI("l_arm_ik", "square", radius = 20, color = "#3d9b2f")
r_arm_ikpole = GUI("r_arm_ikpole", "circle", radius = 14, color = "#9b3b2f")
r_arm_ik = GUI("r_arm_ik", "square", radius = 20, color = "#9b3b2f")

l_clavicle.drawSelectionButton()
r_clavicle.drawSelectionButton()

l_shoulder.drawSelectionButton()
l_elbow.drawSelectionButton()
l_wrist.drawSelectionButton()
r_shoulder.drawSelectionButton()
r_elbow.drawSelectionButton()
r_wrist.drawSelectionButton()

l_shoulder_fk.drawSelectionButton()
l_elbow_fk.drawSelectionButton()
l_wrist_fk.drawSelectionButton()
r_shoulder_fk.drawSelectionButton()
r_elbow_fk.drawSelectionButton()
r_wrist_fk.drawSelectionButton()

l_arm_ikpole.drawSelectionButton()
l_arm_ik.drawSelectionButton()
r_arm_ikpole.drawSelectionButton()
r_arm_ik.drawSelectionButton()

# L FINGERS #
#THUMB#
l_finger_thumb_metacarpal = GUI("l_finger_thumb_metacarpal", "rect", width = 15, height = 25, color = "#3d9b2f")
l_finger_thumb_proximal = GUI("l_finger_thumb_proximal", "rect", width = 15, height = 10, color = "#3d9b2f")
l_finger_thumb_distal = GUI("l_finger_thumb_distal", "rect", width = 15, height = 10, color = "#3d9b2f")
l_finger_thumb_tip = GUI("l_finger_thumb_tip", "rect", width = 15, height = 10, color = "#3d9b2f")
#INDEX#
l_finger_index_metacarpal = GUI("l_finger_index_metacarpal", "rect", width = 10, height = 25, color = "#3d9b2f")
l_finger_index_proximal = GUI("l_finger_index_proximal", "square", radius = 10, color = "#3d9b2f")
l_finger_index_middlep = GUI("l_finger_index_middlep", "square", radius = 10, color = "#3d9b2f")
l_finger_index_distal = GUI("l_finger_index_distal", "square", radius = 10, color = "#3d9b2f")
l_finger_index_tip = GUI("l_finger_index_tip", "square", radius = 10, color = "#3d9b2f")
#MIDDLE#
l_finger_middlef_metacarpal = GUI("l_finger_middlef_metacarpal", "rect", width = 10, height = 25, color = "#3d9b2f")
l_finger_middlef_proximal = GUI("l_finger_middlef_proximal", "square", radius = 10, color = "#3d9b2f")
l_finger_middlef_middlep = GUI("l_finger_middlef_middlep", "square", radius = 10, color = "#3d9b2f")
l_finger_middlef_distal = GUI("l_finger_middlef_distal", "square", radius = 10, color = "#3d9b2f")
l_finger_middlef_tip = GUI("l_finger_middlef_tip", "square", radius = 10, color = "#3d9b2f")
#RING#
l_finger_ring_metacarpal = GUI("l_finger_ring_metacarpal", "rect", width = 10, height = 25, color = "#3d9b2f")
l_finger_ring_proximal = GUI("l_finger_ring_proximal", "square", radius = 10, color = "#3d9b2f")
l_finger_ring_middlep = GUI("l_finger_ring_middlep", "square", radius = 10, color = "#3d9b2f")
l_finger_ring_distal = GUI("l_finger_ring_distal", "square", radius = 10, color = "#3d9b2f")
l_finger_ring_tip = GUI("l_finger_ring_tip", "square", radius = 10, color = "#3d9b2f")
#PINKY#
l_finger_pinky_metacarpal = GUI("l_finger_pinky_metacarpal", "rect", width = 10, height = 25, color = "#3d9b2f")
l_finger_pinky_proximal = GUI("l_finger_pinky_proximal", "square", radius = 10, color = "#3d9b2f")
l_finger_pinky_middlep = GUI("l_finger_pinky_middlep", "square", radius = 10, color = "#3d9b2f")
l_finger_pinky_distal = GUI("l_finger_pinky_distal", "square", radius = 10, color = "#3d9b2f")
l_finger_pinky_tip = GUI("l_finger_pinky_tip", "square", radius = 10, color = "#3d9b2f")
#EXTRA CONTROLS
l_fingers_thumb = GUI("l_finger_thumb", "circle", radius = 12, color = "#3d9b2f", selections = "thumb")
l_fingers_index = GUI("l_finger_index", "circle", radius = 12, color = "#3d9b2f", selections = "index")
l_fingers_middlef = GUI("l_finger_middlef", "circle", radius = 12, color = "#3d9b2f", selections = "middlef")
l_fingers_ring = GUI("l_finger_ring", "circle", radius = 12, color = "#3d9b2f", selections = "ring")
l_fingers_pinky = GUI("l_finger_pinky", "circle", radius = 12, color = "#3d9b2f", selections = "pinky")

l_fingers_metacarpal = GUI("l_finger_metacarpal", "circle", radius = 12, color = "#3d9b2f", selections = "metacarpal")
l_fingers_proximal = GUI("l_finger_proximal", "circle", radius = 12, color = "#3d9b2f", selections = "proximal")
l_fingers_middlep = GUI("l_finger_middlep", "circle", radius = 12, color = "#3d9b2f", selections = "middlep")
l_fingers_distal = GUI("l_finger_distal", "circle", radius = 12, color = "#3d9b2f", selections = "distal")
l_fingers_tip = GUI("l_finger_tip", "circle", radius = 12, color = "#3d9b2f", selections = "tip")

l_fingers_thumb.drawMultipleSelectionButton(posX = 370, posY = 420)
l_fingers_index.drawMultipleSelectionButton(posX = 385, posY = 420)
l_fingers_middlef.drawMultipleSelectionButton(posX = 400, posY = 420)
l_fingers_ring.drawMultipleSelectionButton(posX = 415, posY = 420)
l_fingers_pinky.drawMultipleSelectionButton(posX = 430, posY = 420)

l_fingers_metacarpal.drawMultipleSelectionButton(posX = 445, posY = 345)
l_fingers_proximal.drawMultipleSelectionButton(posX = 445, posY = 360)
l_fingers_middlep.drawMultipleSelectionButton(posX = 445, posY = 375)
l_fingers_distal.drawMultipleSelectionButton(posX = 445, posY = 390)
l_fingers_tip.drawMultipleSelectionButton(posX = 445, posY = 405)

l_finger_thumb_metacarpal.drawSelectionButton(posX = 370, posY = 340)
l_finger_thumb_proximal.drawSelectionButton(posX = 370, posY = 360)
l_finger_thumb_distal.drawSelectionButton(posX = 370, posY = 375)
l_finger_thumb_tip.drawSelectionButton(posX = 370, posY = 390)

l_finger_index_metacarpal.drawSelectionButton(posX = 385, posY = 340)
l_finger_index_proximal.drawSelectionButton(posX = 385, posY = 360)
l_finger_index_middlep.drawSelectionButton(posX = 385, posY = 375)
l_finger_index_distal.drawSelectionButton(posX = 385, posY = 390)
l_finger_index_tip.drawSelectionButton(posX = 385, posY = 405)

l_finger_middlef_metacarpal.drawSelectionButton(posX = 400, posY = 340)
l_finger_middlef_proximal.drawSelectionButton(posX = 400, posY = 360)
l_finger_middlef_middlep.drawSelectionButton(posX = 400, posY = 375)
l_finger_middlef_distal.drawSelectionButton(posX = 400, posY = 390)
l_finger_middlef_tip.drawSelectionButton(posX = 400, posY = 405)

l_finger_ring_metacarpal.drawSelectionButton(posX = 415, posY = 340)
l_finger_ring_proximal.drawSelectionButton(posX = 415, posY = 360)
l_finger_ring_middlep.drawSelectionButton(posX = 415, posY = 375)
l_finger_ring_distal.drawSelectionButton(posX = 415, posY = 390)
l_finger_ring_tip.drawSelectionButton(posX = 415, posY = 405)

l_finger_pinky_metacarpal.drawSelectionButton(posX = 430, posY = 340)
l_finger_pinky_proximal.drawSelectionButton(posX = 430, posY = 360)
l_finger_pinky_middlep.drawSelectionButton(posX = 430, posY = 375)
l_finger_pinky_distal.drawSelectionButton(posX = 430, posY = 390)
l_finger_pinky_tip.drawSelectionButton(posX = 430, posY = 405)

# R FINGERS #
#THUMB#
r_finger_thumb_metacarpal = GUI("r_finger_thumb_metacarpal", "rect", width = 15, height = 25, color = "#9b3b2f")
r_finger_thumb_proximal = GUI("r_finger_thumb_proximal", "rect", width = 15, height = 10, color = "#9b3b2f")
r_finger_thumb_distal = GUI("r_finger_thumb_distal", "rect", width = 15, height = 10, color = "#9b3b2f")
r_finger_thumb_tip = GUI("r_finger_thumb_tip", "rect", width = 15, height = 10, color = "#9b3b2f")
#INDEX#
r_finger_index_metacarpal = GUI("r_finger_index_metacarpal", "rect", width = 10, height = 25, color = "#9b3b2f")
r_finger_index_proximal = GUI("r_finger_index_proximal", "square", radius = 10, color = "#9b3b2f")
r_finger_index_middlep = GUI("r_finger_index_middlep", "square", radius = 10, color = "#9b3b2f")
r_finger_index_distal = GUI("r_finger_index_distal", "square", radius = 10, color = "#9b3b2f")
r_finger_index_tip = GUI("r_finger_index_tip", "square", radius = 10, color = "#9b3b2f")
#MIDDLE#
r_finger_middlef_metacarpal = GUI("r_finger_middlef_metacarpal", "rect", width = 10, height = 25, color = "#9b3b2f")
r_finger_middlef_proximal = GUI("r_finger_middlef_proximal", "square", radius = 10, color = "#9b3b2f")
r_finger_middlef_middlep = GUI("r_finger_middlef_middlep", "square", radius = 10, color = "#9b3b2f")
r_finger_middlef_distal = GUI("r_finger_middlef_distal", "square", radius = 10, color = "#9b3b2f")
r_finger_middlef_tip = GUI("r_finger_middlef_tip", "square", radius = 10, color = "#9b3b2f")
#RING#
r_finger_ring_metacarpal = GUI("r_finger_ring_metacarpal", "rect", width = 10, height = 25, color = "#9b3b2f")
r_finger_ring_proximal = GUI("r_finger_ring_proximal", "square", radius = 10, color = "#9b3b2f")
r_finger_ring_middlep = GUI("r_finger_ring_middlep", "square", radius = 10, color = "#9b3b2f")
r_finger_ring_distal = GUI("r_finger_ring_distal", "square", radius = 10, color = "#9b3b2f")
r_finger_ring_tip = GUI("r_finger_ring_tip", "square", radius = 10, color = "#9b3b2f")
#PINKY#
r_finger_pinky_metacarpal = GUI("r_finger_pinky_metacarpal", "rect", width = 10, height = 25, color = "#9b3b2f")
r_finger_pinky_proximal = GUI("r_finger_pinky_proximal", "square", radius = 10, color = "#9b3b2f")
r_finger_pinky_middlep = GUI("r_finger_pinky_middlep", "square", radius = 10, color = "#9b3b2f")
r_finger_pinky_distal = GUI("r_finger_pinky_distal", "square", radius = 10, color = "#9b3b2f")
r_finger_pinky_tip = GUI("r_finger_pinky_tip", "square", radius = 10, color = "#9b3b2f")
#EXTRA CONTROLS
r_fingers_thumb = GUI("r_finger_thumb", "circle", radius = 12, color = "#9b3b2f", selections = "thumb")
r_fingers_index = GUI("r_finger_index", "circle", radius = 12, color = "#9b3b2f", selections = "index")
r_fingers_middlef = GUI("r_finger_middlef", "circle", radius = 12, color = "#9b3b2f", selections = "middlef")
r_fingers_ring = GUI("r_finger_ring", "circle", radius = 12, color = "#9b3b2f", selections = "ring")
r_fingers_pinky = GUI("r_finger_pinky", "circle", radius = 12, color = "#9b3b2f", selections = "pinky")

r_fingers_metacarpal = GUI("r_finger_metacarpal", "circle", radius = 12, color = "#9b3b2f", selections = "metacarpal")
r_fingers_proximal = GUI("r_finger_proximal", "circle", radius = 12, color = "#9b3b2f", selections = "proximal")
r_fingers_middlep = GUI("r_finger_middlep", "circle", radius = 12, color = "#9b3b2f", selections = "middlep")
r_fingers_distal = GUI("r_finger_distal", "circle", radius = 12, color = "#9b3b2f", selections = "distal")
r_fingers_tip = GUI("r_finger_tip", "circle", radius = 12, color = "#9b3b2f", selections = "tip")

r_fingers_thumb.drawMultipleSelectionButton(posX = 100, posY = 420)
r_fingers_index.drawMultipleSelectionButton(posX = 85, posY = 420)
r_fingers_middlef.drawMultipleSelectionButton(posX = 70, posY = 420)
r_fingers_ring.drawMultipleSelectionButton(posX = 55, posY = 420)
r_fingers_pinky.drawMultipleSelectionButton(posX = 40, posY = 420)

r_fingers_metacarpal.drawMultipleSelectionButton(posX = 25, posY = 345)
r_fingers_proximal.drawMultipleSelectionButton(posX = 25, posY = 360)
r_fingers_middlep.drawMultipleSelectionButton(posX = 25, posY = 375)
r_fingers_distal.drawMultipleSelectionButton(posX = 25, posY = 390)
r_fingers_tip.drawMultipleSelectionButton(posX = 25, posY = 405)

r_finger_thumb_metacarpal.drawSelectionButton(posX = 100, posY = 340)
r_finger_thumb_proximal.drawSelectionButton(posX = 100, posY = 360)
r_finger_thumb_distal.drawSelectionButton(posX = 100, posY = 375)
r_finger_thumb_tip.drawSelectionButton(posX = 100, posY = 390)

r_finger_index_metacarpal.drawSelectionButton(posX = 85, posY = 340)
r_finger_index_proximal.drawSelectionButton(posX = 85, posY = 360)
r_finger_index_middlep.drawSelectionButton(posX = 85, posY = 375)
r_finger_index_distal.drawSelectionButton(posX = 85, posY = 390)
r_finger_index_tip.drawSelectionButton(posX = 85, posY = 405)

r_finger_middlef_metacarpal.drawSelectionButton(posX = 70, posY = 340)
r_finger_middlef_proximal.drawSelectionButton(posX = 70, posY = 360)
r_finger_middlef_middlep.drawSelectionButton(posX = 70, posY = 375)
r_finger_middlef_distal.drawSelectionButton(posX = 70, posY = 390)
r_finger_middlef_tip.drawSelectionButton(posX = 70, posY = 405)

r_finger_ring_metacarpal.drawSelectionButton(posX = 55, posY = 340)
r_finger_ring_proximal.drawSelectionButton(posX = 55, posY = 360)
r_finger_ring_middlep.drawSelectionButton(posX = 55, posY = 375)
r_finger_ring_distal.drawSelectionButton(posX = 55, posY = 390)
r_finger_ring_tip.drawSelectionButton(posX = 55, posY = 405)

r_finger_pinky_metacarpal.drawSelectionButton(posX = 40, posY = 340)
r_finger_pinky_proximal.drawSelectionButton(posX = 40, posY = 360)
r_finger_pinky_middlep.drawSelectionButton(posX = 40, posY = 375)
r_finger_pinky_distal.drawSelectionButton(posX = 40, posY = 390)
r_finger_pinky_tip.drawSelectionButton(posX = 40, posY = 405)

# LEGS #

l_thigh = GUI("l_thigh", "circle", radius = 20, color = "#3d9b2f")
l_knee = GUI("l_knee", "circle", radius = 20, color = "#3d9b2f")
l_ankle = GUI("l_ankle", "circle", radius = 20, color = "#3d9b2f")
r_thigh = GUI("r_thigh", "circle", radius = 20, color = "#9b3b2f")
r_knee = GUI("r_knee", "circle", radius = 20, color = "#9b3b2f")
r_ankle = GUI("r_ankle", "circle", radius = 20, color = "#9b3b2f")

l_thigh_fk = GUI("l_thigh_fk", "circle", radius = 20, color = "#3d9b2f")
l_knee_fk = GUI("l_knee_fk", "circle", radius = 20, color = "#3d9b2f")
l_ankle_fk = GUI("l_ankle_fk", "circle", radius = 20, color = "#3d9b2f")
r_thigh_fk = GUI("r_thigh_fk", "circle", radius = 20, color = "#9b3b2f")
r_knee_fk = GUI("r_knee_fk", "circle", radius = 20, color = "#9b3b2f")
r_ankle_fk = GUI("r_ankle_fk", "circle", radius = 20, color = "#9b3b2f")

l_leg_ikpole = GUI("l_leg_ikpole", "circle", radius = 14, color = "#3d9b2f")
l_leg_ik = GUI("l_leg_ik", "square", radius = 20, color = "#3d9b2f")
r_leg_ikpole = GUI("r_leg_ikpole", "circle", radius = 14, color = "#9b3b2f")
r_leg_ik = GUI("r_leg_ik", "square", radius = 20, color = "#9b3b2f")

l_thigh.drawSelectionButton()
l_knee.drawSelectionButton()
l_ankle.drawSelectionButton()
r_thigh.drawSelectionButton()
r_knee.drawSelectionButton()
r_ankle.drawSelectionButton()

l_thigh_fk.drawSelectionButton()
l_knee_fk.drawSelectionButton()
l_ankle_fk.drawSelectionButton()
r_thigh_fk.drawSelectionButton()
r_knee_fk.drawSelectionButton()
r_ankle_fk.drawSelectionButton()

l_leg_ikpole.drawSelectionButton()
l_leg_ik.drawSelectionButton()
r_leg_ikpole.drawSelectionButton()
r_leg_ik.drawSelectionButton()

# FOOT #

l_foot_ankle = GUI("l_ankle", "rect", width = 55, height = 20, color = "#3d9b2f")
r_foot_ankle = GUI("r_ankle", "rect", width = 55, height = 20, color = "#9b3b2f")

l_foot_ankle_fk = GUI("l_ankle_fk", "rect", width = 55, height = 20, color = "#3d9b2f")
l_foot_ball = GUI("l_foot_ball", "rect", width = 15, height = 15, color = "#3d9b2f")
l_foot_toes = GUI("l_foot_toes", "rect", width = 20, height = 10, color = "#3d9b2f")
r_foot_ankle_fk =GUI("r_ankle_fk", "rect", width = 55, height = 20, color = "#9b3b2f")
r_foot_ball = GUI("r_foot_ball", "rect", width = 15, height = 15, color = "#9b3b2f")
r_foot_toes = GUI("r_foot_toes", "rect", width = 20, height = 10, color = "#9b3b2f")

l_foot_ankle.drawSelectionButton(370, 489)
r_foot_ankle.drawSelectionButton(100, 489)

l_foot_ankle_fk.drawSelectionButton(370, 489)
l_foot_ball.drawSelectionButton(408, 492)
l_foot_toes.drawSelectionButton(428, 494)
r_foot_ankle_fk.drawSelectionButton(100, 489)
r_foot_ball.drawSelectionButton(62, 492)
r_foot_toes.drawSelectionButton(42, 494)

# IK FK #

l_arm_ikfk_switch = GUI("l_arm_ikfk_switch", "square", radius = 30, color = "#3d9b2f")
r_arm_ikfk_switch = GUI("r_arm_ikfk_switch", "square", radius = 30, color = "#9b3b2f")
l_leg_ikfk_switch = GUI("l_leg_ikfk_switch", "square", radius = 30, color = "#3d9b2f")
r_leg_ikfk_switch = GUI("r_leg_ikfk_switch", "square", radius = 30, color = "#9b3b2f")

l_leg_ikfk_switch_select = GUI("l_leg_ikfk_switch", "rect", width = 30, height = 9, color = "#3d9b2f")
r_leg_ikfk_switch_select = GUI("r_leg_ikfk_switch", "rect", width = 30, height = 9, color = "#9b3b2f")

l_arm_ikfk_switch.drawToggleButton(420, 300)
r_arm_ikfk_switch.drawToggleButton(55, 300)
l_leg_ikfk_switch.drawToggleButton(360, 450)
r_leg_ikfk_switch.drawToggleButton(110, 450)

l_leg_ikfk_switch_select.drawSelectionButton(360, 472)
r_leg_ikfk_switch_select.drawSelectionButton(110, 472)

#print(window.frameGeometry().width())
setNamespace()
ikfkuichange()

window.show(dockable=True)