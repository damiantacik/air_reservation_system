class Flight:
    def __init__(self, flight_number, plane):
        self.plane = plane
        self.flight_number = flight_number

    def get_airlines(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.plane.get_model()


class Airplane:
    pass


class Boeing737(Airplane):
    @staticmethod
    def get_model():
        return "Boeing 737 Max"


class AirbusA390(Airplane):
    @staticmethod
    def get_model():
        return "Airbus A390"


boeing = Boeing737()
airbus = AirbusA390
f = Flight('BA123', airbus)
print(f.flight_number)
print(f.get_airlines())
print(f.get_number())
print(f.get_airplane_model())