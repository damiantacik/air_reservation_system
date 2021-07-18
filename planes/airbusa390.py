from airplane import Airplane


class AirbusA390(Airplane):
    @staticmethod
    def get_model():
        return "Airbus A390"

    @staticmethod
    def get_seating_plan():
        return range(1, 52), "ABCDEGHIK"