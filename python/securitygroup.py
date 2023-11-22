import boto3
from botocore.exceptions import ClientError

def _sgrule_add(sg):
    ip_ranges = ['23.99.92.154/32', '3.108.0.29/32', "3.109.224.121/32","52.11.6.209/32", "54.245.40.87/32", "65.1.138.147/32", "65.1.192.116/32", "49.249.54.254/32", "115.117.125.178/32"]
    print(sg)
    sgid, FromPort, ToPort, IpProtocol = sg.split(':')
    for ip_range in ip_ranges:
        try:
            print(f"Adding for {sgid} from {FromPort} to {ToPort} and {ip_range}")
            response = client.authorize_security_group_ingress(
                GroupId=sgid,
                IpPermissions=[
                    {
                        'IpProtocol': 'tcp',
                        'FromPort': int(FromPort),
                        'ToPort': int(ToPort),
                        'IpRanges': [
                            {
                                'CidrIp': ip_range,
                                'Description': "Office IP and OpenVPN IPs"
                            }
                        ]
                    }
                ]
            )
            print('Rule added successfully.')
        except ClientError as e:
            if e.response['Error']['Code'] == 'InvalidPermission.Duplicate':
                print('Rule already exists.')
            else:
                raise e

    return


def _security_group_list(vpc_id):
    sgs = client.describe_security_groups(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}], MaxResults=1000)
    whitelist_sgid = []
    whitelist_all_sgid = []
    for sg in sgs["SecurityGroups"]:
        # print(sg)
        for rule in sg['IpPermissions']:
            # print(rule)
            if len(rule['IpRanges']) > 0:
                for ingress in rule['IpRanges']:
                    matched_ips = ["0.0.0.0/0"]
                    IpProtocol = rule['IpProtocol']
                    if (ingress['CidrIp'] in matched_ips and str(IpProtocol) != "-1") :
                        FromPort = rule['FromPort']
                        # print(FromPort)
                        ToPort = rule['ToPort']
                        if FromPort == 22 and ToPort == 22:
                            sgid = f"{sg['GroupId']}:{FromPort}:{ToPort}:{IpProtocol}"
                            whitelist_sgid.append(sgid)
                    elif ingress['CidrIp'] in matched_ips and str(IpProtocol) == "-1":
                        IpProtocol = rule['IpProtocol']
                        sgid = f"{sg['GroupId']}:{IpProtocol}"
                        whitelist_all_sgid.append(sgid)

    if len(whitelist_all_sgid) > 0 or len(whitelist_sgid) > 0:
        whitelist_sgid_joined = whitelist_all_sgid + whitelist_sgid
        print(whitelist_sgid_joined)


#profile_name = ['tk-bang', 'tk-poc', 'tk-nonprod', 'tk-prod', 'tk-perf', 'tk-uat', 'tk-usa']
profile_name = "poc"
# region_name = ["ap-south-1", "eu-north-1", "eu-west-3", "eu-west-2", "eu-west-1", "ap-northeast-3", "ap-northeast-2", "ap-northeast-1", "ca-central-1", "sa-east-1", "ap-southeast-1", "ap-southeast-2", "eu-central-1", "us-east-1", "us-east-2", "us-west-1", "us-west-2"]
region_name = [ "us-east-1" ]

for region in region_name:
    session = boto3.Session(profile_name=profile_name)
    client = session.client('ec2', region_name=region)
    vpc = client.describe_vpcs(MaxResults=500)
    vpc_ids = []
    for id in vpc['Vpcs']:
        vpc_ids.append(id['VpcId'])

    for vpc in vpc_ids:
        print(f"Gathering Requirements for Account {profile_name} and Region {region} for VPC:{vpc}")
        _security_group_list(vpc_id=vpc)