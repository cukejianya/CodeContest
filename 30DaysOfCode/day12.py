class Grade(Student):
    def __init__(self,firstName,lastName,phone,score):
        Student.__init__(self, firstName,lastName,phone)
        self.score=score
    def calculate(self):
        if (90 <= self.score):
            return 'O'
        if (75 <= self.score):
            return 'E'
        if (60 <= self.score):
            return 'A'
        if (40 <= self.score):
            return 'B'
        return 'D'
