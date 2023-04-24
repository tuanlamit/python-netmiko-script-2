# Save the config and export it as a back-up.

Code executed on Ubuntu 22.04 to script approximately 200 Cisco testing switches.

Telnet was used instead of SSH because this is a testing environment running in the company's internal network, so SSH wasn't necessary; firewall was also disabled. 

These testing switches are used for testing purposes and do not have a management IP address configured. However, they all have their console ports connected to the console cables of the terminal servers. So we could reach the switches through the terminal server's line numbers. Example: telnet x.x.x.x 2002 (where x.x.x.x is the IP address of the terminal server and 2002 is the line number that is used to reach the switch)

Below is the topology:

![image](https://user-images.githubusercontent.com/128099142/233898056-e13bac22-cf78-45fd-9e7a-a1408e092b31.png)

You'll need to create a .txt file to store IP addresses and line numbers in the same folder.

At line:
```
'device_type': 'cisco_ios_telnet'
```

This is telnet within netmiko, SSH could also be used if this line is changed to:
```
'device_type': 'cisco_ios'
```


# Outputs sync to apache</summary>

At line:
```
out_file_name = f"/var/www/shared/BUILDING-ABC/testing_switches_backup_configs/show_running-config/sho_run***{hostname_output.split()[1]}***{ip}-{port}.txt"
```

You can save the back-ups to your desired destination, I prefer to use the above path because I wanted the changes to reflect on the web browser (apache2 is needed).
