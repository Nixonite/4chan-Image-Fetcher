from HTMLParser import HTMLParser
import urllib2
import sys,os

board = str(sys.argv[1])

counter = 0

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
		if(tag == "a"):
			if((".jpg" or ".png" or ".gif") in (dict(attrs)["href"])):
				if "class" not in dict(attrs):
					global counter
					fullURL = "http:"+(dict(attrs)["href"])
					print fullURL
					response = urllib2.urlopen(fullURL)
					filename = board+"_"+str(counter) + ".jpg"
					output = open(directory+"/"+filename,"wb")
					output.write(response.read())
					output.close()
					counter = counter+1

directory = "/Users/nixonite/Desktop/"+board
os.chdir("/")
if not os.path.exists(directory):
    os.makedirs(directory)

webtry = urllib2.urlopen('http://boards.4chan.org/'+board+"/")
html = webtry.read()

parser = MyHTMLParser()
parser.feed(html)

for i in range(2,11):
	webtry = urllib2.urlopen('http://boards.4chan.org/'+board+"/"+str(i))
	html = webtry.read()

	parser = MyHTMLParser()
	parser.feed(html)