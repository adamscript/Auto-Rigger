from pymel.core import *
import importlib

import riggingtoolkit as toolkit
import picker

toolkit.window.show(dockable = True)
picker.pickerwin.show(dockable = True)

importlib.reload(toolkit)
importlib.reload(picker)

picker.getNamespace_list()
picker.setNamespace()

