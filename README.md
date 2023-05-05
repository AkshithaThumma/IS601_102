# IS601_102

# Volunteer Management System

The Volunteer Management System is a web application built with Django that allows users to manage volunteer events. The system supports user registration, event creation, and event registration.

## Features

- User registration: Users can create an account to access the system.
- User authentication: Users can log in to the system using their credentials.
- Event creation: Organizers can create new volunteer events, providing event details such as title, description, date, and location.
- Event registration: Users can view the list of available events and register or unregister themselves as volunteers for specific events.
- Admin User: Login to Django admin and Make a user as Organiser

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/volunteer-management.git
```

2. Navigate to the project directory:

```
cd volunteer-management

```
3. Run database migrations:
```
python manage.py migrate
```
4. Start the development server:
```
python manage.py runserver
```

5. Open your web browser and access the application at http://localhost:8000.

## Usage

- Create a user account by registering on the registration page.
- Log in using your credentials.
- View the list of available events on the home page.
- Register or unregister yourself as a volunteer for specific events.
- Admin User can make any user an organiser
- Organizers can login and create new events.
