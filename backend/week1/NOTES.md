# Learning about web servers:

- [What is a web server? | MDN web docs](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_web_server)

- [Network Programming Python – HTTP Server | GeeksForGeeks](https://www.geeksforgeeks.org/network-programming-python-http-server/)

### What are sockets?

- [Python Socket Programming | DigitalOcean](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client)

- (more in-depth) [Socket Programming in Python (Guide) | RealPython](https://realpython.com/python-sockets/)

- [Socket Programming in Python | GeeksForGeeks](https://www.geeksforgeeks.org/socket-programming-python/)

I had to go through all the above links to get enough base knowledge to understand the below documentation content.

## Important documentation links:

- [http.server | Python docs](https://docs.python.org/3/library/internet.html)

- [socketserver | Python docs](https://docs.python.org/3/library/socketserver.html)

- [Python Documentation - Internet Protocols and Support - Index | Python docs](https://docs.python.org/3/library/internet.html) - has an index of useful documentations related to internet, contains earlier two links.

# To set up a working custom server:

## Making custom defined do_GET() function

#### Example starter code

from Google Bard:

```python
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
```

#### Example for checking if client can accept certain response types

from Google Bard

```python
import http.server

class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Get the requested path
        path = self.path

        # Get the Accept header
        accept = self.headers.get('Accept')

        # If the client accepts text/plain, send the content
        if accept and 'text/plain' in accept:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Content-Length', len('Hello, world!'))

            # Send the content of the response
            self.wfile.write('Hello, world!'.encode('utf-8'))

        # Otherwise, the client does not accept text/plain, so send a 406 error
        else:
            self.send_response(406)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('The client does not accept text/plain.'.encode('utf-8'))
```
