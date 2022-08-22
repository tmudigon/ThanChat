# ThanChat
This project implements a simple chat server backend using the Django REST framework, and Djoser for authentication.

The following functionality has been implemented for this app: 
•	sign in and sign out 
•	list existing chat rooms and create new chat rooms 
•	post messages to any chat room (there is no need to join the room) 
•	post messages to any other user 
•	list messages from any chatroom 
•	list messages posted to directly them 

### Endpoints
The following endpoints are available in this chat server implementation:

#### POST create user:
Used to create a user in the system

POST http://127.0.0.1:8000/userauth/token/login
Example body: {
    "email": "lion@chatapp.com",
    "username": "lion",
    "password": "testing321",
    "first_name": "Lion",
    "last_name": "Zoo",
    "phone": "1234567",
    "address": "lion zoo street"
}

#### POST login


