# (Script is being improved, will upload once complete)

# Script the testing switches and store the configs locally

Code executed on Ubuntu 22.04 to script approximately 200 Cisco testing switches.

As team requested, telnet was used to script the testing switches in the lab. Below is the physical lab topology:

These testing switches are used for testing purposes and don't have a management IP address configured (no uplink). However, their console ports connect to the octal console cables from the HWIC/NIM modules of the terminal servers. So we could reach the switches through the terminal server's line numbering. 

For example: telnet x.x.x.x 2002 (where x.x.x.x is the IP address of the terminal server and 2002 is the line number that is used to reach the access the switch's console port)

Below is the topology:

![image](https://user-images.githubusercontent.com/128099142/233898056-e13bac22-cf78-45fd-9e7a-a1408e092b31.png)
