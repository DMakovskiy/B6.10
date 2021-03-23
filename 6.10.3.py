class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        if isinstance(self.balance, int) and self.balance >= 0:
            return self.balance

    def display_client(self):
        print(f'Клиент "{self.name}". Баланс: {self.balance} руб.')

client1 = Client('Иван Петров', 50)

client1.display_client()
