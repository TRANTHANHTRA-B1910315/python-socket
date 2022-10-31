# import socket
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

# import socket

# def find_ser_name():
#     protocolname='tcp'
#     for port in [80,25,143,110,20,21]:
#         print("Port: %s => Service name: %s" % (port,socket.getservbyport(port,protocolname)))
#     print("Port: %s => Service name: %s" % (53,socket.getservbyport(53,'UDP')))
# if __name__=='__main__':
#     find_ser_name()

import socket 
 
# def convert_integer(): 
#     data = 1234 
#     # 32-bit 
#     print ("Original: %s => Long  host byte order: %s, Network byte order: %s" %(data, socket.ntohl(data), socket.htonl(data))) 
#     # 16-bit 
#     print ("Original: %s => Short  host byte order: %s, Network byte order: %s" %(data, socket.ntohs(data), socket.htons(data))) 
 
     
# if __name__ == '__main__': 
#     print (sys.version)
#     convert_integer()
# ---------------------------
# def testSock_timeout():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print("Defalt socket timeout %s" % s.gettimeout())
#     s.settimeout(100)
#     print("Current socket timeout %s" % s.gettimeout())

# if __name__ == '__main__':
#     testSock_timeout()
# ---------------------------

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bufsize = socket.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Buffer size [Before:]%d", % bufsize)
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)


