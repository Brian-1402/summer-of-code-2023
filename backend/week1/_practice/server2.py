import http.server

HandlerClass = http.server.SimpleHTTPRequestHandler

ServerClass = http.server.HTTPServer

Protocol = "HTTP/1.0"

server_address = ("127.0.0.1", 8324)

HandlerClass.protocol_version = Protocol

server_instance = ServerClass(server_address, HandlerClass)

# For gettings logs
sa = server_instance.socket.getsockname()

print(sa)
print(f"serving on link: http://{sa[0]}:{sa[1]}")

server_instance.serve_forever()
