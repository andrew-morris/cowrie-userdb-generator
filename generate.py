#!/usr/bin/env python

from random import shuffle

def main():
	f = open("passwords.txt", "r")
	passwords = f.read().split("\n")
	f.close()
	shuffle(passwords)
	for i in range(1, 15):
		print "root:x:%s" % passwords[i]

if __name__ == "__main__":
	main()