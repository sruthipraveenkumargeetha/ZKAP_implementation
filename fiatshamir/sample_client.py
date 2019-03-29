# Script file: sample_client.py
import socket
import common
import random

#getting n value from the trusted outsider

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345				

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
print

n=common.n
print("n value:",n)
s.send(str(n))
# receive data from the server
#step 1: choose s, private key
secret_key=random.randrange(1,n-1)#s
print "Private key : ",secret_key

#step 2: construct public key 
v=(secret_key ** 2) % n
print "Public key : ",v

#step 3: send the public key to verifier
print
print "Sending the public key to the verifier"
s.send(str(v))
print
#step 4 : choose r
r=random.randrange(0,n-1)
print "chosen r",r

#step 5 : calculate witness
x= (r**2) % n
print "calculated witness",x

#step 6 : sending witness
print "Sending witness..."
s.send(str(x))
print 
#step 7 : receiving challenge
str_c=s.recv(1024)
print "challenge received", str_c

print 
#step 8 : calculating y
y=r*(secret_key**int(str_c))
print "Calculated y: ",y
print "Sending y"
s.send(str(y))

print
print s.recv(1024) 


# close the connection 
s.close()	 

