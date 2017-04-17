
class Check(object):

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def calculate_sum(self):
        total_sum = 0
        for dish in self.items:
            total_sum += dish.price
        return total_sum
