import http.server, os, sqlite3


def abs_path(relative_pos):
    return os.path.join(os.path.dirname(__file__), relative_pos)


def init_db(conn):
    # cur = conn.cursor()
    with open(abs_path("schema.sql"), "r") as f:
        conn.executescript(f.read())
    conn.commit()


class HandlerClass(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        conn = sqlite3.connect(abs_path("url.db"))
        cur = conn.cursor()

        path = self.path

        print(path)
        if path == "/":
            self.send_response(200)
            f = open(
                abs_path("static\\index.html"),
                "r",
            )
            page = f.read()
            self.send_header("Content-type", "text/html")
            self.send_header("Content-length", len(page))
            self.end_headers()
            self.wfile.write(page.encode())
            f.close()

        elif path[:10] == "/redirect/":
            short = path[10:]
            result = cur.execute(
                "SELECT unshortened FROM urls WHERE shortened = ?", (short,)
            ).fetchone()
            if result:
                message = "Redirecting"
                redirect = result[0]
                self.send_response(302, "Found")
                self.send_header("Location", redirect)
                self.send_header("Content-type", "text/plain")
                self.send_header("Content-length", len(message))
                self.end_headers()
                self.wfile.write(message.encode())
            else:
                message = "404 Not found"
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.send_header("Content-length", len(message))
                self.end_headers()
                self.wfile.write(message.encode())
        # for testing purposes, reset the entire database
        elif path == "/init":
            init_db(conn)
            message = "table reseted"
            self.send_response(201, "Created")
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(message))
            self.end_headers()
            self.wfile.write(message.encode())
        # for testing purposes, see all values in the database
        elif path == "/seeall":
            message = str(cur.execute("select * from urls").fetchall())
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(message))
            self.end_headers()
            self.wfile.write(message.encode())

        else:
            # This is an unknown path.
            message = "404 Not found"
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(message))
            self.end_headers()
            self.wfile.write(message.encode())

        conn.commit()
        conn.close()

    def do_POST(self):
        conn = sqlite3.connect(abs_path("url.db"))
        cur = conn.cursor()

        path = self.path

        if path[:8] == "/create/":
            val = path[8:]
            i = val.find("/")
            code = 201
            message = "Added to table"
            if i == -1:
                code = 400
                message = 'Error: missing "/" between <short_code> and <destination>.'
            else:
                spl = (val[:i], val[i + 1 :])
                if spl[0] != "" and spl[1] != "":
                    short, dest = spl
                    if (
                        len(
                            cur.execute(
                                "SELECT * FROM urls WHERE shortened = ?", (short,)
                            ).fetchall()
                        )
                        > 0
                    ):
                        code = 409
                        message = "Error: short code is already used, try another one."
                    else:
                        cur.execute(
                            "INSERT INTO urls (shortened, unshortened) VALUES (?, ?)",
                            tuple(spl),
                        )
                        code = 201
                        message = "Added to table"
                else:
                    code = 400
                    message = "short_code or destination url missing"
            if code == 201:
                self.send_response(201, "Created")
                self.send_header("Content-type", "text/plain")
                self.send_header("Content-length", len(message))
                self.end_headers()
                self.wfile.write(message.encode())
            else:
                self.send_response(code)
                self.send_header("Content-type", "text/plain")
                self.send_header("Content-length", len(message))
                self.end_headers()
                self.wfile.write(message.encode())

        else:
            # This is an unknown path.
            message = "404 Not found"
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(message))
            self.end_headers()
            self.wfile.write(message.encode())

        conn.commit()
        conn.close()


ServerClass = http.server.HTTPServer

Protocol = "HTTP/1"
HandlerClass.protocol_version = Protocol

server_address = ("127.0.0.1", 8324)

server_instance = ServerClass(server_address, HandlerClass)

# For gettings logs
sa = server_instance.socket.getsockname()

print(f"serving on link: http://{sa[0]}:{sa[1]}")

server_instance.serve_forever()
