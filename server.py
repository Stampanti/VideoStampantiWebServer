import http.server
import datetime
import os.path

port = 80

class VideoStampantiServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            if os.path.exists('index.html'):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(open("index.html", "r").read(), "utf-8"))
            else:
                self.send_error(404)
        else:
            print(f'request at {self.path}')
            currentpath = self.path
            if '/index.html' in currentpath:
                if (os.path.exists(currentpath.lstrip('/'))):
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(bytes(open(currentpath.lstrip('/'), "r").read(), "utf-8"))
                else:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(bytes(open("404.html", "r").read(), "utf-8"))
            else:
                if (os.path.exists(currentpath.lstrip('/') + '/index.html')):
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(bytes(open(currentpath.lstrip('/') + '/index.html', "r").read(), "utf-8"))
                else:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(bytes(open("404.html", "r").read(), "utf-8"))

server = http.server.HTTPServer(('localhost', port), VideoStampantiServer)
currentdatetime = datetime.datetime.now()
print(f"{currentdatetime} | Server started.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    currentdatetime = datetime.datetime.now()
    server.server_close()
    print(f"{currentdatetime} | Server stopped.")