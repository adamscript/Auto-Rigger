from pymel.core import *

win = window(title="Awan's Auto Rigger")
layout = columnLayout()

#CREATE BUTTONS

guides_btn = button(l = "Create Guides", w = 200, p = layout)
mirrorguides_btn = button(l = "Mirror Guides", w = 200, p = layout)
deleteguides_btn = button(l = "Delete Guides", w = 200, p = layout)
separator()
displayaxes_btn = button(l = "Display Local Rotation Axes", w = 200, p = layout)
separator()
resetpose_btn = button(l = "Reset Pose", w = 200, p = layout)
deleterig_btn = button(l = "Delete Rig", w = 200, p = layout)
separator()
autorig_btn = button(l = "Awto Rig!", w = 200, p = layout)

guides_btn.setCommand(createGuides)
mirrorguides_btn.setCommand(mirrorGuides)
deleterig_btn.setCommand(deleteGuides)
displayaxes_btn.setCommand(displayAxes)
resetpose_btn.setCommand(resetPose)
deleterig_btn.setCommand(deleteRig)
autorig_btn.setCommand(createRig)

win.show();