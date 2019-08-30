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