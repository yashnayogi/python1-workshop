# creating class
class car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

# creating objects from the class
car1 = car("toyota","camry")
car2 = car("honda","ciyic")


print(car1.make,car1.model)
print(car2.make,car2.model)