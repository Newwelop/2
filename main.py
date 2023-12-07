class Dog:


    def __init__(self, name="No name", height=100):
        self.height = height
        self.name = name
        self.meals_eaten = 3


    def __str__(self):
        return f"Я собака мое имя {self.name}.\nМой рост {self.height} см."

    def eat(self):
        self.meals_eaten -= 1
        print(f"{self.name} поел . Всего {self.meals_eaten} разa.")





dog = Dog("Bobik", height=32)
print(dog)

dog.eat()
print(gjyznyj)


