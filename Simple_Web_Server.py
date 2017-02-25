'''
A very very simple python code to demonstrate web server and how REST API works

Alex Feng
Jan,2017
'''
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT


while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    print type(request)
    
    http_response = """\
HTTP/1.1 200 OK

Hello, World!
This is a very simple  web server

"""
    client_connection.sendall(http_response)
    print "---------This is a fire and forget session , closed-----------------------------"  
    client_connection.close()
    