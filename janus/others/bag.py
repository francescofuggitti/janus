from collections import Counter

class Bag(Counter):

    def __init__(self, _items=None, **kwargs):
        _items = [] if _items is None else _items
        super().__init__(_items, **kwargs)

    def __len__(self):
        return sum(self.values())

    def __add__(self, other):
        merged_bag = Bag()
        merged_bag.update(self)
        merged_bag.update(other)
        return merged_bag

    def __str__(self):
        format_str = '{}[{}]'.format
        return 'Bag({})'.format(', '.join(format_str(k, v) for k, v in self.items()))

    def __iter__(self):
        yield from self.elements()

    def count(self, item):
        return self[item]

if __name__ == '__main__':
    #b = Bag([{('s1','A1')}, {('s0','A1')}, {('s0','A1'), ('s0','A2')}]) #set is not hashable
    b = Bag('aaabbccd')
    print(b)