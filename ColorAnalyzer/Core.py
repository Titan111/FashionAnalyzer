class Core():
	def __init__(self,frame):
		self.frame = frame
		self.state = "neutral"
		pass
	
	def BtnTop(self,event):
		self.state = "inner"

	def BtnOuter(self,event):
		self.state = "outer"

	def BtnBottom(self,event):
		self.state = "bottom"
	
	def ColorCheck(self,event):
		print(event.X)
		print(event.Y)
		red = self.image.GetRed(event.X,event.Y)
		green = self.image.GetGreen(event.X,event.Y)
		blue = self.image.GetBlue(event.X,event.Y)

		if self.state == "inner":
			self.frame.ctl_panel.inner.SetColor(red,green,blue)

		if self.state == "outer":
			self.frame.ctl_panel.outer.SetColor(red,green,blue)

		if self.state == "bottom":
			self.frame.ctl_panel.bottom.SetColor(red,green,blue)

