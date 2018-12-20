# Cloud-compliance
cloud-compliance is set to be a lightweight tool that provides
universal automation to all of your Public cloud instances.

## Usage
- Establish pre-requisites for you cloud provider.
- Edit ```etc/pam.d/sshd``` to contain ```session optional pam_exec.so /usr/local/bin/cloud-compliance/cloud-compliance.py -c``` the -c argument lets
the tool know to set the ssh kwarg to true.
- ```chmod +x deploy.sh``` to make it executable.
- Run ```sudo ./delpoy.sh```.

## Requirements
- Root permissions to your instance.

### GCP
- IAM service account permissions:
  - compute.instances.setLabel IAM permission.
  - Compute Write API Scope

### AWS
- Planned for future deployment.

### Azure
- Planned for future deployment.

## Contribution
- If you'd like to contribute feel free to make a pull request. We welcome
improvements, bug fixes, and feature-adds.

## License
- [GNU GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
