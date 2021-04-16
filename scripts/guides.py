class Guide:

	def __init__(self, name, translate, scale, parent):
		self.name = name
		self.translate = translate
		self.scale = scale
		self.parent = parent

	def create(self):
		self.locator = spaceLocator(n = self.name, p = self.translate)
		self.locator.scale.set([self.scale, self.scale, self.scale])
		self.locator.parent(self.parent)

group(em = True, n = "guides")

# SPINE #

hips_guide = Guide("hips_guide", (0, 106.85, 2.652), 10, "guides")
waist_guide = Guide("waist_guide", (0, 119.473, 5), 10, "hips_guide")
chest_guide = Guide("chest_guide", (0, 131.713, 5), 10, "waist_guide")
sternum_guide = Guide("sternum_guide", (0, 153.569, 1.886), 5, "chest_guide")
l_clavicle_guide = Guide("l_clavicle_guide", (3.107, 152.95, 4.807), 5, "sternum_guide")
r_clavicle_guide = Guide("r_clavicle_guide", (-3.107, 152.95, 4.807), 5, "sternum_guide")

# HEAD #

neck_guide = Guide("neck_guide", (0, 156.891, 1.886), 5, "chest_guide")
head_guide = Guide("head_guide", (0, 170.281, 3.69), 5, "neck_guide")
jaw_guide = Guide("jaw_guide", (0, 170.281, 7.175), 5, "head_guide")
chin_guide = Guide("chin_guide", (0, 163.448, 15.213), 5, "jaw_guide")
l_eye_guide = Guide("l_eye_guide", (3.125, 175.471, 12.969), 1, "head_guide")
r_eye_guide = Guide("r_eye_guide", (-3.125, 175.471, 12.969), 1, "head_guide")
