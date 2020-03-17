import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.43.14', 7990))
sock.send('GET /text.html HTTP/1.1\r\n'.encode())
'''
sock.send('Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'.encode())
sock.send('Accept-Language: en-GB\r\n'.encode())
sock.send('Upgrade-Insecure-Requests: 1\r\n'.encode())
sock.send('User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362\r\n'.encode())
sock.send('Accept-Encoding: gzip, deflate\r\n'.encode())
sock.send('Host: 192.168.43.14\r\n'.encode())
sock.send('Connection: Keep-Alive\r\n'.encode())
'''
k = 10
while k:
    receive_data = sock.recv(1024)
    print(receive_data.decode())
    k = k - 1
    #sock.close()

sock.close()
