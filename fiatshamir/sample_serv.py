# Script file: sample_serv.py
import socket
import common
import random
 

# next create a socket object 
s = socket.socket()		 
print "Socket successfully created"

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345				

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))		 
print "socket binded to %s" %(port) 
print
# put the socket into listening mode 
s.listen(5)	 
print "socket is listening"			
print
# a forever loop until we interrupt it or 
# an error occurs 
while True: 

# Establish connection with client. 
    c, addr = s.accept()	 
    print 'Got connection from', addr 
    str_n=c.recv(1024)
    n=int(str_n)
    
#receiving public key from prover : step 3
    print
    str_v=c.recv(1024)
    print "Public key received as ",str_v
    print
    str_x=c.recv(1024)
    print "Witness received as ",str_x

    print
    #send challenge
    challenge=random.choice([0,1])
    print "Sending challenge",challenge
    c.send(str(challenge))
    print
   #step 8: receiving y
    str_y=c.recv(1024)
    print "Received y",str_y

    print
    #veri fication
    y=int(str_y)
    item_1=(y**2)
    x=int(str_x)
    v=int(str_v)
    item_2=x*(v**challenge)
    if ( (item_1%n)  == (item_2%n)):

# send a thank you message to the client. 
        print 'Verification successful'
    	c.send('Verification successful') 
    else:
        print 'Verification failed'
    	c.send('Verification failed')

# Close the connection with the client 
    c.close() 

