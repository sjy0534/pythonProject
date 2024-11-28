'''
파일명: Ex09-1-built-in-function.py

내장함수
    파이썬에서 제공해주는 별도의 import 없이 사용할 수 있는 함수
'''
# 예제 1: 리스트와 관련된 내장 함수들
number = [1, -5, 3, 2, -8, 3, 9, -3, 4, 7, -1]
print('1. 합계:', sum(number))
print('2. 최대값:', max(number))
print('3. 최소값:', min(number))
print('4-1. 정렬된 리스트:', sorted(number))
print('4-2. 역정렬된 리스트:', sorted(number, reverse=True))
print('5-1. 절대값 맵핑:', list(map(abs, number)))   # map 함수는 모든 요소를 하나씩 abs 처리하겠다
                                                    # map(적용할 함수, 반복가능한 객체)
print('5-2. 절대값 함수:', abs(number[1]))
print('6. 리스트 길이:', len(number))

# 예제 2: 문자열과 관련된 함수들
text = "Python Programming 123"
words = ["apple", "banana", "cherry", "date"]
str_alpha = "ABC"
str_numeric = "123"

print("1-1. 문자열이 알파벳인가?:", str_alpha.isalpha())        # isalpha() 모든 문자열이 알파벳이어야 True임
print("1-2. 문자열이 숫자인가?:", str_numeric.isnumeric())        # isnumeric()
print("2. 대문자로:", text.upper())                     # upper()
print("3. 소문자로:", text.lower())                     # lower()
print("4. 문자열 분할:", text.split())                  # split()
print("5. ASCII 코드:", ord('A'))                      # ord()
print("6. ASCII to 문자:", chr(65))                    # chr()
print("7-1. 문자열 위치:", text.find("Pro"))            # find()
print("7-2. 문자열 위치:", text.index("Pro"))          # index() - 없으면 에러
print("8. 문자 개수:", text.count('P'))                # count()
print("9. 공백 제거:", text.strip())                   # strip()
print("10. 문자열 합치기:", " ".join(words))           # join()

# 예제 3: 수학과 관련된 함수들
import math
numbers = [3.14, -2.7, 5.0, -1.8, 2.5]
print("1. 반올림:", round(3.7))                        # round()
print("2. 내림:", math.floor(3.7))                     # floor()
print("3. 올림:", math.ceil(3.2))                      # ceil()
print("4. 절대값:", abs(-5))                          # abs()
print("5. 거듭제곱:", pow(2, 3))                      # pow()
print("6. 제곱근:", math.sqrt(16))                    # sqrt()
print("7. 로그:", math.log(10))                       # log()
print("8. 삼각함수:", math.sin(math.pi/2))            # sin()
print("9. 지수:", math.exp(2))                        # exp()
print("10. 팩토리얼:", math.factorial(5))             # factorial()

