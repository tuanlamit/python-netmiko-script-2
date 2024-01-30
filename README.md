# Script the testing switches and store the configs locally

Code executed on Ubuntu 22.04 to script approximately 200 Cisco testing switches.

As team requested, telnet was used to script the testing switches in the lab. Below is the physical lab topology:

These testing switches are used for testing purposes and don't have a management IP address configured (no uplink). 

However, we could access these switches via a terminal server.

The testing switches' console ports connect to the console cables (octal cables in this case). 

These console cables are screwed into the HWIC/NIM modules on the terminal servers (ex: C2800/2600/2900 or ISR4221 routers). 

The console cables provide the line numbers, so we could reach the switches through the terminal server's line numbering. 

For example, enter this command into the terminal:
```
telnet x.x.x.x 20xx
```
> [!NOTE]
> x.x.x.x is the IP address of the terminal server and 20xx is the line number defined by the router, which provides access to the switches.
>
>
> Line number usually have 4 digits and could be 20xx, 40xx, 60xx, and etc... but preferably 20xx for normal use.

Below is the physical lab topology:

![image](https://user-images.githubusercontent.com/128099142/233898056-e13bac22-cf78-45fd-9e7a-a1408e092b31.png)


# More on octal cables if you're interested:

Blue
   - Length: short
   - Physical numbering on each cable: 1 through 8

     ![blue](https://github.com/tuanlamit/python-netmiko-script-2/assets/128099142/cc30f5dc-1555-4e1a-93be-07ef7056ef0b)

Green
   - Length: long
   - Physical numbering on each cable: 0 through 7

     ![green](https://github.com/tuanlamit/python-netmiko-script-2/assets/128099142/7d4c3156-7c0d-4a9a-b5f6-b55978e18813)

> [!NOTE]
> On the Cisco terminal server (router), display the line numbers with the "show line" command
>
> Line numbers virtually map to physical console cables, but they don't exactly match the physical numbering
>
> For example: physical console cable labeled with number one from the first HWIC/NIM module might show up as "2002 or 2003" from "show line" command
>
> Each console cable could be extended using an RJ45 coupler.


# Virtual lab example using the same codes

Working Directory & Result:

![3](https://github.com/tuanlamit/python-netmiko-script-2/assets/128099142/67805886-28fd-45ff-b71e-9179ad4595e3)

Stored Configs

![4](https://github.com/tuanlamit/python-netmiko-script-2/assets/128099142/56943d90-34aa-48c9-add7-b3e7f4715104)
