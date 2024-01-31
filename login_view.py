# login_view.py

class LoginView:
    def render_login_page(self):
        return """
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

            <p><a href="/logout">Logout</a></p>
        </body>
        </html>
        """

    def render_logout_page(self):
        return """
        <html>
        <head>
            <title>Logout Page</title>
        </head>
        <body>
            <h2>Logout</h2>
            <p>You have been logged out.</p>
            <p><a href="/">Back to Login</a></p>
        </body>
        </html>
        """
    def render_login_result(self, success, __username):
        if success:
            html = """
            <html>
                <body>
                    <h2>Login successful!</h2>
                    <p>Hi {}
                    <p><a href="/logout">Logout</a></p>
                </body>
            </html>
            """
            return html.format(__username)
        else:
            return """
            <html>
                <body>
                    <h2>Login failed. Invalid credentials.</h2>
                    <p><a href="/">Back to Login</a></p>
                </body>
            </html>
            """
