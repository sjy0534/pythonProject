'''
파일명: Ex08-4-continue.py

continue
    while 문이나 for 문과 같은 반복문을 강제로 건너뛰게 한다.
'''

total = 0

for n in range(1, 101):
    if n % 3 == 0:  # n % 3: n을 3으로 나눈 나머지 값
        continue    # n이 3의 배수일때 아래 코드 실행안하고 for문
    total += n
    print(f'n: {n}, total: {total}')

