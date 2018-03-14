import math
import wx
import Color
import Plot

class ColorBoxes():
	def __init__(self,parent,name):
		self.boxes = []
		for i in range(3):
			self.boxes.append(wx.TextCtrl(parent,wx.ID_ANY,size=(100,30)))
		self.button = wx.Button(parent,wx.ID_ANY,"check")

		self.box = wx.StaticBox(parent,wx.ID_ANY,name)
		self.sizer = wx.StaticBoxSizer(self.box,wx.HORIZONTAL)
		for i in range(3):
			self.sizer.Add(self.boxes[i])
		self.sizer.Add(self.button)

	def SetColor(self,r,g,b):
		self.hsv = Color.RGB2HSV(r,g,b)
		self.boxes[0].SetValue(str( round(100*self.hsv.H)/100 ))
		self.boxes[1].SetValue(str( round(100*self.hsv.S)/100 ))
		self.boxes[2].SetValue(str( round(100*self.hsv.V)/100 ))

class ControlPanel(wx.Panel):
	def __init__(self,parent,core):
		self.core = core

		wx.Panel.__init__(self,parent,id=wx.ID_ANY,size=(400,300))
		
		self.outer = ColorBoxes(self,"outer")
		self.inner = ColorBoxes(self,"inner")
		self.bottom = ColorBoxes(self,"bottom")

		self.outer.button.Bind(wx.EVT_BUTTON,self.core.BtnOuter)
		self.inner.button.Bind(wx.EVT_BUTTON,self.core.BtnTop)
		self.bottom.button.Bind(wx.EVT_BUTTON,self.core.BtnBottom)

		self.plot_btn = wx.Button(self,wx.ID_ANY,"plot")
		self.plot_btn.Bind(wx.EVT_BUTTON,self.plot)

		layout = wx.BoxSizer(wx.VERTICAL)
		layout.Add(self.outer.sizer)
		layout.Add(self.inner.sizer)
		layout.Add(self.bottom.sizer)
		layout.Add(self.plot_btn)
		self.SetSizer(layout)

	def plot(self,event):
		plot_window = Plot.Plot(
			self.outer.hsv,self.inner.hsv,self.bottom.hsv
		)
		plot_window.plot()
