from person import Person

class Order:
    order_count = 0
    def __init__(self, price, name, owner: Person):
        self.__price = price
        self.__name = name
        self._owner = owner
        Order.order_count += 1

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def display_info(self):
        print(f"=" * 25)
        print(f"Displayinfo Order")
        print(f"=" * 25)
        print(f"Name: {self.get_name()}")
        print(f"Name: ${'%.2f'%self.get_price()}")
        print(f"-" * 25)
        self._owner.display_info()

def main():
    owner = Person("Alec", "Borque", 20.00)
    order = Order(19.99, "Coffee", owner )
    order.display_info()



if __name__ == "__main__":
    main()