data = {"A": [384, 341, 349, 327], "C": [352, 350, 346, 352], "B": [356, 335, 347, 332], "E": [343, 360, 347, 367], "D": [353, 356, 345, 348], "G": [357, 361, 348, 346], "F": [351, 354, 353, 389], "I": [344, 366, 341, 381], "H": [366, 365, 353, 364], "K": [356, 347, 337, 322], "J": [390, 369, 359, 374], "M": [363, 351, 361, 335], "L": [350, 390, 328, 363], "O": [350, 345, 350, 350], "N": [345, 342, 345, 334], "Q": [365, 351, 351, 322], "P": [343, 346, 336, 373], "S": [348, 337, 348, 326], "R": [350, 344, 340, 343], "U": [340, 366, 348, 337], "T": [369, 339, 392, 351], "W": [353, 339, 368, 353], "V": [340, 353, 371, 347], "Y": [363, 352, 384, 367], "X": [371, 348, 372, 337], "Z": [372, 335, 341, 356]}

def get_result(new_img):
	min_dist = 999999999999
	letter_chosen = ""
	for i in data:
		dist = 0
		for j in range(4):
			dist += pow(int(data[i][j]) - int(new_img[j]), 2)
		if dist < min_dist:
			min_dist = dist
			letter_chosen = i

	return letter_chosen	 

if __name__ == '__main__':
	rc = raw_input().split()
	rows = int(rc[0])
	cols = int(rc[1])
	red_array = [[] for i in range(rows)]
	green_array = [[] for i in range(rows)]
	blue_array = [[] for i in range(rows)]
	for r in range(rows):
		cols_val = raw_input().split(' ')
		for c in cols_val:
			rgb = c.split(',')
			red_array[r].append(int(rgb[0]))
			green_array[r].append(int(rgb[1]))
			blue_array[r].append(int(rgb[2]))
	image = [[] for i in range(rows)]
	for i in range(rows):
		for j in range(cols):
			if (0.299*red_array[i][j] + 0.587*green_array[i][j] + 0.114*blue_array[i][j]) > 127:
				image[i].append(1)
			else:
				image[i].append(0)
	iter_image = [[[] for j in range(rows)] for i in range(5)]
	for iter in range(5):
		for i in range(len(image)):
			for j in range(int(iter*cols/5), int((iter+1)*cols/5)):
				iter_image[iter][i].append(image[i][j])
	answer = ""
	for x in range(5):	
		img = []
		for j in iter_image[x]:
			for k in j:
				img.append(k)

		new_img = []
		for iter_quad in range(0,4):
			counter = 0
			for k in range(iter_quad*len(img)/4, (iter_quad+1)*len(img)/4):
				if img[k] == 1:
					counter += 1 
			new_img.append(counter)

		result = get_result(new_img)
		answer += result

	print answer