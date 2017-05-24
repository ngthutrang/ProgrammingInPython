import os
from os import listdir

def rename_files():
	directory = "/Users/trang/Documents/Courses/ProgrammingInPython/secret"
	# 1. get files from a folder
	file_list = os.listdir(directory)
	print(file_list)

	# 2. rename each file
	for file_name in file_list:
		new_name = file_name.translate(None, "0123456789")
		print(file_name)
		print(new_name)
		os.rename(directory + "/" + file_name, directory + "/" + new_name)

rename_files()

