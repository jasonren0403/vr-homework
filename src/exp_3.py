# coding=utf-8
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def RenderScene():
    global xRot, yRot
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # Save the matrix state
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    # 绕x轴和y轴旋转(角度,x,y,z)
    glRotatef(xRot, 1.0, 0.0, 0.0)
    glRotatef(yRot, 0.0, 0.0, 1.0)
    # 启用并指定顶点数组
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, corners)
    # Using Drawarrays
    glDrawElements(GL_QUADS, 24, GL_UNSIGNED_BYTE, indexes)
    glPopMatrix()
    # 双缓冲的刷新模式：Swap buffers
    glutSwapBuffers()


# 设置渲染状态
def SetupRC():
    # 背景黑色
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3ub(0, 0, 255);


# 改变窗口大小时调用
def ChangeSize(w, h):
    nRange = 100.0
    # 防止除数为0
    if h == 0:
        h = 1
    # 设置视区大小
    glViewport(0, 0, w, h)
    # 投影矩阵模式
    glMatrixMode(GL_PROJECTION)
    # 矩阵堆栈清空
    glLoadIdentity()

    # 设置裁剪窗口大小
    if w <= h:
        glOrtho(-nRange, nRange, -nRange * h / w, nRange * h / w, -nRange * 2.0, nRange * 2.0)
    else:
        glOrtho(-nRange * w / h, nRange * w / h, -nRange, nRange, -nRange * 2.0, nRange * 2.0)
    # 模型矩阵模式
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def SpecialKey(key,x,y):
    global xRot,yRot
    if key==GLUT_KEY_UP:
        xRot-=5.0
    if key==GLUT_KEY_DOWN:
        xRot+=5.0
    if key==GLUT_KEY_LEFT:
        yRot-=5.0
    if key==GLUT_KEY_RIGHT:
        yRot+=5.0
    if key>356.0:
        xRot=0.0
    if key<-1.0:
        yRot=355.0
    glutPostRedisplay()

# 立方体顶点，front:0,1,2,3 back:4,5,6,7
corners=[[-25.0,25.0,25.0],[25.0,25.0,25.0],[25.0,-25.0,25.0],[-25.0,-25.0,25.0],[-25.0,25.0,-25.0],
         [25.0,25.0,-25.0],[25.0,-25.0,-25.0],[-25.0,-25.0,-25.0]]
# 立方体面 Front,Top,Bottom,Back,Right,Left
indexes=[[0,1,2,3],[4,5,1,0],[3,2,6,7],[5,4,7,6],[1,5,6,2],[4,0,3,7]]
xRot=0.0
yRot=0.0
print("三维立方体，按箭头键改变视角！")
# 使用glut初始化OpenGL
glutInit()
glutInitWindowSize(700,700)
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutCreateWindow(b'lesson 3')
glutReshapeFunc(ChangeSize)
glutSpecialFunc(SpecialKey)
glutDisplayFunc(RenderScene)
SetupRC()
glutMainLoop()
