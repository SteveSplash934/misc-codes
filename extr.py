#!/data/data/com.termux/files/usr/bin/python
import string
import random

filename = str(input("Filename: "))

'''
p1 = int(input("Enter first position: "))
p2 = int(input("Enter last position: "))
c1 = str(input("Enter character in start position: "))
c2 = str(input("Enter character in last position: "))
'''

file = open(filename, "r")
newFilename = "extracted__" + filename

newFile = open(newFilename, "w")

for content in file:
	if content[5] == "7" and content[6] == "9":
		newFile.write(content)
	else:
		print("Data provide are not found and nothing is done")
print("Done Boss!!! ROCK ON")
file.close()
newFile.close()

# p1: 5, c1: 7, p2:6, c2:8
