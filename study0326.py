#topAvg=topName=None
#bottomAvg=bottomName=None
n=int(input("학생수 입력: "))

print("\n%d번째 학생 성적처리"%1)

name = input("이름: ")
eng = int(input("영어 성적: ")) ;  math = int(input("수학 성적: "))
total = eng + math ;  avg = total / 2

if avg>=90 :  grade = 'A'
elif avg>=80 :  grade = 'B'
elif avg>=70 :  grade = 'C'
elif avg>=60 :  grade = 'D'
else :  grade =  'F'

print("-"*53)
print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
print("-"*53)
print (" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name, eng, math, total, avg, grade))
print("-"*53)

topAvg = bottomAvg= avg; topName = bottomName = name #최고, 최저 평균(이름)에 첫번째 학생 평균(이름)을 저장

for i in range(2,n+1):
    print("\n%d번째 학생 성적처리" %i)
    name = input("이름: ")
    eng = int(input("영어 성적: ")) ;  math = int(input("수학 성적: "))
    total = eng + math ;  avg = total / 2

    if avg>=90 :  grade = 'A'
    elif avg>=80 :  grade = 'B'
    elif avg>=70 :  grade = 'C'
    elif avg>=60 :  grade = 'D'
    else :  grade =  'F'
    print("-"*53)
    print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
    print("-"*53)
    print (" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name, eng, math, total, avg, grade))
    print("-"*53)

    if topAvg < avg:
       topAvg = avg; topName = name
    if bottomAvg > avg:
       bottomAvg = avg; bottomName = name
       
print("\n최고평균: %6.2f(%s)" %(topAvg, topName))
print("\n최저평균: %6.2f(%s)" %(bottomAvg, bottomName))





# 다르게 수정
n = int(input("학생수 입력: "))

topAvg = topName = None 
bottomAvg = bottomName = None

for i in range(1,n+1):

    print("\n%d번째 학생 성적처리" %i)
    name = input("이름: ")
    eng = int(input("영어 성적: ")) ;  math = int(input("수학 성적: "))
    total = eng + math ;  avg = total / 2
       
    if avg>=90 :  grade = 'A'
    elif avg>=80 :  grade = 'B'
    elif avg>=70 :  grade = 'C'
    elif avg>=60 :  grade = 'D'
    else :  grade =  'F'
    print("-"*53)
    print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
    print("-"*53)
    print (" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name, eng, math, total, avg, grade))
    print("-"*53)
  
    if topAvg is None or avg > topAvg: 
       topAvg = avg; topName = name
       
    if bottomAvg is None or avg < bottomAvg:
       bottomAvg = avg; bottomName = name

print("\n최고평균: %6.2f(%s)" %(topAvg, topName))
print("\n최저평균: %6.2f(%s)" %(bottomAvg, bottomName))


