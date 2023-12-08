"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        total_pay = self.contract.calculate_pay()
        if self.commission:
            total_pay += self.commission.calculate_commission()
        return total_pay

    def __str__(self):
        contract_description = self.contract.description()
        commission_description = ""
        if self.commission:
            commission_description = f' and {self.commission.description()}'
        return f'{self.name}{contract_description}{commission_description}. Their total pay is {self.get_pay()}.'

class Contract:
    def calculate_pay(self):
        pass

    def description(self):
        pass

class MonthlySalary(Contract):
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self):
        return self.salary

    def description(self):
        return f' works on a monthly salary of {self.salary}'

class HourlySalary(Contract):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_pay(self):
        return self.hours * self.rate

    def description(self):
        return f' works on a contract of {self.hours} hours at {self.rate}/hour'

class Commission:
    def calculate_commission(self):
        pass
    
    def description(self):
        pass

class BonusCommission(Commission):
    def __init__(self, bonus):
        self.bonus = bonus

    def calculate_commission(self):
        return self.bonus

    def description(self):
        return f'receives a bonus commission of {self.bonus}'

class ContractCommission(Commission):
    def __init__(self, num_contracts, rate):
        self.num_contracts = num_contracts
        self.rate = rate

    def calculate_commission(self):
        return self.num_contracts * self.rate

    def description(self):
        return f'receives a commission for {self.num_contracts} contract(s) at {self.rate}/contract'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(100, 25))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(150, 25), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalary(120, 30), BonusCommission(600))
