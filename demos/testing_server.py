#!/usr/bin/python3

# CS1440 Recursive Web Crawler testing server
#
# Usage:
#   python testing_server.py [address=localhost] [port=8000] [timeout=3]
#
# Example: Respond to http://localhost:4444 and stay running for 30 seconds
#   python testing_server.py localhost 4444 30
#
# Specify a timeout of 0 to let the server run forever


from http.server import HTTPServer, BaseHTTPRequestHandler
import sys
import threading
import time


class Based(BaseHTTPRequestHandler):

    def snoozer(self):
        """
        Prevent a broken crawler from running forever by shutting this server
        down after a few seconds
        """
        while self.server.timeout > 0:
            print(f"Server will shutdown in {self.server.timeout} second{plural(self.server.timeout, '', 's')}...")
            self.server.timeout -= 1
            time.sleep(1)
        self.server.shutdown()

    def listOfAnchors(self, urls):
        """
        Form an HTML list of anchor tags (links) pointing to input urls
        """
        return "\n".join([ f'<li>Visit <a href="{link}">{link}</a></li>' for link in urls.keys() ])

    def serve(self):
        """
        Called when a valid page is requested to form an HTTP response.
        """
        self.server.pages[self.path] += 1

        if self.path == "/deadend":
            new_pages = { }
        else:
            # Given my URL, what new pages can you visit from here?
            new_pages = {
                    f"{self.path}a": 0,
                    f"{self.path}b": 0,
                    f"{self.path}c": 0,
                    }

            for path in new_pages:
                if path not in self.server.pages:
                    self.server.pages[path] = new_pages[path]

        self.send_response(200)
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(
                bytes(f"""
                <head>
                    <title>Welcome to {self.path}</title>
                </head>
                <body>
                    <h1>Welcome to {self.path}</h1>
                    <h2>From here you can visit<h2>
                    <ul>
                        <li><a href="/deadend">A dead end</a></li>
                        {self.listOfAnchors(new_pages)}
                        <li><a href="/">Return home</a></li>
                        {self.listOfAnchors(new_pages)}
                    </ul>
                </body>
                """, encoding="utf_8"))

    def do_404(self):
        """
        Called when a non-existant page is requested.
        """
        if self.path not in self.server.non_existant:
            self.server.non_existant[self.path] = 1
        else:
            self.server.non_existant[self.path] += 1

        self.send_response(404)
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(
                bytes(f"""
                <head>
                    <title>404, Dude!</title>
                </head>
                <body>
                    <h1>Error 404!</h1>
                    <h2>Sorry dude, wrong file!</h2>
                    <p>You wanted to visit <code>{self.path}</code>, but that's not a place I can take you</p>
                </body>
                """, encoding="utf_8"))

    def do_GET(self):
        """
        Called when the server receives an HTTP GET request
        """
        if not self.server.snoozed:
            self.server.snoozed = True
            threading.Thread(target=self.snoozer).start()

        if self.path.endswith('/shutdown') \
                or self.path.endswith('/shutdown/'):
            print("Shutting down...")
            #import pdb; pdb.set_trace()
            self.server.timeout = 0
            threading.Thread(target=self.server.shutdown).start()
        elif self.path in self.server.pages:
            self.serve()
        else:
            self.do_404()


def plural(n, sing, plur):
    if n == 1:
        return sing
    else:
        return plur


if __name__ == '__main__':
    bind, port = 'localhost', 8000

    if len(sys.argv) > 1:
        bind = sys.argv[1]

    if len(sys.argv) > 2:
        port = int(sys.argv[2])

    server_address = (bind, port)
    based = HTTPServer(server_address, Based)

    # The initial set of pages that exist in the server
    # New pages are created as the server is explored
    based.pages = {
            "/": 0,
            "/deadend": 0,
            }
    based.non_existant = {}

    if len(sys.argv) > 3:
        based.timeout = int(sys.argv[3])
    else:
        based.timeout = 3

    if based.timeout == 0:
        # When a timeout of 0 is specified the server runs forever
        based.snoozed = True
    else:
        based.snoozed = False

    if based.snoozed:
        print(f"Serving from http://{server_address[0]}:{server_address[1]}/ forever\nPress Ctrl-C or visit http://{server_address[0]}:{server_address[1]}/shutdown/ to quit\n")
    else:
        print(f"Serving from http://{server_address[0]}:{server_address[1]}/ for {based.timeout} second{plural(based.timeout, '', 's')} after first contact\nPress Ctrl-C or visit http://{server_address[0]}:{server_address[1]}/shutdown/ to quit\n")

    try:
        based.serve_forever()
    except KeyboardInterrupt:
        based.shutdown()
    finally:
        zero = []
        once = []
        many = []
        for page in based.pages:
            if based.pages[page] == 0:
                zero.append(page)
            elif based.pages[page] == 1:
                once.append(page)
            else:
                many.append(page)

        l = len(once)
        if l > 0:
            print(f"{l} page{plural(l, ' was', 's were')} visited exactly once")
            # TODO: uncomment to see which URLs were visited exactly once
            # for page in once: print(f"\t{page}")

        l = len(zero)
        if l > 0:
            print(f"\n{l} page{plural(l, ' was', 's were')} not visited at all")
            # TODO: uncomment to see which URLs were never visited
            # for page in zero: print(f"\t{page}")

        l = len(many)
        if l > 0:
            print(f"\n{l} page{plural(l, ' was', 's were')} visited many times")
            for page in many: print(f"\t{page}: {based.pages[page]}")

        l = len(based.non_existant)
        if l > 0:
            print(f"\n{l} page{plural(l, ' was', 's were')} visited before they were created:")
            for page in based.non_existant: print(f"\t{page}")
