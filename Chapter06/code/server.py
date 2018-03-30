import time
import json
import random
from http.server import HTTPServer, BaseHTTPRequestHandler


class RandomRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Simulate latency
        time.sleep(3)

        # Write response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Write response body
        body = json.dumps({'random': random.random()})
        self.wfile.write(bytes(body, "utf8"))


def main():
    """Starts the HTTP server on port 8080"""
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RandomRequestHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
