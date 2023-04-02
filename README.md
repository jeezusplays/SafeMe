# SafeMe
## About this Project
SafeMe is a <b>natural disaster relief</b> mobile application that aims to provide real-time updates on individuals dealing with disasters such as: earthquakes, cyclones, floods, volcanoes, droughts and forest fires. 

This application is targeted towards two types of users – <b>Public Users</b> and <b>Government</b>. Each user type has access to different features that best suit their usage needs. For Public Users, they are able to:
* Receive a danger notification when in the risk of being in danger
* View family members safety through a status dashboard
* Acknowledge safety status notification or prompts
* Accept volunteer request for volunteer event – <i>Event to get volunteers to help out after a natural disaster</i>

For Government, they are able to:
* View the list of possible casualties in affected disaster areas
* Access GPS coordinates of affected individuals that have not acknowledged safety status notifications
* Create and manage volunteer event

### Assumptions
The following functions are assumed to be completed:

Public Users:
* Create and join a family – <i>A group of people that can track each other in real-time</i>
* Announce to family when no longer in risk of being in danger
* Receive alerts of other family members when they are in the risk of being in danger

Government:
* Announce the list of safe individuals

Other Assumptions:
* A user can only be affected by 1 disaster at any given time
* Manager microservices are used for security and scaling purposes
* Disaster & Volunteer events have a start and end datetimes
* For the purpose of demonstration, users are in a family. 

## Built With
### Major Frameworks / Libraries
This section lists any major frameworks/libraries used to develop SafeMe.

* [HTML](https://www.w3schools.com/html/)
* [Bootstrap](https://getbootstrap.com/)
* [CSS](https://www.w3schools.com/css/)
* [Vue.js](https://vuejs.org/)
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [AMQP](https://www.amqp.org/)

### APIs
This are the APIs used to provide SafeMe with data on natural disasters.
* [Kong API Gateway](https://docs.konghq.com/gateway/latest/)
* [GDACS API](https://www.gdacs.org/)

## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
To get started and use the **Send Email Microservice**, you will need to follow the instructions on creating a [Google App Password](https://support.google.com/accounts/answer/185833?visit_id=638159212202344047-122164626).

You will also need the following software installed in your machine.
* [Visual Studio Code](https://code.visualstudio.com/)
* [Docker](https://www.docker.com/)
* [Postman](https://www.postman.com/) <i>(for testing)</i>
* [Python](https://www.python.org/)
* [Node.js](https://nodejs.org/en/)
* [npm](https://www.npmjs.com/)

<!-- To run this project locally on your machine, follow the following steps.
* npm
  ```sh
  npm install -g npm
  ``` -->
### Installation

_Instructions on how to install this respository onto your local machine._

1. Clone the repo
   ```sh
   git clone https://github.com/samchung95/SafeMe
   ```
<!-- 2. Create a Firebase Project and add service account key json to api folder
3. Change service account key json to "serviceAccountKey.json" -->
2. Install NPM packages
   ```sh
   npm install
   ```
3. Run vue
   ```sh
   npm run dev
   ```
4. Go to your local host
   ```sh
   http://localhost:8080 or https://localhost:8081
   ```

## Usage

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b /newFeature`)
3. Commit your Changes (`git commit -m 'Add some newFeature'`)
4. Push to the Branch (`git push origin /newFeature`)
5. Open a Pull Request

## Contact
Feel free to contact and connect!
<table>
   <tr>
      <th></th>
      <th>Name</th>
      <th>Main Role</th>
      <th>LinkedIn</th>
   </tr>
   <tr>
      <td align="center">
         <a href="https://linkedin.com/in/joey-tan-zuyi"><img src="https://avatars.githubusercontent.com/u/68149788?v=4" width="100px;" alt=""/></a>
      </td>
      <td>Joey Tan</td>
      <td>Project Manager</td>
      <td><a href="https://linkedin.com/in/joey-tan-zuyi">LinkedIn</a></td>
   </tr>
   <tr>
      <td align="center">
         <a href="https://www.linkedin.com/in/samuel-chung-339688154/"><img src="https://avatars.githubusercontent.com/u/41113285?v=4" width="100px;" alt=""/></a>
      </td>
      <td>Samuel Chung</td>
      <td>Software Engineer</td>
      <td><a href="https://www.linkedin.com/in/samuel-chung-339688154/">LinkedIn</a></td>
   </tr>
   <tr>
      <td align="center">
         <a href="https://www.linkedin.com/in/liowhongxiang/"><img src="https://avatars.githubusercontent.com/u/111420736?v=4" width="100px;" alt=""/></a>
      </td>
      <td>Liow Hong Xiang</td>
      <td>Software Engineer</td>
      <td><a href="https://www.linkedin.com/in/liowhongxiang/">LinkedIn</a></td>
   </tr>
   <tr>
      <td align="center">
         <a href="https://www.linkedin.com/in/anthony-ho-uxdesign/"><img src="https://avatars.githubusercontent.com/u/111410622?v=4" width="100px;" alt=""/></a>
      </td>
      <td>Anthony Ho</td>
      <td>UX Designer</td>
      <td><a href="https://www.linkedin.com/in/anthony-ho-uxdesign/">LinkedIn</a></td>
</table>

## Acknowledgements
These are other fellow team members who contributed to this project!
* [Tan Zuyi Joey](https://linkedin.com/in/joey-tan-zuyi)
* [Samuel Chung](https://www.linkedin.com/in/samuel-chung-339688154/)
* [Liow Hong Xiang](https://www.linkedin.com/in/liowhongxiang/)
* [Anthony Ho](https://www.linkedin.com/in/anthony-ho-uxdesign/)
* Aaron Wong
* John Choong