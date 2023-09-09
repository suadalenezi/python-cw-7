class person:
    name = "suad"
    age = 16
first_person = person()
print(first_person.age)
print(first_person.name)


class person :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age < 18:
            print("You have too much responsibilities")
        else:
            print("Lucky you")

    def __str__(self):
        return f"my name is {self.name} and im {self.age} years old"











