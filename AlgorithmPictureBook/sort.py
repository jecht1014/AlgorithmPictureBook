#選択ソート
def selection_sort(sort_list, list_print = False):
	for i in range(len(sort_list)-1):
		min = sort_list[i]
		argmin = i
		for j in range(i+1, len(sort_list)):
			if(min > sort_list[j]):
				min = sort_list[j]
				argmin = j
				
		tmp = sort_list[i]
		sort_list[i] = sort_list[argmin]
		sort_list[argmin] = tmp
		if list_print:
			print('loop:{0} list:{1}'.format(i, sort_list))