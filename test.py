# import ipaddress
# adrv4 = ipaddress.ip_address('192.10.0.1')
# # print(adrv4)
# adrv4.version
# adrv6 = ipaddress.ip_address('2001:D88::1')
# print(adrv6)
# adrv6.version

import socket
print(socket.gethostbyname('www.facebook.com'))
print(socket.getfqdn('31.13.77.35'))
print(socket.gethostname())