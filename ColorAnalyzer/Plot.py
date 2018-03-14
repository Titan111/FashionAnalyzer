import math
import Color
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Coord:
	def __init__(self,x,y,z):
		self.X=x
		self.Y=y
		self.Z=z

class Plot:
	def __init__(self,outer,inner,bottom):
		colors = [outer,inner,bottom]
		self.coords = []
		for i in colors:
			rad = i.H*math.pi/180
			x = math.cos(rad)*i.S*2
			z = math.sin(rad)*i.S*2
			y = (i.V-1)*3
			self.coords.append(Coord(x,y,z))

	def plot(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
		glutInitWindowSize(500, 500) # window size
		glutInitWindowPosition(100, 100) # window position
		glutCreateWindow("HSV") # show window
		glutDisplayFunc(self.display)# draw callback function
		glutReshapeFunc(self.reshape)# resize callback function
		self.init(500, 500)
		glutMainLoop()

	def init(self,width, height):
		""" initialize """
		glClearColor(0.0, 0.0, 0.0, 1.0)
		glEnable(GL_DEPTH_TEST) # enable shading

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		##set perspective
		gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

	def display(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluLookAt(0.0, 5.0, 3.0, 0.0, -2.5, 0.0, 0.0, 1.0, 0.0)
		glColor3f(1.0, 1.0, 1.0)
		glRotated(0.0, 0.0, 1.0, 0.0)
		glutWireCone(2.0,3.0,10,10)

		glColor3f(1.0, 0.0, 0.0)

		for i in self.coords:
			glTranslated( i.X,  i.Y,  i.Z)
			glutSolidSphere(0.1,50,50)
			glTranslated(-i.X, -i.Y, -i.Z)

		glBegin(GL_LINE_STRIP)
		for i in self.coords:
			glVertex3d( i.X,  i.Y,  i.Z)
		glEnd()

		glFlush()  # enforce OpenGL command

	def reshape(self,width, height):
		"""callback function resize window"""
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
