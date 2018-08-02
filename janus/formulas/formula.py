from janus.formulas.separatedFormula import SeparatedFormula

class Formula:

    def __init__(self, separatedFormulas):
        self.separatedFormulas = separatedFormulas
        self.validate()

    def validate(self):
        if all(isinstance(x, SeparatedFormula) for x in self.separatedFormulas) and self.separatedFormulas:
            return True
        else:
            raise ValueError('[ERROR]: Different types for conjuncts')

    def __str__(self):
        return ', '.join(map(str, self.separatedFormulas))

    def __iter__(self):
        for triple in self.separatedFormulas:
            yield triple