import numpy as np 

def point_match(x:float, y:float, z:float, X2:np.ndarray, Y2:np.ndarray, Z2:np.ndarray, tol:float=1E-6):
    """Checks to see if x,y,z is present in a Face
        x,y,z are the point that you want to match in Face defined using X2,Y2,Z2

    Args:
        x (float): Block 1 face coordinate.  
        y (float): Block 1 face coordinate 
        z (float): Block 1 face coordinate 
        X2 (np.ndarray): X(i,j,k)
        Y2 (np.ndarray): Y(i,j,k)
        Z2 (np.ndarray): Z(i,j,k)

    Returns:
        [np.ndarray]: indicies where match is found.  (-1,-1) if no match found
    """
    location = np.zeros(X2.ndim) - 1 
    dx = x - X2
    dy = y - Y2
    dz = z - Z2
    d = np.sqrt(dx* dx + dy* dy + dz* dz)    
    val = np.amin(d)
    location = np.where(d == val)
        
    if val < tol:
        return [location[0][0], location[1][0]]
    
    return [-1,-1]
    