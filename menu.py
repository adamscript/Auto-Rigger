import maya.cmds

# Name of the global variable for the Maya window
MainMayaWindow = language.melGlobals['gMainWindow'] 

# Build a menu and parent underthe Maya Window
customMenu = menu('Custom Menu', parent=MainMayaWindow)
# Build a menu item and parent under the 'customMenu'
menuItem(label="menu item 'hihi'", command="print ('hello from root')", parent=customMenu)

print("hello world")