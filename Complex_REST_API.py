'''
A very very simple python code to demonstrate how REST API works

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


payload='No' #init a content


while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    print type(request)
    
    http_response = """\
HTTP/1.1 200 OK

Hello, World!

Your HTTP Method is %s
"""
    client_connection.sendall(http_response%request[0:4])
    
    ###try to simply parese HTTP GET request
    
    if request[0:6] == 'GET /a':
        client_connection.sendall(" You GET this  a=%s  ^_^  !   "%payload)
        
    if request[0:6] == 'GET /b':
        client_connection.sendall(" You GET this  b  ^_^  !   ")
        
    if request[0:9] == 'POST /yes':
        client_connection.sendall("POST make a=Yes")
        payload='yes'
        
    if request[0:8] == 'POST /no':
        client_connection.sendall("POST make a=No")
        payload='No'
        
    if len(request)>10:
        client_connection.sendall("Absolute not a termianl request ,maybe by POSTMAN or some browser")
        # try to parse long request
        if request[0:4]=='POST':
            
            content_len_loc=request.find('content-length:',0,len(request))
            Connection_loc=request.find('Connection:',0,len(request))
            content_len=request[content_len_loc+16:Connection_loc-2]
            print content_len
            print len(content_len)
            print type(content_len)
            payload=request[len(request)-int(content_len):len(request)]
            print "--------Request content all ----------"
            print request
            print "--------Paylaod parsed here  ---------"
            print payload
            print "--------------------------------------"
    client_connection.close()