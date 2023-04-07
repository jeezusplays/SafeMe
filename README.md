# SafeMe
## About this Project
SafeMe is a **natural disaster relief** mobile application that aims to provide real-time updates on individuals dealing with disasters such as: earthquakes, cyclones, floods, volcanoes, droughts and forest fires. 

This application is targeted towards two types of users – **Public Users** and **Government**. Each user type has access to different features that best suit their usage needs. For Public Users, they are able to:
* Receive a danger notification when in the risk of being in danger
* View family members safety through a status dashboard
* Acknowledge safety status notification or prompts
* Accept volunteer request for volunteer event – *Event to get volunteers to help out after a natural disaster*

For Government, they are able to:
* View the list of possible casualties in affected disaster areas
* Access GPS coordinates of affected individuals that have not acknowledged safety status notifications
* Create and manage volunteer event

### Assumptions
The following functions are assumed to be completed:

Public Users:
* Create and join a family – *A group of people that can track each other in real-time*
* Announce to family when no longer in risk of being in danger
* Receive alerts of other family members when they are in the risk of being in danger

Government:
* Announce the list of safe individuals

Other Assumptions:
* A user can only be affected by 1 disaster at any given time
* Disaster & Volunteer events have a start and end datetimes
* For the purpose of demonstration, users are in one family group already. 

## Built With
### Major Frameworks / Libraries
This section lists any major frameworks/libraries used to develop SafeMe.

* [HTML](https://www.w3schools.com/html/), [Bootstrap](https://getbootstrap.com/), [CSS](https://www.w3schools.com/css/), [Vue.js](https://vuejs.org/)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/), [flask_sock](https://flask-sock.readthedocs.io/en/latest/) *(websocket used to disseminate notifications and alerts to users, allowing for 2-way communication between the client and the server)*
* [AMQP](https://www.amqp.org/)

### APIs
This section lists any APIs used to develop SafeMe.
* [Kong API Gateway](https://docs.konghq.com/gateway/latest/) is used as a middleware to help hide the microservices' endpoints while being able to route the client to the needed services. It acts a message-oriented middleware (MOM) to help with future scalability.
* [GDACS API](https://www.gdacs.org/)

## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
To get started and use the **Send Email Microservice**, you will need to follow the instructions on creating a [Google App Password](https://support.google.com/accounts/answer/185833?visit_id=638159212202344047-122164626).

You will also need the following software installed in your machine.
* [Visual Studio Code](https://code.visualstudio.com/)
* [Docker](https://www.docker.com/)
* [Postman](https://www.postman.com/) *(for testing)*
* [Python](https://www.python.org/)
* [Node.js](https://nodejs.org/en/)
* [WAMP](https://www.wampserver.com/en/) / [MAMP](https://www.mamp.info/en/) / [XAMPP](https://www.apachefriends.org/index.html)
* [MySQL](https://www.mysql.com/)

### Installation and Implementation

_Instructions on how to install and run this respository onto your local machine._

1. Clone the repo
   ```sh
   git clone https://github.com/samchung95/SafeMe
   ```
2. Start WAMP and Docker

<!-- 3. Ensure that you have replaced **ALL** the `<dockerid>` in `docker-compose.yml` with your Docker ID. -->

3. In a CMD Window, change directory to the repository and start the docker containers
   ```sh
   docker-compose up
   ```
4. Go to your localhost and test out the application!
   ```sh
   http://localhost:8080/
   ``` 

To stop and remove all containers, networks, volumes, and images created by `up`
   ```sh
   docker-compose down
   ```

## Usage


