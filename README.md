# DoorDash Delivery Data 

Welcome to the DoorDash Delivery Data Processing project! This project automates the processing of daily delivery data from DoorDash using AWS services. By leveraging AWS Lambda, Amazon S3, and Amazon SNS, this solution streamlines the handling of delivery records and provides efficient notifications regarding processing outcomes.

## Overview

The project encompasses the following key components:

- Uploading daily delivery data in JSON format to an S3 bucket (`doordash-landing-zn`).
- Processing the uploaded data using an AWS Lambda function triggered by S3 events.
- Filtering the delivery records based on status and saving the filtered data to another S3 bucket (`doordash-target-zn`).
- Sending processing outcome notifications via Amazon SNS.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [AWS CodeBuild](#aws-codebuild)
4. [Contributing](#contributing)

## Installation

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.10
- AWS CLI

### Setup

1. Clone the repository:

    ```bash
    $ git clone https://github.com/vishhaaal/DoorDash-Delivery-Data.git
    $ cd DoorDash-Delivery-Data
    ```

2. Install dependencies:

    ```bash
    $ pip install -r requirements.txt
    ```

3. Set up AWS credentials and configure AWS CLI.

## Usage

Follow these steps to utilize the DoorDash Delivery Data Processing:

1. Upload daily delivery data JSON files to the `doordash-landing-zn` S3 bucket.
   
2. AWS Lambda function will automatically trigger upon file upload, processing the data and saving filtered records to the `doordash-target-zn` bucket.

3. Receive notifications regarding processing outcomes via Amazon SNS.

## AWS CodeBuild

To ensure smooth deployment and continuous integration, this project includes AWS CodeBuild. The CodeBuild project is linked to the GitHub repository, and the `buildspec.yml` file automates the deployment process.

To set up CodeBuild:

1. Host your Lambda function code on GitHub.
2. Create an AWS CodeBuild project linked to your GitHub repository.
3. Configure the `buildspec.yml` file to automate deployment of your Lambda function code updates.

## Contributing

We welcome contributions from the community! If you encounter any issues or have suggestions for improvements, please don't hesitate to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.
