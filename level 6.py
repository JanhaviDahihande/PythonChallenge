import zipfile, re
f=zipfile.ZipFile("channel.zip","r")
nothing="94191"	
comments=[]
while(nothing):		
	nothing=nothing+".txt"
	comments.append(f.getinfo(nothing).comment)
	a=f.read(nothing)
	b="".join(re.findall("nothing is [0-9]+",a))
	nothing="".join(re.findall("[0-9]+",b))
	print nothing	
	

f=open("opfile.txt","w")
for i in comments:
	f.write(i)
