class Person:
    def __init__(self, first_name, last_name, amount_of_money: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__amount_of_money = float(amount_of_money)

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        if type(first_name) == str:
            self.__first_name = first_name
        else:
            print("ValueError")

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        if type(last_name) == str:
            self.__last_name = last_name
        else:
            print("ValueError")

    def get_amount_of_money(self):
        return self.__amount_of_money

    def update_money_value(self, amount: float):
        if 0 > self.__amount_of_money + amount:
            print(f"Transaction cannot be done due to lack of funds.")
        else:
            self.__amount_of_money += amount


    def display_info(self):
        print(f"This is the output for a person whose first name is {self.get_first_name()}, last name is {self.get_last_name()} and has ${'%.2f'%self.get_amount_of_money()}")



def main() -> None:
    test_person = Person("Albert", "Einstein", 100)
    test_person.display_info()
    test_person.update_money_value(-90)
    test_person.display_info()
    test_person.update_money_value(50)
    test_person.display_info()
    test_person.update_money_value(-100)
    test_person.display_info()

if __name__ == "__main__":
    main()