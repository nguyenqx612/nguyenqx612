class Car:
    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
    
    def print_car(self):
        print("Manufacturer: {}, Model: {}, HP: {}".format(self.manufacturer, self.model, self.hp))