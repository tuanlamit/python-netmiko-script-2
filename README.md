# (Script is being improved, will upload once complete)

# Script the testing switches and store the configs locally

Code executed on Ubuntu 22.04 to script approximately 200 Cisco testing switches.

As team requested, telnet was used to script the testing switches in the lab. Below is the physical lab topology:

These testing switches are used for testing purposes and don't have a management IP address configured (no uplink). However, we could access via terminal server.

The testing switches' console ports connect to the octal console cables. 

These cables came from the HWIC/NIM modules on the terminal servers (ex: C2800/2600/2900 or ISR4221 routers). 

So we could reach the switches through the terminal server's line numbering. 

For example, enter this command into the terminal:
```
telnet x.x.x.x 2002
```
Note: x.x.x.x is the IP address of the terminal server and 2002 is the line number defined by the router that is used to access the switch's console port)

Below is the physical lab topology:

![image](https://user-images.githubusercontent.com/128099142/233898056-e13bac22-cf78-45fd-9e7a-a1408e092b31.png)

# Example from GNS3 VM

Working Directory:

![1](https://github.com/tuanlamit/python-netmiko-script-2/assets/128099142/5cfd0613-73a5-426a-bfdc-25195006a6d5)

Result:

![2](https://github.com/tuanlamit/python-netmiko-script-2/assets/128099142/5efac279-8985-496a-844d-84b50ef82e2f)


