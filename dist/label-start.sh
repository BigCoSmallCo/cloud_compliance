#!/bin/sh
#sets the labels on startup.
python3 /usr/local/bin/cloud-compliance/cloud-compliance.py -s
touch /tmp/instance-label
