def transform(array, upsample_factor, new_rows, new_cols):
	new_array = [[] for i in range(new_rows)]
	for i in range(new_rows):
		for j in range(new_cols):
			new_array[i].append(array[i/upsample_factor][j/upsample_factor])
	return new_array



if __name__ == '__main__':
	dims = raw_input().split()
	
	rows = int(dims[0])
	cols = int(dims[1])
	upsample_factor = int(dims[2])

	new_dims = raw_input().split()
	new_rows = int(new_dims[0])
	new_cols = int(new_dims[1])

	red_array = [[] for i in range(rows)]
	green_array = [[] for i in range(rows)]
	blue_array = [[] for i in range(rows)]

	for i in range(rows):
		val_cols = raw_input().split()
		for vc in val_cols:
			rgb = vc.split(',')
			red_array[i].append(int(rgb[0]))
			green_array[i].append(int(rgb[1]))
			blue_array[i].append(int(rgb[2]))				


	new_red_array = transform(red_array,upsample_factor,new_rows,new_cols)
	new_green_array = transform(green_array,upsample_factor,new_rows,new_cols)
	new_blue_array = transform(blue_array,upsample_factor,new_rows,new_cols)

	for i in range(new_rows):
		string = ""
		for j in range(new_cols):
			string += "%s,%s,%s " % (str(new_red_array[i][j]), str(new_green_array[i][j]), str(new_blue_array[i][j]))
		print string	
