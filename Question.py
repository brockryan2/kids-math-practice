from random import randint

class Question():

    def __init__(self, operator, number_min=0, number_max=10):
        self._number_one = randint(number_min, number_max)
        self._number_two = randint(number_min, number_max)
        self.operator   = operator

        if(operator == "+"):
            self._answer = self._number_one + self._number_two

        if(operator == "-"):
            self._answer = self._number_one - self._number_two

        if(operator == "*"):
            self._answer = self._number_one * self._number_two

        if(operator == "/"):
            self._answer = self._number_one / self._number_two

    def number_one():
        return self._number_one

    def number_two():
        return self._number_two

    def answer(self):
        return self._answer
