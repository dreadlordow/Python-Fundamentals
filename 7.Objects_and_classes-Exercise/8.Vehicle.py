class Vehicle:

    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner
        self.money = 0

    def buy(self, money, owner):
        self.money = money

        if self.money >= self.price and self.owner is None :
            change = self.money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
            #print(f"Successfully bought a {self.type}. Change: {change}")

        elif money < self.price:
            return f'Sorry, not enough money'
            #print(f'Sorry, not enough money')

        elif self.owner is not None:
            return f'Car already sold'
            #print(f'Car already sold')

    def sell(self):
        if self.owner is None:
            return f'Vehicle has no owner'
            #print(f'Vehicle has no owner')

        else :
            self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f'{self.model} {self.type} is owned by: {self.owner}'

        return f'{self.model} {self.type} is on sale: {self.price}'


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)


