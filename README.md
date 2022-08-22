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

*POST* {host}/userauth/users/\
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

*POST* {host}/userauth/token/login\
Example body: {\
    "username": "testuser",\
    "password": "testpass111",\
}


#### POST logout
Used to logout a user
Requires: Valid authorization token in header\

*POST* {host}/userauth/token/logout\


#### POST create chat room:
Used to create a chat room\
Requires: Valid authorization token in header\

*POST* {host}/chatApp/chatRooms/\
Example body:  {/
        "name": "test chat room 1",\
        "capacity": 100,\
        "link": "testLink@test.com",\
        "password": "chatRoomPassword"\
}


#### GET list of existing chat rooms:
Used to list all existing chat rooms\
Requires: Valid authorization token in header\

*GET* {host}/chatApp/chatRooms/


#### GET one chat room:
Used to retrieve information about one chat room\
Requires: Valid authorization token in header\

*GET* {host}/chatApp/chatRooms/{pk}/


#### POST a message:
Used to create a message\
Requires: 
- Valid authorization token in header\
- Either one of user_receiver or chat_room_receiver must be provided, but not both
Returns: Automatically adds the message creation date and the request user as sender at the time a message is posted.

*POST* {host}/chatApp/messages/\
Example body:  {/
    "message_text": "Message to tiger #1",/
    "user_receiver": null,/
    "chat_room_receiver": 1/
}/
Example return:  {/
    "id": 6,/
    "message_text": "Message to tiger #1",/
    "creation_date": "2022-08-22T00:57:32.191943Z",/
    "sender": 3,/
    "user_receiver": null,/
    "chat_room_receiver": 1/
}


#### GET list of messages posted to a specific chat room:
Used to list all messages posted to a specific chat room\
Requires: 
- Valid authorization token in header\
- Parameter: chat room id

*GET* {host}/chatApp/messages/?chat_room_id={pk}/


#### GET list of messages sent to the logged in user:
Used to list all messages sent to the logged in user\
Requires: 
- Valid authorization token in header\
- Parameter: chat room id

*GET* {host}/chatApp/messages/

