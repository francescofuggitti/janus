from janus.formulas.separatedFormula import SeparatedFormula

class Formula:

    def __init__(self, separatedFormulas):
        self.separatedFormulas = separatedFormulas
        self.validate()

    def validate(self):
        if all(isinstance(x, SeparatedFormula) for x in self.separatedFormulas) and not self.separatedFormulas:
            return True
        else:
            raise ValueError('[ERROR]: Different types for conjuncts')

    def __str__(self):
        for triple in self.separatedFormulas:
            return triple