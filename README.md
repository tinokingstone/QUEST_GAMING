# QAProject3
**[presentation link](https://docs.google.com/presentation/d/1gGrvONwapNHR8NOhoLwujwI5iRfyucv5LorXDcGmSqM/edit?usp=sharing)**


## Contents 
* [Introduction](#Introduction) -*Project Brief, Intended Solution*
* [CI/CD Pipeline](#dep_pipeline) -*Description, Pipeline*
* [Planning](#planning) -*Plans, Members, Roles, Decision-Making, Sprints*
* [User Stories](#UserCases) -*Developer Stories, User's Stories*
* [Risk Analysis](#Risk) 
* [Technologies Used](#Technology) -*Ansible, Azure, Git, Jenkins, Kubernetes, Terraform, Nginx* 
* [Testing](#Testing)
* [Deployment](#Deployment) -*Ansible, Terraform, Kubernetes*
* [Costs](#Costs) 
* [Project Conclusion](#Conclusion)  
* [Authors](#Author)
* [Acknowledgement](#acknowledgment)


<a name="Introduction"></a>
## Introduction 
#### *Project Brief*
The brief for this project was to plan, design and implement a solution for automating the deployments and development workflows of the following projects:
 
**[Frontend client](https://github.com/spring-petclinic/spring-petclinic-angular)**

**[Backend API](https://github.com/spring-petclinic/spring-petclinic-rest)**

More info on the [Source Code](https://projects.spring.io/spring-petclinic/)
 
 
#### *Intended Solution*
As a team we decided the direction of our part of the project would utilise technologies that we were either familiar with or had related knowledge that could be transferable to a different technology. We intended to create multiple environments for development, for deployment and load balancing whilst follwoing our planned pipeline. 

The creating would be handled using Ansible, Terraform and Kubernetes. The deployment aspect of this is intended to have automated build and redeployment based on any change made to the respective github repositories for the backend and frontend and handled with Jenkins. The load balancing for incoming traffic would be handled with Nginx, whilst costs would be tracked through the Azure Cost Tracking Utility Tool.

<a name="dep_pipeline"></a>
## CI/CD Pipeline
#### *Description*
The pipeline structure we decided upon made use of Version control system Git with repositories hosted by Github, this is where all files relevant to the project will be stored on relevant branches.

Terraform is being used to actively create the Virtual Machines through the Azure CLI, then Ansible is being applied to create and set up the environments, Git is then used to pull relevant files to their intended environments, once the source code is editted and pushed (uploaded) to Git this will invoke Jenkins to build, test and deploy the product using Kubernetes. 

#### *Pipeline*

![](https://github.com/the-ci-squad/QAProject3/blob/tino_terraform_ansible/README_FILES/FINAL-CI-PIPELINE-DESIGN.png)


<a name="planning"></a>
## Planning
*Plans, Members, Roles, Decision-Making*
#### *Plans*
As this project has such large goal with a sample amount of time and no communication with developers it was important to have adequate planning, internal communication methods and project management in place. For this we decided that we would have 1 a daily Scrum and subsequent meetings when necessary. The scrums were used largely for most of the planning but unlike traditional planning meetings scrums core values are to instill courage, focus, respect, openness and commitment in relation to a project and its team. To track our plan we used Trello, an online, Kanban-style, list-making application, to keep track of progress, any issues and completed tasks. To communicate we utilised Microsoft Teams as it was convenient and had screen sharing capablities which would help with troubleshooting team members' issues.  

A link for further information about [Scrums](https://www.scrum.org/resources/what-is-scrum), [Teams](https://www.microsoft.com/en-gb/microsoft-365/microsoft-teams/group-chat-software) and [Trello](https://help.trello.com/article/708-what-is-trello)


#### *Team members*
Tino - https://github.com/tinokingstone

Benjie - https://github.com/BenjieA

Stef - https://github.com/stefangelova

Harman - https://github.com/hman191



#### *Roles/Tasks:* 
Stef Angelova- Kubernetes/Docker

Tino Mushangwe- Terraform/Ansible/Docker

Benjie Asare- Jenkins/Ansible/Docker

Harman Marwaha- SQL/General Assistance/Docker

#### *Scrum Master* 
Harman Marwaha

#### *Decision-Making*
During the decision making process was driven by Trainer Jay Grindrod acting as the Product Owner and listening in on Scrums and certain meeting that would coincide with the Product Owners interests. Within the team any major decisons would be discussed and the approach would be decided based on which option was deemed most logical. These approaches would then be added to the Trello/planning board in order to keep track of the progress being made.

### Sprints
#### *Sprint 1*
![](https://github.com/the-ci-squad/QAProject3/blob/master/README_FILES/Sprint1.PNG)
#### *Sprint 2*
![](https://github.com/the-ci-squad/QAProject3/blob/master/README_FILES/Sprint2.PNG)
#### *Sprint 3*
![](https://github.com/the-ci-squad/QAProject3/blob/master/README_FILES/Sprint3.PNG)


<a name="UserCases"></a>
## User Stories
#### *Developer Stories*
+ As a developer, I would like to deploy my application using the CI pipeline in order to allow for continuous integration
+ As a developer i would like access to a development environment to test and build my application
+ As a developer I would like the database to be communicating with the back-end in order to display information and so that users can add their own if required
+ As a developer, I would prefer minimal down-time while the website is updating to ensure the smoothest user experience possible
+ As a developer, I would like for the front-end to be the only part accessible to users in order to ensure only devs and engineers can make changes to the functionality/code
+ As a developer, I would like to see an acceptable percentage coverage and majority of testing to pass in order to ensure the application is reliable

#### *User's Stories*
+ As a user, I would like the website to be secure to ensure safety of my personal information
+ As a user, I would like to input my own information to update the database with my information


<a name="Risk"></a>
## Risk Assessment

![](https://github.com/the-ci-squad/QAProject3/blob/master/README_FILES/Capture.PNG)
![](https://github.com/the-ci-squad/QAProject3/blob/master/README_FILES/Capture2.PNG)
![](https://github.com/the-ci-squad/QAProject3/blob/master/README_FILES/Capture3.PNG)

<a name="Technology"></a>
## Technologies Used

+ Ansible
+ Azure
+ Docker
+ Jenkins
+ Kubernetes
+ Nginx
+ Terraform
+ Trello

<a name="Testing"></a>
## Testing
#### *Test results for backend*
![](https://github.com/the-ci-squad/QAProject3/blob/master/README_FILES/test%20result.PNG)

<a name="Deployment"></a>
## Deployment
#### *Ansible*
Ansible is used to configure the dependencies required to have functional development and deployment envirnoments.Used within the continuous integration aspect of the project, sets up the environment by downloading and installing certain packages before deployment of the machine/environment. This was used to set up the CI Server used for Jenkins deployment, machines with the databases requirements and initialisation, Docker installation, Kubernetes, load balancing with Nginx and common installastions needing on every machine with our project 

#### *Terraform*
Terraform is used to create and deploy infrastructure on a large scale. Terraform is used to define the development environment, deployment environment, load balancing and CI machines

#### *Kubernetes*
Kubernetes is a container-orchestration system for automating application deployment and scaling


<a name="Costs"></a>
## Costs 
To run the development environment we estimate a total of £31.80 a month based on how much has been spent by the time of finishing the project.
To run the deployment environment we estimate it will cost a total of £30.60 a month based on how much was pent by the time of finishing the project.
The cost for running the Kubernetes cluster is estimated at £44.00 for a month based on the figures collected by the finishing of the project.
This takes the total running cost to approximately £106.40 to run the project a month, this could possibly be higher or lower depending on traffic, changes in VM costs, number of Nodes deployed by Kubernetes


<a name="Conclusion"></a>
## Project Conclusion
As a team we were able to utilise our planned technologies and applied our transferable skills to different unfamiliar technology suchas Maven and AngularJS. We created multiple environments for development, for deployment and load balancing in accordance with our planned pipeline. The creation using Ansible, Terraform and Kubernetes all went according to planned though there were issues faced along the way as there parts of the original source code that we were not familiar with. The tasks were handled well by the assigned team members and with what we were able to complete we are satisfied with its performance and our own performance during this task. 

<a name="authors"></a>
## Authors
Benjie, Tino, Stef and Harman

<a name="acknowledgment"></a>
## Acknowledgments
- *Our Families, Jay and Everyone else* Thanks for all the help and support
