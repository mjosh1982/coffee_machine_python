# Write your code here
class CoffeeMachine:
    '''
    This class is used to calculate the amount of material needed to make coffee
    '''

    def __init__(self, message, water_count, milk_count, coffee_bean_count, disposable_cups=None, money1=None):
        self.message = message
        self.water = water_count
        self.milk = milk_count
        self.coffee_beans = coffee_bean_count
        self.total_possible_coffee_count = 0
        self.disposable_cups = disposable_cups
        self.money = money1

    def display_default_message(self):
        '''
        This function is used to display the message that is stored in the message variable
        '''

        self.message = ""
        # self.message += self.get_message_based_on_ingredients(self.water, self.milk, self.coffee_beans,
        #                                                       self.coffee_drink_count)
        # display the coffee machine message
        self.message += "The coffee machine has:\n"
        self.message += f"{self.water} ml of water\n"
        self.message += f"{self.milk} ml of milk\n"
        self.message += f"{self.coffee_beans} g of coffee beans\n"
        self.message += f"{self.disposable_cups} of disposable cups\n"
        self.message += f"${self.money} of money\n"
        self.action = 'fill'
        self.coffee_type = 0

        print(self.message)

    def calculate_material(self, coffee_count):
        '''
        This function is used to calculate the material needed to make coffee

        :param coffee_count: The type of coffee that the user wants to drink
        :return: The material needed to make coffee
        '''
        if coffee_count == 1:
            return 250, 0, 16
        elif coffee_count == 2:
            return 350, 75, 20
        elif coffee_count == 3:
            return 200, 100, 12

    def get_message_based_on_ingredients(self, water, milk, coffee_beans, coffee_drink_count):
        '''
        This function is used to get the message based on the ingredients

        :param water: The water quantity as mentioned in the input
        :param milk:  The milk quantity as mentioned in the input
        :param coffee_beans: The coffee beans quantity as mentioned in the input
        :param coffee_drink_count: The amount of cups of coffee that the user expects
        :return: The message based on the ingredients
        '''
        self.total_possible_coffee_count = min(water // 200, milk // 50, coffee_beans // 15)
        if self.total_possible_coffee_count == coffee_drink_count:
            return "Yes, I can make that amount of coffee"
        elif self.total_possible_coffee_count > coffee_drink_count:
            return f"Yes, I can make that amount of coffee (and even {self.total_possible_coffee_count - coffee_drink_count} more than that)"
        else:
            return f"No, I can make only {self.total_possible_coffee_count} cups of coffee"

    def execute_action(self):
        self.action = input("Write action (buy, fill, take, remaining, exit):\n")
        if self.action == 'buy':
            self.buy_coffee()
            return 'buy'
        elif self.action == 'fill':
            self.fill_coffee()
            return 'fill'
        elif self.action == 'take':
            self.take_money()
            return 'take'
        elif self.action == 'remaining':
            self.display_default_message()
            return 'remaining'
        elif self.action == 'exit':
            return 'exit'

    def buy_coffee(self):
        try:
            self.coffee_type = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
            self.adjust_material_values(self.coffee_type)
        except ValueError:
            pass
        # self.display_default_message()

    def adjust_material_values(self, option_selected):
        water, milk, coffee_beans = self.calculate_material(option_selected)
        if self.water < water:
            print("Sorry, not enough water!")
            return
        elif self.milk < milk:
            print("Sorry, not enough milk!")
            return
        elif self.coffee_beans < coffee_beans:
            print("Sorry, not enough coffee beans!")
            return
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            return
        self.water -= water
        self.milk -= milk
        self.coffee_beans -= coffee_beans
        self.disposable_cups -= 1
        if option_selected == 1:
            self.money += 4
        elif option_selected == 2:
            self.money += 7
        elif option_selected == 3:
            self.money += 6
        print("I have enough resources, making you a coffee!")

    def fill_coffee(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        # self.display_default_message()

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        # self.display_default_message()


water_count = 400
milk_count = 540
coffee_beans_count = 120
disposable_cup = 9
money = 550

coffee_machine = CoffeeMachine("", water_count, milk_count, coffee_beans_count, disposable_cup, money)
# coffee_machine.display_default_message()
while True:
    action = coffee_machine.execute_action()
    if action == 'exit':
        break
