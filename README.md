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

<!-- [![Vue][Vue.js]][Vue-url]  -->
* HTML
* Bootstrap
* CSS
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

You will need the following software installed in your machine.
* npm
  ```sh
  npm install -g npm
  ```
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

## To Do



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
These are other fellow team members who contributed to this project!
* [Tan Zuyi Joey](https://linkedin.com/in/joey-tan-zuyi)<br>
* [Samuel Chung](https://www.linkedin.com/in/samuel-chung-339688154/)<br>
* [Liow Hong Xiang](https://www.linkedin.com/in/liowhongxiang/)<br>
* Aaron Wong<br>
* John Choong<br>
* [Anthony Ho](https://www.linkedin.com/in/anthony-ho-uxdesign/)<br>

## Acknowledgements
Team: Joey Tan, Hong Xiang, Samuel Chung, Aaron Wong, John Choong, Anthony Ho



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- 
[homepage-screenshot]: src/assets/product.png
[general-screenshot]: src/assets/general_stats.png
[regional-screenshot]: src/assets/regional_stats.png -->