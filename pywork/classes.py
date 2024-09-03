class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self):
        print("Moves along...")
    def get_make_model(self):
        print(f"This is {self.make} {self.model}.")

my_car = Vehicle("Honda","Odyssey")

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Tesla","Model Y")
your_car.get_make_model()
your_car.moves()

class Airplace(Vehicle):
    def __init__(self, make, model,faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print("Flies Along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles Along...")

class GolfCart(Vehicle):
    pass

airbus = Airplace("Airbus","380","faa234")
truck = Truck("Ford","F150")
golfcart = GolfCart("Yamaha","GC100")

airbus.get_make_model()
airbus.moves()
truck.get_make_model()
truck.moves()
golfcart.get_make_model()
golfcart.moves()

print("#####\n\n")

for v in(my_car,your_car,airbus,truck,golfcart):
    v.get_make_model()
    v.moves()

