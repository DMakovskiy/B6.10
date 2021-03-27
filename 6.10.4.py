class Volunteer:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

class Guest(Volunteer):
    def __init__(self, name, city, status, hotel_nights=2):
        super().__init__(name, city, status)
        self.hotel_nights = hotel_nights

    def add_to_list(self, g_list):
        return g_list.append(f'{self.name}, г.{self.city}, статус "{self.status}"')

    def display_guest(self):
        print(f'{self.name}, г.{self.city}, статус "{self.status}"')

guests_list = []
guest1 = Guest('Иван Петров', 'Москва', 'Наставник')
guest2 = Guest('Андрей Кузнецов', 'Рязань', 'Лидер')
guest1.add_to_list(guests_list)
guest2.add_to_list(guests_list)
guest1.display_guest()
print(guests_list)
