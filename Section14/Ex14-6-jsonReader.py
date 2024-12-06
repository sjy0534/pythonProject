'''
파일명: Ex14-6-jsonReader.py
'''

import json
with open('dictList.json', 'r', encoding='UTF-8') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)     # json 타입에서 파이썬 리스트형식으로 변환

    for dic in dict_list:
        print(f'이름: {dic['name']}')
        print(f'나이: {dic['age']}')
        print(f'키: {dic['spec'][0]}')
        print(f'몸무게: {dic['spec'][1]}')
        print()

