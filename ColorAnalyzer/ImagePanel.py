import wx

class ImageDropTarget(wx.FileDropTarget):
	def __init__(self,parent):
		wx.FileDropTarget.__init__(self)
		self.parent = parent

	def OnDropFiles(self,x,y,filename):
		print(filename[0])
		self.parent.core.image = wx.Image(filename[0])
		self.parent.core.bitmap = self.parent.core.image.ConvertToBitmap()
		self.parent.Refresh()
		return 0

class ImagePanel(wx.Panel):
	def __init__(self,parent,core):
		wx.Panel.__init__(self,parent,id=wx.ID_ANY,size=(300,300))
		self.core = core

		self.Bind(wx.EVT_PAINT,self.OnPaint)
		self.Bind(wx.EVT_LEFT_DOWN,self.core.ColorCheck)
		self.core.image = wx.Image("test.png")
		self.core.bitmap = self.core.image.ConvertToBitmap()
		dt = ImageDropTarget(self)
		self.SetDropTarget(dt)

	def OnPaint(self,event=None):
		dc = wx.PaintDC(self)
		dc.Clear()
		dc.SetPen(wx.Pen(wx.BLACK,4))
		dc.DrawBitmap(self.core.bitmap,0,0,True)


