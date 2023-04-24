from netmiko import ConnectHandler
from datetime import datetime
import time
import threading

start = time.time()


def backup(testing_switch, ip, port, successful_backups):
    try:
        connection = ConnectHandler(**testing_switch)
        connection.enable()
        connection.send_command('wr')
        send_the_command = connection.send_command('sho run', read_timeout=45)
        hostname_output = connection.send_command('sho run | include hostname')
        out_file_name = f"/var/www/shared/BLD-18/testing_switches_backup_configs/show_running-config/sho_run***{hostname_output.split()[1]}***{ip}-{port}.txt"
        out_file = open(out_file_name, "w")
        out_file.write(send_the_command)
        out_file.close()
        connection.disconnect()
        print(f'[DONE] switch {ip} {testing_switch["port"]}')
        successful_backups.append(ip)
    except Exception as e:
        print(f'[FAILED] switch {ip} {testing_switch["port"]} - Clear Port Might Fix.')


with open('testing_switches.txt') as f:
    devices = [line.split() for line in f.read().splitlines()]

threads = []
successful_backups = []
scripted_devices = 0

for ip, port in devices:
    testing_switch = {
        'device_type': 'cisco_ios_telnet',
        'host': ip,
        'port': port,
        'username': 'lab',
        'password': 'lab',
        'secret': 'cisco',
        'verbose': True,
    }

    scripted_devices += 1

    th = threading.Thread(target=backup, args=(testing_switch, ip, port, successful_backups))
    threads.append(th)
    th.start()
for th in threads:
    th.join()

end = time.time()
print(f'Total Switches Scripted: {scripted_devices}')
print(f'Total Switches Successfully Backed Up: {len(successful_backups)}')
print(f'Total Execution Time: {end-start}')
