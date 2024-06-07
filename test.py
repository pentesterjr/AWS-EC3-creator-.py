import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Define a function to create an EC2 instance
def create_ec2_instance(ami_choice):
    ec2 = boto3.resource('ec2')
    client = boto3.client('ec2')

    # Define the AMI IDs (make sure these are up-to-date)
    ami_dict = {
        'kali': 'ami-0aef57767f5404a3c',  # Example AMI ID for Kali Linux
        'ubuntu': 'ami-0c55b159cbfafe1f0',  # Example AMI ID for Ubuntu
        'windows': 'ami-0d8f6eb4f641ef691'  # Example AMI ID for Windows
    }

    if ami_choice not in ami_dict:
        raise ValueError("Invalid AMI choice. Valid choices are: 'kali', 'ubuntu', 'windows'.")

    ami_id = ami_dict[ami_choice]

    # Security Group configuration
    security_group = client.create_security_group(
        Description='allow SSH and HTTP',
        GroupName='SecGroup'
    )

    client.authorize_security_group_ingress(
        GroupId=security_group['GroupId'],
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            },
            {
                'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
            },
        ]
    )

    # Create a new EC2 instance
    instances = ec2.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',  # Using a free tier instance type
        KeyName='your-key-pair-name',  # Make sure you have a key pair created
        SecurityGroupIds=[security_group['GroupId']]
    )

    print(f'Created instance with ID: {instances[0].id}')

# Main function to prompt user for AMI choice
def main():
    print("Choose an AMI to launch an EC2 instance:")
    print("1. Kali Linux")
    print("2. Ubuntu")
    print("3. Windows")
    choice = input("Enter the number of your choice: ")

    ami_choice_map = {
        '1': 'kali',
        '2': 'ubuntu',
        '3': 'windows'
    }

    ami_choice = ami_choice_map.get(choice)

    if not ami_choice:
        print("Invalid choice. Exiting.")
        return

    try:
        create_ec2_instance(ami_choice)
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials not found. Please configure your AWS credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
