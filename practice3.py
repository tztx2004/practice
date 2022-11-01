# #문자열
# #print('풍선'*3)

# #참/거짓
# #print(5>10)
# #print(not True)

# # animal = "강아지"
# # name = "연탄이"
# # age = 4
# # hobby = "산책"
# # is_adult = age >= 3

# # print("우리집 " + animal + "의 이름은 " + name + "에요")
# # print(name + "는 "+ str(age) +"살이며, " + hobby + "을 아주 좋아해요")
# # print(name, "는 어른일까요?", str(is_adult))

# # station = "사당"
# # print(station + "행 열차가 들어오고 있습니다.")

# # print(5//3) #몫
# # print(5%3) #나머지
# # print(3 == 3) #true
# # print(1 != 3) #true
# # print(not(1 != 3))#false
# # print((3>0)and(3<5)) #true
# # print((3>0) | (3>5)) #or

# # number = 2 + 3 * 4 #14
# # print(number)
# # number += 2
# # print(number)
# # number *= 2
# # print(number)

# # print(abs(-5)) #절댓값
# # print(pow(4, 2)) # 4^2
# # print(max(5, 12))
# # print(round(3.12)) # 반올림

# # from math import *
# # print(floor(4.99)) # 내림
# # print(ceil(3.14)) # 올림
# # print(sqrt(16)) # 제곱근

# from random import *

# # print(random())
# # print(random()*10)
# # print(int(random()* 45) + 1)

# # print(randrange(1, 46))
# # print(randrange(1, 46))
# # print(randrange(1, 46))
# # print(randrange(1, 46))
# # print(randrange(1, 46))
# # print(randrange(1, 46))

# from random import *

# date = randint(4, 29)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# # 튜플
# menu = ("돈가스", "치즈까스")
# print(menu[0])
# (name, age, hobby) = ("김종국", "24", "코딩")
# print(name, age, hobby)

# # 집합 (set)
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유", "김", "양"}
# py = set(["유", "박"])
# # 교집합
# print(java & py) # print(java.intersection(py))
# # 합집합
# print(java | py) # print(java.union(py))
# # 차집합
# print(java - py) # print(java.difference(py))

# java.add("정")
# print(java)

# py.remove("유")
# print(py)

# # 자료구조 변경 
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))

# # 퀴즈
# from random import *
# users = range(1, 21)
# users = list(users)
# shuffle(users)
# print(users)
# winners = sample(users, 4)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하드립니다 --")

# # if
# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지마세요")
    
# # for
# for wating_no in [0,1,2,3,4,5]:
#     print("대기번호 : {0}".format(wating_no))

# # while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피 준비되었습니다. {1} 남았어요 ".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피 준비되었습니다. {1} 호출".format(customer, index))
#     index += 1

# customer = "토르"
# person = "unknown"

# while person != customer:
#     print("{0}, 커피 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# absent = [2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와.".format(student))
#         break
#     print("{0} 책읽어봐.".format(student))

# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student]
# print(student)

# students = ["iron man", "thor", "i am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["iron man", "thor", "i am groot"]
# students = [i.upper() for i in students]
# print(students)

# # 퀴즈 5
# from random import *
# cnt = 0
# for i in range(1,51):
#     time = randrange(1,51)
#     if 5 <= time <= 15:
#         print("[o] {0} 번째 손님 (소요시간 : {1}분)".format(i,time))
#         cnt += 1
#     else :
#         print("[ ] {0} 번째 손님 (소요시간 : {1}분)".format(i,time))
# print("총 탑승승객 : {0} 분".format(cnt))

# 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else: 
#          print("출금이 완료되지 못하였습니다. 잔액은 {0} 원입니다.".format(balance))
#          return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission
    
# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름: {0} \t나이 : {1} \t주 사용 언어 : {2}".\
#         format(name, age, main_lang))
# profile("유재석", 20, "파이썬")

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0} \t나이 : {1} \t주 사용 언어 : {2}".\
#         format(name, age, main_lang))
# profile("유재석")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)
# profile(name="유재석", main_lang="파이썬", age = 20)

# 가변인수
# def profile(name, age, *language):
#     print("이름: {0}\t나이 : {1}\t".format(name, age), end = " ")
#     for lang in language:
#         print(lang, end = " ")
#     print()

# profile("유재석", 20, "python", "java", "c", "c++", "c#")
# profile("김태호", 21, "Kotline", "Swift")

# # 지역변수, 전역변수
# gun = 10

# def checkout(soldiers): #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkout_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 :{0}".format(gun))
# gun = checkout_ret(gun, 2) # 두명이 경계근무 나감
# print("남은 총 : {0}".format(gun))

# 퀴즈
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     elif gender == "여자":
#         return height * height * 21

# height, gender = 175, "남자"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# import sys
# print("python", "java", file = sys.stdout)
# print("python", "java", file = sys.stderr)

# # 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#    print(subject, score)
#    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행순번표
# for num in range(1,21):
#     print("대기번호 :" + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ") # 사용자한테서 받는 값은 전부 str(문자형)처리됨
# print(type(answer))
#print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일땐 +표시, 음수일 땐 -표시
# print("{0: >+10}".format(-500))
# # 왼쪽정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))
# # 세자리수 마다 ,찍기
# print("{0:,}".format(1000000000))
# # 세자리수 마다 ,찍고 부호까지
# print("{0:+,}".format(-1000000000))
# # 빈자리는 ^로 채우기
# print("{0:^<+30,}".format(-1000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# 소수점 특정자리수까지 출력(소수점 3째 자리까지 출력)
# print("{0:.2f}".format(5/3))

# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline(), end = "") # 커서이동 막기
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profill.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# # with
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# 퀴즈 7
for i in range(1,51):
    with open(str(i) + "주차.txt","w",encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")


