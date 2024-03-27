# 1번
'''
for i in range(1,6):
    print("* "*10)
print("")
'''
#2번
'''
i = 5
while i >= 1:
    print("* "*10)
    i -= 1
print("")
'''
#3번
'''
# 3-2 C샵으로
for i in range(6,0,-1):
    for j in range(1,i+1):
        print("%d" %i, end=" ")
    print("")
'''
'''
# 3-1
for i in range(6,0,-1):
    for j in range(1,7):
        while j <= i: 
            print("%d" %i, end=" ")
            break    
    print("")
'''
#4번
'''
# 4-3 C샵으로
for i in range(1,7):
    for j in range(0,i):
        print(j, end=" ")
    print("")
'''
'''
# 4-2
for i in range(0,6):
    for j in range(0,6):
        if j <= i:
            print("%d" %j, end=" ")      
    print("")
'''
'''
# 4-1
for i in range(0,6):
    for j in range(0,6):
        print("%d" %j, end=" ")
        if j == i:
            break
    print("")
'''
#5번
'''
for i in range(1,9):
    if i >=2 and i<=7:
        print("*", format("*",">6"))
    else:
        print("*"*8)
'''
#6번
'''
total = 0
for i in range(1,100,2):
    total += i
    if i == 99:
        break
    print("%d + " %i, end="")   
print("99 = %d" %total)
'''
    

