import sys
print(sys.path)#if you are seeing this it's becasue I forgot to remove it
import OpenGL

#OpenGL.ERROR_CHECKING = False
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


'''
Importing * from libraries is very unpythonic and should not be done.
A proper refactor would instead import the libraries correctly or would
import each necessary function/variable individually (not a good idea).
For the purpose of this code we are breaking those rules
'''


class GLHandler():
    def __init__(self):
        self.INIT_WINDOW_SIZE = 400
        self.WINDOW_TITLE = "My_Title"
        self.BACKCOLOR = [ 0.0, 0.0, 0.0, 1.0]
        self.DebugOn = 1                #default = 0
        self.Xmouse = self.Ymouse = 0   #known cursor loc. Default should be 0.

        self.InitGraphics()



        print(GLUT_LEFT_BUTTON, GLUT_MIDDLE_BUTTON, GLUT_RIGHT_BUTTON)
        return

    def InitGraphics(self):
        #displaymodes
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        #Window init size and location
        glutInitWindowPosition(0, 0);
        glutInitWindowSize(self.INIT_WINDOW_SIZE, self.INIT_WINDOW_SIZE)

        self.MainWindow = glutCreateWindow(self.WINDOW_TITLE)
        glutSetWindowTitle(self.WINDOW_TITLE)
        glClearColor(*self.BACKCOLOR)#python unpack list into individual args
        
        #callback funcs
        glutSetWindow( self.MainWindow );
        glutDisplayFunc( self.Display );
        glutReshapeFunc( self.Resize );
        glutKeyboardFunc( self.Keyboard );
        glutMouseFunc( self.MouseButton );
        glutMotionFunc( self.MouseMotion );
        glutPassiveMotionFunc( None );
        glutVisibilityFunc( self.Visibility );
        glutEntryFunc( None );
        glutSpecialFunc( None );
        glutSpaceballMotionFunc( None );
        glutSpaceballRotateFunc( None );
        glutSpaceballButtonFunc( None );
        glutButtonBoxFunc( None );
        glutDialsFunc( None );
        glutTabletMotionFunc( None );
        glutTabletButtonFunc( None );
        glutMenuStateFunc( None );
        #glutTimerFunc( -1, None, 0 );
        glutIdleFunc( None );

    def Display(self):
        return

    def Resize(self, width, height ):
        if self.DebugOn:
            print("ReSize: {}, {}".format(width,height), file=sys.stderr)
        glutSetWindow( self.MainWindow )
        glutPostRedisplay( )
        #MJB says: Don't do anything since `Display( )` does it for us!
        return

    def Keyboard(self):
        return
    
    def MouseButton(self, button, state, x, y):
        if self.DebugOn:
            print("MouseButton: {}, {}, {}, {}".format(button, state, x, y) )


        if state == GLUT_DOWN:
            self.Xmouse = x
            self.Ymouse = y
            #self.ActiveButton |= b
        #else:
            #ActiveButton &= ~b

        return
    
    
    def MouseMotion(self, x, y):
    
        #finish MouseButton and object variables first
        
        return

    def Visibility(self, state):
    #int state, can be used to optimize by not drawing when occluded
        if self.DebugOn:
            print("Visibility: {}".format(state), file=sys.stderr)
        #GLUT_VISIBLE is a library constint object equivalent to 1
        if( state == GLUT_VISIBLE):
            glutSetWindow( self.MainWindow )
            glutPostRedisplay( )
        else:
            pass
            #this is where occlusion code can go

        return



def main():
    glutInit(sys.argv)
    #glutInitWindowPosition
    hand = GLHandler()


    #glShadeModel(GL_SMOOTH)
    #glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0,0.,0.,1.]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    glutSolidSphere(2,20,20)
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
