f=open("level 2.txt","r")
g=open("opfile.txt","w")
a=f.read()
a=a.splitlines()
dic={}
p=[]
for i in a:
    for j in i:
        if j not in p:
            p.append(j)
        dic[j]=dic.get(j,0)+1


for i in p:
    if dic[i]==1:
        g.write(i)



g.close()
f.close()
