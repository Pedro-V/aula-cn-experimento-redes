import http.server
import socketserver
import socket
import psycopg
from psycopg.rows import dict_row

conn = psycopg.connect(
    dbname="postgres",
    user="postgres",
    password="aulacn2024",
    host=input("[-->] Informe o DNS do banco correspondente a esta instancia: "),
    row_factory=dict_row
)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        host_ip = socket.gethostbyname(socket.gethostname())
        with conn.cursor() as cur:
            cur.execute('SELECT version();');
            db_version = cur.fetchone()

        response_content = f"Host IP: {host_ip}\nPostgreSQL version: {db_version['version']}"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(response_content.encode('utf-8'))

if __name__ == '__main__':
    PORT = 8080
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print(f'Servindo na porta {PORT}')
        httpd.serve_forever()
