class Bank:
    def __init__(self, salary, incentives):
        self.salary = salary
        self.incentives = incentives

    def __add__(self, other):
        x = self.salary + other.incentives
        y = other.salary + other.incentives
        return Bank(x, y)
    
    def __str__(self):
        total = self.salary + self.incentives
        return f"total = {total}"

Account = Bank(15000, 5000)
Acount = Bank(10000, 3000)
print(Account + Acount)
