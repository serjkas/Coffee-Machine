# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self, l_country):
        print("The {} has sailed for {}!".format(self.name, l_country))


black_pearl = Ship("Black Pearl", 800)
text_input = input()
black_pearl.sail(text_input)
