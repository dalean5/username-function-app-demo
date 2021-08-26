# Azure Functions Demo

This is a simple function app that has three functions:

- **create_user**: This functions takes a JSON payload and persists to the database.
- **get_user**: This functions takes a numeric parameter which is a database ID for a stored user. If the ID is found, the data associated is returned. Otherwise, return 404.
- **get_users**: This function returns a list of all users found in the database.