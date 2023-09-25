s='Pz-/aI/J`EvfthGH'
k=66
asci=[]
for i in range(len(s)):
    asci.append(ord(s[i]))
# print(asci)
new=[i+k for i in asci]
# print(new)
for i in new:
    if 97<=i<=122:
        pass
    elif(65<=i<=90):
        pass
    else:
        if(i>65):
          a=new.index(i)
          if(s[a].islower()):
            new[a]=97+(asci[a]-97+k)%26
          else:
              new[a]=65+(asci[a]-65+k)%26
# print(new)
ch=[]
for i in new:
    if chr(i).isalpha():
      ch.append(chr(i))
    else:
        id=new.index(i)
        ch.append(s[id])
f="".join(ch)
print(f)
