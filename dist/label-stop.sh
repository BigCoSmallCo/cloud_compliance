#! bin/sh

if [ -f /tmp/instance-label ]; then
    rm /tmp/instance-label
else
    echo "instance-label is not running."
fi
