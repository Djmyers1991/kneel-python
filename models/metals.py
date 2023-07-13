class Metal():
    """ Creating new metals!"""
    # Class initializer. It has 3 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, metal, price):
        self.id = id
        self.metal = metal
        self.price = price
       
        new_metal = Metal(6, "9000K Gold", "10494454.5")