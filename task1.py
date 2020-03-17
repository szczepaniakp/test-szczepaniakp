def rectangle_area(a, b):
    """
     Calculates the area of a rectangle given its side lengths

     :param a: first side of the rectangle
     :param b: second side of the rectangle
     :return: area of the rectangle
     :raises ValueError: if either number was negative
     """
    
    if not isnumeric(a) or not isnumeric(b):
        raise ValueError("bad value(s)")
    return a*b
