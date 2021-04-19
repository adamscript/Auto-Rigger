group(em = True, n = "guides")

# SPINE #

hips = Rig("hips", t = (0, 106.85, 2.652), 10)
waist = Rig("waist", t = (0, 119.473, 5), 10, p = "hips")
chest = Rig("chest", t = (0, 131.713, 5), 10, p = "waist")
sternum = Rig("sternum", t = (0, 153.569, 1.886), 5, p = "chest")
l_clavicle = Rig("l_clavicle", t = (3.107, 152.95, 4.807), 5, p = "sternum")
r_clavicle = Rig("r_clavicle", t = (-3.107, 152.95, 4.807), 5, p = "sternum")

# HEAD #

neck = Rig("neck", (0, 156.891, 1.886), 5, "chest")
head = Rig("head", (0, 170.281, 3.69), 5, "neck")
jaw = Rig("jaw", (0, 170.281, 7.175), 5, "head")
chin = Rig("chin", (0, 163.448, 15.213), 5, "jaw")
l_eye = Rig("l_eye", (3.125, 175.471, 12.969), 1, "head")
r_eye = Rig("r_eye", (-3.125, 175.471, 12.969), 1, "head")

# ARMS #

# FINGERS #
#THUMB#
#INDEX#
#MIDDLE#
#RING#
#PINKY#

# LEGS #

class Rig:

	def __init__(self, name, t = (0, 0, 0)):
		self.name = name
		self.translate = translate
		self.parent = parent

	def createGuide(self, s = 5, p = "guides"):
		self.locator = spaceLocator(n = self.name + "_guide", p = self.translate)
		self.locator.scale.set([s, s, s])
		self.locator.parent(self.parent + "_guide")