from http.server import HTTPServer
from app.server.request_handler import RequestHandler

# Defining a main function to start the server
def main():
    # Defining the port number that the server should listen on
    port = 9000
    
    # Creating a tuple containing the server's address (an empty string means listen on all available network interfaces)
    server_address = ('', port)
    
    # Creating a new HTTPServer instance with the specified server address and request handler
    httpd = HTTPServer(server_address, RequestHandler)
    
    # Printing a message indicating that the server is running
    print('Server running on port', port)
    
    # Starting the server's main event loop
    httpd.serve_forever()

# Running the main function if this module is executed as the main program
if __name__ == '__main__':
    main()
