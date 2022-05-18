import boto3
region = "us-east-1"
image_id = "ami-123456789abcd"
client = boto3.client('ec2',region_name=region)
#bootMode or tpmSupport
response = client.describe_image_attribute(Attribute='tpmSupport',  ImageId=image_id)
print(response)