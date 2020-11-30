class Catalogue:
    products = []
    def __init__(self,name):
        self.name = name

    def add_product(self,product):
        self.product = product
        self.products.append(self.product)

    def get_by_letter(self,first_letter):
        self.first_letter = first_letter
        new_list =[]
        for element in self.products:
            if element[0] == self.first_letter:
                new_list.append(element)
        return new_list

    def __repr__(self):
        something = [x for x in self.products]
        something_else = '\n'.join(sorted(something))
        return f"Items in the {self.name} catalogue:\n{something_else}"



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
