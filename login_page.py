from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import psycopg2
from psycopg2 import sql

# Database configuration
DB_CONFIG = {
    'dbname': 'login_app',
    'user': 'postgres',
    'password': 'intelligo1',
    'host': 'localhost',
    'port': '5432',
}

class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        page_content = """
        <html>
        <head>
            <title>Login Page</title>
        </head>
        <body>
            <h2>Login</h2>
            <form method="post" action="/login">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br>

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br>

                <input type="submit" value="Login">
            </form>
        </body>
        </html>
        """

        self.wfile.write(page_content.encode())

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        params = parse_qs(post_data)

        username = params.get("username", [""])[0]
        password = params.get("password", [""])[0]

        print(f"Received POST request with username: {username}, password: {password}")

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        try:
            # Check user credentials
            # query = sql.SQL("SELECT * FROM users WHERE username = {} AND password = {}").format(
            #     sql.Identifier(username), sql.Identifier(password)
            # )
            queryText = "SELECT * FROM users WHERE username = '"+username+"' AND password = '"+password+"'"
            query = sql.SQL(queryText)
            print(f"Executing SQL query: {query}")
            cur.execute(query)

            if cur.fetchone():
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<html><body><h2>Login successful!</h2></body></html>")
                print("Login successful!")
            else:
                self.send_response(401)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<html><body><h2>Login failed. Invalid credentials.</h2></body></html>")
                print("Login failed. Invalid credentials.")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Close database connection
            cur.close()
            conn.close()

if __name__ == "__main__":
    port = 8000
    server_address = ("", port)

    httpd = HTTPServer(server_address, LoginHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()
