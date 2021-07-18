def card_printer(passenger, seat, flight_number, airplane_model):
    text = f"| Name: {passenger}, Seat: {seat}, Flight: {flight_number}, Model: {airplane_model} |"
    frame = f"+{'-' * (len(text) - 2)}+"
    frame_empty = f"|{' ' * (len(text) - 2)}|"

    banner = [frame, frame_empty, text, frame_empty, frame]
    banner_text = "\n".join(banner)

    print(banner_text)