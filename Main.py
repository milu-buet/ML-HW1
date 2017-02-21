
from DataReader import DataReader
from SingleLayerPerceptron import SingleLayerPerceptron


filenames = ['d-10.csv','d-500.csv','d-100.csv']
#filenames = ['d-100.csv',]
folds = 5
learning_rates = [0.01, 0.1, 0.2]
iterations = [100,500,1000]

for filename in filenames:
	for learning_rate in learning_rates:
		for iteration in iterations:

			dataset = DataReader(filename).get_data()
			scores = SingleLayerPerceptron(dataset, folds, learning_rate, iteration).run()

			print("File: %s, Learning rate: %s, Iterations: %s" %(filename,learning_rate,iteration))
			print('Miss Classification: %f%%' % (100.0 - sum(scores)/float(len(scores))))