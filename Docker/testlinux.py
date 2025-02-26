from netmiko import ConnectHandler
server = {
    "device_type": "linux",
    "ip": "127.0.0.1",
    "username": "admin",
    "password": "password",
    "port": 2222,
}
net_connect = ConnectHandler(**server)
print("Connected to server")
command = "cat /etc/config/hostname/config.txt"
output = net_connect.send_command(command)
print(output)