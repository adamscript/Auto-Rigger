##GUIDES##

group(em = True, n = "guides")

# SPINE #

hips_guide = Guide("hips", (0, 106.85, 2.652), 10)
waist_guide = Guide("waist", (0, 119.473, 5), 10, "hips")
chest_guide = Guide("chest", (0, 131.713, 5), 10, "waist")
sternum_guide = Guide("sternum", (0, 153.569, 1.886), 5, "chest")
l_clavicle_guide = Guide("l_clavicle", (3.107, 152.95, 4.807), 5, "sternum")
r_clavicle_guide = Guide("r_clavicle", (-3.107, 152.95, 4.807), 5, "sternum")

# HEAD #

neck_guide = Guide("neck", (0, 156.891, 1.886), 5, "chest")
head_guide = Guide("head", (0, 170.281, 3.69), 5, "neck")
jaw_guide = Guide("jaw", (0, 170.281, 7.175), 5, "head")
chin_guide = Guide("chin", (0, 163.448, 15.213), 5, "jaw")
l_eye_guide = Guide("l_eye", (3.125, 175.471, 12.969), 1, "head")
r_eye_guide = Guide("r_eye", (-3.125, 175.471, 12.969), 1, "head")

# ARMS #

# FINGERS #
#THUMB#
#INDEX#
#MIDDLE#
#RING#
#PINKY#

# LEGS #

class Guide:

	def __init__(self, name, translate, scale, p = guides):
		self.name = name
		self.translate = translate
		self.scale = scale
		self.parent = parent

	def create(self):
		self.locator = spaceLocator(n = self.name + "_guide", p = self.translate)
		self.locator.scale.set([self.scale, self.scale, self.scale])
		self.locator.parent(self.parent + "_guide")