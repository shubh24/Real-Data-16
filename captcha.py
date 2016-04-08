import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier


directory = './inputTraining'
for file in os.walk(directory):
	files = file[2]

data = {}
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
			if (0.299*red_array[i][j] + 0.587*green_array[i][j] + 0.114*blue_array[i][j])>127:
				image[i].append(255)
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
			for j in range(iter*cols/5, (iter+1)*cols/5):
				iter_image[iter][i].append(image[i][j])
	
	for i in range(5):
		img = np.array(iter_image[i])
		img = img.reshape(img.shape[0]*img.shape[1])
		if captcha_value[i] not in data:
			data[captcha_value[i]] = [img]
		else:
			data[captcha_value[i]].append(img)

res = {}
for i in data:
	c = 0
	res[i] = [0 for k in range(len(data[i][0]))]
	for j in data[i]:
		for k in range(len(j)):
			res[i][k] += j[k]
		c += 1
	for j in res[i]:
		j = j/c
import json
with open('res_json.json','w') as fp:
	json.dump(res, fp)

#model= RandomForestClassifier(n_estimators=1000)
# nsamples, nx, ny = data.shape
# train_dataset = data.reshape((nsamples,nx*ny))
# model.fit(train_dataset, captchas)

# import cPickle
# with open('train_random_forest','wb') as fp:
# 	cPickle.dump(train_dataset, fp)	

# with open('labels_random_forest','wb') as fp:
# 	cPickle.dump(captchas, fp)