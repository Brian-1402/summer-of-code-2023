import http.server
import os


def find_absolute_path(relative_pos):
    return os.path.join(os.path.dirname(__file__), relative_pos)


class HandlerClass(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            f = open(
                find_absolute_path("sample.html"),
                "r",
            )
            text = f.read()
            self.send_header("Content-length", len(text))
            self.end_headers()
            self.wfile.write(text.encode())
            f.close()
        else:
            # This is an unknown path.
            message = "404 Not found"
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(message))
            self.end_headers()
            self.wfile.write(message.encode())


ServerClass = http.server.HTTPServer

Protocol = "HTTP/1"

server_address = ("127.0.0.1", 8324)

HandlerClass.protocol_version = Protocol

server_instance = ServerClass(server_address, HandlerClass)

# For gettings logs
sa = server_instance.socket.getsockname()

print(sa)
print(f"serving on link: http://{sa[0]}:{sa[1]}")

server_instance.serve_forever()
