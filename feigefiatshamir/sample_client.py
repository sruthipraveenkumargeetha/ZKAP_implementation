# Script file: sample_client.py
import socket
import common
import random
import json

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
#step 1: choose s values, private key
secret_key=[]
for i in range(10):
	secret_key.append(random.randrange(1,n-1))
print
print "Secret key values :"
for i in range(10):
	print secret_key[i],

#step 2: construct public key 
v=[]
for i in range(10):
	v.append((secret_key[i] ** 2) % n)
print
print "Public key values :"
for i in range(10):
	print v[i],

#step 3: send the public key to verifier
print
print "Sending the public key to the verifier"
v_str=json.dumps(v).encode()
s.send(v_str)
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
c_str=s.recv(1024)
challenge=json.loads(c_str)
print "Challenges received "
for i in range(10):
	print challenge[i],

print 
#step 8 : calculating y
y=r
for i in range(10):
	y=y*(secret_key[i]**challenge[i])
print "Calculated y: ",y
print "Sending y"
s.send(str(y))

print
print s.recv(1024) 


# close the connection 
s.close()	 

