# 1) for 문은 while 문과 상호피환될 수 있다
# 다만 명시적인 시작과 끝이 있을 때 사용
# while문보다 사용빈도가 높다

# 1) 나무를 10번 찍기
# for i in range(1,11): # 1 ~ 10
#     print("나무를 {0}번 찍는다.".format(i))

# 2) 리스트, 튜플과 함께 사용하기
# datas = [2,4,6,8,10]
# for num in datas:
#     print(num, end=", ")
# print()
#
# datas = (10,20,30,40,50)
# for num in datas:
#     print(num, end=", ")
# print()

# 3) range 함수와 사용
for i in range(10,21):
    print(i,end=" ")
print()

for i in range(10,101,2):
    print(i,end=" ")
print()

for i in range(100, 0, -2):
    print(i, end= " ")
print()