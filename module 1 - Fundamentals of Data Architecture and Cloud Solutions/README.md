# Annotations

## Chapter 1 - Fundamentals of Data Architecture
### 1.1 - Why cloud?

The main difference between on-premises architecture and cloud architecture is the cost model. 

- On-premises: Using on-premises we have to buy resources based on predictions and in a good prediction case, a lot of resources will be less useful for some time, in a bad prediction case the resources won’t be enough to attend to the demand.
- Cloud architecture (pay-as-you-go): In a cloud architecture case is possible to buy just the resources that are needed for each situation, in a simple and small project that uses few resources you will pay only for those few resources, if this project became a big one, you don’t need to wait to buy and implement new resources, the cloud elasticity allows to expand the project in a dynamic way.
- IaaS x PaaS x SaaS: IaaS is Virtual Machines; PaaS is SQL Databases; SaaS is Gmail;

### 1.2 - Well-Architected Framework

Well-Architected Framework is a framework created by AWS that defines the five pillars to design a cloud architecture, theses pillars are:

- Operational Excellence
- Security
- Reliability
- Performance Efficiency
- Costs Optimization

<p align="center">
  <img width="400" src="https://user-images.githubusercontent.com/48625700/196230940-6f090e42-1c63-4aa3-ac7c-94f7eb1f549c.png">
</p>

### 1.3 - Operational Excellence

The main topics of operational excellence are change management and automatization, fast and efficient response for infrastructure events, and guidelines definitions for daily operations. Those topics are related to IaC (infrastructure as code), small + frequent + reversible changes, frequent operational procedures refinements, failure and event predictions, and documentation production.

### 1.4 - Security

The main topics of security are to protect information and active systems and besides that create value for business through risk evaluations and mitigation strategies. Those topics are related to identifying and managing the profiles on each environment (authorizations, authentications, and user tracking), applying security for all layers, protecting data in traffic and in rest, preparing the system for security events, and guaranteeing data integrity and confidentiality.

### 1.5 - Reliability

The main topics of reliability are avoiding and recovering from failures to attend to business demands. Those topics are related to automating recovery procedures, frequent recovery procedure tests, horizontal scalability of resources to increase availability, and change management in automated processes.

### 1.6 - Performance Efficiency

The main topics of performance efficiency are to keep attending to the business demand in an efficient way while the project is growing, and the tools are renewing themselves. Those topics are related to spreading advanced technologies into the team, the uses of serverless architecture and resources, and the exploration and experiments of new technologies in a periodic way.

### 1.7 - Costs Optimization

The main idea here is to choose the resources with minor prices that create value for the business. This idea is related to the cloud model consumption (ex: CapEx or OpEx), cost measuring and cost tracking of the development environments, mitigation (or elimination) of operational expenses with data centers and hardware, and cost segmentation.

## Chapter 2 - Data Architecture Models on Cloud

## Chapter 3 - Hands-on

## Chapter 4 - IaC Infrastructure as Code

## Chapter 5 - Use cases (hands-on)

## Chapter 6 - Review
