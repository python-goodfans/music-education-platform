# Music Education Platform

## Introduction
This project is a comprehensive music education platform designed to provide resources and tools for both teachers and students. It includes a frontend built with Vue 3, and a backend powered by Django, along with a MySQL database. The platform features user registration, an admin dashboard, and various file management functionalities.

## Technology Stack
- **Frontend:** Vue.js 3
- **Backend:** Django
- **Database:** MySQL

## Project Structure Overview
```
- frontend/  # Vue 3 application
- backend/   # Django application
- db_setup/  # Database setup scripts
- README.md  # This documentation file
```

## Installation Instructions
### Frontend Setup
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Run the development server:**
   ```bash
   npm run serve
   ```

### Backend Setup
1. **Navigate to the backend:**
   ```bash
   cd backend
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Database Configuration:**
   - Modify the `settings.py` file to set up your MySQL database.
   
## API Endpoints
| Method | Endpoint            | Description                       |
|--------|---------------------|-----------------------------------|
| GET    | /api/users          | List all users                   |
| POST   | /api/users/register | Register a new user              |
| GET    | /api/courses        | Get all courses                  |
| POST   | /api/login          | User authentication                  |

## Authentication Flow
1. **User Registration:** Users can create an account via `/api/users/register`.
2. **Login:** Users authenticate through `/api/login` to receive a token.
3. **Access protected endpoints:** Include the token in the Authorization header for protected routes.

## File Management Features
- Users can upload and manage their own files related to courses and lessons.

## User Registration
- Users must provide basic details such as username, password, and email to register.

## Admin Dashboard Features
- Admins can manage users, courses, and view statistics about platform usage.

## Usage Examples
### Frontend
1. **To display courses,** use the following method:
   ```javascript
   fetch('/api/courses')
       .then(response => response.json())
       .then(data => console.log(data));
   ```

### Backend
1. **Example of user registration:**
   ```python
   import requests
   response = requests.post('http://localhost:8000/api/users/register', data={'username': 'testuser', 'password': 'mypassword'})
   print(response.json())
   ```

## Conclusion
This project is designed to enhance the music education experience, making resources easily accessible and manageable for both educators and learners.