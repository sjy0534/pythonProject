'''
파일명: Ex03-2-print.py

print() 함수
    - sep: 값 사이 구분자 (기본: 공백)
    - end: 출력 끝 문자 (기본: \n)
    - file: 출력 대상(기본: sys.stdout)
'''
from idlelib.iomenu import encoding

# 1. 기본 출력
pokemon = '피카츄'
level = 25
print('포켓몬:', pokemon, '레벨:', level) # , 자동 공백 추가

# 2. sep 매개변수
stats = ['피카츄', '전기', '35', '55']
# * 언패킹(unpacking) 피카츄 전기 35 55
print(*stats, sep=',')  # 쉼표로 구분

# 3. end 매개변수
print('피카츄', end='>')
print('라이츄', end='>')
print('파이리')

# 4. 파일 출력
with open('pokemon.txt', 'w', encoding='UTF-8') as file:    # with 코드가 끝나면 자동으로 저장하고 꺼줌, W 쓰기 권한 줌, 이 파일을 변수화 시킴 as file
    print('name: 피카츄', file=file)   # file=file 프린트의 목적지, 위에서 만든 파일에 출력
    print('type: 전기', file=file)

file = open('pokemon1.txt', 'w', encoding='UTF-8') as file:   # with 없이 하려면 close 해줘야 함
    print('name: 피카츄', file=file)
    print('type: 전기', file=file)
file.close()



