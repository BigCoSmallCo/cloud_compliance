#! usr/bin/env python3
import argparse
import time
import requests
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

METADATA_URL = 'http://metadata.google.internal/computeMetadata/v1/'
METADATA_HEADER = {'Metadata-Flavor':'Google'}

def get_project():
    response = requests.get('{}project/project-id'.format(METADATA_URL),
            headers=METADATA_HEADER).text
    return response

def get_zone():
    response = requests.get('{}instance/zone'.format(METADATA_URL),
            headers=METADATA_HEADER).text
    return response.rsplit('/',1)[1]

def get_instance():
    response = str(requests.get('{}instance/id'.format(METADATA_URL),
            headers=METADATA_HEADER).json())
    return response

def get_instance_data(service, project, zone, instance):
    request = service.instances().get(
            project=project, zone=zone,
            instance=instance)
    response = request.execute()
    return response

def set_labels(service, project, zone, instance, first_run=False, ssh=False):
    data = get_instance_data(service, project, zone, instance)
    if 'label' in data.keys():
        request_body = {
                'labelFingerprint' : data['labelFingerprint'],
                'labels' : data['labels']}
    else:
        request_body = {
                'labelFingerprint' : data['labelFingerprint'],
                'labels' : {}}
    if first_run:
        ssh_key = "ssh"
        if ssh_key in request_body['labels']:
            pass
        else:
            request_body['labels'].update(
                {'ssh' : 'compliant', 'logger' : 'running',})
    if ssh:
        request_body['labels'].update(
            {'ssh' : 'compromised'})

    request = service.instances().setLabels(
            project=project, zone=zone,
            instance=instance, body=request_body)
    response = request.execute()
    operation = response['name']
    return operation

def check_operation(service, project, zone, instance, operation):
    while True:
        response = service.zoneOperations().get(
                project=project,
                zone=zone,
                operation=operation).execute()

        if response['status'] == 'DONE':
            if 'error' in response:
                print(Exception(response['error']))

        return respone
        time.sleep(1)

def main():
    # Define and parse command line arguments
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-s", "--startup", action="store_true", help="set initial labels and keys on instance.")
    parser.add_argument("-c", "--compr", action="store_true", help="set instance label to compromised")
    args = parser.parse_args()
    #gcp auth.
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    # Project ID for this request.
    project =  get_project()
    # The name of the zone for this request.
    zone = get_zone()
    # Name of the instance scoping this request.
    instance = get_instance()
    args = parser.parse_args()
    if args.startup:
        set_labels(service, project, zone, instance, first_run=True)
    elif args.compr:
        set_labels(service, project, zone, instance, ssh=True)
    else:
        pass

if __name__ == '__main__':
    main()
