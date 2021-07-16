from pprint import pprint as pp


class Flight:
    def __init__(self, flight_number, plane):
        self.plane = plane
        self.flight_number = flight_number

        rows, letters = self.plane.get_seating_plan()
        self.seats = [None] + [{letters: None for letters in letters} for _ in rows]  # _ zamiast zmiennej x gdy wiemy ze używamy jej tylko tutaj, [None] + przesuniecie listy z 0 na 1

    def get_airlines(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.plane.get_model()

    def _parse_seat(self, seat):  # enkapsulacja _ przed nazwa fn jest to gentelmens agreement i oznacza protected
        rows, letters = self.plane.get_seating_plan()

        letter = seat[-1]

        if letter not in letters:
            raise ValueError("invalid seat letter: {letter}")  # raise - wyrzuc mi wyjatek

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number: {row_text} ")

        if row not in rows:
            raise ValueError(f"Row number is out of seating range: {row}")

        return row, letter

    def allocate_passenger(self, seat, passenger):
        row, letter = self._parse_seat(seat)
        if self.seats[row][letter] is not None:
            raise ValueError(f"Seat {seat} is already taken")

        self.seats[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):
        row_from, letter_from = self._parse_seat(seat_from)

        if self.seats[row_from][letter_from] is None:
            raise ValueError(f"No passenger assigned to place {seat_from}")

        row_to, letter_to = self._parse_seat(seat_to)

        if self.seats[row_to][letter_to] is not None:
            raise ValueError(f"Seat {seat_to} is already taken")

        self.seats[row_to][letter_to] = self.seats[row_from][letter_from]
        self.seats[row_from][letter_from] = None

    def get_num_empty_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None)
                   for row in self.seats
                   if row is not None)

    def print_card(self, printer):
        for passenger, seat in self.get_passengers():
            printer(passenger, seat, self.flight_number, self.get_airplane_model())

    def get_passengers(self):
        for idx, row in enumerate(self.seats):
            if row is not None:
                for letter, passenger in row.items():  # .items - ze slownika robimy tuple 2 elementowa
                    if passenger is not None:
                        yield passenger, f"{idx}{letter}"  # zapytac sie w jaki to sposob dziala


class Airplane:  # klasa abstrakcyjna - nie da sie sensownie stworzyc obiektu (nie wykorzystujemy get_seating_plan)
    def get_num_seats(self):
        row, letters = self.get_seating_plan()
        return len(row) * len(letters)


class Boeing737(Airplane):
    @staticmethod
    def get_model():
        return "Boeing 737 Max"

    @staticmethod
    def get_seating_plan():
        return range(1, 25), "ABCDEG"


class AirbusA390(Airplane):
    @staticmethod
    def get_model():
        return "Airbus A390"

    @staticmethod
    def get_seating_plan():
        return range(1, 52), "ABCDEGHIK"


def card_printer(passenger, seat, flight_number, airplane_model):
    text = f"| Name: {passenger}, Seat: {seat}, Flight: {flight_number}, Model: {airplane_model} |"
    frame = f"+{'-' * (len(text) - 2)}+"
    frame_empty = f"|{' ' * (len(text) - 2)}|"

    banner = [frame, frame_empty, text, frame_empty, frame]
    banner_text = "\n".join(banner)

    print(banner_text)


boeing = Boeing737()  # tworzenie obiektu
airbus = AirbusA390()
f = Flight('BA123', boeing)


f.allocate_passenger("11C", "Lech")
f.allocate_passenger("12A", "Jaro")
f.allocate_passenger("12B", "Czech")
f.relocate_passenger("11C", "24C")
f.print_card(card_printer)
f.get_num_empty_seats()
# card_printer("DAMIAN", "12B", "LO123", "Boeing737")

# print(f.get_num_empty_seats())
# pp(f.seats)

# print(f.flight_number)
# print(f.get_airlines())
# print(f.get_number())
# print(f.get_airplane_model())

# print(boeing.get_seating_plan())
# print(airbus.get_seating_plan())
# print(boeing.get_num_seats())
# print(airbus.get_num_seats())
