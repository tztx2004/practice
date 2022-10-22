print("hello world")
station = "사당"
print("" + station +"행 열차가 들어오고 있습니다")
print(3/2)
print(10//3) # 몫 3
print(10%3) # 나머지 1

#연산자
print(abs(-5)) # 절댓값 5
print(pow(4,2)) # 4^2 = 16
print(max(12,5)) # 가장 큰 값 = 12
print(min(12,5)) # 가장 작은 값 = 5
print(round(3.14)) # 반올림 = 3

from random import *
print(random()) # 0.0~1.0 미만의 임의의 값 생성
print(int(random() * 10)) # 정수값만
print(int(random() * 10) + 1) # 1 ~10 이하의 임의의 값 생성

# 로또 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
print("----")
print(randrange(1,46)) # 1~46미만의 임의의 값 생성
print(randrange(1,46)) # 1~46미만의 임의의 값 생성
print(randrange(1,46)) # 1~46미만의 임의의 값 생성
print(randrange(1,46)) # 1~46미만의 임의의 값 생성
print(randrange(1,46)) # 1~46미만의 임의의 값 생성
print(randrange(1,46)) # 1~46미만의 임의의 값 생성
print("----")
print(randint(1,45)) # 1~45 이하의 임의의 값 생성

jumin = "960928-1234567"
print("성별 = " + jumin[7]) #
print("연 : " + jumin[0:2]) # 0부터 2직전까지의(0.1)
print("생년월일 = " + jumin[:6]) # 처음부터 6직전까지
print("뒷자리 = " + jumin[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 찾는문자가없으면 -1을 출력
# print(python.index("Java"))
print("hi")
print(python.count("n"))

# 문자열포맷
# 방법1 
from turtle import color
print("나는 %d살입니다" % 20) # 정수만 가능
print("나는 %s를 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A")
# %s 어지간하면 다 가능
print("나는 %s색과 %s색을 좋아해요" % ("빨간", "파란"))

# 방법2
print("나는 {}살이며, {}색을 좋아해요".format(20, "파란"))
print("나는 {1}색과 {0}색을 좋아해요".format("빨간", "파란"))

#방법3
print("나는 {age}살이며 {color}색을 좋아해요".format(age = 20, color = "파란"))

#방법4 
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색을 좋아해요") # 문장앞에 f를 입력해야함

#탈출문자
#\n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타") 
print("저는 \"정찬\"입니다")
print("저는 '정찬'입니다")

# \\ : 문장 내에서 \
print("C:\\Users\\chan\\Desktop\\pythonworkspac")
# \r : 커서를 맨앞으로 이동
print("Red Apple\rpine")
# \b : 백스페이스
print("redd\bapple")
# \t : 탭
print("red\tapple")
