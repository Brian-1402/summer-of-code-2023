from http.server import SimpleHTTPRequestHandler, HTTPServer


class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # This code will be executed when a GET request is received.

        path = self.path
        if path == "/":
            # This is the root path.
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header("Content-length", len(DUMMY_RESPONSE))
            self.end_headers()
            self.wfile.write(DUMMY_RESPONSE)
        elif path == "/hello":
            # This is the /hello path.
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len("Hello, world!"))
            self.end_headers()
            self.wfile.write("Hello, world!".encode())
        else:
            # This is an unknown path.
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len("Not found"))
            self.end_headers()
            self.wfile.write("Not found".encode())


if __name__ == "__main__":
    httpd = HTTPServer(("localhost", 8000), MyHTTPRequestHandler)
    httpd.serve_forever()
