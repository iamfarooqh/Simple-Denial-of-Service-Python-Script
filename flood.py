#!/usr/bin/env python

# Python script to automate Flooding tests.
# Written by Farooq Mohammad 
# Use the script at your own risk

import sys
import os
import subprocess
os.system('clear')   
#ip = raw_input("Please provide the IP address of the Test Server: ")
ip = sys.argv[1]
print("")
print("")
print ("++++++++++Starting TCP Protocol Scan +++++++++++++")
tcpScan = os.system("/usr/bin/nmap -sS -p 1-100 -Pn --webxml -oA TCPSCAN %s" %ip)
#print tcpScan
print ("++++++++++ END OF TCP Protocol Scan ++++++++++++++")
#print("")
#print("")
ports = os.popen("/bin/cat  $PWD/TCPSCAN.xml | grep 'portid' |cut -d '=' -f 3 | cut -d '>' -f 1 | cut -d '\"' -f 2 ").read()
print ports
for port in ports.split():
    #flood = os.system("/bin/ping  -c %s " %port)
    print "hello"
    print port
