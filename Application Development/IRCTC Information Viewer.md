# IRCTC PNR Information Application

## Problem Statement
The goal is to create an application that allows users to input their IRCTC PNR number or travel details to fetch relevant information such as berth number, train status, and other travel-related data. This information will be gathered through web crawling from various websites that provide PNR status and train information.

## Overview
This application will provide users with a seamless way to check their travel status by entering their PNR number. It will utilize web crawling to gather data from multiple sources, ensuring that users receive accurate and timely information regarding their train journeys.

## Subtasks

### 1. User Input Interface
- **Functionality:** Design a user-friendly interface where users can enter their PNR number or travel details.
- **Requirements:**
  - Include validation to ensure the PNR number is in the correct format.

### 2. Web Crawling Functionality
- **Functionality:** Implement web crawling to extract data from sources that provide PNR status and train information.
- **Requirements:**
  - Ensure the crawler can handle various website structures and extract relevant information such as berth number, train status, and platform details.

### 3. Data Aggregation and Processing
- **Functionality:** Aggregate the data fetched from different sources to provide a comprehensive view of the user's travel status.
- **Requirements:**
  - Implement logic to handle discrepancies in data from different sources and present the most accurate information.

### 4. Background Fetching and Caching
- **Functionality:** Develop functionality to periodically fetch updates for the entered PNR number, allowing users to receive real-time updates on their travel status.
- **Requirements:**
  - Implement caching to store previously fetched data for quick access and to reduce the load on web sources.

### 5. Notification System (Bonus Task)
- **Functionality:** Create a notification system to alert users of significant updates regarding their travel status, such as changes in berth allocation or train delays.
