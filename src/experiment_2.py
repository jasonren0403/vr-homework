from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *


# 画四个点
def drawFunc():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    # 设置点大小
    glPointSize(5)
    # 只绘制端点
    glBegin(GL_POINTS)
    # 第一个点
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.25, 0.25, 0)
    # 第二个点
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.75, 0.25, 0)
    # 第三个点
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.75, 0.75, 0)
    # 第四个点
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(0.25, 0.75, 0)
    glEnd()
    glFlush()


# 画一条线
def drawLine():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(3)  # 线宽
    glBegin(GL_LINES)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glEnd()
    glFlush()


# 画条带线
def drawStrip():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(3)  # 线宽
    glBegin(GL_LINE_STRIP)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glEnd()
    glFlush()


# 画循环线
def drawLoop():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(3)  # 线宽
    glBegin(GL_LINE_LOOP)
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glEnd()
    glFlush()


# 画独立三角形
def drawPolygon():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # 改变投影矩阵
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)  # 条带三角形——GL_TRIANGLE_STRIP，扇面三角形——GL_TRIANGLE_FAN
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glEnd()
    glFlush()


# 条带三角形和扇面三角形
def drawt():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # 改变投影矩阵
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)  # 条带三角形——GL_TRIANGLE_STRIP，扇面三角形——GL_TRIANGLE_FAN
    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)
    glVertex3f(0.4, 0.4, 0.0)
    glVertex3f(0.6, 0.6, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glEnd()
    glFlush()


# 画六边形
def drawsix():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_LINE)
    glBegin(GL_POLYGON)
    glVertex2f(0.5, -0.1)
    glVertex2f(0.2, -0.3)
    glVertex2f(0.2, -0.6)
    glVertex2f(0.5, -0.8)
    glVertex2f(0.8, -0.6)
    glVertex2f(0.8, -0.3)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow(b"Second")
# glutDisplayFunc(drawFunc)
# glutDisplayFunc(drawLine)
# glutDisplayFunc(drawStrip)
# glutDisplayFunc(drawLoop)
# glutDisplayFunc(drawPolygon)
# glutDisplayFunc(drawt)
glutDisplayFunc(drawsix)
glutMainLoop()
