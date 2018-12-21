#!/bin/sh

#edit to your needs.
DIR=/usr/local/bin/cloud-compliance

#desired download location
cd ~

mkdir tmp
cd tmp
# wget tar file here.
wget https://github.com/BigCoSmallCo/cloud_compliance/archive/master.tar.gz

tar -xvzf master.tar.gz
cd cloud_compliance-master
apt install python3-pip -y
pip3 install -r requirements.txt
#create directory to house relevant files.
mkdir $DIR

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

#setup service
cd /etc/systemd/system
echo "Setting up systemctl service."
systemctl enable instance-label.service

#cleanup
cd ~
echo "Cleaning up files."
rm -r tmp

#only useful if deploying on already running instance, not advised.
python3 $DIR/cloud-compliance.py -s
