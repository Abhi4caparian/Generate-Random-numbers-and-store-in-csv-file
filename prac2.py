from random import randint
k=100
j=100
fo = open("csv3.csv","w")
print('File open')
i=0
for k in range(10):
    for j in range(10):
        t=randint(0,100)
        fo.write(str(t)+",")
        j=j+1
        k=k+1
    fo.write("\n")
fo.close();
print('File close')

mp=open("csv3.csv","r")
print('File open 2')
i=0
c=[0]
for k in range(10):
    l=mp.readline();
    print(l);
    while l:
        print("inside while")
        x=l.split(',')
        for j in range(len(x)-1):
            print(l)            
            print('x[j]=',x[j])
            c.append(int(x[j]))
#            fo.write(str(t)+",")
        l=mp.readline()
#        print('c=',c)
mp.close();
print('File close 2 lines=',i);
