import socket
print socket.gethostbyname('localhost') # result from hosts file
print socket.gethostbyname('google.com') # your os sends out a dns query
