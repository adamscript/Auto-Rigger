from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import*

import math
import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI

import maya.OpenMaya as om
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from guides import *
from rig import *

#importlib.reload(guides)
#importlib.reload(gui)

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

#if __name__ == "__main__":
window = Window()
window.show(dockable=True)

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

guides_btn.drawButton(createGuides).setLayout(guidecreate_layout)

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