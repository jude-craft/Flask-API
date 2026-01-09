# Flask User API

A simple RESTful API built with Flask and Flask-RESTful for managing user data. This project uses SQLAlchemy for database operations and SQLite for data persistence.

## Features

- **GET** all users or a specific user by ID
- **POST** new users to the database
- **PUT** to update an entire user record
- **PATCH** to partially update a user record
- **DELETE** users from the database
- SQLite database for persistent storage
- Request validation and error handling

## Requirements

- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy

See [requirements.txt](requirements.txt) for a complete list of dependencies.

## Installation

1. Clone or download this project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create the database:
   ```bash
   python create_db.py
   ```

## Running the Server

Start the Flask development server:

```bash
python api.py
```

The server will run on `http://localhost:5000` by default.

## API Endpoints

### Get all users

```
GET /api/users
```

### Get a specific user

```
GET /api/users/<user_id>
```

### Create a new user

```
POST /api/users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Update a user (full update)

```
PUT /api/users/<user_id>
Content-Type: application/json

{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

### Update a user (partial update)

```
PATCH /api/users/<user_id>
Content-Type: application/json

{
  "name": "Jane Doe"
}
```

### Delete a user

```
DELETE /api/users/<user_id>
```

## Home Endpoint

```
GET /home
```

Returns a welcome message.

## Database

The application uses SQLite with the following User model:

- **id** (Integer): Primary key
- **name** (String): User's name (unique, required)
- **email** (String): User's email (unique, required)

## Project Structure

```
.
├── api.py           # Main Flask application
├── create_db.py     # Database initialization script
├── requirements.txt # Python dependencies
└── README.md        # This file
```
