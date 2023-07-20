import sqlite3
import json
from .size_requests import get_single_size
from .style_requests import get_single_style
from .metal_requests import get_single_metal
from models import Order, Size, Style, Metal

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
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            o.id,
            o.style_id,
            o.size_id,
            o.metal_id,
            o.time_stamp
        FROM orders o
        WHERE o.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        order = Order(data['id'], data['style_id'], 
                      data['size_id'], data['metal_id'], 
                      data['time_stamp'])
        return order.__dict__

   

def get_all_orders():
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            o.id,
            o.size_id,
            o.style_id,
            o.metal_id,
            o.time_stamp,
            m.id metal_id,
            m.metal,
            m.price,
            s.id style_id,
            s.style,
            s.price,
            si.id size_id,
            si.size,
            si.price
        FROM Orders o
        JOIN Metals m, Styles s, Sizes si ON m.id = o.metal_id AND s.id = o.style_id AND si.id = o.size_id
        """)

        orders = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['id'], row['size_id'], row['style_id'], row['metal_id'], row['time_stamp'])
            size = Size(row['id'], row['size'], row ['price'])
            style = Style(row['id'], row['style'], row['price'])
            metal = Metal(row['id'], row['metal'], row['price'])

            order.style = style.__dict__
            order.style.pop('id')


            order.size = size.__dict__
            order.size.pop('id')
           
            order.metal = metal.__dict__
            order.metal.pop('id')
            

            orders.append(order.__dict__)


    return orders


def create_order(new_order):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO Orders 
        (style_id, size_id, metal_id, time_stamp)
        VALUES
            (?, ?, ?, ?)                 
        """, (new_order['style_id'], new_order['size_id'], new_order['metal_id'], new_order['time_stamp']))

        id = db_cursor.lastrowid

        new_order['id'] = id
    return new_order


def delete_order(id):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Orders
            SET
                style_id = ?,
                size_id = ?,
                metal_id = ?,
                time_stamp = ?
      
        WHERE id = ?
        """, (new_order['style_id'], new_order['size_id'],
              new_order['metal_id'], new_order['time_stamp'],
              id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

    
  
    
    