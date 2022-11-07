# Annotations 📜✍️

## Chapter 1 - Fundamentals of Data Architecture
### 1.1 - Why cloud?

The main difference between on-premises architecture and cloud architecture is the cost model. 

- On-premises: Using on-premises we have to buy resources based on predictions and in a good prediction case, a lot of resources will be less useful for some time, in a bad prediction case the resources won’t be enough to attend to the demand.
- Cloud architecture (pay-as-you-go): In a cloud architecture case is possible to buy just the resources that are needed for each situation, in a simple and small project that uses few resources you will pay only for those few resources, if this project became a big one, you don’t need to wait to buy and implement new resources, the cloud elasticity allows to expand the project in a dynamic way.
- IaaS x PaaS x SaaS: IaaS is Virtual Machine; PaaS is SQL Database; SaaS is Gmail;

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

### 2.1 - DaaS Database as a Service (Relational)

- AWS resources
    - RDS (Relational Database Service): It is compatible with Oracle, Microsoft SQL Server, MySQL, PostgreSQL, MariaDB, and the AWS serverless option Amazon Aurora.
    - DW solutions: Amazon Redshift and Amazon Redshift Spectrum.
- Azure resources
    - Relational solutions: Azure SQL Database, Azure SQL Server, SQL Server in VM, Azure Database for PostgreSQL Azure Database for MySQL, Azure Database for MariaDB.
    - DW solutions: Azure SQL Data Warehouse and Azure Synapse Analytics.
- GCP resources
    - Relational solutions: Bare Mental Solution, Cloud SQL (it is compatible with MySQL, PostgreSQL, and Microsoft SQL Server), Cloud Spanner (it is compatible with Oracle and DynamoDB).
    - DW solutions: BigQuery.

### 2.2 - DaaS Database as a Service (Non-relational)

- AWS resources
    - DynamoDB (key-value)
    - DocumentDB (it is compatible with MongoDB)
    - Amazon Neptune (graph)
    - Amazon Elasticache (database in memory, it is compatible with Memcached and Redis)
    - Amazon ElasticSearch Service
- Azure resources
    - Azure Cosmos DB: it is compatible with key-value, document-oriented, and graph database types
    - Azure Cache for Redis (database in memory, it is compatible with Redis)
    - Elastic in Azure (Elastic Search)
- GCP resources
    - Cloud BigTable (key-value)
    - Firestore (document-oriented)
    - Firebase Realtime Database (document-oriented)
    - Memorystore (database in memory, it is compatible with Redis and Memcached)
    - Integration with partners: MongoDB Atlas, Datastax, Redis Labs, Neo4j, and ElasticSearch.

### 2.3 - Data Lake (Architecture Design)

- Lambda Architecture: what defines this architecture is the existence of two layers, the batch layer, and the speed layer. Both layers work in parallel, the batch layer works with data batches and the speed layer works in real-time or near-real-time. It is important to cite the serving layer too, it is the layer of data consumption that receives that from the batch layer.
    - Advantages: it is helpful for attending requirements that have these two necessities (historical data and real-time data)
    - Disadvantages: The simultaneous processing usually requires a lot of data storage and sometimes causes duplicates

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/48625700/196685326-f02ae667-e64e-4bb1-bfd1-5caa3d57cafe.png">
</p>

- Kappa Architecture: this architecture has only one layer, that calls Data Processing Layer. This unique layer is a kind of speed layer, that works in real-time or near-real-time, but also works with batches. So, it solves the problem of duplicates that the Lambda architecture has.
    - Advantages: it avoids duplicates and reduces the data storage space (when we compare it with Lambda architecture)
    - Disadvantages: the architecture is hard to be implemented especially for the data reprocessing of streaming

<p align="center">
  <img width="650" src="https://user-images.githubusercontent.com/48625700/196685419-d314b93e-fb68-441a-8bd2-c662d232cc1d.png">
</p>

- Unifield Architecture: it is very similar to Lambda architecture, the novelty here is that the machine learning layer is combined with the speed layer.
    - Advantages: the possibility to create real-time machine learning can offer a lot of insights for the users
    - Disadvantages: it is more complex to be implemented

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/48625700/196685477-739ac305-b72e-4389-a3d6-afab97b290fc.jpeg">
</p>

- Lakehouse Architecture: it is a modern structure that allows flexibility, cost optimization, and scalability for the Data Lake, besides that it also brings ACID operations that are common in relational databases. Data Lakehouse is the mix between Data Lake and Data Warehouse, it gets the best from these two architectures to create a new one.
    - Main tools: delta lake + query engines
    
<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/48625700/197502558-044519b0-dec1-45b2-ad21-465b5a0913cd.png">
</p>

### 2.4 - Data Lake (Storage - Amazon S3)

Amazon S3 (Simple Storage Service) is the main storage solution in AWS. The main features are:

- Volume limit: limitless. There is just a limit for each object, and each one has to have up to 5 TB.
- Durability: 11 nines (99,999999999%)
- Replication: it does automatic replication for all objects in all disponibility zones of the region. We only need to choose the region.
- Costs: it has the pay-as-you-go model.
    - Pay:
        1. GBs per month; 
        2. Data traffic for other regions or out of AWS;
        3. Queries PUT, COPY, POST, LIST, and GET;
    - Non-pay:
        1. Data traffic to put data into S3;
        2. Data traffic for AWS services at the same region;

### 2.5 - Data Lake (Data Ingestion)

- Batch ingestion: Spark; Python; Apache Nifi;
- Real-time: Kafka (near real-time);
- Managed Services:
    - AWS: DMS (Database Migration Service); Amazon Kinesis;
    - GCP: Google PubSub;
    - Azure: Azure EventHub;

### 2.6 - Data Lake (Big Data Processing)

- Open source tools:
    - Apache Spark (Batch and Real-time)
    - ksqlDB (Kafka - Real-time)
- Managed tools:
    - AWS:
        - EMR: it is a PaaS service that is compatible with Hadoop, Spark, Hive, and others;
        - Glue Job: it is a SaaS service that uses mainly spark;
        - Kinesis Data Analytics: a resource for data streaming solution (it seems Kafka);
    - Azure:
        - HD Insight: batch and real-time processing;
        - Azure Stream Analytics: data streaming solution (it seems Kafka);
    - Google Cloud:
        - Dataproc;
        - Pub/Sub;
        - BigQuery
    - Databricks

### 2.7 - Data Lake (Data Consumption - DW & Engines)

- Managed engines:
    - AWS:
        - Amazon Athena (it is combined with Glue Data Catalog);
    - Azure:
        - Azure Data Lake Analytics;
    - Google Cloud:
        - BigQuery is a DW service, but it is the nearest resource that GCP has
- Non-managed engines:
    - Presto;
    - Trino;
    - Apache Drill;
    - Dremio;

## Chapter 4 - IaC Infrastructure as Code

### 4.1 - IaC Tools

- Why IaC?
    - Automation;
    - Cycle time: velocity to implement;
    - Easy replication for other environments (dev, prod, etc);
    - Reliability: easy and fast to rebuild in a disaster recovery situation;
- Open-source tools:
    - Terraform;
    - Pulimi;
    - Chef infra;
    - Puppet;
- Cloud-based:
    - AWS CloudFormation;
    - Azure Resource Manager;
    - Google Cloud Deployment Manager;
