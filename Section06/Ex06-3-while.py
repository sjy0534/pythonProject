'''
파일명: Ex06-3-while.py
'''

my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
    my_list.append(n)   # 0까지 리스트에 추가되고 끝남

my_list.pop()   # 마지막에 추가된 것 제거(0 제거)
print(my_list)

