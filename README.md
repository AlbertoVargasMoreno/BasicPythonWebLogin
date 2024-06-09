# Simple Login Page with Python

## Overview
A basic Python web application demonstrating a simple login page. The project uses standard Python libraries for HTTP server functionality and connects to a PostgreSQL database for user authentication.

## Features
* User Authentication: Verify user credentials against a PostgreSQL database.
* Minimalistic Login Page: Provides a straightforward interface for user login.
* Modular Architecture: Organized into separate files for improved code structure.
* Easy Deployment: Designed for straightforward deployment on various hosting platforms.

## Technologies Used
* Python: The primary programming language.
* HTTP Server: Utilizes Python's built-in http.server module.
* PostgreSQL: Database management system for user authentication.

## Usage
1. Clone the repository:
```bash
 git clone https://github.com/AlbertoVargasMoreno/BasicPythonWebLogin.git
```
2. Install dependencies (I think there's no need to install anything else).
```bash
pip install -r requirements.txt
```

3. Configure the PostgreSQL database.
4. Run the application:
```bash
 python login_controller.py
```
5. Access the login page at http://localhost:8000.

### Configure POSTGRES

- https://dbasco.com/installing-postgres-on-ubuntu-20-04-for-wsl/
- https://www.cyberciti.biz/faq/howto-add-postgresql-user-account/

```bash
sudo -u postgres psql
[sudo] password for developer:
psql (12.18 (Ubuntu 12.18-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# CREATE USER pythonuser WITH PASSWORD 's3cr3t';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE login_app TO pythonuser;
GRANT
sudo su - postgres
postgres@MSI:/home/developer/python/web_dev/BasicPythonWebLogin/docs$ psql -d login_app -f create_tables.sql
CREATE TABLE

  File "/home/developer/python/web_dev/BasicPythonWebLogin/user_model.py", line 21, in authenticate_user
    cur.execute(query)
psycopg2.errors.InsufficientPrivilege: permission denied for table users

❯ sudo su - postgres
[sudo] password for developer:
postgres@MSI:~$ pslq -U login_app

postgres@MSI:~$ psql -U postgres -d login_app
psql (12.18 (Ubuntu 12.18-0ubuntu0.20.04.1))

login_app=# insert into users(username, password) values("jane.doe", "j4n3d03");

login_app=# GRANT ALL PRIVILEGES ON TABLE users TO pythonuser;
GRANT
```

## Deployment
For deployment on a public server, until now it has not been deployed in a public server.

## Contributing
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests. For major changes, please open an issue first to discuss potential changes.

## License
This project is licensed under the MIT License.

## Acknowledgements
* Assistance from ChatGPT 3.5