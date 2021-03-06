# 1) function => 함수
#     특정 목적 수행을 위해
#     해당 목적의 결과를 반환계산하는
#     기능으로 프로그래밍하여 묶어 놓는 것
#
#     장점
#     a) 코드를 정리할 수 있다.
#     b) 한번 만든 함수는 이름만 호출해서 재사용할 수 있다.

# 2) 함수의 사용
# def add(a,b):
#     return  a+b
#
# def sub(a,b):
#     return  a-b
#
# def mul(a,b):
#     return  a*b
#
# def div(a,b):
#     return  a/b
#
# def quote(a,b):
#     return  a//b
#
# def reminder(a,b):
#     return  a%b
#
# num0 = 1000
# num1 = 30
# print(add(num0, num1))
# print(sub(num0, num1))
# print(mul(num0, num1))
# print(div(num0, num1))
# print(quote(num0, num1))
# print(reminder(num0, num1))

# 3) 구구단 함수 제작
#    숫자를 넣으면 해당 단을 출력하는 함수
# gugudan(3)

# def gugudan(num):
#     for i in range(1,10):
#         print("{0}X{1}={2}",format(num,i,nu*i))
#     print()
#
# gugudan(3)
# gugudan(5)
# gugudan(7)
# gugudan(9)
#
# 4) 구구단 함수 제작
# 숫자를 넣으면 해당 단의 결과를 리스트로 반환하는 함수
#      dan = gugudan(3)
#      [3,6,9,12,15,18,21,24,27]
#
# def gugudan(num):
#     return [num*i for i in range(1,10)]
#
# def gugudan1(num):
#     result = []
#     for i in range(1,10):
#         result.append(num*i)
#     return result
#
# dan = gugudan(3)
# print(dan)
# dan = gugudan1(3)
# print(dan)
# dan = gugudan(5)
# print(dan)
#
# 5) 구구단 함수 제작
#     gugudan(2,7)
#     2단 ~ 7단까지 출력하는 함수
# def gugudan(start,end):
#     for i in range(start,end+1):
#         for j in range(1,10):
#             print("{0}X{1}={2}".format(i,j,i*j),end="\t")
#         print()
#     print()
#
# gugudan(2,7)
# gugudan(3,5)

# def gugudan(start, end):
#     pass
#
# 6) 별찍기 함수 제작
#     star(5) => 아래 처럼 출력
#     *
#     **
#     ***
#     ****
#     *****

# def star(num):
#     for i in range(0,num):
#         print("*"*(i+1))
#     print()

# 7) 별찍기 함수 제작
#     star(5) => 아래 처럼 출력
#     0
#     *0
#     **0
#     ***0
#     ****0

# def star(num):
#     for i in range(0,num):
#         print("*"*i, end=" ")
#         print("O")
#     print()
#
# star(5)
# star(9)

# 8) return이란?
# def add(a,b):
#     """
#     값을 반환하지 않는 함수,
#     return을 사용하지 않아서
#     별도의 결과값을 반환하지 않으므로
#     자동으로 None 객체를 반환한다.
#     :param a: 첫번째 숫자
#     :param b: 두번째 숫자
#     :return: None
#     """
#     print(a+b)
#
# help(add)
# result = add(10,20)
# print(result)

# def add(a,b):
#     """
#     이 함수의 호출이 끝나게 되면
#     이 함수의 호출한 부분은
#     num에 담긴 값으로 교체되게 된다
#     즉, num이 이 함수가 실행된 결과값이다.
#     :param a: 첫번째 숫자
#     :param b: 두번째 숫자
#     :return: num 더해진 결과값
#     """
#     num = a+b
#     return  num
#
# result = add(100,200)
# print(result)
#
# 9) 여러 값 return

# def calc(a,b):
#     plus = a+b
#     minus = a-b
#     mul = a*b
#     div = a/b
#     return plus, minus, mul, div
# num0, num1, num2, num3 = calc(100, 50)
# print(num0); print(num1), print(num2), print(num3)
# print()
#
# result = calc()
# print(result)

# 10) 초를 입력하면 시, 분, 초를 반환하는 함수
# hour, minute, second = hmTime(3672)
# hour => 1
# minute => 1
# second = 12

def hmsTime(total_sec):
    hour = total_sec // 3600   #몫(시간)
    tempSec = total_sec % 3600 #나머지 초(분계산전)
    minute = tempSec // 60     #몫(분)
    second = tempSec % 60      #나머지 초(분계산후)
    return hour,minute,second

h,m,s = hmsTime(3672)
print("{0}시간 {1}분 {2}초".format(h,m,s))
h,m,s = hmsTime(360)
print("{0}시간 {1}분 {2}초".format(h,m,s))
