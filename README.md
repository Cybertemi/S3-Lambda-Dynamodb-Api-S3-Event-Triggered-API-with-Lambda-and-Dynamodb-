# ☁️ AWS Serverless File Metadata API

This project implements a fully serverless AWS application that stores metadata of uploaded files and exposes the data through an API. It combines AWS S3, Lambda, DynamoDB and API Gateway using Python and Boto3.


## 🔧 What It Does

1. A file is uploaded to an S3 bucket
2. An S3 event triggers a Lambda function
3. The Lambda function gives response by extracting the filename from uploaded file and stores the data in a DynamoDB table
4. A RESTful API via API Gateway retrieves the stored metadata using a GET request


## How It Works

Ever wondered what happens when you make a request to a website from your browser?

That’s where API Gateway and AWS Lambda come in.

The API Gateway acts as the middleman between the frontend (user/browser) and backend (Lambda and DynamoDB). When a user makes a request in the browser, it hits the API Gateway, which then triggers the Lambda function. Based on the request method (GET, POST, etc.), Lambda fetches or updates data in DynamoDB and the response is returned to the user.

Similarly, AWS also allows automatic triggers from services like S3 such that When a user uploads a file to the S3 bucket, an event notification automatically invokes the same Lambda function. The Lambda function then  extracts metadata and stores it in DynamoDB.

Using API Gateway, this metadata can then be retrieved through a public HTTP GET request which enables real-time access to stored data, all without managing servers.


## Prerequisites

- **S3** – File storage and event trigger source  
- **Lambda** – Event-driven compute  
- **DynamoDB** – NoSQL metadata storage  
- **API Gateway** – Public RESTful API  
- **Boto3** – Used to interact with AWS services programmatically


## 🚀 Features

- Upload files to S3 using Python & Boto3
- Automatically trigger metadata extraction via Lambda
- Store metadata in DynamoDB 
- Retrieve metadata through a deployed HTTP endpoint
- Fully serverless, event-driven, and scalable

---

## 📌 Deployment Steps

### ✅ 1. S3 Bucket
- Created using Boto3
- Uploaded a file
### ✅ 2. DynamoDB Table
- Table name: `Students`

### ✅ 3. Lambda Function
- Written in Python
- Deployed and tested via AWS Console
- Connected to S3 bucket as a trigger

### ✅ 4. API Gateway
- REST API created
- Resource connected to Lambda
- `GET` method created and deployed
- Endpoint available via `prod` stage

### Invoke URL
Use the following format to access metadata:


GET https://hwqzfjfeig.execute-api.eu-north-1.amazonaws.com/prod/Students


👨🏽‍💻 Author
Temitope Ilori
Cybersecurity & Cloud Security Analyst
LinkedIn Profile https://www.linkedin.com/in/iloritemi

