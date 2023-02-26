
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


Q/A:
1) For this backend API, I would use the following AWS services:

Amazon RDS (Relational Database Service) to host the PostgreSQL database used by the API.
Amazon EC2 (Elastic Compute Cloud) to host the Flask application that runs the API.
Amazon Elastic Load Balancer (ELB) to distribute traffic to multiple EC2 instances if needed.
Amazon CloudWatch to monitor the application's performance and set alarms for potential issues.
Amazon S3 (Simple Storage Service) to store any static files that the API might use (e.g. API documentation).

2) If the API becomes very popular, there are several changes that might need to be made to the infrastructure and/or code to handle the increased traffic:

Increase the number of EC2 instances running the Flask application and configure an Elastic Load Balancer to distribute traffic evenly between them.
Increase the size of the RDS instance or cluster to handle the increased database load.
Use Amazon ElastiCache to cache frequently accessed data and reduce the load on the database.
Optimize the code for performance, including database queries and API endpoint response times.
Use Amazon CloudFront as a content delivery network (CDN) to serve static files and reduce latency for users in different regions.
Implement rate limiting and other security measures to prevent abuse and protect against attacks.
