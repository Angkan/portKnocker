root@kali:~/Desktop/tools# cat knocker.py 
from itertools import permutations
import socket

def knockPort(ipAddr,port):
	s = socket.socket()
	port = int(port)
	try:
		s.connect((ipAddr,port))
		s.send("data")
		s.close()
	except Exception,e:
		print str(e)

def main():
	print "[+]A simple port knocker made for CTF"
	ipAddr = raw_input("Enter the IP address: ")
	userInput = raw_input("Enter port list comma separated: ")
	userInput = userInput.split(",")
	print "[+]list is " + str(userInput)
	for item in permutations(userInput,3):
		portList = list(item)
		print "[+]Trying combination: " + str(portList)
		for port in portList:
			knockPort(ipAddr,port)

if __name__ == "__main__":
	main()
