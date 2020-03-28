from socket import *
import base64

# Mail content
subject = "I love computer networks!"
content_type = "text/plain"
msg = "I love computer networks!"
end_msg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mail_server = 'smtp.qq.com' #Fill-in-start  #Fill-in-end

# Sender and reciever
from_address = '2442344049@qq.com' #Fill-in-start  #Fill-in-end
to_address = 'timeschangezhao@gmail.com' #Fill-in-start  #Fill-in-end

# Auth information (Encode with base64)
user_name = base64.b64encode(b'2442344049@qq.com').decode() #Fill-in-start  #Fill-in-end
password = base64.b64encode(b'***').decode() #Fill-in-start  #Fill-in-end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill-in-start

clientSocket = socket(AF_INET, SOCK_STREAM)  #建立套接字
clientSocket.connect(('smtp.qq.com', 25))

#Fill-in-end

recv = clientSocket.recv(1024) .decode()
print(recv)

# Send HELO command and print server response.
#Fill-in-start
clientSocket.sendall('HELO qq.com\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')
#Fill-in-end

# Send AUTH LOGIN command and print server response.
clientSocket.sendall('AUTH LOGIN\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.sendall((user_name + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.sendall((password + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Send MAIL FROM command and print server response.
#Fill-in-start
MailFromCommand = ('MAIL FROM:<%s>'%from_address + '\r\n').encode()
clientSocket.sendall(MailFromCommand)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server')
#Fill-in-end

# Send RCPT TO command and print server response.
#Fill-in-start
RcptToCommand = ('RCPT TO:<%s>'%to_address + '\r\n').encode()
clientSocket.sendall(RcptToCommand)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server')
#Fill-in-end

# Send DATA command and print server response.
#Fill-in-start
DataCommand = 'DATA\r\n'.encode()
clientSocket.sendall(DataCommand)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '354':
    print('354 reply not received from server')
#Fill-in-end

# Send message data.
#Fill-in-start
message = 'from:' + from_address + '\r\n'
message += 'to:' + to_address + '\r\n'
message += 'subject:' + subject + '\r\n'
message += 'Content-Type:' + content_type + '\t\n'
message += '\r\n' + msg
clientSocket.send(message.encode())
#Fill-in-end

# Message ends with a single period and print server response.
#Fill-in-start
clientSocket.sendall(end_msg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server')
#Fill-in-end

# Send QUIT command and print server response.
#Fill-in-start
QuitCommand = ('QUIT' + '\r\n').encode()
clientSocket.sendall(QuitCommand)

#Fill-in-end

# Close connection
clientSocket.close()
