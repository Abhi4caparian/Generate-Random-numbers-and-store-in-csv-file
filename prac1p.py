from random import randint

fo = open("csv.csv","w")
print("file open")
i=0
while(i<10000):
    t=randint(0,10000)
    fo.write(str(t)+"\n")    
    i=i+1
fo.close();
print("file close")
