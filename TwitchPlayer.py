__author__ = 'Artem Gorokhov'
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse
import subprocess

class GetHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.getheader('content-length'))
        field_data = self.rfile.read(length)
        fields = urlparse.parse_qs(field_data)
        url = fields.get('url ')
        startLivestreamer(url)
        return

def startLivestreamer(url):

    CREATE_NO_WINDOW = 0x08000000
    subprocess.call(["livestreamer", url, "best"], creationflags=CREATE_NO_WINDOW)

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 10000), GetHandler)
    server.serve_forever()
