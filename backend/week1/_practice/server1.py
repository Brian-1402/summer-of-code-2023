import http.server
import socketserver

PORT = 9043

handler = http.server.SimpleHTTPRequestHandler

http = socketserver.TCPServer(("", PORT), handler)

print("serving at port", PORT)
http.serve_forever()
