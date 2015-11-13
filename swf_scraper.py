import requests
import time

# Flynn Acworth

# This tool is designed to scrape .swf files off of a website. Was designed to scrape .swf mandarin lessons from the website

cd_number = 1 # the cd_number (this was important for my specific URL)
track_number = 1 # the track number (this was important for my specific URL)

while cd_number != 9: # while we are not on cd 9 (8 is the last cd for my example)
	
	time.sleep(5) # wait for 5 seconds so they don't think the server is being dossed.

	file_name = "mandarin_lesson_cd{}_track{}.swf".format(cd_number, track_number) # generate the file name based on current cd and track number

	"""
	URL GOES HERE:  Mine was automatically generated as the url for each file was predictable. it allowed me to download all .swf files
					by modifying the url based on cd and track number.
	"""

	r = requests.get(url) # request the SWF object

	if r.content[0] == "<": # if the content has this, it means it is an HTML (likely an error page). This means the cd/track doesnt exist, so we go to the next CD.
		cd_number += 1 # move onto the next cd
		track_number = 1 # reset the track back down to 1
		continue # start the loop again
	else:
		f = open(file_name, 'wb') # create a new file using the generated name in write byte mode
		f.write(r.content) # write the content to the opened file
		f.close() # close the file
		track_number += 1 # go to the next track on the cd
		print "SAVED CD{} LESSON{}".format(cd_number, track_number)

