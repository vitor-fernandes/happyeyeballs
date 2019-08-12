# /usr/bin/python3

import socket
import sys
import ipaddress

def usage():
    print("Usage: python3 happyeyeballs.py HOST PORT")

def get_IP_infos(host, port):
    result = socket.getaddrinfo(host, port)
    return result

def connect_IPv4(host, port):
    try:
        IPv4_SOCK = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        
        IPv4_SOCK.connect( (host, int(port)) )

        return True

    except Exception as e:
        return False

def connect_IPv6(host, port):
    
    try:
        IPv6_SOCK = socket.socket(family = socket.AF_INET6, type = socket.SOCK_STREAM, proto = 0)
        
        IPv6_SOCK.connect((host, int(port), 0, 0))

        return True

    except Exception as e:
        return False

def main():
    if(len(sys.argv) < 3):
        usage()
        exit(1)

    host = sys.argv[1]
    port = sys.argv[2]

    results = get_IP_infos(host, port)

    IPs = []

    for result in results:
        if(type(ipaddress.ip_address(result[-1][0])) == ipaddress.IPv6Address):
            if(result[-1][0] not in IPs):
                pass
        else:
            if(result[-1][0] not in IPs):
                pass
        
        IPs.append(result[-1][0])
    
    IPv4 = False
    IPv6 = False

    for IP in set(IPs):
        if(type( ipaddress.ip_address(IP) ) == ipaddress.IPv6Address):
            IPv6 = connect_IPv6(IP, port)
        else:
            IPv4 = connect_IPv4(IP, port)

    print('[+] IPv4 Avaliable for Connection: {}'.format(IPv4))
    print('[+] IPv6 Avaliable for Connection: {}'.format(IPv6))

    if(IPv6):
        print('[+] IPv6 have more privileges over IPv4...')
        print('[+] IPv6 will be used for this application')
    
    else:
        print()
        print('[+] IPv4 will be used for this application')

if __name__ == '__main__':
    main()


    