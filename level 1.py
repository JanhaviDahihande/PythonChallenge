
p="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a=list(p)
for i in range(0,len(a)):
    if a[i]!=' ':
        k=ord(a[i])
        if k>96:
            k+=2
            if k>122:
                k-=26
        
            a[i]=chr(k)
        
p=''.join(str(i) for i in a)
print p




