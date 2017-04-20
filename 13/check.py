
class Check:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def calculate_sum(self):
        return sum([dish.price for dish in self.items])
