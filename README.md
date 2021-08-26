# Azure Functions Demo

This is a simple function app that has three functions:

- **create_user**: This functions takes a JSON payload and persists to the database.
- **get_user**: This functions takes a numeric parameter which is a database ID for a stored user. If the ID is found, the data associated is returned. Otherwise, return 404.
- **get_users**: This function returns a list of all users found in the database.

### Running the function app

If you want to run this function app, please ensure the following environment variables are present.

- **DB_HOST**: PostgreSQL database server name. The default is *localhost*
- **DB_PORT**: Port for database server. The default is *5432*
- **DB_PASSWORD**: Password for the database user. The default is *password*
- **DB_USER**: Username to access the database. The default is *user*
- **DB_NAME**: The name of the database. The default is *db*