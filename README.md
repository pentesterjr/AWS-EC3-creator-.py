#AWS-EC2 creator 

This script provides a high-level overview and can be further customized based on specific requirements and security best practices.

Key Points:This script provides a high-level overview and can be further customized based on specific requirements and security best practices.

    AMIs: Update the AMI IDs with the latest free tier AMIs for Kali Linux, Ubuntu, and Windows.
    Security Group: Creates a security group allowing SSH (port 22) and HTTP (port 80) access. Modify the security group settings as needed for your security requirements.
    Instance Type: Uses t2.micro for free tier eligibility.
    Key Pair: Replace 'your-key-pair-name' with your actual key pair name.
    Error Handling: Handles potential errors, including credential issues.

Prerequisites:

    AWS Credentials: Configure AWS credentials on your system (~/.aws/credentials or using environment variables).
    Permissions: Ensure the IAM role or user has the necessary permissions to create EC2 instances and security groups.
