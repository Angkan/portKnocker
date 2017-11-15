from itertools import permutations
import socket

def knockPort(ipAddr,port):
	s = socket.socket()
	port = int(port)
	try:
		print "here"
		s.settimeout(1)
		s.connect((ipAddr,port))
		s.send("data")
#		s.settimeout(1)
		s.close()
		print "done"
	except Exception,e:
		print str(e)

def main():
	print "[+]A simple port knocker made for CTF"
	ipAddr = raw_input("Enter the IP address: ")
	userInput = raw_input("Enter port list comma separated: ")
	userInput = userInput.split(",")
	print "[+]list is " + str(userInput)
	l = len(userInput)
	print "[+]list length: " + str(l)
	for item in permutations(userInput,l):
		print "loop"
		portList = list(item)
		print "[+]Trying combination: " + str(portList)
		for port in portList:
			knockPort(ipAddr,port)

if __name__ == "__main__":
	main()
