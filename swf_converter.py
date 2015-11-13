import os

swf_files = os.listdir("./swf_files") # get a list of every swf file I want to get audio out of

for f in swf_files: # for every file in the list
	name_length = len(f) # get the length of the file name
	command = "swfextract -m -o {}.mp3 ./swf_lessons/{}".format(f[:name_length - 4], f) # generate the command to be used for each file
	os.system(command) # execute that command