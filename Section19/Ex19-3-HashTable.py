'''
파일명: Ex19-3-HashTable.py

해시테이블(Hash Table)
    해시테이블은 키와 값을 저장하는 데이터 구조로,
    요소를 빠르고 효율적인 검색, 삽입, 삭제를 허용한다.
    해시 함수는 키를 입력으로 받아 값을 저장하거나
    검색할 수 있는 배열 인덱스를 반환한다.
'''

class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size
        # self.hash_table = [None, None, None, None, None, None, None, None, None, None]

    def has_function(self, key):
        return hash(key) % self.size    # 10(size 크기)으로 나눴을 때 나머지 값인 0~9 사이의 값으로 나오게 하겠다.

    def insert(self, key, value):
        hash_index = self.has_function(key)

        if self.hash_table[hash_index] is None:
            self.hash_table[hash_index] = []

        self.hash_table[hash_index].append((key,value))

    def search(self, key):
        hash_index = self.has_function(key)
        bucket = self.hash_table[hash_index]
        if bucket is None:
            return None

        for k, v in bucket: # 튜플 언패킹(튜플에 있는 두개의 값을 k, v 각각의 변수로 받는다.)
            if k == key:
                return v

        return None

# 실행코드
hash_table = HashTable(10)  # 크기가 10인 hashtable 생성
hash_table.insert('John Doe', '555-555-5555')
hash_table.insert('Jane Doe', '555-555-5556')
hash_table.insert('Kim Doe', '555-555-5557')
hash_table.insert('Jiyoung Seo', '555-555-5558')


print(hash_table.search('John Doe'))
