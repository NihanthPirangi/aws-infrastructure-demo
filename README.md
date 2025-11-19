# AWS Infrastructure Demo

This repository contains AWS CloudFormation templates and infrastructure-as-code demonstrating a basic three-tier architecture.

## Architecture Overview
- **Frontend**: Static website hosted on Amazon S3
- **Backend**: AWS Lambda function for serverless compute
- **Security**: IAM roles with least privilege access

## Services Used
- AWS S3 (Static Website Hosting)
- AWS Lambda (Serverless Computing)
- AWS IAM (Identity and Access Management)
- AWS CloudFormation (Infrastructure as Code)

## Deployment
```bash
aws cloudformation create-stack \
  --stack-name my-web-app \
  --template-body file://cloudformation-template.yml \
  --parameters ParameterKey=ProjectName,ParameterValue=my-app
