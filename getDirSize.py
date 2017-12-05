#prompt the user for a path of a directory, and return the size of the direcory and items in it
import os

#prompt user for file path
filePath = input("Please enter the path of a directory to check its contents and size: ")
#print contents of directory
if os.path.isdir(filePath):
	print("\n".join(os.listdir(filePath)))
#print size of direcotry
	print(os.path.getsize(filePath), "Bytes in size")

