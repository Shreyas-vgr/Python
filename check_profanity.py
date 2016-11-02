import urllib
def read_text():
	quotes = open("movie_quotes.txt")
	contents = quotes.read()
	#print(contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
	output = connection.read()
	#print(output)
	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("No harsh words")
	connection.close()

read_text()
