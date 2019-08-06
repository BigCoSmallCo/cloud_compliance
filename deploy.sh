#!/bin/sh

DIR=/usr/local/bin/cloud-compliance

#Install requirements.
apt install python3-pip -y
pip3 install -r requirements.txt

#Copy files to correct locations and setting permissions.
echo "Copying files to $DIR."
cp ./cloud-compliance.py $DIR
cp ./dist/label-start.sh $DIR
cp ./dist/label-stop.sh $DIR
cp ./dist/instance-label.service /etc/systemd/system/

echo "Setting up executables and permissions."
chmod 755 $DIR/label-start.sh
chmod +x $DIR/label-start.sh
chmod 755 $DIR/label-stop.sh
chmod +x $DIR/label-stop.sh
chmod 755 $DIR/cloud-compliance.py
chmod +x $DIR/cloud-compliance.py

#edit pam.d
echo session optional pam_exec.so /usr/local/bin/cloud-compliance/cloud-compliance.py -c >> /etc/pam.d/sshd

#setup service
cd /etc/systemd/system
echo "Setting up systemctl service."
systemctl enable instance-label.service

#cleanup
cd ~
echo "Cleaning up files."
rm -r tmp

#only useful if deploying on already running instance, not advised.
# python3 $DIR/cloud-compliance.py -s
