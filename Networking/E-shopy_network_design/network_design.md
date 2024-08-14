# Network Design of E-shopy

## Problem Statement
You are tasked with designing and configuring a secure network for an e-commerce company called "E-Shopy". The company requires a robust network infrastructure to handle both internal operations and customer interactions securely. Your goal is to create a network topology using GNS3 that ensures secure and efficient operation of web services while protecting against external and internal threats.

## **Tasks**:

### Network Topology and Components:

* Firewall: To filter incoming and outgoing traffic.
* DMZ (Demilitarized Zone): A subnet where external-facing services such as web servers and application servers are hosted.
* Web Server: Hosts the company's public-facing website.
* Application Server: Hosts business logic and interacts with the database server.
* Database Server: Stores sensitive customer and transaction data.
* Internal Network: For employee access to internal resources.
* VPN Gateway: Allows secure remote access for employees.
* Router: Connects different network segments and provides internet access.
* Switches: Connects devices within each subnet.

#### Firewall Configuration:

* Allow HTTP/HTTPS traffic to the web server.
* Allow application server traffic only from the web server.
* Restrict database server access to the application server only.
* Block all other traffic between the DMZ and the internal network.

#### DMZ Setup:

* Place the web server and application server in the DMZ.
* Ensure that the DMZ is isolated from the internal network but can communicate with it through controlled channels.

#### Internal Network Configuration:

* Set up a secure internal network for employees.
* Configure VPN access to ensure remote employees can securely access internal resources.

#### Assumptions while designing:

Web content:

* Use basic HTML and CSS files for web content.
* Assume these files are hosted on the web server and accessible through the web.

Database and Application Data:

* Mock data files (JSON or CSV) for products, customers, and orders available from internet.