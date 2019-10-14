
import socket
import tkinter


def getAddress(name):
    ip_list = []
    address = socket.getaddrinfo(name,0,0,0,0)
    for result in address:
        ip_list.append(result[-1][0])
#    ip_list = list(set(ip_list))

    return ip_list

def main():
    name = "et.iupui.edu"
    length = len(getAddress(name))
    print(length)
    print(getAddress(name)[0])
    return

main()