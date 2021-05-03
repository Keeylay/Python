for i in range(0, 151):
    print(i)

for x in range(5, 1001):
    if x % 5 == 0:
        print(x)

for a in range(1, 101):
    if a % 10 == 0:
        print("Coding Dojo")
    elif a % 5 == 0:
        print("Coding")
    else:
        print(a)

num = 500000
oddsum = 0

for number in range(1, num+1):
    if(number % 2 != 0):
        # print(f"{number}")
        oddsum = oddsum + number
print("The final sum is {}".format(oddsum))

for count in range(2018, 0, -4):
    if count > 0:
        print(count)

lownum = 2
highnum = 9
multi = 3

for j in range(lownum, highnum+1):
    if j % multi == 0:
        print(j)