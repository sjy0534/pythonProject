'''
파일명: Ex02-5-list-2.py

리스트 주요 메소드
    - append(): 끝에 항목 추가
    - insert(): 지정 위치에 항목 추가
    - remove(): 항목 제거
    - pop(): 마지막 또는 지정 위치 제거하고 반환
    - clear(): 리스트 비우기
'''
from platform import release

# 1. 리스트 기본 메소드
starter_pokemon = ['피카츄', '파이리', '꼬부기']
starter_pokemon.append('이상해씨') # 끝에 추가
print('스타터 포켓몬:', starter_pokemon)

starter_pokemon.insert(1, '잠만보') #중간 삽입
print('삽입된 포켓몬:', starter_pokemon)

# 2. 리스트 제거 메소드
legendary_pokemon = ['그라돈', '가이오가', '레쿠쟈', '히드런']
print('전설의 포켓몬:', legendary_pokemon)

legendary_pokemon.remove('히드런')     # 값으로 제거
print('방출 후:', legendary_pokemon)

release = legendary_pokemon.pop(1)    # 인덱스로 제거
print('현재 남은 포켓몬:', legendary_pokemon)
print('방출 된 포켓몬:', release)

# 3. 리스트 확장과 초기화
a_team = ['나무지기', '가디안']
b_team = ['불꽃숭이', '팽도리']

a_team.extend(b_team) # 리스트 합치기
print('연합팀:', a_team)

c_team = a_team + b_team
print('연합팀2:', c_team)

a_team.clear() # 리스트 비우기
print('리셋된 팀:', a_team)

del a_team # 리스트 객체 삭제












