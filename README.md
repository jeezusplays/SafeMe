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
|User|Functions |
|:--|:--|
|Public Users|1. Create and join a family – *A group of people that can track each other in real-time*<br> 2. Announce to family when no longer in risk of being in danger<br> 3. Receive alerts of other family members when they are in the risk of being in danger|
|Government| 1. Announce the list of safe individuals|
| Both | 1. Registration and login |

Other Assumptions:
* A user can only be affected by 1 disaster at any given time
* Disaster & Volunteer events have a start and end datetimes
* For the purpose of demonstration, users are in one family group already. 

## Built With
### Major Frameworks / Libraries
This section lists any major frameworks/libraries used to develop SafeMe.

![HTML](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white) 

[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3.svg?style=for-the-badge&logo=Bootstrap&logoColor=white)](https://getbootstrap.com/)

![CSS](https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white) 

[![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D.svg?style=for-the-badge&logo=vuedotjs&logoColor=white)](https://vuejs.org/)
 
[![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)](https://www.python.org/)

[![Flask](https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white)](https://flask.palletsprojects.com/en/1.1.x/)

Others: 
* [AMQP](https://www.amqp.org/)

### APIs
This section lists any APIs used to develop SafeMe.
| APIs |  Description  | 
|:-----:|:--------|
| [![Kong API Gateway](https://img.shields.io/badge/Kong-003459.svg?style=for-the-badge&logo=Kong&logoColor=white)](https://docs.konghq.com/gateway/latest/)  | Middleware to hide the microservices' endpoints and route the client to services |
| [![Google Maps API](https://img.shields.io/badge/Google%20Maps-4285F4.svg?style=for-the-badge&logo=Google-Maps&logoColor=white)](https://developers.google.com/maps) | Helps the government visualise location of affected casualties |
| [GDACS API](https://www.gdacs.org/) | Retrieve disaster information from GDACS  | 


## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
To get started and use the **Send Email Microservice**, you will need to follow the instructions on creating a [Google App Password](https://support.google.com/accounts/answer/185833?visit_id=638159212202344047-122164626).

You will also need the following software installed in your machine.

[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white)](https://code.visualstudio.com/)

[![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white)](https://www.docker.com/)

[![MySQL](https://img.shields.io/badge/MySQL-4479A1.svg?style=for-the-badge&logo=MySQL&logoColor=white)](https://www.mysql.com/)

![Postman](https://img.shields.io/badge/Postman-FF6C37.svg?style=for-the-badge&logo=Postman&logoColor=white) *(for testing)*

[![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)](https://www.python.org/)

<!-- ![Node.js](https://img.shields.io/badge/Node.js-339933.svg?style=for-the-badge&logo=nodedotjs&logoColor=white) -->

Others: 
* [WAMP](https://www.wampserver.com/en/) / [MAMP](https://www.mamp.info/en/) / [XAMPP](https://www.apachefriends.org/index.html)
* [Websocket: flask_sock](https://flask-sock.readthedocs.io/en/latest/) *(websocket used to disseminate notifications and alerts to users, allowing for 2-way communication between the client and the server)*


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
4. Open interface `html` files and test out the application!
   ```sh
   // Government Interface
   countryDisaster.html
   volunteerGov.html
   casualtyList.html

   // Public User Interface
   disastersNearMe.html
   myFamily.html
   volunteerPublic.html
   ``` 

To stop and remove all containers, networks, volumes, and images created by `up`
   ```sh
   docker-compose down
   ```

## Demo and Usage
### Demo
A demo of the application can be found [here](https://youtu.be/Weka3bW8NJw).
### UI
_Simple run down of each HTML page._
<table>
   <tr>
      <td>User</td>
      <td>Interface</td>
      <td>Description</td>
   </tr>
   <tr>
      <td rowspan="3">Government</td>
      <td>countryDisaster.html</td>
      <td>Real-time list of global disasters</td>
   </tr>
   <tr>
      <td>volunteerGov.html</td>
      <td>Create and manage volunteer event</td>
   </tr>
   <tr>
      <td>casualtyList.html</td>
      <td>View the list of affected users in a disaster area</td>
   </tr>
   <tr>
      <td rowspan="3">Public User</td>
      <td>disastersNearMe.html</td>
      <td>Receive a danger notification when in the risk of being in danger and acknowledge safety status notification</td>
   </tr>
   <tr>
      <td>myFamily.html</td>
      <td>View family members safety through a status dashboard</td>
   </tr>
   <tr>
      <td>volunteerPublic.html</td>
      <td>Volunteer for volunteer event</td>
   </tr>
</table>

### Requests
_Simple run down of each request._
<table>
   <tr>
      <td>Request</td>
      <td>Method</td>
      <td>Description</td>
      <td>Link</td>
   </tr>
      <tr>
      <td>User</td>
      <td>GET</td>
      <td>Get single user information</td>
      <td> <a href="http://localhost:5001/user/family/1">http://localhost:5001/user/family/1</a>
      </td>
   </tr>
      <tr>
      <td rowspan="2">Location</td>
      <td>GET</td>
      <td>Get all user locations</td>
      <td> <a href="http://localhost:5001/location/all">http://localhost:5001/location/all</a>
      </td>
   </tr>
   <tr>
      <td>GET</td>
      <td>Get user location</td>
      <td> <a href="http://localhost:5001/location/1">http://localhost:5001/location/1</a>
      </td>
   </tr>
   <tr>
      <td>Disaster</td>
      <td>GET</td>
      <td>Get all disasters</td>
      <td>
       <a href="http://localhost:5002/disaster">http://localhost:5002/disaster</a>
      </td>
   </tr>
   <tr>
      <td>Volunteer</td>
      <td>GET</td>
      <td>Get all volunteers for a disaster </td>
      <td> <a href="http://localhost:5003/volunteer">http://localhost:5003/volunteer</a>
      </td>
   </tr>
   <tr>
      <td rowspan="2">Volunteer Event</td>
      <td>GET</td>
      <td>Get all volunteer events</td>
      <td> <a href="http://localhost:5003/volunteer/event">http://localhost:5003/volunteer/event</a>
      </td>
   </tr>
   <tr>
      <td>POST</td>
      <td>Create a volunteer event</td>
      <td> <a href="http://localhost:5003/volunteer/event/create">http://localhost:5003/volunteer/event/create</a>
      </td>
   </tr>
   <tr>
      <td>Affected</td>
      <td>GET</td>
      <td>Get all affected users/casualties</td>
      <td> <a href="http://localhost:5002/affected">http://localhost:5002/affected</a>
   </tr>
</table>

## Contributions

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b /newFeature`)
3. Commit your Changes (`git commit -m 'Add some newFeature'`)
4. Push to the Branch (`git push origin /newFeature`)
5. Open a Pull Request

## Contact
Feel free to contact and connect!

|| Name | Main Role | Github | LinkedIn |
|-----------| ----------- | ----------- | ----------- | ----------- |
|<img src="https://avatars.githubusercontent.com/u/68149788?v=4" width="100"></img>|Tan Zuyi Joey|Project Manager|[![jeezusplays](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/jeezusplays)|[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://linkedin.com/in/joey-tan-zuyi)|
|<img src="https://avatars.githubusercontent.com/u/41113285?v=4" width="100"></img>|Samuel Chung|Software Engineer|[![samchung95](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/samchung95)|[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/samuel-chung-339688154/)|
|<img src="https://avatars.githubusercontent.com/u/111420736?v=4" width="100"></img>|Liow Hong Xiang|Software Engineer|[![hx240](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/hx240)|[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/liowhongxiang/)|
|<img src="https://avatars.githubusercontent.com/u/111410622?v=4" width="100"></img>|Anthony Ho|UX Designer|[![anthonyckho](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/anthonyckho)|[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/anthony-ho-uxdesign/)|


