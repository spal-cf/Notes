#!/usr/bin/env python

# sudo openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365

# SSL web server using simple HTTP in Python3
# Create the certs/keys first using the first command in this document
# adjust responses to handle CORS from XHR as necessary (edit the SimpleHTTPRequestHandler class)

import ssl
import http.server

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
      def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.send_header('Access-Control-Allow-Credentials', 'True')
            http.server.SimpleHTTPRequestHandler.end_headers(self)

      def do_OPTIONS(self):
            self.send_response(200, "ok")
            self.end_headers()

      def do_POST(self):
            content_length=int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(post_data)

def run_ssl_server(port=9443, certfile='<cert file location>', keyfile='<cert key location>'):
       """Runs a simple HTTPS server."""
       context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
       context.load_cert_chain(certfile=certfile, keyfile=keyfile)
       context.check_hostname = False # Disable hostname verification (for testing)

       with http.server.HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler) as httpd:
           httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
           print(f"Serving HTTPS on port {port}...")
           httpd.serve_forever()

if __name__ == "__main__":
       run_ssl_server()
