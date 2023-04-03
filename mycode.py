def power(x, y): 
    """Multiplies value x by itself y number of times.

    Args:
        x (num): any numeric object
        y (int): any positive integer
    """
    v = x # v is return value
    for i in range(y): 
        v = v * x # multiply each time
    return(v) # return our calculation
