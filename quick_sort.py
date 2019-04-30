def quick_sort(data):
	if len(data) <= 1:  # If list contains only 1 number or no numbers at all
		return data
	else:
		pivot = data[0]  # Set the pivot to be the first number in the list
		lesser = [i for i in data if i <= data[pivot]]  # Get list of all numbers lesser than or equal to the pivot
		greater = [i for i in data if i > data[pivot]]  # Get list of all numbers greater than the pivot
		return quick_sort(lesser) + [pivot] + quick_sort(greater)  # Recursively get sorted list

