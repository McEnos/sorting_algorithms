def bubble_sort(data):
	for i in range(len(data)):#traverse through all data elements
		for j in range(0,len(data)-i-1):#last i elements are already in place,travrse the data from 0 to n-i-1
			if data[j] > data[j+1]:#swap if the element found is greater than the next element
				data[j],data[j+1] = data[j+1],data[j]
	return data