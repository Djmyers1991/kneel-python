
""" Here, I am compiling a dictionary of styles"""

STYLES = [
    {
      "id": 1,
      "style": "Classic",
      "price": 500
    },
    {
      "id": 2,
      "style": "Modern",
      "price": 710
    },
    {
      "id": 3,
      "style": "Vintage",
      "price": 965
    }
  ]


def get_all_styles():
    """ Here I am defining a function which will allow me to retrieve these style"""
    return STYLES

def get_single_style(id):
    """ Variable to hold the found animal, if it exists"""
    requested_style = None 

    for style in STYLES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if style["id"] == id:
            requested_style = style

    return requested_style

