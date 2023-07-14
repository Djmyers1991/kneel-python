import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_single_metal
from views import get_all_styles, get_single_style
from views import get_all_orders, create_order, delete_order, update_order, get_single_order
from views import get_all_sizes, get_single_size



class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None
        #try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple
    
    def do_GET(self):
        """Handles GET requests to the server """
        response = {}
        (resource, id) = self.parse_url(self.path)

        if resource == "orders":
            if id is not None:
                response = get_single_order(id)
                if response is not None:
                    self._set_headers(200)
                else: 
                    self._set_headers(404)
                    response = {"message": f"That order {id} was never placed ... or cancelled. THE CODE IS FINE, DAMN IT!!" } 
            else:
                self._set_headers(200)
                response = get_all_orders()
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = {"message": f"Style {id} don't exist. You a loser."}
            else: 
                self._set_headers(200)
                response = get_all_styles()
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = {"message": f"Size {id} is a figment of your pitiful imagination."}
            else:
                self._set_headers(200)
                response = get_all_sizes()

        elif resource == "metals":
            if id is not None:
                response = get_single_metal(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = {"message": f"Metal {id} is like Brad Pitt in fight club. He don't exist."}


            else:
                self._set_headers(200)
                response = get_all_metals()
        else:
            response = []

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """
        
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
       
        # (resource, id) = self.parse_url(self.path)
        response = {}
        (resource, id) = self.parse_url(self.path)

        new_order = None
        
        if resource == "orders":
            if "metal_id" not in post_body:
                self._set_headers(405)
                response = {"message": "Bruh, where's your mettle?"}
                self.wfile.write(json.dumps(response).encode())
            elif "style_id" not in post_body:
                self._set_headers(405)
                response = {"message": "Bruh, get a sense of style."}
                self.wfile.write(json.dumps(response).encode())
            elif "size_id" not in post_body:
                self._set_headers(405)
                response = {"message": "Bruh, the size is what counts."}
                self.wfile.write(json.dumps(response).encode())   
            else:
                self._set_headers(201)
                new_order = create_order(post_body)
                self.wfile.write(json.dumps(new_order).encode())


    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "orders":
            update_order(id, post_body)
            self.wfile.write("".encode())


    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    def do_DELETE(self):
    # Set a 204 response code
        self._set_headers(204)

        (resource, id) = self.parse_url(self.path)
        if resource == "orders":
            delete_order(id)
            self.wfile.write("".encode())

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()



# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
