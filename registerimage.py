import boto3
region = "us-east-1"
image_name = "myimage-tpm20"
snapshot_id1 = "snap-001122ddccbb"
client = boto3.client('ec2',region_name=region)

response = client.register_image(
    Architecture='x86_64',
    BlockDeviceMappings=[
        {
            'DeviceName':'/dev/sda1',
            'Ebs': {
                'SnapshotId':snapshot_id1
            }
        },
    ],
    Name=image_name,
    RootDeviceName='/dev/sda1',
    TpmSupport='v2.0',
    BootMode='uefi'
)
print(response)