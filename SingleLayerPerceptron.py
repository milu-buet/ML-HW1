from random import seed
from random import randrange, random

class SingleLayerPerceptron():

	def __init__(self,dataset, folds,learning_rate, iteration):
		self.dataset = dataset
		self.folds = folds
		self.iteration = iteration
		self.learning_rate = learning_rate
		self.scores = None
		seed(1)

	def run(self):
		self.scores = self.RunAlgo(self.dataset, self.perceptron, self.folds, self.learning_rate, self.iteration)
		return self.scores



	def crossValidationSplit(self,dataset, folds):
		dataset_split = list()
		dataset_copy = list(dataset)
		fold_size = int(len(dataset) / folds)
		for i in range(folds):
			fold = list()
			while len(fold) < fold_size:
				index = randrange(len(dataset_copy))
				fold.append(dataset_copy.pop(index))
			dataset_split.append(fold)
		return dataset_split


	def metric(self,actual, ThresholdEvaluateed):
		correct = 0
		for i in range(len(actual)):
			if actual[i] == ThresholdEvaluateed[i]:
				correct += 1
		return correct / float(len(actual)) * 100.0


	def RunAlgo(self,dataset, algorithm, folds, *args):
		folds = self.crossValidationSplit(dataset, folds)
		scores = list()
		for fold in folds:
			train_set = list(folds)
			train_set.remove(fold)
			train_set = sum(train_set, [])
			test_set = list()
			for row in fold:
				row_copy = list(row)
				test_set.append(row_copy)
				row_copy[-1] = None
			ThresholdEvaluateed = algorithm(train_set, test_set, *args)
			actual = [row[-1] for row in fold]
			accuracy = self.metric(actual, ThresholdEvaluateed)
			scores.append(accuracy)
			print("30% ...")
		return scores


	def ThresholdEvaluate(self,row, weights):
		activation = weights[0]
		for i in range(len(row)-1):
			activation += weights[i + 1] * row[i]
		return 1 if activation >= 0.0 else 0


	def trainWeights(self,train, learning_rate, iteration):
		weights = [random() for i in range(len(train[0]))]
		for epoch in range(iteration):
			for row in train:
				ThresholdEvaluateion = self.ThresholdEvaluate(row, weights)
				error = row[-1] - ThresholdEvaluateion
				weights[0] = weights[0] + learning_rate * error
				for i in range(len(row)-1):
					weights[i + 1] = weights[i + 1] + learning_rate * error * row[i]
		return weights


	def perceptron(self,train, test, learning_rate, iteration):
		ThresholdEvaluateions = list()
		weights = self.trainWeights(train, learning_rate, iteration)
		for row in test:
			ThresholdEvaluateion = self.ThresholdEvaluate(row, weights)
			ThresholdEvaluateions.append(ThresholdEvaluateion)
		return(ThresholdEvaluateions)