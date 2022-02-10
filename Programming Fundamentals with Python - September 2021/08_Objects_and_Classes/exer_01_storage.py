class Storage:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage

# class Storage:
#     __storage = []
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def add_product(self, product: str):
#         if len(self.__storage) < self.capacity:
#             self.__storage.append(product)
#
#     def get_products(self):
#         return self.__storage

storage = Storage(1)
storage2 = Storage(2)
storage.add_product("apple")
storage.add_product("banana")
storage2.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")
print(storage.get_products())
print(storage2.get_products())
