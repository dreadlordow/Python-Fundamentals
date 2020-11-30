class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else :
            return f'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity-len(self.items)}"

inventory = Inventory(2)
inventory.add_item("potion")

print(inventory.get_capacity())
print(inventory)
