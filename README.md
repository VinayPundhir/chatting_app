# Chatting App

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Introduction

The Chatting App is a web application that allows users to create accounts, make friends, and chat with them in real-time. It's built using the Django framework and offers a range of features to enhance the chatting experience.

# Screenshots
![Screenshot from 2023-07-09 00-23-42](https://github.com/VinayPundhir/chatting_app/assets/51248042/cf74f5b0-107e-4366-9c77-b27dc834c6c4)
![Screenshot from 2023-07-09 00-23-50](https://github.com/VinayPundhir/chatting_app/assets/51248042/3d8291ee-8379-41c2-9032-b8e38ff7f56b)
![Screenshot from 2023-07-08 23-45-55](https://github.com/VinayPundhir/chatting_app/assets/51248042/4aae687f-e5ae-4840-9b76-d6aa3068fdf7)
![Screenshot from 2023-07-08 23-45-23](https://github.com/VinayPundhir/chatting_app/assets/51248042/25ec1b13-c0fe-48f8-b4df-ef8dd4b4d9b8)
![Screenshot from 2023-07-08 23-44-41](https://github.com/VinayPundhir/chatting_app/assets/51248042/08e278f0-37c9-4888-b408-38a701f4eba8)












## Features

- User registration and authentication: Users can create accounts and securely log in to the app.
- Friend management: Users can add friends and manage their friend list.
- Real-time chat functionality: Users can chat with their friends in real-time using WebSocket communication.
- User profiles: Users have profiles that display their information and activity.
- Chat history: Users can view their chat history with friends.

## Prerequisites

Before setting up the app, make sure you have the following installed:

- Python (version 3.6 or higher)
- Django (version 3.2 or higher)

## Installation

1. Change to the project directory:
   ```bash
   cd chatting_app

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/chatting_app.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Unix/macOS
   env\Scripts\activate  # For Windows
      ```

3. Install the dependencies:
  ```bash
   pip install -r requirements.txt
   ```


4. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
  ```bash
   python manage.py runserver
   ```

Access the app in your browser at http://localhost:8000


   
