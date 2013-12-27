import string
p="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
q="map"
a=''.join(chr(97+i)for i in range(0,26))
b=''.join(chr(99+i)for i in range(0,24))
b+="ab"
hand=string.maketrans(a,b)
p=p.translate(hand)
q=q.translate(hand)
print q
f=open("opfile.txt","w")
f.write(p)
f.write("\n")
f.write(q)
f.close()
