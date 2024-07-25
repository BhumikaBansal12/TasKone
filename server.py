import http.server
import socketserver
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')

httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()

























# from http.server import BaseHTTPRequestHandler, HTTPServer

# class HelloWorldHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         self.wfile.write(b"Hello, World!")

#         def run(server_class = HTTPServer, handler_class=HelloWorldHandler,port=8000):
#             server_address = ('', port)
#             httpd = server_class(server_address,handler_class)
#             print(f"Serving on port {port}")
#             httpd.serve_forever()

#             if __name__ == '__main__':
#                 run()
