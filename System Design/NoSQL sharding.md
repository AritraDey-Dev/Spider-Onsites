# Configuration of a NoSQL Database with Sharded Read Requests and Eventual Consistency

## Overview

The objective is to configure a NoSQL database architecture with one writer instance and multiple reader instances. A reverse proxy function will be developed to shard read requests across the reader databases, ensuring efficient load distribution. Additionally, logic will be implemented to maintain eventual consistency between the writer and reader databases.

## Subtasks

### 1. Design Document

- **Create a Design Doc**  
  Develop a design document explaining the implementation strategy, including different tools and technologies that can be used for each aspect of the architecture.

### 2. Database Configuration

- **NoSQL Database Selection**  
  Choose a suitable NoSQL database (e.g., MongoDB, Cassandra, or DynamoDB) that supports multiple instances and sharding.

- **Instance Setup**  
  Configure one writer instance and multiple reader instances, ensuring they can communicate effectively.

### 3. Reverse Proxy Function Implementation

- **Proxy Server Setup**  
  Set up a reverse proxy server using a framework like Nginx or a custom Node.js application to handle incoming requests.

- **Sharding Logic**  
  Implement logic in the reverse proxy to distribute read requests among the available reader instances, ensuring load balancing and efficient resource utilization.

### 4. Eventual Consistency Logic (Bonus Task)

- **Data Replication Strategy**  
  Define a strategy for replicating data from the writer instance to the reader instances, ensuring that updates are propagated efficiently and reliably.

- **Consistency Check Mechanism**  
  Implement a mechanism to check for consistency between the writer and reader databases, using techniques such as versioning or timestamps.

- **Conflict Resolution**  
  Develop logic for handling conflicts that may arise during the replication process, ensuring that eventual consistency is maintained across all instances.

## Resources

- **NoSQL Database Documentation:**
  - [MongoDB](https://docs.mongodb.com/)
  - [Cassandra](https://cassandra.apache.org/doc/latest/)
  - [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- **Reverse Proxy Server Documentation:**
  - [Nginx](https://nginx.org/en/docs/)
  - [Node.js](https://nodejs.org/en/docs/)
- **Sharding and Consistency Strategies:**
  - [MongoDB Sharding](https://docs.mongodb.com/manual/sharding/)
  - [Cassandra Data Replication](https://cassandra.apache.org/doc/latest/architecture/dynamo.html)
  - [Eventual Consistency in NoSQL](https://aws.amazon.com/nosql/)
