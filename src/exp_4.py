from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# display-window size
winWidth = 400
winHeight = 300


def init():
    # 设置显示的颜色为蓝色
    glClearColor(0, 0, 1, 1)
    # 三维显示模式
    glMatrixMode(GL_PROJECTION)
    # 二维显示框大小
    gluOrtho2D(0, 200, 0, 150)


def displayFcn():
    # 将颜色显示在屏幕上
    glClear(GL_COLOR_BUFFER_BIT)
    # glColor3f(1,0,0)
    # 设置点的颜色为红色
    # 点的大小
    glPointSize(3)


def winReshapeFcn(newWidth, newHeight):
    glViewport(0, 0, newWidth, newHeight)
    # 三维显示模式
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, newWidth, 0, newHeight)
    winHeight = newHeight
    winWidth = newWidth


def plotPoint(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


def mousePtPlot(button, action, xMouse, yMouse):
    if button == GLUT_LEFT_BUTTON and action == GLUT_DOWN:
        # 绿色的点
        glColor3f(0, 1, 0)
        plotPoint(xMouse, winHeight - yMouse)
        # 强制清空所有缓存来执行OpenGL函数
        glFlush()
    if button == GLUT_RIGHT_BUTTON and action == GLUT_DOWN:
        # 白色的点
        glColor3f(1, 1, 1)
        plotPoint(xMouse, winHeight - yMouse)
        glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE or GLUT_RGB)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(winWidth, winHeight)
    glutCreateWindow('lesson4'.encode())
    init()
    glutDisplayFunc(displayFcn)
    glutReshapeFunc(winReshapeFcn)
    glutMouseFunc(mousePtPlot)
    glutMainLoop()


main()
