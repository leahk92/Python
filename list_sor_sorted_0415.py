'''
str1 = "Hello!"
str1 = list(str1)
print(str1)

str1.insert(5,"beautiful")
print(str1)
'''
'''
I = [50,30,20]
print(I)
I.remove(0)
print(I)
'''

'''
StringBuilder sb = new StringBuilder("Hello!");

sb.Insert(5, "beautiful");
sb.Insert(0, "Wow, ");

Console.WriteLine(sb.ToString()); // "Wow, Hellobeautiful!"
'''
'''
# 21p
class1 = [70, 80, 60, 80, 90]
class2 = [85, 95, 80, 65, 70]
print(class1)
print(class2)

class1.extend(class2)
print(class1)

n = class1.count(80)
'''

# sort()
# 원본 리스트를 정렬 (새로운 변수 x)
s = [20, 50, 30, 20]
print("원본 리스트 : ",s)

s.sort()
print(s)

ss = s
print(ss)

s.sort(reverse=True) #내림차순 정렬
print(s)

print("\n")
s2 = [20, 50, 30, 20, 10]
print("원본 리스트 : ",s2)

s3 = s2.sort()
print(s3) #결과: None
print(s2)

print("\n")
# sorted()
# 새로운 변수에 할당 (복사본으로 정렬)
std = [20, 50, 30, 20]
print("원본 리스트 : ",std) 

std2 = sorted(std)
print(std2)  #정렬됨
print(std)   #그대로











