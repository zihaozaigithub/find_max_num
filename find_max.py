def find_max(a_list):
	if len(a_list) == 0:  # check if a list
		return 0
	if len(a_list) > 0:
		max_num = a_list[0]   # compare each num with [0]
		for num in a_list:
			if num >= max_num:
				max_num = num
	return max_num


a_list = [-2, 0, -1]
print(find_max(a_list))