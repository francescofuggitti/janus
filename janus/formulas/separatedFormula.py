class SeparatedFormula:

    def __init__(self, triple):
        self.triple = triple
        self.validate()

    def validate(self):
        if len(self.triple) == 3:
            return True
        else:
            raise ValueError('[ERROR]: input is not a triple')

    def __str__(self):
        return str(self.triple)

    def __iter__(self):
        for elem in self.triple:
            yield elem