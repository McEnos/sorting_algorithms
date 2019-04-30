def insertion_sort(data):
	for index in range(1,len(data)):
		current_value = data[index]
		position = index
		while position > 0 and data[position - 1] > current_value:
			data[position] = data[position - 1]
			position = position - 1
		data[position] = current_value

	return data