class _Star_Cinema:
    _hall_list = []

    @classmethod
    def _entry_hall(cls, hall_obj):
        cls._hall_list.append(hall_obj)


class _Hall(_Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        # Insert this hall object to Star_Cinema's hall_list
        self._entry_hall(self)

    def _entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = [['free' for _ in range(self.__cols)] for _ in range(self.__rows)]

    def _book_seats(self, id, seats_list):
        if id not in self.__seats:
            print("Invalid Show ID!")
            return
        for row, col in seats_list:
            if row >= self.__rows or col >= self.__cols or row < 0 or col < 0:
                print(f"Invalid seat ({row}, {col})")
            elif self.__seats[id][row][col] == 'booked':
                print(f"Seat ({row}, {col}) already booked!")
            else:
                self.__seats[id][row][col] = 'booked'

    def _view_show_list(self):
        for show in self.__show_list:
            print(show)

    def _view_available_seats(self, id):
        if id not in self.__seats:
            print("Invalid Show ID!")
            return
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 'free':
                    print(f"Seat ({i}, {j}) is available")

    # Replica system for the counter
    def _counter_system(self):
        while True:
            print("\n1. View Shows\n2. View Available Seats\n3. Book Seats\n4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self._view_show_list()
            elif choice == 2:
                id = input("Enter show ID: ")
                self._view_available_seats(id)
            elif choice == 3:
                id = input("Enter show ID: ")
                n = int(input("How many seats you want to book? "))
                seats_to_book = []
                for _ in range(n):
                    r, c = map(int, input("Enter row and col of the seat: ").split(","))
                    seats_to_book.append((r, c))
                self._book_seats(id, seats_to_book)
            elif choice == 4:
                break
            else:
                print("Invalid choice!")


# Example Usage
hall1 = _Hall(5, 5, 1)
hall1._entry_show("101", "Oppenheimer", "5:00 PM")
hall1._entry_show("102", "Barbie", "7:00 PM")

hall1._counter_system()
