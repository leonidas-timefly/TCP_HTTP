from socket import *
import threading
import os

# Define thread process
def Server(tcpClisock, addr):

    BUFSIZE = 1024
    print('Received a connection from:', addr)
    data = tcpClisock.recv(4096).decode() #Fill-in-start  #Fill-in-end
    print(data)

    if len(data):
        # Extract the filename from the received message
        getFile = data.split()[1]
        print('getFile:', getFile)

        # Form a legal filename
        filename = data.split(' ', 2)[1]
        filename = filename.split('/', 1)[1]
        filename = filename.replace('.', '_', 3)
        #Fill-in-start  #Fill-in-end
        print('filename:', filename)

        # Check wether the file exist in the cache
        if os.path.exists(filename):
            print('File exist')
            # ProxyServer finds a cache hit and generates a response message
            f = open(filename, "r")
            CACHE_PAGE = f.read()
            # ProxyServer sends the cache to the client
            #Fill-in-start
            for i in range(0, len(CACHE_PAGE)):
                tcpClisock.send(CACHE_PAGE[i].encode())
            #Fill-in-end
            print('Send the cache to the client')
            tcpClisock.close()
        else:
            print('File not exist')
            # Handling for file not found in cache
            # Create a socket on the ProxyServer
            c = socket(AF_INET, SOCK_STREAM)  #Fill-in-start  #Fill-in-end
            try:
                # Connect to the WebServer socket to port 80
                hostn = getFile.partition("/")[2].partition("/")[0]
                #Fill-in-start
                c.connect((hostn, 80))
                #Fill-in-end
                print('Connect to', hostn)

                # Some information in client request must be replaced before it can be sent to the server
                #Fill-in-start
                os.makedirs(filename.rsplit('/', 1)[0])
                data = "GET /" + data.split('/', 2)[2]
                #Fill-in-end
                # Send the modified client request to the server
                #Fill-in-start
                c.sendall(data.encode())
                #Fill-in-end

                # Read the response into buffer
                buff = c.recv(4096)
                #print(buff.decode)
                print('recvbuff len:', len(buff))

                # Send the response in the buffer to client socket
                tcpClisock.send(buff)
                print('Send to client\r\n')

                # Create a new file to save the response in the cache for the requested file
                tmpFile = open("./" + filename, "w")
                #Fill-in-start
                tmpFile.writelines(buff.decode().replace('\r\n', '\n'))
                tmpFile.close()
                #Fill-in-end
            except:
                print("Illegal request")
            tcpClisock.close()

# Main process of  ProxyServer
if __name__ == '__main__':

    # Create a server socket, bind it to a port and start listening
    tcpSersock = socket(AF_INET, SOCK_STREAM)
    #Fill-in-start
    tcpSerPort = 7990
    tcpSersock.bind(('', tcpSerPort))
    tcpSersock.listen(5)
    #Fill-in-end

    print("Ready to serve......\n")
    while True:
        tcpClisock, addr = tcpSersock.accept()
        thread = threading.Thread(target=Server, args=(tcpClisock, addr))
        thread.start()
    tcpSersock.close()

