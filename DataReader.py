from csv import reader

class DataReader():

	def __init__(self,filename):
		self.filename = filename


	def load_csv(self,filename):
		dataset = list()
		with open(self.filename, 'r') as file:
			csv_reader = reader(file)
			for row in csv_reader:
				if not row:
					continue
				dataset.append(row)


		return dataset[1:]


	def str_column_to_float(self,dataset, column):
		for row in dataset:
			row[column] = float(row[column].strip())


	def str_column_to_int(self,dataset, column):
		class_values = [row[column] for row in dataset]
		unique = set(class_values)
		lookup = dict()
		for i, value in enumerate(unique):
			lookup[value] = i
		for row in dataset:
			row[column] = lookup[row[column]]
		return lookup


	def get_data(self):
		dataset = self.load_csv(self.filename)
		for i in range(len(dataset[0])-1):
			self.str_column_to_float(dataset, i)
		self.str_column_to_int(dataset, len(dataset[0])-1)
		return dataset
