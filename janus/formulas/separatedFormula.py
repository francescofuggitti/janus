class SeparatedFormula:

    def __init__(self, triple):
        self.triple = triple
        self.validate()

    def validate(self):
        if len(self.triple) == 3:
            return True
        else:
            raise ValueError('[ERROR]: the triple is too long')

    def __str__(self):
        return str(self.triple)