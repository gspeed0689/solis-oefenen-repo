def power(x, y): 
    """Multiplies value x by itself y number of times.

    Args:
        x (num): any numeric object
        y (num): any positive numeric integer
    """
    if y <= 0:
        raise ValueError("y cannot be a negative number")
    
    v = x ** y # v is return value

    return(v) # return our calculation