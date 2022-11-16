class Project:
    def __init__(self, name, start_date, priority, cost, complete_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.complete_percentage = complete_percentage

    def __str__(self):
        return f'{self.name}, start:{self.start_date},priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.complete_percentage} %'

    def is_complete(self):
        return self.progress == 100

    def is_not_complete(self):
        return self.progress < 100
