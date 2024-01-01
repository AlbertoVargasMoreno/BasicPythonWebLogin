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
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        params = parse_qs(post_data)

        username = params.get("username", [""])[0]
        password = params.get("password", [""])[0]
        print(username+", "+password)

        # Check user credentials using the UserModel
        authenticated = self.user_model.authenticate_user(username, password)
        print("authenticated result: " + authenticated)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if authenticated:
            self.wfile.write(b"<html><body><h2>Login successful!</h2></body></html>")
        else:
            self.wfile.write(b"<html><body><h2>Login failed. Invalid credentials.</h2></body></html>")

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
