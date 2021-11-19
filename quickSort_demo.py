def quickSort(arr):
	print(f'quickSort(arr)')
	print(f'len(arr) = {len(arr)}')
	if arr.__len__() <= 1:
		
		return
	
	def subSort(l, r):
		print(f'\tlen(arr) = {len(arr)}, l = {l}, r = {r}')
		if l > r:
			return
		wall = l
		pivot = r
		for i in range(1, r):
			print(f'\t\ti = {i}')
			if arr[i] < arr[pivot] and wall < arr.__len__():
				arr[i], arr[wall] = arr[wall], arr[i]
				wall += 1
		
		arr[wall], arr[pivot] = arr[pivot], arr[wall]
		
		print(f'l = {l}', '\t', f'wall + 1 = {wall + 1}')
		subSort(l, wall - 1)
		print(f'wall + 1 = {wall + 1}', '\t', f'r = {r}')
		subSort(wall + 1, r)
	
	# subSort(0, arr.__len__())
	subSort(0, arr.__len__() - 1)
	return arr
