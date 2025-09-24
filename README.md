# Car Booking System API

A FastAPI-based car booking system with user authentication, car management, and booking functionality. This system provides a RESTful API for managing car rentals with role-based access control.

## Features

- **User Authentication & Authorization**
  - User registration and login
  - JWT token-based authentication
  - Role-based access control (user, admin, org)
  
- **Car Management**
  - Add car details (admin only)
  - View all available cars
  - Search cars by model name
  
- **Booking System**
  - Book cars
  - View booking details
  - Update booking information
  - Relationship between cars and bookings

## Technology Stack

- **Backend Framework**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: Custom hashing implementation
- **Server**: Uvicorn
