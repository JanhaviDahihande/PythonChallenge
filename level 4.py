import urllib2,re

nothing="8022"

#"yes. now divide by 2 and go on" comes at nothing=16044"
	
while(nothing):
	rul='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing
	response = urllib2.urlopen(rul)
	html = response.read()
	something="".join(re.findall("nothing is [0-9]+",html))
	nothing="".join(re.findall("[0-9]+",something))#to deal with stupid condition where they put some random numbers to mislead the code.
	print html

f=open("opfile.txt","w")
f.write(html)