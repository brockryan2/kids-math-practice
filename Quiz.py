from kids-math-practice import Question

class Quiz():

	def __init__(self, number_of_questions=10, scored=False, number_range_min=0, number_range_max=10, timed=False, operators="+"):
		self.number_of_questions = number_of_questions
		self.scored = scored
		self.number_range_min = number_range_min
		self.number_range_max = number_range_max
		self.timed = timed
		self.operators = operators
		self._question_num = 0
		self._number_correct = 0