# Task Management API

This is a Django-based Task Management API that allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users. The API is built using Django and Django REST Framework (DRF) and uses JWT for authentication.

## Features

1. **Create a Task**: Allows the creation of new tasks with a name and description.
2. **Assign a Task to Users**: Enables assigning a task to one or multiple users.
3. **Retrieve Tasks for a Specific User**: Fetches all tasks assigned to a particular user.
4. **Update and Delete Tasks**: Modify or remove tasks as needed.

## Requirements

- Python 3.8+
- Django 5.1.7
- Django REST Framework
- Django REST Framework Simple JWT

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <repository_url>
cd task_management_api
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```sh
python manage.py createsuperuser
```
Follow the prompts to set up a superuser account.

### 6. Run the Development Server
```sh
python manage.py runserver
```
The server will start at `http://127.0.0.1:8000/`.

## API Endpoints

### **Authentication**

#### 1. Obtain Access and Refresh Tokens
**Endpoint:** `POST /token/`
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
**Response:**
```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

#### 2. Refresh Access Token
**Endpoint:** `POST /token/refresh/`
```json
{
    "refresh": "your_refresh_token"
}
```
**Response:**
```json
{
    "access": "new_access_token"
}
```

### **Task Management**

#### 1. Create a Task
**Endpoint:** `POST /tasks/`

**Headers:**
```
Authorization: Bearer <your_access_token>
```

**Request Body:**
```json
{
    "name": "Grocery Shopping",
    "description": "Purchase sugar, dal, rice",
    "status": "pending",
    "assigned_users": [2]  
}
```

**Response:**
```json
{
    "id": 6,
    "assigned_users": [2],
    "name": "Grocery Shopping",
    "description": "Purchase sugar, dal, rice",
    "created_at": "2025-03-26T08:57:00.211834Z",
    "status": "pending"
}
```

#### 2. Retrieve All Tasks
**Endpoint:** `GET /tasks/`

**Headers:**
```
Authorization: Bearer <your_access_token>
```

**Response:**
```json
[
    {
        "id": 1,
        "assigned_users": [],
        "name": "grocery",
        "description": "purchase sugar, dal, rice",
        "created_at": "2025-03-25T14:43:24.924077Z",
        "status": "pending"
    },
    {
        "id": 6,
        "assigned_users": [2],
        "name": "Grocery Shopping",
        "description": "Purchase sugar, dal, rice",
        "created_at": "2025-03-26T08:57:00.211834Z",
        "status": "pending"
    }
]
```

#### 3. Retrieve Tasks for a Specific User
**Endpoint:** `GET /tasks/?user_id=1`

**Headers:**
```
Authorization: Bearer <your_access_token>
```

**Response:**
```json
[
    {
        "id": 6,
        "assigned_users": [2],
        "name": "Grocery Shopping",
        "description": "Purchase sugar, dal, rice",
        "created_at": "2025-03-26T08:57:00.211834Z",
        "status": "pending"
    }
]
```

#### 4. Update a Task
**Endpoint:** `PUT /tasks/1/`

**Headers:**
```
Authorization: Bearer <your_access_token>
```

**Request Body:**
```json
{
    "name": "Updated Grocery Task",
    "description": "Purchase sugar, dal, rice, and wheat",
    "status": "in_progress",
    "assigned_users": [2]
}
```

**Response:**
```json
{
    "id": 1,
    "assigned_users": [2],
    "name": "Updated Grocery Task",
    "description": "Purchase sugar, dal, rice, and wheat",
    "created_at": "2025-03-25T14:43:24.924077Z",
    "status": "in_progress"
}
```

#### 5. Delete a Task
**Endpoint:** `DELETE /tasks/2/`

**Headers:**

Authorization: Bearer <your_access_token>


**Response:**
   json
{
    "detail": "Task deleted successfully."
}


## API Testing

The API has been tested using [Postman], a popular API testing tool. Below are the steps to test the API using Postman:

1. **Import the API Endpoints**:
   - Open Postman and create a new collection.
   - Add the API endpoints mentioned in the "API Endpoints" section of this README.

2. **Set Up Authorization**:
   - Use the `POST /token/` endpoint to obtain an access token.
   - Add the token to the `Authorization` header for all subsequent requests:
    
     Authorization: Bearer <your_access_token>
     

3. **Test the Endpoints**:
   - Use the provided sample requests and responses in this README to test the API endpoints (`POST`, `GET`, `PUT`, `DELETE`).

4. **Verify Responses**:
   - Ensure the responses match the expected outputs mentioned in this README.

## Test Credentials

Superuser:
- **Username:** `Utkarsh_kayasth`
- **Password:** `Krishu@8804`

## Project Structure

task_management_api/
├── task_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
└── README.md


