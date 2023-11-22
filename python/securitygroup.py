import boto3
from botocore.exceptions import ClientError

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