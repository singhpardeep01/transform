import math

def make_translate( x, y, z ):
    matrix = new_matrix()
    ident(matrix)
    matrix[0][3] = x
    matrix[1][3] = y
    matrix[2][3] = z
    return matrix
    pass

def make_scale( x, y, z ):
    matrix = new_matrix()
    ident(matrix)
    matrix[0][0] = x
    matrix[1][1] = y
    matrix[2][2] = z
    return matrix    
    pass

def make_rotX( theta ):
    rad = Math.radians( theta )
    matrix = new_matrix()
    ident(matrix)
    matrix[1][1] = Math.cos( rad )
    matrix[1][2] = -1 * Math.sin( rad )
    matrix[2][1] = Math.sin( rad )
    matrix[2][2] = Math.cos( rad )
    return matrix
    pass

def make_rotY( theta ):    
    rad = Math.radians( theta )
    matrix = new_matrix()
    ident(matrix)
    matrix[1][0] = Math.cos( rad )
    matrix[0][2] = Math.sin( rad )
    matrix[2][0] = -1 * Math.sin( rad )
    matrix[1][2] = Math.cos( rad )
    return matrix
    pass

def make_rotZ( theta ):
    rad = Math.radians( theta )
    matrix = new_matrix()
    ident(matrix)
    matrix[0][0] = Math.cos( rad )
    matrix[0][1] = -1 * Math.sin( rad )
    matrix[1][0] = Math.sin( rad )
    matrix[1][1] = Math.cos( rad )
    return matrix
    pass

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1
    pass

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
