import os
#import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
#import scipy

directory = './inputTraining'
for file in os.walk(directory):
	files = file[2]

data = {}
#data = []
#captchas = []

for f in files:
	g = open('./inputTraining/' + f,'r')
	text = g.read()
	
	array = text.split('\n')
	rows = int(array[0].split(' ')[0])
	cols = int(array[0].split(' ')[1])

	red_array = [[] for i in range(rows)]
	green_array = [[] for i in range(rows)]
	blue_array = [[] for i in range(rows)]

	for r in range(1, rows+1, 1):
		cols_val = array[r].split(' ')
		for c in cols_val:
			rgb = c.split(',')
			red_array[r-1].append(int(rgb[0]))
			green_array[r-1].append(int(rgb[1]))
			blue_array[r-1].append(int(rgb[2]))

	
	image = [[] for i in range(rows)]
	for i in range(rows):
		for j in range(cols):
			if (0.299*red_array[i][j] + 0.587*green_array[i][j] + 0.114*blue_array[i][j]) > 127:
				image[i].append(1)
			else:
				image[i].append(0)


	# plt.imshow(np.array(image), cmap="Greys_r")
	# plt.show()

	output_file_name = './outputTraining/' +f
	output_file_name = output_file_name.replace('input', 'output')
	g = open(output_file_name, 'r')
	captcha_value = g.read()

	
	iter_image = [[[] for j in range(rows)] for i in range(5)]

	for iter in range(5):
		for i in range(len(image)):
			for j in range(int(iter*cols/5), int((iter+1)*cols/5)):
				iter_image[iter][i].append(image[i][j])
	
	for i in range(5):
		# img = np.array(iter_image[i])
		# img = img.reshape(img.shape[0]*img.shape[1])
		# # if captcha_value[i] not in data:
		# 	data[captcha_value[i]] = [img]
		# else:
		# 	data[captcha_value[i]].append(img)

		new_img = []
		for iter_quad_x in range(0,2):
			for iter_quad_y in range(0,2):
				counter = 0
				for k in range(iter_quad_x*len(iter_image[i])/2, (iter_quad_x+1)*len(iter_image[i])/2):
					for l in range(iter_quad_y*len(iter_image[i][0])/2, (iter_quad_y+1)*len(iter_image[i][0])/2):
						if iter_image[i][k][l] == 1:
							counter += 1 
				new_img.append(counter)

		if captcha_value[i] not in data:
			data[captcha_value[i]] = [new_img]
		else:
			data[captcha_value[i]].append(new_img)

		#captchas.append(captcha_value[i])

res = {}
for i in data:
	c = 0
	res[i] = [0 for k in range(4)]
	for j in data[i]:
		for k in range(4):
			res[i][k] += j[k]
		c += 1
	for j in range(len(res[i])):
		res[i][j] = res[i][j]/c

# with open('data.txt','w') as f:
# 	f.write(str(data))

# with open('captchas.txt','w') as f:
# 	f.write(str(captchas))

import json
with open('res_json.json','w') as fp:
	json.dump(res, fp)

# model= RandomForestClassifier(n_estimators=1000)
# #nsamples, nx, ny = data.shape
# #train_dataset = data.reshape((nsamples,nx*ny))

# import zlib
# com = zlib.compress(str(data))

# com_val = zlib.compress(str(captchas))

# import ast
# decom_data = ast.literal_eval(zlib.decompress(com))[0]
# decom_captcha = ast.literal_eval(zlib.decompress(com_val))
# model.fit(decom_data, decom_captcha)

# import cPickle
# with open('train_random_forest','wb') as fp:
# 	cPickle.dump(train_dataset, fp)	

# with open('labels_random_forest','wb') as fp:
# 	cPickle.dump(captchas, fp)