def selection_sort(data):
	for i in range(len(data)):# Traverse through all data elements 
		min_index = i
		for j in range(i+1,len(data)):#Find the minimum element in remaining  unsorted array 
			if data[min_index] > data[j]:
				min_index = j
		if min_index != i:
			data[min_index],data[i] = data[i],data[min_index]
	return data