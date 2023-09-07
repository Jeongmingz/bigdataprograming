class People:
	def __init__(self, lags, arms, head, knowledge):
		self.lags = lags
		self.arms = arms
		self.head = head
		self.knowledge = knowledge

	def about(self):
		print(f'I Have {self.lags}, {self.arms}, {self.head} and {self.knowledge}')


class Animal:
	def __init__(self, lags, arms, head):
		self.lags = lags
		self.arms = arms
		self.head = head

	def about(self):
		print(f'I Have {self.lags.left_lag}, {self.arms.left_arm}, {self.head.nose} but I dont have any knowledge')


class Lags:
	def __init__(self, left, right):
		self.left_lag = left
		self.right_lag = right


class Arms:
	def __init__(self, left, right):
		self.left_arm = left
		self.right_arm = right


class Head:
	def __init__(self, eyes, mouth, noes, ears):
		self.eyes = eyes
		self.mouth = mouth
		self.nose = noes
		self.ears = ears


class Knowledge:
	def __init__(self, kinds):
		self.kinds = kinds


arms = Arms('long','long')
lags = Lags('short','long')
head = Head('good', 'eat', 'smell', 'sight')
know = Knowledge('Programming')

jeong = People(arms=arms, lags=lags, head=head, knowledge=know)
dog = Animal(arms=arms, lags=lags, head=head)

jeong.about()
dog.about()
