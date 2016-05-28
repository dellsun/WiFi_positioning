#! /bin/sh

if [ -z $1  ]
then
echo "USAGE: ./BuildRadioMap Name-of-Area"
echo " "
exit 1
fi


fileName=$1


temp=$(mktemp "/tmp/${fileName}.XXX")

echo "collecting radio signature for $fileName"


local1=5

while test $local1 -ne 0
do


iw dev wlan0 scan  > ${temp}


gawk -v location=${fileName} -f ./Scripts/iw_processOutput.awk  ${temp} > ./DATA/realtimeData/${local1}.txt



local1=`expr $local1 - 1`


done


exit 0
