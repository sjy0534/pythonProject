'''
파일명: Ex02-3-type-1.py

기본 데이터 타입:
    - 문자열(str): 문자열 저장
    - 정수(int): 숫자를 저장
    - 실수(float): 소수점 있는 숫자를 저장
    - 불린(bool): 참/거짓(True/False) 저장
연산 할 때 타입이 구분이 되어 있어야 함

줄 이동 단축키 Ctrl + Shift + 위아래 방향키

'''
from operator import truediv

# 1. 문자열 타입
text = 'Hello, World'
print('문자열:', text)
print('문자열 타입:', type(text))

# 2. 숫자 타입
interger = 20
float_number = 20.5
print('정수:', interger)
print('정수 타입:', type(interger))
print('실수:', float_number)
print('실수 타입:', type(float_number))

# 3. 불린 타입
bool_true = True
bool_false = False
print('불린1:', bool_true)
print('불린1 타입:', type(bool_true))
print('불린2:', bool_false)
print('불린2 타입:', type(bool_false))

