'''
파일명: Ex08-2-break.py
'''
i = 0
while i < 7:
    j = 0
    while j < i+1:
        print('*', end='')
        j += 1
    print()
    i += 1



i = 0
while i < 7:
    j = 0
    while j < i+1:
        print('*', end='')
        if j == 3:
            break
        j += 1
    print()
    i += 1

