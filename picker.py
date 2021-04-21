from PySide2.QtWidgets import *
from PySide2.QtGui import *

import math
import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI
from pymel.core import *

import maya.OpenMaya as om

workspace = workspace(q = True, rd = True)
pb = playblast(st = 1, et = 1, fmt = 'image', f = workspace + "testpb",  fp = 0, p = 10, c = 'jpg', qlt = 100, w = 2700, h = 4800, orn = False, v = False)
 
def pointWorldToCam(cameraName, point, res):
    sel = om.MSelectionList()
    dag = om.MDagPath()
 
    sel.add(cameraName)
    sel.getDagPath(0,dag)
 
    cam = om.MFnCamera(dag)
    floatMat = cam.projectionMatrix()
    projMat = om.MMatrix(floatMat.matrix)
    floatMat = cam.postProjectionMatrix()
    postProjMat = om.MMatrix(floatMat.matrix)
    transMat = dag.inclusiveMatrix()
 
    #long form ensures compatibility with MPoint and any iterable
    point = om.MPoint(point[0],point[1],point[2]) 
 
    fullMat =  transMat.inverse() * projMat * postProjMat 
    nuPoint = point * fullMat
    return [(nuPoint[0]/nuPoint[3]/2+0.5)*res[0],
            (1-(nuPoint[1]/nuPoint[3]/2+0.5))*res[1]]

pos = cmds.xform('pSphere1', q=True, t=True, ws=True)
pos2 = cmds.xform('pSphere2', q=True, t=True, ws=True)
pos3 = cmds.xform('pSphere3', q=True, t=True, ws=True) 

#print (pointWorldToCam('camera2', pos3, (270,480)))

window = QWidget()

label = QLabel(window)
pixmap = QPixmap(workspace + 'testpb.1.jpg')
label.setPixmap(pixmap)

button = QPushButton(window)
button.setText("sphere1")
button.setGeometry(pointWorldToCam('camera2', pos, (270,480))[0], pointWorldToCam('camera2', pos, (270,480))[1], 10, 10)
button2 = QPushButton(window)
button2.setText("sphere2")
button2.setGeometry(pointWorldToCam('camera2', pos2, (270,480))[0], pointWorldToCam('camera2', pos2, (270,480))[1], 10, 10)
button3 = QPushButton(window)
button3.setText("sphere3")
button3.setGeometry(pointWorldToCam('camera2', pos3, (270,480))[0], pointWorldToCam('camera2', pos3, (270,480))[1], 10, 10)

#layout = QGridLayout()

#layout.addWidget(button)
#layout.addWidget(button2)

#window.setLayout(layout)
window.setFixedWidth(270)
window.setFixedHeight(480)
window.show()