# login_controller.py

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from user_model import UserModel
from login_view import LoginView

# Database configuration
DB_CONFIG = {
    'dbname': 'login_app',
    'user': 'postgres',
    'password': 'intelligo1',
    'host': 'localhost',
    'port': '5432',
}

class LoginController(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = UserModel(db_config=DB_CONFIG)

    def render_login_page(self):
        return LoginView().render_login_page()

    def render_logout_page(self):
        return LoginView().render_logout_page()

    def do_GET(self):
        if self.path == "/logout":
            self.logout()
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            if self.path == "/":
                page_content = self.render_login_page()
            else:
                page_content = "Invalid URL"

            self.wfile.write(page_content.encode())

    def do_POST(self):
        # Your existing do_POST method code
        print("Post response")

    def logout(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        page_content = self.render_logout_page()
        self.wfile.write(page_content.encode())

if __name__ == "__main__":
    port = 8000
    server_address = ("", port)

    httpd = HTTPServer(server_address, LoginController)
    print(f"Server running on port {port}")
    httpd.serve_forever()
