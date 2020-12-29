class Animal:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def animalSays (self):
        print(self.name, ' says "', self.voice.upper(), '"', sep='', end = ' ')

class HomeAnimal(Animal):
    def __init__(self, name, voice, function):
        super().__init__(name,voice)
        self.function = function
    def animalDo (self):
        self.animalSays()
        print('and', self.function, end = ' ')


class Dog (HomeAnimal):
    def __init__(self, name, voice, function, breed):
        super().__init__(name, voice, function)
        self.breed = breed
    def breedDo(self):
        print(self.name, 's of ', self.breed, ' breed are lovely to ', self.function, sep='', end = ' ')

class Cat (HomeAnimal):
    def __init__(self, name, voice,  function, breed, color, pattern):
        super().__init__(name, voice, function)
        self.pattern = pattern
        self.color = color
        self.breed = breed
    def breedColor(self):
        if self.breed:
            if self.pattern:
                print(self.name, 's of ', self.breed, ' breed are usually  ', self.color, ' with ', self.pattern,
                      sep='', end=' ')
            else:
                print(self.name, 's of ', self.breed, ' breed are usually  ', self.color, sep='', end=' ')
        else:
            self.breed = 'no'
            if self.pattern:
                print(self.name, 's of ', self.breed, ' breed are usually  ', self.color, ' with ', self.pattern,
                      sep='', end=' ')
            else:
                print(self.name, 's of ', self.breed, ' breed are usually  ', self.color, sep='', end=' ')

class HunterDog (Dog):
    def __init__(self, name, voice,  function, breed, whotohunt):
        super().__init__(name, voice, function, breed)
        self.whotohunt = whotohunt
    def dogHunt(self):
        self.breedDo()
        print(self.whotohunt)


mouse = Animal('mouse', 'pi')
mouse.animalSays()
print('\t', '\t')
cow = HomeAnimal('cow', 'moo', 'gives milk')
cow.animalDo()
print('\t', '\t')
dog = Dog('dog', 'gav', 'carry slades', 'Haski')
dog.breedDo()
print('\t', '\t')
cat = Cat('cat', 'meow','catches mice', 'British', 'grey', None)
cat.breedColor()
print('\t', '\t')
cat = Cat('cat','meow','catches mice', None, 'grey', 'stripes')
cat.breedColor()
print('\t', '\t')
taksa = HunterDog('dog', 'gav','hunt','taksa', 'foxes')
taksa.dogHunt()




