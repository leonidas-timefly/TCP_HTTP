from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
#Fill-in-start

serverSocket.bind(('192.168.43.14', 7990))    #IP地址及端口号
serverSocket.listen(1)   #一个用户

#Fill-in-end

while True:
    # Establish the connection
    print(' The server is ready to receive')
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    # Fill-in-start #Fill-in-end
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024)  # Fill-in-start #Fill-in-end
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes
        # a character '/', we read the path from the second character
        f = open(filename[1:])
        # Store the entire content of the requested file in a temporary buffer
        output_data = f.read()  # Fill-in-start #Fill-in-end

        # Send the HTTP response header line to the connection socket
        # Fill-in-start
        connectionSocket.send(message.decode().encode())
        print(output_data)
        # Fill-in-end
        # Send the content of the requested file to the connection socket
        connectionSocket.send(output_data.encode())
        #for i in range(0, len(output_data)):
        #    connectionSocket.send(output_data[i].encode())
        # Close the client connection socket
        connectionSocket.close()
    except IOError:
        # Send HTTP response message for file not found
        # Fill-in-start
        error_message = '404 Not Found'
        connectionSocket.send(error_message.encode())
        # Fill-in-end
        # Close the client connection socket
        # Fill-in-start
        connectionSocket.close()
        # Fill-in-end

while 1:
    k = 0

#serverSocket.close()
# Terminate the program after sending the corresponding data
