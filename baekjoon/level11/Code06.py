from cProfile import label
import sys 
n = int(sys.stdin.readline())
array = []
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    array.append((x, y))

array = sorted(array, key = lambda array : (array[0], array[1]))

for i in range(len(array)) :
    print(array[i][0], array[i][1])
