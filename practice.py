# print("저는 %d살입니다." % 20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("Apple은 %c로 시작해요" % "A")

# # %s
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # 방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))

# # 방법 4
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

# # 탈출문자
# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 \"나도코딩\"입니다.")
# # \" \' : 문장 내에서 따옴표
# print("C:\\Users\\chan\\Desktop\\pythonworkspace>")
# # \r : 커서를 맨앞으로 이동

# # quiz
# url = "http://naver.com"
# my_str = url.replace("http://","")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))

# 리스트 []
# 지하철 칸별로 10명, 20명, 30명


# subway = [10, 20, 30]
# print(subway)
# subway = ["유", "조", "박"]
# print(subway)
# # 조는 몇 번째 칸에 타고 있는가?
# print(subway.index("조"))
# # 하가 다음 정류장에서 다음 칸에 탐
# subway.append("하")
# print(subway)
# # 정을 유/조 사이에 태움
# subway.insert(1, "정")
# print(subway)
# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)
# # 같은 이름의 사람이 몇 명 있는 지 확인
# subway.append("유")
# print(subway)
# print(subway.count("유"))

# # 정렬도 가능
# num_list = [5,4,3,2,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)
# # 다양한 자료형 함께 사용
# num_list = [5,4,3,2,1] 
# mix_list = ["조", 20, True]
# print(mix_list)

# num_list.extend(mix_list)
# print(num_list)


# # 사전
# cabinet = {3:"유", 100:"김"}
# print(cabinet[3])
# print(cabinet.get(3))

# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능"))
# print("hi")

# print(3 in cabinet)

cabinet = {"A-3":"유", "B-100":"김"}
print(cabinet["A-3"])

# 새손님
print(cabinet)
cabinet["A-3"] = "종"
cabinet["C-20"] = "조"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)