class Flight():
    def __init__(self, capasity):
        self.capasity = capasity
        self.passengers = []
    
    def add_passengers(self, name):
        if len(self.passengers)> self.capasity:
            print(f"Вільних місць для {name} немає")
            return False
        else:
            self.passengers.append(name)
            print(f"Пасажира  {name} додано")

f = Flight(2)
people = ["Andriy","Roma","Lioha","Max", "Djon"]

for person in people:
    f.add_passengers(person)
    