import pymel.core as pm

import riggingtoolkit as toolkit
import picker

mainMayaWindow = pm.language.melGlobals['gMainWindow'] 
awtoRigMenu = pm.menu('Awto Rigger', parent = mainMayaWindow)

def opentoolkit(*args):
    toolkit.window.show(dockable = True)
    toolkit.checkGuides()
    toolkit.checkRig()

def openpicker(*args):
    picker.pickerwin.show(dockable = True)
    picker.getNamespace_list()
    picker.setNamespace()

pm.menuItem(label = "Auto Rigging Toolkit", command = opentoolkit, parent = awtoRigMenu)
pm.menuItem(label = "Picker GUI", command = openpicker, parent = awtoRigMenu)
