class CoffeeMachine:

    def __init__(self, water, milk, coffee, money, cups):

        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
        self.cups = cups

    def state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money\n")

    def buy(self):

        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")

        answer = input("> ")

        if answer == "back":

            return

        elif answer == "1":

            if self.water >= 250 and self.coffee >= 16:

                print("I have enough resources, making you a coffee!")

                self.water -= 250
                self.coffee -= 16
                self.money += 4

            elif self.water < 250:

                print("Sorry, not enough water!\n")
                return

            else:

                print("Sorry, not enough coffee beans!\n")
                return

        elif answer == "2":

            if self.water >= 350 and self.milk >= 75 and self.coffee >= 20:

                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7

            elif self.water < 350:

                print("Sorry, not enough water!\n")
                return

            elif self.milk < 75:

                print("Sorry, not enough milk!\n")
                return

            else:

                print("Sorry, not enough coffee beans!\n")
                return

        else:

            if self.water >= 200 and self.milk >= 100 and self.coffee >= 12:

                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6

            elif self.water < 200:

                print("Sorry, not enough water!\n")
                return

            elif self.milk < 100:

                print("Sorry, not enough milk!\n")
                return

            else:

                print("Sorry, not enough coffee beans!\n")
                return

        self.cups -= 1

        print()

    def take(self):

        print(f"I gave you ${self.money}\n")

        self.money -= self.money

    def fill(self):

        print("Write how many ml of water do you want to add:")
        answer = input("> ")
        self.water += int(answer)

        print("Write how many ml of milk do you want to add:")
        answer = input("> ")
        self.milk += int(answer)

        print("Write how many grams of coffee do you want to add:")
        answer = input("> ")
        self.coffee += int(answer)

        print("Write how many disposable cups of coffee beans do you want to add:")
        answer = input("> ")
        self.cups += int(answer)

        print()

    def interact(self):

        while True:

            print("Write action (buy, fill, take, remaining, exit):")

            action = input("> ")

            if action == "remaining":

                self.state()

            elif action == "exit":

                break

            elif action == "buy":

                print()
                self.buy()

            elif action == "fill":

                print()
                self.fill()

            elif action == "take":

                print()
                self.take()


SavelysCoffee = CoffeeMachine(400, 540, 120, 550, 9)
SavelysCoffee.interact()
