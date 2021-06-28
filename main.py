import socket
import sys
from datetime import datetime


# Asks for input
remoteServer = input("Enter a remote host's Ipv4 address to be scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
ports_amt = int(input("How many ports shall be checked ? : ")) + 2

print ("--------")
print ("Please wait, scanning remote host"), remoteServerIP
print ("--------")

# Check what time the scan started
t1 = datetime.now()

try:
    for port in range(1, ports_amt):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:    [Open]".format(port))
        sock.close()

except socket.gaierror:
    print ('Hostname could not be resolved...')
    sys.exit()

except socket.error:
    print ("[CONNEXION ERROR] Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()
total =  t2 - t1

print('Scanning Completed in: ' + total)
