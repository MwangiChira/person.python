#class person:
#    def __init__(self, name, age, gender):
#        self.name = name
#        self.age = age
#        self.gender = gender
        
#        def introduce(self):
#            print(f"Hello, my name is {self.name}.I am {self.age}years old and identify as {self.gender}.")
#person_instance = person(name="Mwangi", age=24,gender="male")


#person_instance.introduce()
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

person_instance = Person(name="Mwangi", age=24, gender="male")

person_instance.introduce()





