import sort
import time
import random

#再帰条件の変更
import sys
sys.setrecursionlimit(100000)

l = list(range(3000))
random.shuffle(l)

start_time = time.time()
sorted_list = sort.bubble_sort(l)
print('time:{0:.3f}'.format(time.time()-start_time))

start_time = time.time()
sorted_list = sort.selection_sort(l)
print('time:{0:.3f}'.format(time.time()-start_time))

start_time = time.time()
sorted_list = sort.insertion_sort(l)
print('time:{0:.3f}'.format(time.time()-start_time))

start_time = time.time()
sorted_list = sort.heap_sort(l)
print('time:{0:.3f}'.format(time.time()-start_time))

start_time = time.time()
sorted_list = sort.merge_sort(l)
#print(sorted_list)
print('time:{0:.3f}'.format(time.time()-start_time))

start_time = time.time()
sorted_list = sort.quick_sort(l)
print('time:{0:.3f}'.format(time.time()-start_time))