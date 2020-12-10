import sys
class Program:
    bmw = 10
    toyota = 10
    volkswagen = 10
    ford = 10
    hyundai = 10
    cars = bmw + toyota + volkswagen + ford + hyundai
    item = "brand"
    cost = 0
    no_item = 0

    def __init__(self):
        print("menu")
        print("1: Rent ")
        print("2: amount of available cars")
        print("3: Exit")
        choice = input("write your choice number: ")
        if choice == "1":
            self.brand_list()
        elif choice == "2":
            print("There are " + str(self.cars) + " available cars ")
        elif choice == "3":
            sys.exit("program exit")
        else:
            print("invalid choice please try again")
            Program()

    def brand_list(self):
        print("Available cars brand list with their hourly basis rent")
        print("1: Toyota     $5/item")
        print("2: Ford       $6/item")
        print("3: BMW        $7/item")
        print("4: Hyundai    $9/item")
        print("5: Volkswagen $10/item")
        print("6: back")
        brand = input("choose brand number: ")
        if brand == "1" or brand == "Toyota":
            self.item = self.toyota
            self.cost = 5
        elif brand == "2" or brand == "Ford":
            self.item = self.ford
            self.cost = 6
        elif brand == "3" or brand == "BMW ":
            self.item = self.bmw
            self.cost = 7
        elif brand == "4" or brand == "Hyundai":
            self.item = self.hyundai
            self.cost = 9
        elif brand == "5" or brand == "Volkswagen":
            self.item = self.volkswagen
            self.cost = 10
        elif brand == "6" or brand == "back":
            Program()
        else:
            print("invalid choice try again")
            self.brand_list()
        while brand == 1 or 2 or 3 or 4 or 5 or 6 and self.no_item == 0:
            try:
                self.no_item = int(input("how much item do you want to rent? "))
            except(ValueError):
                print("input error please try again")
        self.rental_basis()

    def rental_basis(self):
        if self.no_item <= self.item:
            print("choose your rent basis ")
            print("1: Hourly")
            print("2: Daily")
            print("3: Weekly")
            print("4: back")
            basis = input()
            if basis == "1":
                length = int(input("for how many hours do you want to rent this car?"))
                print("congratulation you have successfully rented the car ")
                print("Total cost = $" + str(self.no_item * self.cost * length))
            elif basis == "2":
                length = int(input("for how many days do you want to rent this car?"))
                print("congratulation you have successfully rented the car")
                print("Total cost = $" + str(self.no_item * 10 * self.cost * length))
            elif basis == "3":
                length = int(input("for how many weeks do you want to rent this car?"))
                print("congratulation you have successfully rented the car ")
                print("Total cost = $" + str(self.no_item * 10 * 7 * self.cost * length))
            elif basis == "4":
                self.brand_list()
            else:
                print("invalid try again")
                self.rental_basis()
        else:
            print("there is no enough amount please try less amount")
            self.no_item = int(input("how much item do you want to rent? "))
            self.rental_basis()

Program()
