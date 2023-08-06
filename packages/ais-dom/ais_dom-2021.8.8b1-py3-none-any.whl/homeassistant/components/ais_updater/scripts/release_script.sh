#!/bin/sh
echo "AIS release script starting for 21.07.29 on chanel 2" 
echo "Switch AIS repo"  

echo "# The main AI-Speaker repository:" > /data/data/pl.sviete.dom/files/usr/etc/apt/sources.list 

echo "deb [trusted=yes] https://powiedz.co/apt dom stable" >> /data/data/pl.sviete.dom/files/usr/etc/apt/sources.list 

echo "deb [trusted=yes] https://powiedz.co/apt python 3.9" >> /data/data/pl.sviete.dom/files/usr/etc/apt/sources.list 

echo "deb [trusted=yes] https://powiedz.co/apt dom-dev beta" >> /data/data/pl.sviete.dom/files/usr/etc/apt/sources.list 


echo "AIS save config file for mosquitto" 

cp /data/data/pl.sviete.dom/files/usr/etc/mosquitto/mosquitto.conf /sdcard/mosquitto.conf 


echo "AIS apt update" 

apt update 

DEBIAN_FRONTEND=noninteractive apt -y upgrade 


echo "AIS back config file for mosquitto" 

cp /sdcard/mosquitto.conf /data/data/pl.sviete.dom/files/usr/etc/mosquitto/mosquitto.conf 


pm2 delete zigbee  


echo "21.08.03" > /data/data/pl.sviete.dom/files/home/AIS/.ais_apt  

