class Car:

    #costruttore, costruisce l'oggetto definendo i suoi attributi e inizializzandoli
    def __init__(self):
        self.licensePlate = 0
        self.bodyColor = ''
        self.turnedOn = False
    def paint(self, color):
        self.bodyColor = color
    def turnOn(self):
        self.turnedOn = True


c = Car()
#con il punto posso accedere ai suoi contenuti
c.licensePlate = "AB123CD"
print(c.licensePlate)