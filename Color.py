class Color:
	def __init__(self,r,g,b):
		self.R = r
		self.G = g
		self.B = b

class HSV:
	def __init__(self,h,s,v):
		self.H = h
		self.S = s
		self.V = v

def RGB2HSV(r,g,b):
	rgb = [r/255,g/255,b/255]
	
	s = max(rgb)-min(rgb)
	v = max(rgb)
	if min(rgb)==max(rgb):
		h = 0
	else:
		min_color = rgb.index(min(rgb))
		if min_color == 2:
			h = 60*(g-r)/s+60

		if min_color == 0:
			h = 60*(b-g)/s+180

		if min_color == 1:
			h = 60*(r-b)/s+300

	h%=360
	hsv = HSV(h,s,v)
	return hsv
