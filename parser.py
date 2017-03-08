from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a fun
     Any command that requires arguments must have those arguments in the second fun.
     The commands are as follows:
         fun: add a fun to the edge matrix - 
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
	 display: draw the funs of the edge matrix to the screen
	    display the screen
	 save: draw the funs of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open( fname, "r" )
    fun = f.readline()
    fun = fun.strip( "\n" )
    while( fun != "" ):
        if( fun == "line" ):
            fun = f.readline()
            fun = fun.strip( "\n" )
            fun = fun.split(" ")
            add_edge( points, int(fun[0]), int(fun[1]), int(fun[2]), int(fun[3]), int(fun[4]), int(fun[5]) )
        elif( fun == "ident" ):
            ident(transform)
        elif( fun == "scale" ):
            fun = f.readline()
            fun = fun.strip( "\n" )
            fun.split(" ")
            matrix_mult( make_scale( fun[0], fun[1], fun[2] ), transform )
        elif( fun == "translate" ):
            fun = f.readline()
            fun = fun.strip( "\n" )
            fun.split(" ")
            matrix_mult( make_translate( fun[0], fun[1], fun[2] ), transform )
        elif( fun == "rotate" ):
            fun = f.readline()
            fun = fun.strip( "\n" )
            fun.split(" ")
            if( fun[0] == 'x' ):
                matrix_mult( make_rotX( fun[1] ), transform )
            elif( fun[0] == 'y' ):
                matrix_mult( make_rotY( fun[1] ), transform )
            elif( fun[0] == 'z' ):
                matrix_mult( make_rotZ( fun[1] ), transform )
        elif( fun == "apply" ):
            matrix_mult( transform, points )
        elif( fun == "display" ):
            clear_screen( screen )
            draw_lines( points, screen, color )
            display( screen )
        elif( fun == "save" ):
            fun = f.readline()
            fun = fun.strip( "\n" )
            fun.split(" ")
            clear_screen( screen )
            draw_lines( points, screen, color )
            save_extension( screen, fun[0] )
        elif( fun == "quit" ):
            sys.exit
        #print_matrix(transform)
        fun = f.readline()
        fun = fun.strip( "\n" )
    f.close()
    pass
