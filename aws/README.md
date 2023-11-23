# Setup AWS Cloudwatch Alarms from Logs using Terraform

This repository contains the setup AWS Cloudwatch Alarms from Logs using Terraform.

## Requirements

To install and run this example you need:
- Terraform
- aws cli
- git (only to clone this repository)



## Installation

The commands below set everything up to run the examples:
```
$ git clone https://github.com/nsayed123/quince-assignment.git
$ cd quince-assignment/aws/cloudwatch_alaram
```

## NOTE:
1. Before running the terraform init change the profile and region in the provider.tf file.
2. Create an aws credentials profile.
```
aws configure --profile <profilename>
```
3. Update the profile name in the provider.tf.


## Run

Make sure you are in the right directory "quince-assignment/aws/cloudwatch_alaram"
```
terraform init
terraform plan
terraform apply

If everything looks good type `yes` and hit `Enter` 
```


## Destroy
If you want to destroy run
```
terraform destroy
```

