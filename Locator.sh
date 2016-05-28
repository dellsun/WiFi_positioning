#! /bin/sh

echo "script requires root access to scan WiFi with iw command"
echo " "


./Scripts/BuildRadioMap.sh UNK

python ./locatorClient.py
