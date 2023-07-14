from .size_requests import get_single_size
from .style_requests import get_single_style
from .metal_requests import get_single_metal

ORDERS = [
    {
        "id": 1,
        "style_id": 2,
        "size_id": 2,
        "metal_id": 2,
        "time_stamp": "January 7th"

    },
     {
        "id": 2,
        "style_id": 1,
        "size_id": 1,
        "metal_id": 1,
        "time_stamp": "December 7th"

    }
]

def get_single_order(id):
    """ Variable to hold the found animal, if it exists"""
    requested_order = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order
            matching_size = get_single_size(requested_order["size_id"])
            requested_order ["size"] = matching_size
            matching_style = get_single_style(requested_order["style_id"])
            requested_order ["style"] = matching_style
            matching_metal = get_single_metal(requested_order["metal_id"])
            requested_order["metal"] = matching_metal
            del order["style_id"]
            del order["metal_id"]
            del order["size_id"]

    return requested_order

def get_all_orders():
    return ORDERS

def create_order(order):
    max_id = ORDERS[-1]["id"]
    correct_id = max_id + 1
    order["id"] = correct_id
    ORDERS.append(order)

    return order

def delete_order(id):
    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id: 
            order_index = index
        if order_index >= 0:
            ORDERS.pop(order_index)

def update_order(id, new_order):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Update the value.
            ORDERS[index] = new_order
            break