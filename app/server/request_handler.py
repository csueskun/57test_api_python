from http.server import BaseHTTPRequestHandler
from .http_response import send_response
from .routes import routes
from urllib.parse import parse_qs
from cgi import parse_header, parse_multipart
import re

# Defining a RequestHandler class that extends BaseHTTPRequestHandler
class RequestHandler(BaseHTTPRequestHandler):
    
    # Defining a method to handle GET requests
    def do_GET(self):
        self.handle_request('GET')

    # Defining a method to handle POST requests
    def do_POST(self):
        self.handle_request('POST')
    
    # Defining a method to handle all requests
    def handle_request(self, method):
        
        # Iterating over the routes
        for route in routes:
            
            # Compiling the regular expression 
            # pattern defined in the route
            pattern = re.compile(route['path'])
            
            # Matching the regular expression 
            # pattern against the requested path
            match = pattern.match(self.path)
            
            # Checking if the pattern matches and 
            # the method is allowed for this route
            if match and method in route['methods']:
                
                # Extracting parameters from the matched pattern
                params = match.groupdict()
                
                # Calling the route's handler function with parameters
                response = route['handler'](self, params)
                
                # Sending the response back to the client
                send_response(self, *response)
                
                # Exiting the loop after handling the request
                return
        
        # If no matching route is found, sending a 404 error response
        send_response(self, 404)

    def get_post_data(self):
        try:
            content_len = int(self.headers.get('Content-Length'))
            data = self.rfile.read(content_len)
            data = data.decode()
            result = parse_qs(data, strict_parsing=True)
            for key in result:
                if len(result[key]) == 1:
                    result[key] = result[key][0]
            return result
        except: return {}