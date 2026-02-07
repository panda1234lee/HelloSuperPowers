def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("All inputs must be numbers (int or float).")
    return a + b
