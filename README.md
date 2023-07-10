# Chatting App

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Introduction

The Chatting App is a web application that allows users to create accounts, make friends, and chat with them in real-time. It's built using the Django framework and offers a range of features to enhance the chatting experience.

# Screenshots
![Screenshot from 2023-07-09 00-23-42](https://github.com/VinayPundhir/chatting_app/assets/51248042/53eb6d03-07b8-4893-a1c6-2d16250c24fa)
![Screenshot from 2023-07-09 00-23-50](https://github.com/VinayPundhir/chatting_app/assets/51248042/efe7f26c-c654-43f1-bc10-8c34f1d750ab)
![Screenshot from 2023-07-08 23-45-55](https://github.com/VinayPundhir/chatting_app/assets/51248042/631ee65e-e5db-44fd-8ab9-f48de4c66fed)
![Screenshot from 2023-07-08 23-45-23](https://github.com/VinayPundhir/chatting_app/assets/51248042/8532802f-c981-4ae9-9d6e-04be3e38e239)
![Screenshot from 2023-07-08 23-44-41](https://github.com/VinayPundhir/chatting_app/assets/51248042/08276efd-3c6f-4327-83c2-f7e193479073)



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


   
