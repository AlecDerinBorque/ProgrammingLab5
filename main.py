from person import Person
from order import Order







def main():
    x = 5
    if x < 10:
        print("x = 5")
    y = 20
    if x >= y:
        print("x = 5")
    print("y = 20")
    p = Person("Alan", "Turing", 950.67)
    if p.get_amount_of_money() < 100:
        print("a")
    if p.get_amount_of_money() < 200:
        print("b")
    if p.get_amount_of_money() < 350:
        print("c")
    if p.get_amount_of_money() < 800:
        print("d")
    print("ok")
    r = Order(7.99, "Cafe Mocha", p)
    if p.get_amount_of_money() >= r.get_price():
        if x == y:
            print(p.get_amount_of_money())
        else:
            print(r.get_price())
        print("Done with A")
    elif x <= y:
        print(r.get_price())





main()



def info_header(name, panther_id, section, semester, assignment):
    print("=" * 70)
    print(f" PROGRAMMER: {name}")
    print(f" PANTHER ID: {panther_id}")
    print()
    print(" CLASS: COP2047")
    print(f" SECTION: {section}")
    print(f" SEMESTER: {semester}")
    print()
    print(f" Assignment: {assignment}")
    print()
    print(f" CERTIFICATION: I UNDERSTAND FIU's academic policies, and I certify that this work is my own and that none of it is the work of any other person")
    print("=" * 70)


def header_caller(step_number: int):
    print("\n\n")
    print("=" * 20)
    print(f"Stop: {step_number}")
    print("=" * 20)






def main() -> None:
    header_caller(2)
    info_header("Alec Borque", "6280315", "U01 1248", "Fall 2024", "Lab 5")






if __name__ == "__main__":
    main()