def replace_list(l, i, j):
	tmp = l[i]
	l[i] = l[j]
	l[j] = tmp
	return l

#バブルソート
def bubble_sort(sort_list, list_print = False):
	for i in range(len(sort_list)-1):
		for j in range(len(sort_list) - 1 - i):
			if sort_list[j] > sort_list[j+1]:
				sort_list = replace_list(sort_list, j, j+1)
		
		if list_print:
			print('loop:{0} list:{1}'.format(i, sort_list))

	return sort_list

#選択ソート
def selection_sort(sort_list, list_print = False):
	for i in range(len(sort_list)-1):
		min = sort_list[i]
		argmin = i
		for j in range(i+1, len(sort_list)):
			if(min > sort_list[j]):
				min = sort_list[j]
				argmin = j
		
		sort_list = replace_list(sort_list, i, argmin)
		if list_print:
			print('loop:{0} list:{1}'.format(i, sort_list))
	
	return sort_list

#挿入ソート
def insertion_sort(sort_list, list_print = False):
	for i in range(len(sort_list)):
		if i != 0:
			if sort_list[i] < sort_list[i-1]:
				for j in reversed(range(i)):
					if j != 0:
						if sort_list[j-1] < sort_list[i]:
							sort_list.insert(j, sort_list[i])
							del sort_list[i+1]
							break
					elif i != 0 and j == 0:
						sort_list.insert(0, sort_list[i])
						del sort_list[i+1]

		if list_print:
			print('loop:{0} list:{1}'.format(i, sort_list))

	return sort_list

#ヒープソート
import heapq
def heap_sort(sort_list, list_print = False):
	heapq.heapify(sort_list)
	sorted_list = []
	for i in range(len(sort_list)):
		sorted_list.append(sort_list[0])
		heapq.heappop(sort_list)

		if list_print:
			print('loop:{0} list:{1}'.format(i, sorted_list))
	
	return sorted_list

#マージソート
def merge_sort_merge(left_l, right_l, list_print):
	merge_l = []
	while((len(left_l) == 0 and len(right_l) == 0) is not True):
		if len(right_l) == 0:
			merge_l.append(left_l[0])
			left_l.pop(0)
		elif len(left_l) == 0:
			merge_l.append(right_l[0])
			right_l.pop(0)
		elif left_l[0] < right_l[0]:
			merge_l.append(left_l[0])
			left_l.pop(0)
		else:
			merge_l.append(right_l[0])
			right_l.pop(0)
	
	if list_print:
		print(merge_l)
	
	return merge_l

import math
def merge_sort(sort_list, list_print = False):
	mid = int(len(sort_list) / 2)
	if list_print:
		print(sort_list[:mid], sort_list[mid:])
	if(len(sort_list[:mid]) != 1):
		left = merge_sort(sort_list[:mid], list_print)
	else:
		left = sort_list[:mid]
	if(len(sort_list[mid:]) != 1):
		right = merge_sort(sort_list[mid:], list_print)
	else:
		right = sort_list[mid:]

	return merge_sort_merge(left, right, list_print)