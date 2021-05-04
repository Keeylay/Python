def countdown(num):
    arr = []
    for i in range(num, -1, -1):
        arr.append(i)
    return arr
print(countdown(num = int(input("enter number"))))

def printandreturn(a, b):
    print(a)
    return b
print(printandreturn(3, 4))

def firsrpluslength(list):
    sum = list[0] + len(list)
    return sum
print(firsrpluslength([2,3,4,5,1,3]))

def valuesgreaterthansecond(greater):
    list = []
    for i in greater:
        if i > greater[1]:
            list.append(i)
    print(len(list))
    if (len(list) == 1):
        return False
    else:
        return list
print(valuesgreaterthansecond([1,2,3,4,5,6,7]))

def thislenghtthatvalue(size, value):
    arr = []
    count = 0
    while count < size:
        arr.append(value)
        count += 1
    return arr
print(thislenghtthatvalue(22, 4))
