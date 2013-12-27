import re
f=open("level 3.txt","r")
g=open("opfile.txt","w")
a=f.read()
p=re.findall("[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]",a)

for i in p:
    for j in range(1,len(i)-1):
        if i[j].islower()==True:
            print i[j]
            g.write(i[j])


g.close()
f.close()
