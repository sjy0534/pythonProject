'''
파일명: Ex07-4-for-dict.py
'''
#세로 편집모드 단축키: Alt + shift + insert (끌때도)

John = {'국어':90, '영어':88, '수학':95}
Emily = {'국어':92, '영어':89, '수학':96}
Michael = {'국어':95, '영어':90, '수학':92}
Jessi = {'국어':97, '영어':80, '수학':82}

Score = [John, Emily, Michael, Jessi]
print(Score)

print(f'John의 점수: {Score[0]}')
print(f'Emily의 점수: {Score[1]}')
print(f'Michael의 점수: {Score[2]}')
print(f'Jessi의 점수: {Score[3]}')


# java에서는 JASON 형식이라고 함

students = [
    {'이름':'John', '국어': 90, '영어': 85, '수학': 95},
    {'이름':'Emily', '국어': 92, '영어': 88, '수학': 96},
    {'이름':'Michael', '국어': 98, '영어': 90, '수학': 92},
    {'이름':'Jessica', '국어': 88, '영어': 82, '수학': 78}
]

for student in students:
    print(f'{student['이름']}', end= ' ')
    print(f'{student['국어']}', end= ' ')
    print(f'{student['영어']}', end= ' ')
    print(f'{student['수학']}', end= ' ')
    print()

mike = students[2]
for k, v in mike.items():
    print(f'{k}: {v}')


