#! usr/bin/env python3
import boto3
import argparse
import requests

#Author Tim Kosnik
#Date 02-16-2019
#Retrieve Instance Metadata
response = requests.get("http://169.254.169.254/latest/dynamic/instance-identity/document")
response_json = response.json()
region = response_json.get('region')
instance_id = response_json.get('instanceId')
image_id = response_json.get('imageId')
availability_zone = response_json.get('availabilityZone')
instance_type = response_json.get('instance_type')

ec2 = boto3.resource('ec2', region_name=region)
"""
ec2 = boto3.resource('ec2', region_name='us-east-1')
for instance in ec2.instances.all():
    tag= instance.tags
    #print ("TAG",tag)
    c=0
    for ins in tag:
        if  ins['Key'] == 'ssh':
           c= c+1
    if (c ==0):
        print ('no ssh', instance.tags)
        instance.create_tags(Tags=[{
                "Key":"ssh",
                "Value":"compliant"
            }])
"""
#Set Tags
instances = [i for i in ec2.instances.filter(Filters=[{'Name':'tag:ssh', 'Values':['compliant']}])]
for instance in instances:
        print ('ssh', instance)
        instance.delete_tags(Tags=[{
            "Key":"ssh",
            "Value":"compliant"
            }])
        instance.create_tags(Tags=[{
            "Key":"ssh",
            "Value":"compromised"
            }])
for instance in ec2.instances.all():
    tag= instance.tags
    print ("TAG",tag)
    if tag != None:
        print ("TAG",tag)
        c=0
        for ins in tag:
                if  ins['Key'] == 'ssh':
                        c= c+1
        if (c ==0):
                print ('no ssh', instance.tags)
                instance.create_tags(Tags=[{
                        "Key":"ssh",
                        "Value":"compliant"
                }])
    elif tag == None:
        instance.create_tags(Tags=[{
                "Key":"ssh",
               "Value":"compliant"
        }])