#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :  __init__.py
@Date    :  2021/8/26
@Author  :  Yaronzz
@Version :  1.0
@Contact :  yaronhuang@foxmail.com
@Desc    :
"""

import socket
import threading
import datetime

def bytesToHexString(bs):
    return ''.join(['%02X' % b for b in bs])


def dispose_client_request(tcp_client_1, tcp_client_address):
    print("客户端是:", tcp_client_address)

    while True:
        try:
            recv_data = tcp_client_1.recv(4096)
        except Exception as e:
            print(f"{tcp_client_address[1]} 客户端下线了..{str(e)}")
            tcp_client_1.close()
            break

        if recv_data:
            print(f"[{str(datetime.datetime.now())}][{tcp_client_address}]:", bytesToHexString(recv_data))
        else:
            print("%s 客户端下线了..." % tcp_client_address[1])
            tcp_client_1.close()
            break


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    ip = input("IP:")

    # tcp_server.bind(('192.168.0.151', 8888))
    tcp_server.bind((ip, 61234))
    tcp_server.listen(128)

    while True:
        tcp_client_1, tcp_client_address = tcp_server.accept()
        thd = threading.Thread(target=dispose_client_request, args=(tcp_client_1, tcp_client_address))
        thd.start()


if __name__ == '__main__':
    main()
