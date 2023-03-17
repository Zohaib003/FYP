f = open("kernel-drop-ipt.txt", "r")
l = f.readlines()
sum=0
count= 0
print(len(l))
for i in range(8,len(l),16):
    x= l[i].split("  ")
    x2 = x[len(x)-1].split("\n")
    sum = float(x2[0]) + sum 
    count = count +1
#print(f.readlines())

print("average cpu usage:-", 100 - (sum/count))
