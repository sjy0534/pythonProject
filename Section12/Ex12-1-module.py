'''
파일명: Ex12-1-module.py

모듈(module)
    변수나 함수 또는 클래스를 모아 놓은 파일을 모듈이라고 한다.

모듈 사용법
import 모듈명
'''

import converter

miles = converter.kilometer_to_miles(150)
print(f'150 km = {miles} miles')

pound = converter.gram_to_pound(1000)
print(f'1000 g = {pound} pounds')