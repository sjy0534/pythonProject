'''
파일명: Ex07-2-for-range.py

for문과 range()함수

range()
    연속된 숫자를 만들어 주는 함수
    예) range(1,10) => 1,2,3,4,5,6,7,8,9
'''

# range(stop)
dan = 2
for n in range(10):     # range(10): 0 ~ 9
    print(f'{dan}X{n}={dan * n}', end= ' ')
print()


# range(start, stop)
dan = 3
for n in range(1, 10):     # range(1, 10): 1 ~ 9
    print(f'{dan}X{n}={dan * n}', end = ' ')
print()
# range()를 리스트로 형변환 가능


# range(start, stop, step)
dan = 4
for n in range(1, 10, 2):   # 1부터 2씩 증가 < 10
    print(f'{dan}X{n}={dan * n}', end=' ')
print()


