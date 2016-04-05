def predict(data, all_data):
	result = []

	for i in range(0,12):
		
		historical_yearly_data = []
		for year in data:
			historical_yearly_data.append(int(year[i]))
		historical_avg = sum(historical_yearly_data)/len(historical_yearly_data)
		all_data_avg = 0
		for j in range(len(all_data)-1, len(all_data)-4, -1):
			all_data_avg += int(all_data[j])
		all_data_avg = int(all_data_avg/3)
		all_data.append(all_data_avg)

		result.append((historical_avg + all_data_avg)/2)
	return result

if __name__ == '__main__':
	months = int(raw_input())
	years = months/12
	data = [[] for i in range(0,years)]
	all_data = []
	for i in range(0,years):
		for j in range(0,12):
			x = raw_input().split()[1]
			data[i].append(x)
			all_data.append(x)
	predicted_data = predict(data, all_data)
	for i in predicted_data:
		print i