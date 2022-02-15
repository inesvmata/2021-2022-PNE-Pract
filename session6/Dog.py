class Dog:
    def __init__(self, the_name, the_age): #init es para crear un tipo de variable
        self.name = the_name #any atribute you want to write has to go with self.atribute
        self.age = the_age

    def say_your_name(self):
        print("I´m {}, and I am sitting down here".format(self.name))

    def show_your_age(self):
        print("I´m {} years old".format(self.age))

    def say_what_you_like(self):
        print("I like arithmetic!")

    def multiply(self, first_operand, second_operand):
        print(f'Easy!, the result is {first_operand * second_operand}')
        #print("The result is", first_operand + second_operand)

#name of the variable, dot, name of the method
ares = Dog("ares", 10) #you omly have to put the other parameters, not self
ares.say_your_name()
ares.show_your_age()
ares.say_what_you_like()
ares.multiply(3, 5)