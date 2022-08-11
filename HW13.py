class Humans:
    def __init__(self, name, surname, birth_date, sex, energy):
        # свойства класса
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.sex = sex
        self.energy = 100

    # методы
    def eat(self):
        self.energy = self.energy + 5

    def sleep(self):
        self.energy = self.energy + 10

    def speak(self):
        self.energy = self.energy - 5

    def walking(self):
        self.energy = self.energy - 10

    def homework(self):
        self.energy = self.energy - 90


Man1 = Humans(name="Tony", surname="Stark", birth_date="29.05.1970", sex="male", energy=100)
Man2 = Humans(name="Peter", surname="Parker", birth_date="10.08.2001", sex="male", energy=100)
Man3 = Humans(name="Steve", surname="Rogers", birth_date="04.07.1918", sex="male", energy=100)

Woman1 = Humans(name="Peggy", surname="Carter", birth_date="09.02.1921", sex="female", energy=100)
Woman2 = Humans(name="Natasha", surname="Romanoff", birth_date="30.01.1975", sex="female", energy=100)

Man1.speak(), Man1.eat()
Man2.walking(), Man2.sleep()
Man3.homework()
Woman1.eat(), Woman1.walking()
Woman2.sleep(), Woman2.speak()

print(f"Найбільша енергія:")
print(max(Man1.energy, Man2.energy, Man3.energy, Woman1.energy, Woman2.energy))

