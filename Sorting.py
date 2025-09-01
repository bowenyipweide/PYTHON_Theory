def insertion_sort(arr):
	for i in range(1, len(arr)): #pick up an element from arr
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key: # Shift item to make room for key
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key #Insert key to the correct location
• arr = [11, 14, 5, 13, 6]
• insertion_sort(arr)
• print("Sorted array:", arr)
