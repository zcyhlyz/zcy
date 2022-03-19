
def addTwoNumbers(l1,l2):
    l1=l1[::-1]
    l2=l2[::-1]
    l1 = int(''.join(map(str, l1)))
    l2 = int(''.join(map(str, l2)))
    l=l1+l2
    l=str(l)
    print(l)
    res=[]
    for i in l:
        res.append(int(i))
    res=res[::-1]
    return res
print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))

