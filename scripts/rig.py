group(em = True, n = "guides")

# SPINE #

hips_guide = Rig("hips", t = (0, 106.85, 2.652), 10)
waist_guide = Rig("waist", t = (0, 119.473, 5), 10, p = "hips")
chest_guide = Rig("chest", t = (0, 131.713, 5), 10, p = "waist")
sternum_guide = Rig("sternum", t = (0, 153.569, 1.886), 5, p = "chest")
l_clavicle_guide = Rig("l_clavicle", t = (3.107, 152.95, 4.807), 5, p = "sternum")
r_clavicle_guide = Rig("r_clavicle", t = (-3.107, 152.95, 4.807), 5, p = "sternum")

# HEAD #

neck_guide = Rig("neck", (0, 156.891, 1.886), 5, "chest")
head_guide = Rig("head", (0, 170.281, 3.69), 5, "neck")
jaw_guide = Rig("jaw", (0, 170.281, 7.175), 5, "head")
chin_guide = Rig("chin", (0, 163.448, 15.213), 5, "jaw")
l_eye_guide = Rig("l_eye", (3.125, 175.471, 12.969), 1, "head")
r_eye_guide = Rig("r_eye", (-3.125, 175.471, 12.969), 1, "head")

# ARMS #

# FINGERS #
#THUMB#
#INDEX#
#MIDDLE#
#RING#
#PINKY#

# LEGS #

class Rig:

	def __init__(self, name, t = (0, 0, 0), p = guides):
		self.name = name
		self.translate = translate
		self.parent = parent

	def create(self, s = 5):
		self.locator = spaceLocator(n = self.name + "_guide", p = self.translate)
		self.locator.scale.set([s, s, s])
		self.locator.parent(self.parent + "_guide")