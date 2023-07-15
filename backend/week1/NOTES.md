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

- [Python sqlite3 docs](https://docs.python.org/3/library/sqlite3.html), [How-to guides](https://docs.python.org/3/library/sqlite3.html#sqlite3-howtos)

- [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-commands/)

# Setting up a working custom server:

## Making custom defined do_GET() function

### Code examples

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

#### Example for redirects

from Google Bard

```python
import http.server

class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Get the requested path
        path = self.path

        # If the path is /redirect, redirect to the home page
        if path == '/redirect':
            self.send_response(302)
            self.send_header('Location', 'https://www.google.com')
```

- I am not sure why examples from Google Bard insists on sending `Content-type` and `Content-Length` header everytime even though the page seems to load in the browser without any issues. But I shall follow that for now.

## Getting the server to respond to POST requests

- According to http.server docs (and code reference), there wasn't a `do_POST()` function shown for Base or Simple HTTPRequestHandler classes. And there was one defined for CGIHTTPRequestHandler, but it said something like how it's allowed only for CGI scripts etc and implied it's not for normal scripts. And another issue of CGIHTTPRequestHandler is that it does not work for redirects. So, if I was gonna use that, my `GET redirect/<short_code>` may not work.

- So, I was confused how to implement the `POST /create/<short_code>/<destination_url>` endpoint.

- But, according to this [stackoverflow answer](https://stackoverflow.com/questions/51677570/http-server-unsupported-method-post), making a `do_POST()` function is required to make SimpleHTTPRequestHandler work with POST requests. I tried that and it worked!

## Testing the server

### Sending requests to the server

- For making GET requests I just had to paste the url on the browser omnibar. Or atleast, I assume that the browser just sends a regular GET request if entered through the omnibar.

- For making POST requests on the other hand, the above would not work. So I had to look for methods to send custom requests somehow.

- Postman is capable of doing the above, but I haven't set it up yet, besides, the browser must be capable of the same somehow right?

- This [stackoverflow answer](https://stackoverflow.com/a/38637309) is the answer, add JQuery to the webpage, declare the mentioned function, and execute requests the way you want.

Steps:

1. Add this line to the html code - `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>`

2. Open Chrome DevTools console, enter the following function:

```javascript
(function () {
  var newscript = document.createElement("script");
  newscript.type = "text/javascript";
  newscript.async = true;
  newscript.src =
    "https://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js";
  (
    document.getElementsByTagName("head")[0] ||
    document.getElementsByTagName("body")[0]
  ).appendChild(newscript);
})();
```

3. Now enter your requests, in the below format:

```javascript
url = "http://127.0.0.1:8324/create/new1/https://www.google.com";
$.ajax({
  type: "POST",
  url: url,
});
```

## Error codes to use

- `201 Created` - Used this when the new url was successfully added to the database.
- `302 Found` - When the shortened url matches and proceeds to redirect.
- `404` - usually to put in an else statement when the url matches none of the criterions.
- `400` - When the url matches an endpoint, but server cannot parse the remaining part, usually due to a format error in the url.
- `409` - For conflicts. I used this when the new shortened url to be created was already in use.
