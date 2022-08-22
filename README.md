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
Used to create a user in the system\

**POST** {host}/userauth/users/\
Example body: {\
    "email": "lion@chatapp.com",\
    "username": "testuser",\
    "password": "testpass111",\
    "first_name": "Lion",\
    "last_name": "Zoo",\
    "phone": "1234567",\
    "address": "lion zoo street"\
}

#### POST login
Used to login a user

**POST** {host}/userauth/token/login\
Example body: {\
    "username": "testuser",\
    "password": "testpass111",\
}

#### POST logout
Used to logout a user

**POST** {host}/userauth/token/logout\
Requires: Valid authorization token in header\

#### POST create chat room:
Used to create a chat room\
Requires: Valid authorization token in header\

**POST** {host}/chatApp/chatRooms/\
Example body:  {/
        "name": "test chat room 1",\
        "capacity": 100,\
        "link": "testLink@test.com",\
        "password": "chatRoomPassword"\
}


