# Ch_10 함수, 34p 패드워드 입력횟수 3회 제한

# 1
'''
def checkPassword(pw):
    global count
    count += 1
    if pw == "python":
        return(1)
    return(0)

count = 0
pw = input("패스워드 입력: ")
state = checkPassword(pw)

while count < 3:
    if state == 1:
        break
    pw = input("패스워드 재입력: ")
    state = checkPassword(pw)
    
if count < 3:
    print("로그인 성공")
else:
    print("부정사용자임(3회 패스워드 오류)")
'''
# 2
'''
def checkPassword(pw):
    global count
    count += 1
    if pw == "python":
        return(1)
    return(0)

count = 0
pw = input("패스워드 입력: ")
state = checkPassword(pw)

while count < 3:
    if state == 1:
        print("로그인 성공")
        break
    pw = input("패스워드 재입력: ")
    state = checkPassword(pw)
    
if count == 3:
    print("부정사용자임(3회 패스워드 오류)")
'''
# 3
'''
count = 0
pw = input("패스워드 입력: ")

for i in range(0,2): #0 #1
    if pw == "python":
        print("로그인 성공")
        break
    else:
        pw = input("패스워드 재입력: ")
        count +=1 #1 #2
if count == 2:
    print("부정사용자임(3회 패스워드 오류)")
'''

