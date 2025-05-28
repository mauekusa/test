import http.server
import urllib.parse
import csv
from datetime import datetime

PORT = 8000
CSV_FILE = 'contacts.csv'

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length).decode('utf-8')
            params = urllib.parse.parse_qs(body)
            company = params.get('company', [''])[0]
            name = params.get('name', [''])[0]
            email = params.get('email', [''])[0]
            with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now().isoformat(), company, name, email])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'ok')
        else:
            self.send_error(404)

if __name__ == '__main__':
    http.server.test(HandlerClass=Handler, port=PORT)
