# FastAPI MongoDB User Management API

A RESTful API built with FastAPI and MongoDB for user management operations.

## Features

- Create new users
- Retrieve user information
- List all users
- Update user details
- Delete users
- Email validation
- Error handling for duplicate emails and invalid requests

## Prerequisites

- Python 3.8+
- MongoDB installed and running
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create and activate virtual environment:
```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following content:
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=user_management
```

## Project Structure

```
user_management/
├── .env
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   └── routes/
│       ├── __init__.py
│       └── user.py
```

## Running the Application

1. Make sure MongoDB is running on your system

2. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Create User
- **URL**: `/users/`
- **Method**: `POST`
- **Body**:
```json
{
    "email": "user@example.com",
    "username": "username",
    "full_name": "Full Name",
    "password": "password123"
}
```

### Get User
- **URL**: `/users/{user_id}`
- **Method**: `GET`

### List Users
- **URL**: `/users/`
- **Method**: `GET`

### Update User
- **URL**: `/users/{user_id}`
- **Method**: `PUT`
- **Body**:
```json
{
    "username": "new_username",
    "full_name": "New Name"
}
```

### Delete User
- **URL**: `/users/{user_id}`
- **Method**: `DELETE`

## Documentation

API documentation is automatically generated and can be accessed at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing the API

You can test the API using curl commands or tools like Postman/Thunder Client.

Example curl command to create a user:
```bash
curl -X POST http://localhost:8000/users/ \
-H "Content-Type: application/json" \
-d '{
    "email": "test@example.com",
    "username": "testuser",
    "full_name": "Test User",
    "password": "password123"
}'
```

## Error Handling

The API includes handling for common errors:
- 400: Bad Request (e.g., duplicate email)
- 404: Not Found (invalid user ID or user not found)
- 422: Validation Error (invalid input data)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

