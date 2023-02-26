
# SMS Service
This service is a simple SMS application that allows users to send and receive SMS messages between each other. Users can view their conversations with other users by entering their phone number.

## Setup

1) Clone the repository from Github.

2) Run `docker compose up` command. (This command will spin up postgres (DB) and flask app)

3) Follow the API guide for using this service


# API ENDPOINTS

## Send SMS
**Endpoint**: /api/send-sms
**Method**: POST
**Parameters**:
	senderPhone: Phone number of the sender
	receiverPhone: Phone number of the receiver
messageText: Text of the message
timestamp: Unix timestamp of when the message was sent
uuid: Unique identifier for the message
Response: { "message": "SMS sent successfully" }


## Receive SMS
**Endpoint**: /api/receive-sms
**Method**: POST
**Parameters**:
senderPhone: Phone number of the sender
receiverPhone: Phone number of the receiver
messageText: Text of the message
timestamp: Unix timestamp of when the message was received
uuid: Unique identifier for the message
Response: { "message": "SMS received successfully" }


## Get Conversation
**Endpoint**: /api/get-conversation/<phone_number>
**Method**: GET
**Parameters**:
phone_number: Phone number of the user whose conversation is being requested
Response: { "messages": [ { "phone_number": "1234567890", "message_text": "Hello", "timestamp": 1645845235, "direction": "sent" }, { "phone_number": "0987654321", "message_text": "Hi there", "timestamp": 1645845278, "direction": "received" } ] }


## API Documentation
The API documentation is available in the swagger.yaml file. You can view the documentation using a tool like Swagger UI.