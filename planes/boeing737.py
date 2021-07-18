from airplane import Airplane


class Boeing737(Airplane):
    @staticmethod
    def get_model():
        return "Boeing 737 Max"

    @staticmethod
    def get_seating_plan():
        return range(1, 25), "ABCDEG"