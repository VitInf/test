class Flight():
    def __init__(self, capasity):
        self.capasity = capasity
        self.passengers = []
    
    def add_passengers(self, name):
        if len(self.passengers)> self.capasity:
            print(f"Вільних місць для {name} немає")
        else:
            self.passengers.append(name)

f = Flight(3)
people = ["Andriy","Roma","Lioha","Max"]

for person in people:
    f.add_passengers(person)
    