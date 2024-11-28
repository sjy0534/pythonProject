'''
파일명: Ex08-1-break.py

break 문
    while 문이나 for 문과 같은 반복문을 강제로 종료하는 제어문
'''

n = 1
while True:     # 무한반복문
    print(n)
    if n == 10:
        break   # while문을 종료함, 프로그램을 종료하는 것은 아님
    n += 1

print('while end')
