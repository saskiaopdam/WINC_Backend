class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class JackRusselTerrier(Dog):
    def speak(self, sound="Arf"):
        # return f"{self.name} says {sound}"
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


miles = JackRusselTerrier('Miles', 4)
buddy = Dachshund('Buddy', 9)
jack = Bulldog('Jack', 3)
jim = Bulldog('Jim', 5)
daisy = GoldenRetriever('Daisy', 6)

print(miles.species) # Canis familiaris
print(buddy.name) # Buddy
print(jack) # Jack is 3 years old
print(jim.speak('Woof')) # Jim says Woof

print(type(miles)) # <class '__main__.JackRusselTerrier>
print(isinstance(miles, Dog)) # True
print(isinstance(miles, Bulldog)) # False

print(miles.speak()) # Miles says Arf # Miles barks: Arf
print(miles.speak("Grrr")) # Miles says Grrr
print(jim.speak("Woof")) # Jim barks: Woof

print(daisy.speak()) # Daisy says Bark
