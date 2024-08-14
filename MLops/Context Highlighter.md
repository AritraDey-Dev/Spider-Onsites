# Summarization Chrome Extension with Highlight Storage

## Problem Statement
The goal is to create a Chrome extension that summarizes content from specific websites (such as Reddit or YouTube) and allows users to highlight key points. When a highlight is clicked, it will be stored in a database for later retrieval. This extension will enhance user engagement by enabling users to save and revisit important information easily.

## Overview
This Chrome extension will provide users with concise summaries of content from Reddit and YouTube. Users will be able to highlight important points and store them in a database for future reference. The extension will utilize machine learning APIs for summarization and a database for storing highlights.

## Subtasks

### 1. Summarization Functionality
- **Integrate an API** (like Cohere.ai or OpenAI) to generate concise summaries of the content from the specified websites.
- **Ensure the summarization** can handle different types of content, such as comments on Reddit or video transcripts on YouTube.

### 2. Highlighting Mechanism
- **Implement a user interface** that allows users to select and highlight text within the web page.
- **Create a mechanism** to capture and store the highlighted text along with a summarization of the context of the highlighted text. (it should be prompted to create a summary based on the highlighted text, and not just the generic summary of the page)

### 3. Database Integration
- **Set up a database** (e.g., Firebase, MongoDB) to store the highlights and summaries for each user.
- **Develop an API** to handle CRUD operations (Create, Read, Update, Delete) for the stored highlights.
- **Use Postman** to test out these routes.
