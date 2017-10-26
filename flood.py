#!/usr/bin/env python

# Python script to automate Flooding tests.
# Written by Mr. Farooq Mohammad working as Security Engineer at Nokia.
# Use the script at your own risk. There is lot much validation that needs to be done here.
# Thanks to Mr. Haroon Sharif for his contributions to this script.

import sys
import os

os.system('clear')

ip = raw_input("Please provide the IP address of the Test Server: ")
#ip = sys.argv[1]

print("")
print ("++++++++++Starting TCP Protocol Scan +++++++++++++")
tcpScan = os.system("/usr/bin/nmap -sS -p 1-100 -Pn --webxml -oA TCPSCAN %s" %ip)
print ("++++++++++ END OF TCP Protocol Scan ++++++++++++++")
#print("")

openPorts = os.popen("/bin/cat  $PWD/TCPSCAN.xml | grep 'portid' |cut -d '=' -f 3 | cut -d '>' -f 1 | cut -d '\"' -f 2 ").read()
print ("The list of open ports are: "),
print openPorts.split()

for port in openPorts.split():
    flood = os.system("/bin/ping %s -c %s " %(ip,port))
    #print port

print ("")
print "End of Flooding attack. "
print "Now lets do a Fresh nmap scan again and compare the results"

print("")
print ("++++++++++Starting TCP Protocol Scan +++++++++++++")
newTcpScan = os.system("/usr/bin/nmap -sS -p 1-100 -Pn --webxml -oA TCPSCANnew %s" %ip)
print ("++++++++++ END OF TCP Protocol Scan ++++++++++++++")

newPorts = os.popen("/bin/cat  $PWD/TCPSCANnew.xml | grep 'portid' |cut -d '=' -f 3 | cut -d '>' -f 1 | cut -d '\"' -f 2 ").read()
print ("")

print ("The list of open ports after flood are: "),
print newPorts.split()
print ("The list of open ports before flood are: "),
print openPorts.split()

if openPorts.split() == newPorts.split():
        print "Flooding Test is passed. All ports seems to be OPEN after the tests"
else:
        print "Some ports are not open. Please verify if the ports are reachable"
