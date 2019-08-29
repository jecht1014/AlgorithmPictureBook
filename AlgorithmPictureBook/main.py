import sort
import time

l = [5, 3, 4, 7, 2, 8, 6, 9, 1]
start_time = time.time()
sorted_list = sort.selection_sort(l, True)
print('time:{0:.3f}'.format(time.time()-start_time))