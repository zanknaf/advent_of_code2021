j=0
with open("day1.txt") as f:
    data=f.readlines()
    d=[]
    sums=[]
    for line in data:
        d.append(int(line))
    print(d)
    for i in range(0,len(d)-2):
        sums.append(d[i]+d[i+1]+d[i+2])
    a=sums[0]
    for i in range(1,len(sums)):
        if (a<sums[i]):
            a=sums[i]
            j=j+1
        else:
            a=sums[i]
print(j)
