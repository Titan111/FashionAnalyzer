#!/usr/bin/python3
# -*- coding: utf-8 -*-
import wx
import ImagePanel
import ControlPanel
import Core

class MyApp(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,"Fashion Analyzer",size=(700,300))

		self.core = Core.Core(self)

		self.img_panel = ImagePanel.ImagePanel(self,self.core)
		self.img_panel.SetBackgroundColour("#888888")
		self.ctl_panel = ControlPanel.ControlPanel(self,self.core)
		layout = wx.BoxSizer(wx.HORIZONTAL)
		layout.Add(self.img_panel)
		layout.Add(self.ctl_panel)
		self.SetSizer(layout)

if __name__ == "__main__":
	app = wx.App(False)
	frame = MyApp(None,wx.ID_ANY)
	frame.Show(True)
	app.MainLoop()
