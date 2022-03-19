def towsum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return [i,j]
print(towsum([3,2,4],6))

