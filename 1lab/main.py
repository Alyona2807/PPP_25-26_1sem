def create_hall(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

def display_hall(hall):
    print("Статус зала (0 - свободно, 1 - занято):")
    for row in hall:
        print(' '.join(str(seat) for seat in row))
    print()

def find_and_book_seats(hall, seats_needed):
    for row_index, row in enumerate(hall):
        count = 0
        start_index = 0
        for seat_index, seat in enumerate(row):
            if seat == 0:
                if count == 0:
                    start_index = seat_index
                count += 1
            else:
                count = 0
            if count == seats_needed:
                # Бронируем места
                for i in range(start_index, start_index + seats_needed):
                    hall[row_index][i] = 1
                return (row_index + 1, start_index + 1)  # номера рядов и мест начинаются с 1
    return None

def main():
    n = int(input("Введите число рядов: "))
    m = int(input("Введите число мест в ряду: "))

    hall = create_hall(n, m)
    display_hall(hall)

    while True:
        try:
            seats_needed = int(input("Введите количество мест для бронирования (0 для выхода): "))
            if seats_needed == 0:
                break
            result = find_and_book_seats(hall, seats_needed)
            if result:
                print(f"Забронированы места: ряд {result[0]}, места {result[1]} - {result[1] + seats_needed - 1}")
            else:
                print("Нет подходящих подряд мест для бронирования.")
            display_hall(hall)
        except ValueError:
            print("Пожалуйста, введите корректное число.")

if __name__ == "__main__":
    main()
