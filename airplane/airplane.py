class Airplane:  # klasa abstrakcyjna - nie da sie sensownie stworzyc obiektu (nie wykorzystujemy get_seating_plan)
    def get_num_seats(self):
        row, letters = self.get_seating_plan()
        return len(row) * len(letters)