from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open( fname, "r" )
    line = f.readline()
    while( line != "" ):
        if( line == "line" ):
            line = f.readline()
            line.split(" ")
            add_edge( points, line[0], line[1], line[2], line[3], line[4], line[5] )
        elif( line == "ident" ):
            ident(transform)
        elif( line == "scale" ):
            line = f.readline()
            line.split(" ")
            matrix_mult( transform, make_sscale( line[0], line[1], line[2] ) )
        elif( line == "translate" ):
            line = f.readline()
            line.split(" ")
            matrix_mult( transform, make_translate( line[0], line[1], line[2] ) )
        elif( line == "rotate" ):
            line = f.readline()
            line.split(" ")
            if( line[0] == 'x' ):
                matrix_mult( transform, make_rotX( line[1] ) )
            elif( line[0] == 'y' ):
                matrix_mult( transform, make_rotY( line[1] ) )
            elif( line[0] == 'z' ):
                matrix_mult( transform, make_rotZ( line[1] ) )
        elif( line == "apply" ):
            matrix_mult( transform, points )
        elif( line == "display" ):
            clear_screen( screen )
            draw_lines( points, screen, color )
            display( screen )
        elif( line == "save" ):
            line = f.readline()
            line.split(" ")
            clear_screen( screen )
            draw_lines( points, screen, color )
            save_extension( screen, line[0] )
        elif( line == "quit" ):
            sys.exit
        line = f.readline()
        pass
