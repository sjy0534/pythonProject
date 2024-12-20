'''
파일명: Ex19-07-Heap2.py
'''

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        return heapq.heappop(self.heap)

# 실행코드
heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print('======MinHeap=====')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())
