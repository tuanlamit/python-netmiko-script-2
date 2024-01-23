# (Script is being improved, will upload once complete)


# Script the testing switches and store the configs locally

Code executed on Ubuntu 22.04 to script approximately 200 Cisco testing switches.

As team requested, telnet was used to script the testing switches in the lab. Below is the physical lab topology:

These testing switches are used for testing purposes and don't have a management IP address configured (no uplink). 

However, we could access these switches via a terminal server.

The testing switches' console ports connect to the octal console cables. 

These octal cables are screwed into the HWIC/NIM modules on the terminal servers (ex: C2800/2600/2900 or ISR4221 routers). 

So we could reach the switches through the terminal server's line numbering. 

For example, enter this command into the terminal:
```
telnet x.x.x.x 20xx
```
> [!NOTE]

> x.x.x.x is the IP address of the terminal server and 20xx is the line number defined by the router, which provides access to the switches.

> Line number could be 20xx, 40xx, or 60xx, but preferrably 20xx for normal use.

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

> On the Cisco terminal server, display the line numbers with "show line", each line number maps to a physical console cable.

> Each cable could be extended using an RJ45 coupler.


# Virtual lab example using the same codes

Working Directory & Outputs:

![1](https://github.com/tuanlamit/python-netmiko-script-2/assets/128099142/5cfd0613-73a5-426a-bfdc-25195006a6d5)

Stored Configs

![2](https://github.com/tuanlamit/python-netmiko-script-2/assets/128099142/5efac279-8985-496a-844d-84b50ef82e2f)


