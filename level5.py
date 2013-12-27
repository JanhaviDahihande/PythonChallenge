import pickle
f=open("opfile.txt","w")
data=pickle.load(open("level5.txt","r"))

#because pickle data needs to have a readline.


for i in data:
	f.write("\n")
	for j in i:
		for k in range(0,j[1]):
			f.write(j[0])




f.close()