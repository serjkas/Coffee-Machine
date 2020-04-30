g_water = 400
g_milk = 540
g_coffee_beans = 120
g_cups = 9
g_money = 550

g_have_w = 1
g_have_m = 1
g_have_cb = 1
g_have_c = 1

#print("The coffee machine has: \n" + str(g_water), " of water \n" + str(g_milk), "of milk \n" + str(g_coffee_beans),
#      "of coffee beans \n" + str(g_cups), "of disposable cups \n" + str(g_money), "of money \n")


def is_have_(l_name, l_count):
    global g_choice_coffee, g_water, g_milk, g_coffee_beans, g_cups, g_money, g_have_w, g_have_m, g_have_cb, g_have_c

    # print("IS A HAVE!")
    if l_name == 'water':
        if (g_water - l_count) < 0:
            print("Sorry, not enough water!\n")
            g_have_w = 0
        else: g_have_w = 1
    elif l_name == 'coffee_beans':
        if (g_coffee_beans - l_count) < 0:
            print("Sorry, not enough coffee beans!\n")
            g_have_cb = 0
        else: g_have_cb = 1
    elif l_name == 'milk':
        if (g_milk - l_count) < 0:
            print("Sorry, not enough milk!\n")
            g_have_m = 0
        else: g_have_m = 1
    elif l_name == 'cups':
        if (g_cups - l_count) < 0:
            print("Sorry, not enough cups!\n")
            g_have_c = 0
        else: g_have_c = 1


def buy_():
    g_choice_coffee = ""
    while g_choice_coffee != "back":

        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        global g_water, g_milk, g_coffee_beans, g_cups, g_money
        g_choice_coffee = input(">")

        if g_choice_coffee == "1":
            is_have_("water", 250)
            is_have_("coffee_beans", 16)
            is_have_("cups", 1)
            if (g_have_w == 1) and (g_have_m == 1) and (g_have_c == 1) and (g_have_cb == 1):
                print("I have enough resources, making you a coffee!\n")
                g_water -= 250
                g_coffee_beans -= 16
                g_money += 4
                g_cups -= 1
                break
            else: break

        elif g_choice_coffee == "2":
            print(g_have_w,g_have_m,g_have_c,g_have_cb)
            is_have_("water", 350)
            is_have_("milk", 75)
            is_have_("coffee_beans", 7)
            is_have_("cups", 1)
            print(g_have_w,g_have_m,g_have_c,g_have_cb)
            if (g_have_w == 1) and (g_have_m == 1) and (g_have_c == 1) and (g_have_cb == 1):
                print("I have enough resources, making you a coffee!\n")
                g_water -= 350
                g_milk -= 75
                g_coffee_beans -= 20
                g_money += 7
                g_cups -= 1
                break
            else: break

        elif g_choice_coffee == "3":
            is_have_("water", 200)
            is_have_("milk", 100)
            is_have_("coffee_beans", 12)
            is_have_("cups", 1)
            if (g_have_w == 1) and (g_have_m == 1) and (g_have_c == 1) and (g_have_cb == 1):
                print("I have enough resources, making you a coffee!\n")
                g_water -= 200
                g_milk -= 100
                g_coffee_beans -= 12
                g_money += 6
                g_cups -= 1
                break
            else: break


def fill_():
    global g_water, g_milk, g_coffee_beans, g_cups, g_money
    print("\nWrite how many ml of water do you want to add:")
    g_water += int(input(">"))

    print("Write how many ml of milk do you want to add:")
    g_milk += int(input(">"))

    print("Write how many grams of coffee beans do you want to add:")
    g_coffee_beans += int(input(">"))

    print("Write how many disposable cups of coffee do you want to add:")
    g_cups += int(input(">"))
    print("\n")

def take_():
    global g_money
    print("I gave you $" + str(g_money))
    g_money -= g_money


def remaining_():
    print("\nThe coffee machine has: \n" + str(g_water), " of water \n" + str(g_milk), "of milk \n" + str(g_coffee_beans),
          "of coffee beans \n" + str(g_cups), "of disposable cups \n" + str(g_money), "of money \n")


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    text_input = input(">")

    if text_input == 'buy':
        buy_()
    elif text_input == 'fill':
        fill_()
    elif text_input == 'take':
        take_()
    elif text_input == 'remaining':
        remaining_()
    elif text_input == 'exit':
        break
