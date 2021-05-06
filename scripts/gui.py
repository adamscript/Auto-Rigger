from pymel.core import *
from pymel.core.nodetypes import *

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import*

import math
import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI

import maya.OpenMaya as om
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

#from rig import *

#importlib.reload(guides)
#importlib.reload(gui)

global prognum
prognum = 333

# GUI #

guide_layout = QVBoxLayout()

guidecreate_layout = QHBoxLayout()
guidecreate_layout.setContentsMargins(50, 0, 50, 0)
guideedit_layout = QHBoxLayout()
guideedit_layout.setSpacing(2)

settings_layout = QVBoxLayout()

namespace_layout = QHBoxLayout()
namespace_layout.setSpacing(2)

class Window(MayaQWidgetDockableMixin, QDialog):
    def __init__(self):
        super(Window, self).__init__()
        
        # It is crucial we set a unique object name as this is used internally by Maya
        self.setWindowTitle("Awan's Auto Rigging Toolkit")
        
        self.setMinimumSize(265, 500)
        self.resize(265, 500)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.menubar = QMenuBar(self)
        self.showmenu = self.menubar.addMenu("Show")
        self.showmenu.addAction("Local Rotation Axes")
        self.showmenu.addSeparator()
        self.showmenu.addAction("Picker GUI")
        
        self.addmenu = self.menubar.addMenu("Help")
        self.addmenu.addAction("Help on Awan's Auto Rigging Toolkit")
        self.addmenu.addSeparator()
        self.addmenu.addAction("Buy on Gumroad")
        self.addmenu.addAction("Donate")
        self.addmenu.addSeparator()
        self.addmenu.addAction("Developed with ❤ by awwwan")
        
        self.layout.addWidget(self.menubar)
    
    def addLayout(self, layout):
        self.layout.addLayout(layout)

window = Window()

class ProgressWindow(MayaQWidgetDockableMixin, QDialog):
    def __init__(self):
        super(ProgressWindow, self).__init__()
        self.setFixedWidth(450)
        self.setModal(True)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.headerlayout = QHBoxLayout()
        self.headerlayout.alignment()
        self.layout.addLayout(self.headerlayout)

        self.headerlayout.addStretch()
        self.button = QPushButton()
        self.button.setText("Ok")
        self.button.clicked.connect(self.close)
        self.headerlayout.addWidget(self.button)

        self.textbox = QTextEdit()
        self.textbox.setReadOnly(True)
        self.layout.addWidget(self.textbox)

    def close(self):
        self.textbox.clear()
        self.done(True)

progresswin = ProgressWindow()

class UI():
    def __init__(self, label = ""):
        self.label = label
    
    def drawTextLabel(self):
        self.gui = QLabel()
        self.gui.setText(self.label)
        return self
    
    def drawButton(self, command, height = 25):
        self.gui = QPushButton()
        self.gui.setText(self.label)
        self.gui.setFixedHeight(height)
        self.gui.clicked.connect(command)
        window.layout.addWidget(self.gui)
        return self

    def drawToggleButton(self, command, height = 25):
        self.gui = QPushButton()
        self.gui.setText(self.label)
        self.gui.setCheckable(True)
        self.gui.setFixedHeight(height)
        self.gui.clicked.connect(command)
        window.layout.addWidget(self.gui)
        return self

    def drawCheckBox(self):
        self.gui = QCheckBox()
        self.gui.setText(self.label)
        self.gui.setChecked(True)
        return self

    def drawComboBox(self):
        self.gui = QComboBox(editable = True)
        window.layout.addWidget(self.gui)
        return self

    def addItem(self, item):
        self.gui.addItem(item)

    def setLayout(self, layout):
        layout.addWidget(self.gui)

class FrameLayout(QGroupBox):
    def __init__(self, title='', parent=None):
        super(FrameLayout, self).__init__(title, parent)
         
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 7, 0, 0)
        layout.setSpacing(0)
        super(FrameLayout, self).setLayout(layout)
         
        self.__widget = QFrame(parent)
        self.__widget.setFrameShape(QFrame.Panel)
        self.__widget.setFrameShadow(QFrame.Plain)
        self.__widget.setLineWidth(0)
        layout.addWidget(self.__widget)
         
        self.__collapsed = False
     
    def setLayout(self, layout):
        self.__widget.setLayout(layout)
         
    def expandCollapseRect(self):
        return QRect(0, 0, self.width(), 20)
 
    def mouseReleaseEvent(self, event):
        if self.expandCollapseRect().contains(event.pos()):
            self.toggleCollapsed()
            event.accept()
        else:
            event.ignore()
     
    def toggleCollapsed(self):
        self.setCollapsed(not self.__collapsed)
         
    def setCollapsed(self, state=True):
        self.__collapsed = state
 
        if state:
            self.setMinimumHeight(20)
            self.setMaximumHeight(20)
            self.__widget.setVisible(False)
        else:
            self.setMinimumHeight(0)
            self.setMaximumHeight(1000000)
            self.__widget.setVisible(True)
     
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
         
        font = painter.font()
        font.setBold(True)
        painter.setFont(font)
 
        x = self.rect().x()
        y = self.rect().y()
        w = self.rect().width()
        offset = 25
         
        painter.setRenderHint(painter.Antialiasing)
        painter.fillRect(self.expandCollapseRect(), QColor(93, 93, 93))
        painter.drawText(
            x + offset, y + 3, w, 16,
            Qt.AlignLeft | Qt.AlignTop,
            self.title()
            )
        self.__drawTriangle(painter, x, y)#(1)
        painter.setRenderHint(QPainter.Antialiasing, False)
        painter.end()
         
    def __drawTriangle(self, painter, x, y):#(2)        
        if not self.__collapsed:#(3)
            points = [  QPoint(x+10,  y+6 ),
                        QPoint(x+20, y+6 ),
                        QPoint(x+15, y+11)
                        ]
             
        else:
            points = [  QPoint(x+10, y+4 ),
                        QPoint(x+15, y+9 ),
                        QPoint(x+10, y+14)
                        ]
             
        currentBrush = painter.brush()#(4)
        currentPen   = painter.pen()
         
        painter.setBrush(
            QBrush(
                QColor(187, 187, 187),
                Qt.SolidPattern
                )
            )#(5)
        painter.setPen(QPen(Qt.NoPen))#(6)
        painter.drawPolygon(QPolygon(points))#(7)
        painter.setBrush(currentBrush)#(8)
        painter.setPen(currentPen)

def createGuidesCommand():
    createGuides()

def createGuides(*args):
    progresswin.setWindowTitle("Awan is creating your guides...")
    progresswin.show()
    
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
    l_finger_index_middlep.createGuide()
    l_finger_index_distal.createGuide()
    l_finger_index_tip.createGuide()
    r_finger_index_metacarpal.createGuide()
    r_finger_index_proximal.createGuide()
    r_finger_index_middlep.createGuide()
    r_finger_index_distal.createGuide()
    r_finger_index_tip.createGuide()
    
    l_finger_middlef_metacarpal.createGuide()
    l_finger_middlef_proximal.createGuide()
    l_finger_middlef_middlep.createGuide()
    l_finger_middlef_distal.createGuide()
    l_finger_middlef_tip.createGuide()
    r_finger_middlef_metacarpal.createGuide()
    r_finger_middlef_proximal.createGuide()
    r_finger_middlef_middlep.createGuide()
    r_finger_middlef_distal.createGuide()
    r_finger_middlef_tip.createGuide()
    
    l_finger_ring_metacarpal.createGuide()
    l_finger_ring_proximal.createGuide()
    l_finger_ring_middlep.createGuide()
    l_finger_ring_distal.createGuide()
    l_finger_ring_tip.createGuide()
    r_finger_ring_metacarpal.createGuide()
    r_finger_ring_proximal.createGuide()
    r_finger_ring_middlep.createGuide()
    r_finger_ring_distal.createGuide()
    r_finger_ring_tip.createGuide()
    
    l_finger_pinky_metacarpal.createGuide()
    l_finger_pinky_proximal.createGuide()
    l_finger_pinky_middlep.createGuide()
    l_finger_pinky_distal.createGuide()
    l_finger_pinky_tip.createGuide()
    r_finger_pinky_metacarpal.createGuide()
    r_finger_pinky_proximal.createGuide()
    r_finger_pinky_middlep.createGuide()
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
    
    select(cl = True)

    checkGuides()
    checkRig()
    print("Guides Created!")
    progresswin.textbox.append("Guides Created!")

def mirrorGuides():
    selectedGuide = ls(sl = True, l = True)

    if not selectedGuide:
        om.MGlobal.displayError	("No guide selected!")
    else:
        for x in selectedGuide:
            if (x.startswith("l_")):
                #print(x.partition("l_")[2])
                mirrorpos = xform(x, q = True, t = True, ws = True)
                print(mirrorpos)
                xform("r_" + x.partition("l_")[2], t = (mirrorpos[0]*-1, mirrorpos[1], mirrorpos[2]), ws = True)
                print("r_" + x.partition("l_")[2])
                selectedGuideChildren = listRelatives(x, typ = "locator", ad = True)

                for i in selectedGuideChildren:
                    #print(mirrorchildpos)
                    mirrorchildpos = xform(i.partition("Shape")[0], q = True, t = True, ws = True)
                    print(i.partition("Shape")[0])
                    xform("r_" + (i.partition("Shape")[0]).partition("l_")[2], t = (mirrorchildpos[0]*-1, mirrorchildpos[1], mirrorchildpos[2]), ws = True)
            elif (x.startswith("r_")):
                #print(x.partition("r_")[2])
                mirrorpos = xform(x, q = True, t = True, ws = True)
                print(mirrorpos)
                xform("l_" + x.partition("r_")[2], t = (mirrorpos[0]*-1, mirrorpos[1], mirrorpos[2]), ws = True)
                print("l_" + x.partition("r_")[2])
                selectedGuideChildren = listRelatives(x, typ = "locator", ad = True)

                for i in selectedGuideChildren:
                    mirrorchildpos = xform(i.partition("Shape")[0], q = True, t = True, ws = True)
                    print(i.partition("Shape")[0])
                    xform("l_" + (i.partition("Shape")[0]).partition("r_")[2], t = (mirrorchildpos[0]*-1, mirrorchildpos[1], mirrorchildpos[2]), ws = True)
            else:
                om.MGlobal.displayWarning("Selected guide has no symmetry")
        print("Guides Mirrored!")

def deleteGuides():
    allGuides = ls("guides")
    delete(allGuides)
    global prog
    prog = 1

    checkGuides()
    checkRig()
    print("Guides Deleted!")

def createRig(*args):
    if not ls("*guides", r = True):
        om.MGlobal.displayError("Can't create rig because you deleted the 'guides' object, please return it :(")
        return
    else:
        pass
    
    if not namespace_cmb.gui.currentText():
        om.MGlobal.displayError("Namespace must not be empty! (Try your character's name)")
        return
    else:
        pass
    
    if createpickergui_chkbox.gui.isChecked():
        if not ls(sl = True):
            om.MGlobal.displayError("Select a character model!")
            return
        else:
            pass
    else:
        pass

    if not createpickergui_chkbox.gui.isChecked():
        prognum -= 93
    else:
        pass
    
    progresswin.setWindowTitle("Awan is creating your rig...")
    progresswin.show()
    
    namespace(add = namespace_cmb.gui.currentText(), f = True)

    getSelection()
    
    group(n = namespace_cmb.gui.currentText() + ':rig', em = 	True)
    parent(namespace_cmb.gui.currentText() + ':rig', w = True)
    if createpickergui_chkbox.gui.isChecked():
        createPickerGUI()
    elif not createpickergui_chkbox.gui.isChecked():
        pass

    root_ctrl = MakeNurbCircle(r = 50, n = "root_ctrl")
    root_ctrl.setNormalY(1)
    root_ctrl.setNormalZ(0)
    group('root_ctrl', n = "root_ctrl_offset")
    parent('root_ctrl_offset', namespace_cmb.gui.currentText() + ':rig')
    
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

    group(em = True, n = "ikpole_ctrl_connector_offset")
    parent("ikpole_ctrl_connector_offset", "root_ctrl_offset")
    
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
    l_shoulder.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    l_elbow.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    l_wrist.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_clavicle.createJoint()
    r_shoulder.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_elbow.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_wrist.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    
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
    l_finger_index_middlep.createJoint()
    l_finger_index_distal.createJoint()
    l_finger_index_tip.createJoint()
    r_finger_index_metacarpal.createJoint()
    r_finger_index_proximal.createJoint()
    r_finger_index_middlep.createJoint()
    r_finger_index_distal.createJoint()
    r_finger_index_tip.createJoint()
    
    l_finger_middlef_metacarpal.createJoint()
    l_finger_middlef_proximal.createJoint()
    l_finger_middlef_middlep.createJoint()
    l_finger_middlef_distal.createJoint()
    l_finger_middlef_tip.createJoint()
    r_finger_middlef_metacarpal.createJoint()
    r_finger_middlef_proximal.createJoint()
    r_finger_middlef_middlep.createJoint()
    r_finger_middlef_distal.createJoint()
    r_finger_middlef_tip.createJoint()
    
    l_finger_ring_metacarpal.createJoint()
    l_finger_ring_proximal.createJoint()
    l_finger_ring_middlep.createJoint()
    l_finger_ring_distal.createJoint()
    l_finger_ring_tip.createJoint()
    r_finger_ring_metacarpal.createJoint()
    r_finger_ring_proximal.createJoint()
    r_finger_ring_middlep.createJoint()
    r_finger_ring_distal.createJoint()
    r_finger_ring_tip.createJoint()
    
    l_finger_pinky_metacarpal.createJoint()
    l_finger_pinky_proximal.createJoint()
    l_finger_pinky_middlep.createJoint()
    l_finger_pinky_distal.createJoint()
    l_finger_pinky_tip.createJoint()
    r_finger_pinky_metacarpal.createJoint()
    r_finger_pinky_proximal.createJoint()
    r_finger_pinky_middlep.createJoint()
    r_finger_pinky_distal.createJoint()
    r_finger_pinky_tip.createJoint()

    l_thigh.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    l_knee.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    l_ankle.createJoint(ik = createikctrl_chkbox.gui.isChecked(), rev = True)
    l_foot_ball.createJoint(ik = createikctrl_chkbox.gui.isChecked(), rev = True)
    l_foot_toes.createJoint(ik = createikctrl_chkbox.gui.isChecked(), rev = True)
    l_foot_heel.createJoint(rev = True)
    l_foot_inner.createJoint()
    l_foot_outer.createJoint()
    r_thigh.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_knee.createJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_ankle.createJoint(ik = createikctrl_chkbox.gui.isChecked(), rev = True)
    r_foot_ball.createJoint(ik = createikctrl_chkbox.gui.isChecked(), rev = True)
    r_foot_toes.createJoint(ik = createikctrl_chkbox.gui.isChecked(), rev = True)
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
    l_shoulder.orientJoint(ik = createikctrl_chkbox.gui.isChecked())
    l_elbow.orientJoint(ik = createikctrl_chkbox.gui.isChecked())
    l_wrist.orientJoint(oj = False, ik = createikctrl_chkbox.gui.isChecked())
    r_clavicle.orientJoint()
    r_shoulder.orientJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_elbow.orientJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_wrist.orientJoint(oj = False, ik = createikctrl_chkbox.gui.isChecked())
    
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
    l_finger_index_middlep.orientJoint()
    l_finger_index_distal.orientJoint()
    l_finger_index_tip.orientJoint(oj = False)
    r_finger_index_metacarpal.orientJoint()
    r_finger_index_proximal.orientJoint()
    r_finger_index_middlep.orientJoint()
    r_finger_index_distal.orientJoint()
    r_finger_index_tip.orientJoint(oj = False)
    
    l_finger_middlef_metacarpal.orientJoint()
    l_finger_middlef_proximal.orientJoint()
    l_finger_middlef_middlep.orientJoint()
    l_finger_middlef_distal.orientJoint()
    l_finger_middlef_tip.orientJoint(oj = False)
    r_finger_middlef_metacarpal.orientJoint()
    r_finger_middlef_proximal.orientJoint()
    r_finger_middlef_middlep.orientJoint()
    r_finger_middlef_distal.orientJoint()
    r_finger_middlef_tip.orientJoint(oj = False)
    
    l_finger_ring_metacarpal.orientJoint()
    l_finger_ring_proximal.orientJoint()
    l_finger_ring_middlep.orientJoint()
    l_finger_ring_distal.orientJoint()
    l_finger_ring_tip.orientJoint(oj = False)
    r_finger_ring_metacarpal.orientJoint()
    r_finger_ring_proximal.orientJoint()
    r_finger_ring_middlep.orientJoint()
    r_finger_ring_distal.orientJoint()
    r_finger_ring_tip.orientJoint(oj = False)
    
    l_finger_pinky_metacarpal.orientJoint()
    l_finger_pinky_proximal.orientJoint()
    l_finger_pinky_middlep.orientJoint()
    l_finger_pinky_distal.orientJoint()
    l_finger_pinky_tip.orientJoint(oj = False)
    r_finger_pinky_metacarpal.orientJoint()
    r_finger_pinky_proximal.orientJoint()
    r_finger_pinky_middlep.orientJoint()
    r_finger_pinky_distal.orientJoint()
    r_finger_pinky_tip.orientJoint(oj = False)

    l_thigh.orientJoint(ik = createikctrl_chkbox.gui.isChecked())
    l_knee.orientJoint(ik = createikctrl_chkbox.gui.isChecked())
    l_ankle.orientJoint(oj = False, ik = createikctrl_chkbox.gui.isChecked())
    l_foot_ball.orientJoint()
    l_foot_toes.orientJoint(oj = False)
    #l_foot_heel.orientJoint()
    #l_foot_inner.orientJoint()
    #l_foot_outer.orientJoint()
    r_thigh.orientJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_knee.orientJoint(ik = createikctrl_chkbox.gui.isChecked())
    r_ankle.orientJoint(oj = False, ik = createikctrl_chkbox.gui.isChecked())
    r_foot_ball.orientJoint()
    r_foot_toes.orientJoint(oj = False)
    #r_foot_heel.orientJoint()
    #r_foot_inner.orientJoint()
    #r_foot_outer.orientJoint()

    if createikctrl_chkbox.gui.isChecked():
        #IK FK SYSTEMS
            
        group('l_thigh_ik', 'l_thigh_fk', n =  'l_leg_ik_fk')
        group('l_shoulder_ik', 'l_shoulder_fk', n = 'l_arm_ik_fk')

        group('r_thigh_ik', 'r_thigh_fk', n =  'r_leg_ik_fk')
        group('r_shoulder_ik', 'r_shoulder_fk', n = 'r_arm_ik_fk')

        group('l_leg_ik_fk', 'l_arm_ik_fk', 'r_leg_ik_fk', 'r_arm_ik_fk', n = 'ik_fk_joints')
        parent('ik_fk_joints', 'root_ctrl')
    elif not createikctrl_chkbox.gui.isChecked():
        pass

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
    l_shoulder.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    l_elbow.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    l_wrist.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    r_clavicle.createControl(r = 5)
    r_shoulder.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    r_elbow.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    r_wrist.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())

    if createikctrl_chkbox.gui.isChecked():
        l_arm.createIKControl(sj = 'l_shoulder', ee = 'l_wrist', mj = 'l_elbow')
        r_arm.createIKControl(sj = 'r_shoulder', ee = 'r_wrist', mj = 'r_elbow')
    elif not createikctrl_chkbox.gui.isChecked():
        pass

    l_finger_thumb_metacarpal.createControl(r = 1)
    l_finger_thumb_proximal.createControl()
    l_finger_thumb_distal.createControl()
    l_finger_thumb_tip.createControl()
    r_finger_thumb_metacarpal.createControl(r = 1)
    r_finger_thumb_proximal.createControl()
    r_finger_thumb_distal.createControl()
    r_finger_thumb_tip.createControl()
    
    l_finger_index_metacarpal.createControl(r = 1)
    l_finger_index_proximal.createControl()
    l_finger_index_middlep.createControl()
    l_finger_index_distal.createControl()
    l_finger_index_tip.createControl()
    r_finger_index_metacarpal.createControl(r = 1)
    r_finger_index_proximal.createControl()
    r_finger_index_middlep.createControl()
    r_finger_index_distal.createControl()
    r_finger_index_tip.createControl()
    
    l_finger_middlef_metacarpal.createControl(r = 1)
    l_finger_middlef_proximal.createControl()
    l_finger_middlef_middlep.createControl()
    l_finger_middlef_distal.createControl()
    l_finger_middlef_tip.createControl()
    r_finger_middlef_metacarpal.createControl(r = 1)
    r_finger_middlef_proximal.createControl()
    r_finger_middlef_middlep.createControl()
    r_finger_middlef_distal.createControl()
    r_finger_middlef_tip.createControl()
    
    l_finger_ring_metacarpal.createControl(r = 1)
    l_finger_ring_proximal.createControl()
    l_finger_ring_middlep.createControl()
    l_finger_ring_distal.createControl()
    l_finger_ring_tip.createControl()
    r_finger_ring_metacarpal.createControl(r = 1)
    r_finger_ring_proximal.createControl()
    r_finger_ring_middlep.createControl()
    r_finger_ring_distal.createControl()
    r_finger_ring_tip.createControl()
    
    l_finger_pinky_metacarpal.createControl(r = 1)
    l_finger_pinky_proximal.createControl()
    l_finger_pinky_middlep.createControl()
    l_finger_pinky_distal.createControl()
    l_finger_pinky_tip.createControl()
    r_finger_pinky_metacarpal.createControl(r = 1)
    r_finger_pinky_proximal.createControl()
    r_finger_pinky_middlep.createControl()
    r_finger_pinky_distal.createControl()
    r_finger_pinky_tip.createControl()

    l_thigh.createControl(r = 15, fk = createikctrl_chkbox.gui.isChecked())
    l_knee.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    l_ankle.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    l_foot_ball.createControl(r = 5)
    l_foot_toes.createControl(r = 5)
    #l_foot_heel.createControl()
    #l_foot_inner.createControl()
    #l_foot_outer.createControl()
    r_thigh.createControl(r = 15, fk = createikctrl_chkbox.gui.isChecked())
    r_knee.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    r_ankle.createControl(r = 10, fk = createikctrl_chkbox.gui.isChecked())
    r_foot_ball.createControl(r = 5)
    r_foot_toes.createControl(r = 5)
    #r_foot_heel.createControl()
    #r_foot_inner.createControl()
    #r_foot_outer.createControl()

    if createikctrl_chkbox.gui.isChecked():
        l_leg.createIKControl(sj = 'l_thigh', ee = 'l_ankle', mj = 'l_knee')
        r_leg.createIKControl(sj = 'r_thigh', ee = 'r_ankle', mj = 'r_knee')
    elif not createikctrl_chkbox.gui.isChecked():
        pass

    if createrevctrl_chkbox.gui.isChecked():
        l_foot.createReverseControl(sj = 'l_ankle', ee = 'l_foot_toes', mj = 'l_foot_ball', bj = 'l_foot_heel')
        r_foot.createReverseControl(sj = 'r_ankle', ee = 'r_foot_toes', mj = 'r_foot_ball', bj = 'r_foot_heel')
    elif not createrevctrl_chkbox.gui.isChecked():
        pass
    
    editControlShape()

    parent("l_clavicle_ctrl_offset", 'collarbone_ctrl')
    parent("r_clavicle_ctrl_offset", 'collarbone_ctrl')
    
    if createikctrl_chkbox.gui.isChecked():
        #IK FK SYSTEMS
            
        parentConstraint('hip_ctrl', 'l_leg_ik_fk', mo = True)
        parentConstraint('l_clavicle_ctrl', 'l_arm_ik_fk', mo = True)

        parentConstraint('hip_ctrl', 'r_leg_ik_fk', mo = True)
        parentConstraint('r_clavicle_ctrl', 'r_arm_ik_fk', mo = True)
    elif not createikctrl_chkbox.gui.isChecked():
        pass

    #lock and hide attributes

    offsetAttr = ['tx','ty','tz','rx','ry','rz','sx','sy','sz']
    offsetGroup = ls('*_offset')
    
    for i in offsetGroup:
        for j in offsetAttr:
            setAttr(i + '.' + j, l = True, k = False, cb = False)

    if createikctrl_chkbox.gui.isChecked():
        ikfkswitch = ls('*ikfk_switch_ctrl')
        
        for i in ikfkswitch:
            for j in offsetAttr:
                setAttr(i + '.' + j, l = True, k = False, cb = False)
    elif not createikctrl_chkbox.gui.isChecked():
        pass

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
    setAttr("root_ctrl.overrideColor", 18)

    all_joint = ls(type = 'joint')

    for i in all_joint:
        setAttr(i + ".overrideEnabled", 1)
        setAttr(i + ".overrideColor", 0)

    #Delete All Non Deformer History
    bakePartialHistory(all = True)

    #Hide Guides
    setAttr('guides.visibility', 0)

    if createpickergui_chkbox.gui.isChecked():
        #GUI Data
        addAttr("guiData", ln = "name", type = "string")
        setAttr("guiData.name", namespace_cmb.gui.currentText(), type = "string")

        addAttr("guiData", ln = "isIK", type = "bool")
        setAttr("guiData.isIK", createikctrl_chkbox.gui.isChecked())

        allCtrl = ls("*_ctrl")
        for i in allCtrl:
            addAttr("guiData", ln = i + "_guiDataX")
            addAttr("guiData", ln = i + "_guiDataY")
            setAttr("guiData." + i + "_guiDataX", worldToScreen(xform(i, q = True, t = True, ws = True))[0])
            setAttr("guiData." + i + "_guiDataY", worldToScreen(xform(i, q = True, t = True, ws = True))[1])

            progress_msg = "Creating Picker GUI... (" + progressNum(prognum) + "%) " + i
            print(progress_msg)
            progresswin.textbox.append(progress_msg)
            QApplication.processEvents()

    elif not createpickergui_chkbox.gui.isChecked():
        pass

    #Set Namespace
    rigRelatives = listRelatives(namespace_cmb.gui.currentText() + ':rig', ad = True)
    for x in rigRelatives:
        rename(x, namespace_cmb.gui.currentText() + ":" + x)
    
    switches = ls("*switch")
    for x in switches:
        rename(x, namespace_cmb.gui.currentText() + ":" + x)

    conditions = ls("*condition")
    for x in conditions:
        rename(x, namespace_cmb.gui.currentText() + ":" + x)

    pma = ls("*pma")
    for x in pma:
        rename(x, namespace_cmb.gui.currentText() + ":" + x)

    multi = ls("*multi")
    for x in multi:
        rename(x, namespace_cmb.gui.currentText() + ":" + x)

    namespace_list()

    if createpickergui_chkbox.gui.isChecked():
        #Delete Playblast Camera
        delete("picker_cam1")
    elif not createpickergui_chkbox.gui.isChecked():
        pass

    checkRig()

    print("Rig Created!")
    progresswin.textbox.append("Rig Created!")

def deleteRig(*args):
    if not namespace_cmb.gui.currentText():
        om.MGlobal.displayError("Select an existing Namespace!")
        return
    else:
        pass

    for i in ls("*" + namespace_cmb.gui.currentText() + ":rig", r = True):
        delete(i)
    mel.eval('MLdeleteUnused;')
    namespace(rm = namespace_cmb.gui.currentText())
    namespace_list()

    checkGuides()
    checkRig()
    print("Rig Deleted!")

def checkRig():
    if ls("*" + namespace_cmb.gui.currentText() + ":*rig", r = True):
        mirrorctrl_btn.gui.setEnabled(True)
        deleterig_btn.gui.setEnabled(True)
    else:
        mirrorctrl_btn.gui.setEnabled(False)
        deleterig_btn.gui.setEnabled(False)

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

def mirrorControl(*args):
    selectedControl = ls(sl = True, l = True, r = True)

    if not selectedControl:
        om.MGlobal.displayError	("No control selected!")
    else:
        for x in selectedControl:
            if (x.startswith(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_")):
                
                mirrorpos = xform(x + "Shape.cv[0:8]", q = True, t = True, ws = True)
                
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_" + x.partition("l_")[2] + "Shape.cv[0]", t = (mirrorpos[21]*-1, mirrorpos[22], mirrorpos[23]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_" + x.partition("l_")[2] + "Shape.cv[1]", t = (mirrorpos[18]*-1, mirrorpos[19], mirrorpos[20]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_" + x.partition("l_")[2] + "Shape.cv[2]", t = (mirrorpos[15]*-1, mirrorpos[16], mirrorpos[17]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_" + x.partition("l_")[2] + "Shape.cv[3]", t = (mirrorpos[12]*-1, mirrorpos[13], mirrorpos[14]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_" + x.partition("l_")[2] + "Shape.cv[4]", t = (mirrorpos[9]*-1, mirrorpos[10], mirrorpos[11]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_" + x.partition("l_")[2] + "Shape.cv[5]", t = (mirrorpos[6]*-1, mirrorpos[7], mirrorpos[8]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_" + x.partition("l_")[2] + "Shape.cv[6]", t = (mirrorpos[3]*-1, mirrorpos[4], mirrorpos[5]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_" + x.partition("l_")[2] + "Shape.cv[7]", t = (mirrorpos[0]*-1, mirrorpos[1], mirrorpos[2]), ws = True)
                
                print("Control mirrored!")
            elif (x.startswith(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":r_")):
                
                mirrorpos = xform(x + "Shape.cv[0:8]", q = True, t = True, ws = True)
                
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_" + x.partition("r_")[2] + "Shape.cv[0]", t = (mirrorpos[21]*-1, mirrorpos[22], mirrorpos[23]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_" + x.partition("r_")[2] + "Shape.cv[1]", t = (mirrorpos[18]*-1, mirrorpos[19], mirrorpos[20]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_" + x.partition("r_")[2] + "Shape.cv[2]", t = (mirrorpos[15]*-1, mirrorpos[16], mirrorpos[17]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_" + x.partition("r_")[2] + "Shape.cv[3]", t = (mirrorpos[12]*-1, mirrorpos[13], mirrorpos[14]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_" + x.partition("r_")[2] + "Shape.cv[4]", t = (mirrorpos[9]*-1, mirrorpos[10], mirrorpos[11]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_" + x.partition("r_")[2] + "Shape.cv[5]", t = (mirrorpos[6]*-1, mirrorpos[7], mirrorpos[8]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_" + x.partition("r_")[2] + "Shape.cv[6]", t = (mirrorpos[3]*-1, mirrorpos[4], mirrorpos[5]), ws = True)
                xform(x.partition(namespace_cmb.gui.currentText())[0] + namespace_cmb.gui.currentText() + ":l_" + x.partition("r_")[2] + "Shape.cv[7]", t = (mirrorpos[0]*-1, mirrorpos[1], mirrorpos[2]), ws = True)
                
                print("Control mirrored!")
            else:
                om.MGlobal.displayWarning("Selected control has no symmetry")

def componentMode(*args):
    if componentmode_btn.gui.isChecked():
        selectMode(co = True)
        selectType(alc = True)
        print("Control editing on!")
    else:
        selectMode(o = True)
        print("Control editing off")
    
def displayAxes(*args):
    selectedJoints = ls(type = 'joint', sl = True)

    if not selectedJoints:
        allJoints = ls(type = 'joint')
        switch(allJoints, la = True)
    else:
        switch(selectedJoints, la = True)
        print("Axes Displayed!")

def createPickerGUI():
    #setAttr('guides.visibility', 0)
    picker_cam = Camera(n = "picker_cam")
    #picker_cam.rename("picker_cam")
    picker_cam.setOrtho(orthoState = True)
    bb = xform(charmodel, q = True, bb = True, ws = True)
    viewFit("picker_cam1")
    setAttr('picker_camShape1.orthographicWidth', (max(bb)*105)/100)
    
    lookThru("picker_cam1")
    pb = playblast(st = 1, et = 1, fmt = 'image', f = workspace(q = True, rd = True) + "images/" + namespace_cmb.gui.currentText() + "_pb",  fp = 0, p = 10, c = 'jpg', qlt = 100, w = 450 * 10, h = 480 * 10, orn = False, v = False)

    group(em = True, n = "guiData")
    parent("guiData", namespace_cmb.gui.currentText() + ':rig')

def progressNum(max):
    global prog
    prog+=1
    return str(int((prog/max)*100))

def worldToScreen(point):
    defaultAspectRatio = getAttr('defaultResolution.deviceAspectRatio')

    setAttr('defaultResolution.deviceAspectRatio', 0.8393)

    sel = om.MSelectionList()
    dag = om.MDagPath()

    sel.add("picker_cam1")
    sel.getDagPath(0,dag)

    cam = om.MFnCamera(dag)
    floatMat = cam.projectionMatrix()
    projMat = om.MMatrix(floatMat.matrix)
    floatMat = cam.postProjectionMatrix()
    postProjMat = om.MMatrix(floatMat.matrix)
    transMat = dag.inclusiveMatrix()

    point = om.MPoint(point[0], point[1], point[2]) 

    fullMat =  transMat.inverse() * projMat * postProjMat 
    nuPoint = point * fullMat
    screenPoint = [(nuPoint[0]/nuPoint[3]/2+0.5)*470, (1-(nuPoint[1]/nuPoint[3]/2+0.5))*560]

    setAttr('defaultResolution.deviceAspectRatio', defaultAspectRatio)

    return screenPoint

def checkGuides():
    if ls("*guides", r = True):
        guides_btn.gui.setEnabled(False)
        mirrorguides_btn.gui.setEnabled(True)
        deleteguides_btn.gui.setEnabled(True)
        autorig_btn.gui.setEnabled(True)
    else:
        guides_btn.gui.setEnabled(True)
        mirrorguides_btn.gui.setEnabled(False)
        deleteguides_btn.gui.setEnabled(False)
        autorig_btn.gui.setEnabled(False)

def getSelection():
    global charmodel
    charmodel = ls(sl = True)

#BUTTONS

guides_btn = UI(label = "Create Guides")

mirrorguides_btn = UI(label = "Mirror Guides")
deleteguides_btn = UI(label = "Delete Guides")

settings_frame = FrameLayout("Settings", window)

deleterig_btn = UI(label = "Delete Rig")

componentmode_btn = UI(label = "Component Mode")
mirrorctrl_btn = UI(label = "Mirror Control Shape")

namespace_cmb = UI()
namespace_lbl = UI(label = "Namespace :")

createikctrl_chkbox = UI(label = "Create IK Control")
createrevctrl_chkbox = UI(label = "Create Reverse Foot Control")
createpickergui_chkbox = UI(label = "Create Picker GUI")

autorig_btn = UI(label = "Awto Rig!")

guides_btn.drawButton(createGuidesCommand).setLayout(guidecreate_layout)

window.addLayout(guide_layout)
guide_layout.addLayout(guidecreate_layout)
guide_layout.addLayout(guideedit_layout)
mirrorguides_btn.drawButton(mirrorGuides).setLayout(guideedit_layout)
deleteguides_btn.drawButton(deleteGuides).setLayout(guideedit_layout)

autorig_btn.drawButton(createRig, height = 50)

window.layout.addWidget(settings_frame)
settings_frame.setLayout(settings_layout)
settings_layout.addLayout(namespace_layout)

window.addLayout(namespace_layout)
namespace_lbl.drawTextLabel().setLayout(namespace_layout)
namespace_cmb.drawComboBox().setLayout(namespace_layout)

createikctrl_chkbox.drawCheckBox().setLayout(settings_layout)
createrevctrl_chkbox.drawCheckBox().setLayout(settings_layout)
createpickergui_chkbox.drawCheckBox().setLayout(settings_layout)

def ikrevchkbox():
    if createikctrl_chkbox.gui.isChecked():
        createrevctrl_chkbox.gui.setChecked(True)
        createrevctrl_chkbox.gui.setEnabled(True)
    elif not createikctrl_chkbox.gui.isChecked():
        createrevctrl_chkbox.gui.setChecked(False)
        createrevctrl_chkbox.gui.setEnabled(False)

createikctrl_chkbox.gui.clicked.connect(ikrevchkbox)

componentmode_btn.drawToggleButton(componentMode).setLayout(settings_layout)
mirrorctrl_btn.drawButton(mirrorControl).setLayout(settings_layout)

deleterig_btn.drawButton(deleteRig).setLayout(settings_layout)

window.layout.addStretch()

checkGuides()
checkRig()

def namespace_list():
    namespace_cmb.gui.clear()
    nsinfo = namespaceInfo(lon = True, r = True)
    for i in nsinfo:
        if(i != "UI" and i != "shared"):
            namespace_cmb.gui.addItem(i)
        else:
            pass

namespace_list()