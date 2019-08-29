l = [5, 3, 4, 7, 2, 8, 6, 9, 1]

#選択ソート
for i in range(len(l)-1):
	min = l[i]
	argmin = i
	for j in range(i+1, len(l)):
		if(min > l[j]):
			min = l[j]
			argmin = j
			
	tmp = l[i]
	l[i] = l[argmin]
	l[argmin] = tmp
	
	print('loop:{0} list:{1}'.format(i, l))