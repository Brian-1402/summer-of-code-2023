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

        if path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            f = open(
                abs_path("static\\index.html"),
                "r",
            )
            page = f.read()
            self.send_header("Content-length", len(page))
            self.end_headers()
            self.wfile.write(page.encode())
            f.close()

        elif path == "/init":
            init_db(conn)
            message = "table reseted"
            self.send_response(201)
            self.send_header("Content-type", "text/plain")
            self.send_header("Content-length", len(message))
            self.end_headers()
            self.wfile.write(message.encode())

        elif path[:8] == "/create/":
            val = path[8:]
            i = val.find("/")
            if i == -1:
                self.send_response_only(404)
                self.end_headers()
            else:
                spl = (val[:i], val[i + 1 :])
                message = "error"
                if len(spl) == 2:
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
                            message = "shortened url already exists, try another one"
                        else:
                            cur.execute(
                                "INSERT INTO urls (shortened, unshortened) VALUES (?, ?)",
                                tuple(spl),
                            )
                            message = "Added to table"

                self.send_response(201)
                self.send_header("Content-type", "text/plain")
                self.send_header("Content-length", len(message))
                self.end_headers()
                self.wfile.write(message.encode())

        elif path[:10] == "/redirect/":
            short = path[10:]
            result = cur.execute(
                "SELECT unshortened FROM urls WHERE shortened = ?", (short,)
            ).fetchone()
            if result:
                message = "Redirecting"
                redirect = result[0]
                self.send_response(302)
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

        elif path == "/seeall":
            message = str(cur.execute("select * from urls").fetchall())
            self.send_response(200)
            # self.send_header("Content-type", "text/plain")
            # self.send_header("Content-length", len(message))
            self.end_headers()
            self.wfile.write(message.encode())

        else:
            # This is an unknown path.
            message = "404 Not found"
            self.send_response(404)
            # self.send_header("Content-type", "text/plain")
            # self.send_header("Content-length", len(message))
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
