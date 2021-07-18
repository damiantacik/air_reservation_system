from pprint import pprint as pp

from flight import Flight
from planes import *
from helpers import card_printer


def make_flight():
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


if __name__ == '__main__':
    make_flight()
