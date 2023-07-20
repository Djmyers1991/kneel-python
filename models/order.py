class Order():
    """ Creating new Orders!"""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, style_id, size_id, metal_id, time_stamp):
        self.id = id
        self.style_id = style_id
        self.size_id = size_id
        self.metal_id = metal_id
        self.time_stamp = time_stamp
        self.style = None
        self.size = None
        self.metal = None

