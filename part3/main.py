from socket import *
import os
# Determine the port on 9977
port = 9977 

# Create a socket and bind it to the server's address
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("localhost",port))
serverSocket.listen(1) 
# Listen for incoming connections.
print("[STARING] the server is starting...")
while True:
    # Accept a connection (the server is waiting for a client to connect).
    connectionSocket,addr=serverSocket.accept() 
    # Get the client's IP address and port.
    ip=addr[0]
    port=addr[1]
    # Receive the request message and decode it.
    sentence=connectionSocket.recv(1024).decode() 
    print(sentence)
    # Parse the request to determine the requested file.
    fileName = sentence.split('\n')[0]
    fileName = fileName.split(' ')[1]
    fileName=fileName.lstrip('/')

    try:
        # If the file is the main page, send the corresponding HTML file
        if fileName == '' or fileName =='index.html' or fileName =='main_en.html' or fileName == 'en':
            # Open and read the requested file in byte format.
            openFile = open("main_en.html", "rb")  
            # the case of the request is ok.
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) 
            # the Content-Type will be text/html.
            connectionSocket.send("Content-Type: text/html \r\n".encode()) 
            connectionSocket.send('\r\n'.encode())
            connectionSocket.send(openFile.read())
            connectionSocket.close()

        # If the file is the arabic version page, send the corresponding HTML file
        elif fileName == 'ar' or fileName == 'main_ar.html': 
            # the case of the request is ok.
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) 
            # the Content-Type will be text/html.
            connectionSocket.send("Content-Type: text/html \r\n".encode()) 
            connectionSocket.send('\r\n'.encode())
            # Open and read the requested file in byte format.
            openFile = open("main_ar.html", "rb")  
            connectionSocket.send(openFile.read())
            connectionSocket.close()

        # If the file is anything.html page, send the corresponding HTML file
        elif fileName.endswith('.html'): 
            # the case of the request is ok.
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) 
            # the Content-Type will be text/html.
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send('\r\n'.encode())
            try: # if the fileName is exist then it will open
                openFile = open(fileName, "rb")  # Open and read the requested file in byte format.
                connectionSocket.send(openFile.read()) #open the HTML file.
            except: # if not exist.
                errorPage = '<!DOCTYPE html> <html lang="en"> <head> <title>Error 404</title> <link rel="stylesheet" href="errorpage.css"> <meta charset="UTF-8"> </head> <body> <h1>The file is not found!!</h1> <p>Maisam Alaa 1200650</p> <p>Razan Odeh 1200531</p> <p>IP : ' + str(ip) + '<br>Port : ' + str(port) + '</p> </body> </html>'
                connectionSocket.send(errorPage.encode())  #the error page that contains our names  and ip and port of the client will opened.
            connectionSocket.close()

        # If the file is anything.css page, send the corresponding css file named style.css.
        elif fileName.endswith('.css'):
            if os.path.exists(fileName):
                # the case of the request is ok.
                connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
                # the Content-Type will be text/css.
                connectionSocket.send("Content-Type: text/css \r\n".encode())
                connectionSocket.send('\r\n'.encode())
                # Open and read the requested file in byte format.
                openFile = open(fileName, "rb")  
                connectionSocket.send(openFile.read())  
            else:# the case of the request is not found,
                connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())  
                connectionSocket.send("Content-Type: text/html \r\n".encode())  
                connectionSocket.send('\r\n'.encode())
                errorPage = '<!DOCTYPE html> <html lang="en"> <head> <title>Error 404</title> <link rel="stylesheet" href="errorpage.css"> <meta charset="UTF-8"> </head> <body> <h1>The file is not found!!</h1> <p>Maisam Alaa 1200650</p> <p>Razan Odeh 1200531</p> <p>IP : ' + str(ip) + '<br>Port : ' + str(port) + '</p> </body> </html>'
                connectionSocket.send(errorPage.encode()) #the error page that contains our names  and ip and port of the client will opened.
            connectionSocket.close()

        # If the file is an image of .png, send the corresponding image png.
        elif fileName.endswith('.png'): 
            if os.path.exists('img/' + fileName):
                # the case of the request is ok.
                connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
                # the Content-Type will be image/png.
                connectionSocket.send("Content-Type: image/png \r\n".encode())
                connectionSocket.send('\r\n'.encode())
                # Open and read the requested file in byte format.
                openFile = open('img/' + fileName, "rb")  
                 # open the image.
                connectionSocket.send(openFile.read()) 
            else:  # if not exist the error page will open
                 # the case of the request is not found.
                connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode()) 
                connectionSocket.send("Content-Type: text/html \r\n".encode()) 
                connectionSocket.send('\r\n'.encode())
                errorPage = '<!DOCTYPE html> <html lang="en"> <head> <title>Error 404</title> <link rel="stylesheet" href="errorpage.css"> <meta charset="UTF-8"> </head> <body> <h1>The file is not found!!</h1> <p>Maisam Alaa 1200650</p> <p>Razan Odeh 1200531</p> <p>IP : ' + str(ip) + '<br>Port : ' + str(port) + '</p> </body> </html>'
                connectionSocket.send(errorPage.encode()) # the error page that contains our names  and ip and port of the client will opened.
            connectionSocket.close()

        elif fileName.endswith('.jpg'):
            if os.path.exists('img/'+fileName): # the case of the request is ok.
                connectionSocket.send("HTTP/1.1 200 OK\r\n".encode()) 
                # the Content-Type will be image/jpeg.
                connectionSocket.send("Content-Type: image/jpeg \r\n".encode())  
                connectionSocket.send('\r\n'.encode())
                # Open and read the requested file in byte format.
                openFile = open('img/'+fileName, "rb")  
                #open the image.
                connectionSocket.send(openFile.read())
            else:# if not exist the error page will open
                connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())  # the case of the request is ok.
                # the Content-Type will be text/html.
                connectionSocket.send("Content-Type: text/html \r\n".encode())  
                connectionSocket.send('\r\n'.encode())
                errorPage = '<!DOCTYPE html> <html lang="en"> <head> <title>Error 404</title> <link rel="stylesheet" href="errorpage.css"> <meta charset="UTF-8"> </head> <body> <h1>The file is not found!!</h1> <p>Maisam Alaa 1200650</p> <p>Razan Odeh 1200531</p> <p>IP : ' + str(ip) + '<br>Port : ' + str(port) + '</p> </body> </html>'
                connectionSocket.send(errorPage.encode())#the error page that contains our names  and ip and port of the client will opened
            connectionSocket.close()


        elif fileName == 'yt':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())# the case of the request is Temporary Redirect
            connectionSocket.send(b"location: https://www.youtube.com/ \r\n") #redirect to youtube website.
            connectionSocket.close()

        elif fileName == 'so':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())# the case of the request is Temporary Redirect
            connectionSocket.send(b"location: https://www.stackoverflow.com \r\n") # redirect to stackoverflow website
            connectionSocket.close()

        elif fileName == 'rt':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())# the case of the request is Temporary Redirect
            connectionSocket.send(b"location: https://ritaj.birzeit.edu/register/ \r\n") #  redirect to ritaj website
            connectionSocket.close()
        else:
            #if the fileName not exist it will raise an error
            raise error

    except Exception as error:
        # the case of the request is not found.
        connectionSocket.send("HTTP/1.1 404 Not Found \r\n".encode())
        # the Content-Type will be text/html
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send('\r\n'.encode())
        errorPage = '<!DOCTYPE html> <html lang="en"> <head> <title>Error 404</title> <link rel="stylesheet" href="errorpage.css"> <meta charset="UTF-8"> </head> <body> <h1>The file is not found!!</h1> <p>Maisam Alaa 1200650</p> <p>Razan Odeh 1200531</p> <p>IP : ' + str(ip) + '<br>Port : ' + str(port) +'</p> </body> </html>'
        connectionSocket.send(errorPage.encode()) # the error page that contains our names  and ip and port of the client will opened
        connectionSocket.close()