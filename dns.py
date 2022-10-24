import socket


# def get_Host_name_IP():
#     try:
#         host_name = socket.gethostname()
#         host_ip = socket.gethostbyname(host_name)
#         print("Hostname: ", host_name)
#         print("IP:", host_ip)
#     except:
#         print("Unable to get Hostname and IP")


# if __name__ == '__main__':
#     get_Host_name_IP()
# def get_remote_machine_info():
#     remote_hostname = 'elcit.ctu.edu.vn'
#     try:
#         print("IP address of %s: %s"%(remote_hostname, socket.gethostbyname(remote_hostname)))
#     except socket.error as err_msg:
#         print("ERROR: %s: %s"%(remote_hostname, err_msg))



# if __name__ == '__main__':
#     get_remote_machine_info()

# import socket
# from binascii import hexlify

# def convert_ipv4():
#     for ip in ['127.0.0.1', '192.168.0.1']:
#         packet_ip_addr = socket.inet_aton(ip)
#         unpacked_ip_addr = socket.inet_ntoa(packet_ip_addr)
#         print("IP add: %s => Packed: %s, Unpacked: %s" % (ip, hexlify(packet_ip_addr), unpacked_ip_addr))
        
# if __name__ == '__main__':
#     convert_ipv4()
