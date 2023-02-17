# batfish-pytest

In this test, I'll analyze network backups using the batfish network configuration analysis tool to check if the devices have the correct NTP servers configured. I'll use pytest to carry out the verification test and print to the screen any devices that fail the test.

Checking for NTP servers is just scratching the surface of what this tool is capable of, please see documentation for more use cases.

https://batfish.readthedocs.io/en/latest/

![alt text](https://i.imgur.com/ZT3vEGC.png)

## Topology
4 cisco routers in GNS3
![alt text](https://i.imgur.com/2zN5XxH.png)

## Script Steps
- Load the Nornir vars yaml file containing global variables for all devices
- Initialize batfish to analyze the backups and create a dataframe for data analysis
- Create a device list using the dataframe
- Use pytest to run the NTP test to every device. Pytest is checking if the devices configured NTP servers match the golden NTP servers provided by the yaml file.

## Script Example
![alt text](https://i.imgur.com/XYwsFsZ.png)

## Pytest Report
![alt text](https://i.imgur.com/DB3kzBH.png)
![alt text](https://i.imgur.com/hZMRIHn.png)
