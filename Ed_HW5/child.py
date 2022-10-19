from parent import Parent


class Cat(Parent):

    def __init__(self, name, age, lives, breed):
        super().__init__(name)
        self.lives = lives
        self.breed = breed
        self.age = age

    def __str__(self) -> str:
        pass

    def meow(self):
        print('Meow')

    def move(self):
        pass
