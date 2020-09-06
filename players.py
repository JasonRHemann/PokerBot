class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.greeting = "Hello, my name is {} and im {} years old".format(
            name, age)

    def __repr__(self):
        # return "name {}, age {}, greeting {}".format(self.name, self.age, self.
        #                                              greeting)


player = Player("Jayrod", 44)
player.age = 5595
print(player)
