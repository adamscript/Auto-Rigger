from PySide2.QtWidgets import *
from PySide2.QtGui import *

import math
import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI
from pymel.core import *

import maya.OpenMaya as om

#workspace = workspace(q = True, rd = True)
#pb = playblast(st = 1, et = 1, fmt = 'image', f = workspace + "testpb",  fp = 0, p = 10, c = 'jpg', qlt = 100, w = 270 * 10, h = 480 * 10, orn = False, v = False)

#print (pointWorldToCam('camera2', pos3, (270,480)))

window = QWidget()
layout = QVBoxLayout()

picker_bg = QLabel(window)
#bg = QPixmap(workspace + namespace_sel.currentText() +'_pb.1.jpg')
#bg = QPixmap('c:/users/hp/documents/pickerguirefs.jpg')
#picker_bg.setPixmap(bg)

header_layout = QHBoxLayout()
footer_layout = QHBoxLayout()

namespace_label = QLabel()
namespace_label.setText("Namespace :")
namespace_label.setAlignment(Qt.AlignRight)

def setNamespace():
    hip.move()
    waist.move()
    chest.move()
    picker_bg.setPixmap(workspace(q = True, rd = True) + "images/" + namespace_sel.currentText() +'_pb.1.jpg')

namespace_sel = QComboBox()
namespace_list = ls("*guiData", r = True)
for i in namespace_list:
    namespace_sel.addItem(getAttr(i + ".name"))
namespace_sel.activated.connect(setNamespace)

header_layout.addWidget(namespace_label)
header_layout.addWidget(namespace_sel)

key_btn = QPushButton()
keyall_btn = QPushButton()
resetpose_btn = QPushButton()
deselectall_btn = QPushButton()

footer_layout.addWidget(key_btn)
footer_layout.addWidget(keyall_btn)
footer_layout.addWidget(resetpose_btn)
footer_layout.addWidget(deselectall_btn)

layout.addLayout(header_layout)
layout.addWidget(picker_bg)
layout.addLayout(footer_layout)

window.setLayout(layout)
window.setWindowTitle("Awan's Character Rig Picker GUI")

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
        #print("clicked multiple")
        #select(d = True)
        selects = ls(self.name.partition(self.selections)[0] + "*" + self.name.partition(self.selections)[1] + "*_ctrl")
        for x in selects:   
            select(x, add = True)
            print(x)

    def move(self):
        self.namespace = ls("*" + namespace_sel.currentText() + ":guiData", r = True)
        for i in self.namespace:
            self.button.move((getAttr(i + "." + self.name + "_ctrl_guiDataX")) - (self.radius/2), (getAttr(i + "." + self.name + "_ctrl_guiDataY")) - (self.radius/2))

# SPINE #
hip = GUI("hip", "circle", radius = 20, color = "yellow")
waist = GUI("waist", "circle", radius = 20, color = "yellow")
chest = GUI("chest", "circle", radius = 20, color = "yellow")


hip.drawSelectionButton()
waist.drawSelectionButton()
chest.drawSelectionButton()

# FINGERS #
#THUMB#
l_finger_thumb_metacarpal = GUI("l_finger_thumb_metacarpal", "rect", width = 15, height = 25, color = "green")
l_finger_thumb_proximal = GUI("l_finger_thumb_proximal", "rect", width = 15, height = 10, color = "green")
l_finger_thumb_distal = GUI("l_finger_thumb_distal", "rect", width = 15, height = 10, color = "green")
l_finger_thumb_tip = GUI("l_finger_thumb_tip", "rect", width = 15, height = 10, color = "green")
#INDEX#
l_finger_index_metacarpal = GUI("l_finger_index_metacarpal", "rect", width = 10, height = 25, color = "green")
l_finger_index_proximal = GUI("l_finger_index_proximal", "square", radius = 10, color = "green")
l_finger_index_middlep = GUI("l_finger_index_middlep", "square", radius = 10, color = "green")
l_finger_index_distal = GUI("l_finger_index_distal", "square", radius = 10, color = "green")
l_finger_index_tip = GUI("l_finger_index_tip", "square", radius = 10, color = "green")
#MIDDLE#
l_finger_middlef_metacarpal = GUI("l_finger_middlef_metacarpal", "rect", width = 10, height = 25, color = "green")
l_finger_middlef_proximal = GUI("l_finger_middlef_proximal", "square", radius = 10, color = "green")
l_finger_middlef_middlep = GUI("l_finger_middlef_middlep", "square", radius = 10, color = "green")
l_finger_middlef_distal = GUI("l_finger_middlef_distal", "square", radius = 10, color = "green")
l_finger_middlef_tip = GUI("l_finger_middlef_tip", "square", radius = 10, color = "green")
#RING#
l_finger_ring_metacarpal = GUI("l_finger_ring_metacarpal", "rect", width = 10, height = 25, color = "green")
l_finger_ring_proximal = GUI("l_finger_ring_proximal", "square", radius = 10, color = "green")
l_finger_ring_middlep = GUI("l_finger_ring_middlep", "square", radius = 10, color = "green")
l_finger_ring_distal = GUI("l_finger_ring_distal", "square", radius = 10, color = "green")
l_finger_ring_tip = GUI("l_finger_ring_tip", "square", radius = 10, color = "green")
#PINKY#
l_finger_pinky_metacarpal = GUI("l_finger_pinky_metacarpal", "rect", width = 10, height = 25, color = "green")
l_finger_pinky_proximal = GUI("l_finger_pinky_proximal", "square", radius = 10, color = "green")
l_finger_pinky_middlep = GUI("l_finger_pinky_middlep", "square", radius = 10, color = "green")
l_finger_pinky_distal = GUI("l_finger_pinky_distal", "square", radius = 10, color = "green")
l_finger_pinky_tip = GUI("l_finger_pinky_tip", "square", radius = 10, color = "green")
#EXTRA CONTROLS
l_fingers_thumb = GUI("l_finger_thumb", "circle", radius = 12, color = "green", selections = "thumb")
l_fingers_index = GUI("l_finger_index", "circle", radius = 12, color = "green", selections = "index")
l_fingers_middlef = GUI("l_finger_middlef", "circle", radius = 12, color = "green", selections = "middlef")
l_fingers_ring = GUI("l_finger_ring", "circle", radius = 12, color = "green", selections = "ring")
l_fingers_pinky = GUI("l_finger_pinky", "circle", radius = 12, color = "green", selections = "pinky")

l_fingers_metacarpal = GUI("l_finger_metacarpal", "circle", radius = 12, color = "green", selections = "metacarpal")
l_fingers_proximal = GUI("l_finger_proximal", "circle", radius = 12, color = "green", selections = "proximal")
l_fingers_middlep = GUI("l_finger_middlep", "circle", radius = 12, color = "green", selections = "middlep")
l_fingers_distal = GUI("l_finger_distal", "circle", radius = 12, color = "green", selections = "distal")
l_fingers_tip = GUI("l_finger_tip", "circle", radius = 12, color = "green", selections = "tip")

l_fingers_thumb.drawMultipleSelectionButton(posX = 355, posY = 390)
l_fingers_index.drawMultipleSelectionButton(posX = 375, posY = 390)
l_fingers_middlef.drawMultipleSelectionButton(posX = 390, posY = 390)
l_fingers_ring.drawMultipleSelectionButton(posX = 405, posY = 390)
l_fingers_pinky.drawMultipleSelectionButton(posX = 420, posY = 390)

l_fingers_metacarpal.drawMultipleSelectionButton(posX = 435, posY = 310)
l_fingers_proximal.drawMultipleSelectionButton(posX = 435, posY = 330)
l_fingers_middlep.drawMultipleSelectionButton(posX = 435, posY = 345)
l_fingers_distal.drawMultipleSelectionButton(posX = 435, posY = 360)
l_fingers_tip.drawMultipleSelectionButton(posX = 435, posY = 376)

l_finger_thumb_metacarpal.drawSelectionButton(posX = 355, posY = 310)
l_finger_thumb_proximal.drawSelectionButton(posX = 355, posY = 330)
l_finger_thumb_distal.drawSelectionButton(posX = 355, posY = 345)
l_finger_thumb_tip.drawSelectionButton(posX = 355, posY = 360)

l_finger_index_metacarpal.drawSelectionButton(posX = 375, posY = 310)
l_finger_index_proximal.drawSelectionButton(posX = 375, posY = 330)
l_finger_index_middlep.drawSelectionButton(posX = 375, posY = 345)
l_finger_index_distal.drawSelectionButton(posX = 375, posY = 360)
l_finger_index_tip.drawSelectionButton(posX = 375, posY = 375)

l_finger_middlef_metacarpal.drawSelectionButton(posX = 390, posY = 310)
l_finger_middlef_proximal.drawSelectionButton(posX = 390, posY = 330)
l_finger_middlef_middlep.drawSelectionButton(posX = 390, posY = 345)
l_finger_middlef_distal.drawSelectionButton(posX = 390, posY = 360)
l_finger_middlef_tip.drawSelectionButton(posX = 390, posY = 375)

l_finger_ring_metacarpal.drawSelectionButton(posX = 405, posY = 310)
l_finger_ring_proximal.drawSelectionButton(posX = 405, posY = 330)
l_finger_ring_middlep.drawSelectionButton(posX = 405, posY = 345)
l_finger_ring_distal.drawSelectionButton(posX = 405, posY = 360)
l_finger_ring_tip.drawSelectionButton(posX = 405, posY = 375)

l_finger_pinky_metacarpal.drawSelectionButton(posX = 420, posY = 310)
l_finger_pinky_proximal.drawSelectionButton(posX = 420, posY = 330)
l_finger_pinky_middlep.drawSelectionButton(posX = 420, posY = 345)
l_finger_pinky_distal.drawSelectionButton(posX = 420, posY = 360)
l_finger_pinky_tip.drawSelectionButton(posX = 420, posY = 375)

window.setFixedWidth(470)
window.setFixedHeight(560)
#print(window.frameGeometry().width())
setNamespace()
window.show()
