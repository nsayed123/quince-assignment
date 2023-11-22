# Python script to find all open security groups in an AWS account

This repository contains the python script to find all open security groups in an AWS account.

## Requirements

To install and run these example you need:
- Python 3.8+
- pip3
- git (only to clone this repository)
- Following packages required
    - boto3
    - botocore

## Installation

The commands below set everything up to run the examples:
```
$ git clone https://github.com/nsayed123/quince-assignment.git
$ cd quince-assignment/python
```

Install the following packages

- pip3 install boto3
- pip3 install botocore

or

- pip3 install -r requirements.txt

## Changes

1. Create an aws credentials profile.
```
aws configure --profile <profilename>
```
2. Update the profile name in the script at line 34.
3. Update the region in the script at line 36, pass it has a list of regions.

## Run

Make sure you are in the right directory "quince-assignment/python"
```
python3 securitygroup.py

Ex: python3 securitygroup.py
```




