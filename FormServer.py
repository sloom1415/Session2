from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from os import environ

memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('content-length', 0))
        data = self.rfile.read(length).decode()

        info = parse_qs(data)
        memory.append('''
    name: {}
    city: {}
    enrollment: {}
    nanodegree: {}
    status: {}
    '''.format(
            info['name'][0],
            info['city'][0],
            info['enrollment'][0],
            info['nanodegree'][0],
            info['status'][0]
        )
        )

        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-plain', 'text/html; charset=utf-8')
        self.end_headers()

        self.wfile.write(form.format('\n'.join(memory)).encode())


if __name__ == '__main__':
    port = int(environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
