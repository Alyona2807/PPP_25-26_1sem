import re
import json

# Общий интерфейс пользователя
class User:
    def __init__(self, uid, full_name, email):
        self.uid = uid
        self.full_name = full_name
        self.email = email

    def __str__(self):
        return f"{self.full_name} {self.email}"

    def matches_name(self, pattern):
        return pattern.lower() in self.full_name.lower()

    def is_valid_email(self):
        # Простая проверка email
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.email) is not None

# Класс для CSV формата
class CsvUser(User):
    @staticmethod
    def from_csv(record):
        # record: "csv 123;Иван Иванов;ivan@example.com"
        parts = record.strip().split(' ', 1)
        if len(parts) < 2:
            return None
        data = parts[1]
        fields = data.split(';')
        if len(fields) != 3:
            return None
        uid_str, full_name, email = fields
        try:
            uid = int(uid_str)
        except:
            return None
        return CsvUser(uid, full_name, email)

# Класс для JSON формата
class JsonUser(User):
    @staticmethod
    def from_json(record):
        # record: 'json {"uid": 42, "first_name": "Petr", "last_name": "Petrov", "contacts": {"email": "petr@example.com"}}'
        parts = record.strip().split(' ', 1)
        if len(parts) < 2:
            return None
        json_str = parts[1]
        try:
            data = json.loads(json_str)
            uid = data.get('uid')
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')
            email = data.get('contacts', {}).get('email', '')
            if uid is None or not email:
                return None
            full_name = f"{first_name} {last_name}"
            return JsonUser(uid, full_name, email)
        except:
            return None

# Класс для Raw формата
class RawUser(User):
    @staticmethod
    def from_raw(record):
        # record: "raw Иванов Иван ivanov@example.com"
        parts = record.strip().split(' ', 3)
        if len(parts) != 4:
            return None
        _, last_name, first_name, email = parts
        full_name = f"{first_name} {last_name}"
        # Можно добавить uid или оставить None
        return RawUser(None, full_name, email)

# Коллекция пользователей
class UserCollection:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user:
            self.users.append(user)

    def get_all_emails(self):
        return [user.email for user in self.users]

    def find_by_name(self, pattern):
        return [user for user in self.users if user.matches_name(pattern)]

    def get_invalid_emails(self):
        return [user for user in self.users if not user.is_valid_email()]

# Основная программа
def main():
    # Ввод данных
    raw_data = [
        "csv 123;Иван Иванов;ivan@example.com",
        'json {"uid": 42, "first_name": "Petr", "last_name": "Petrov", "contacts": {"email": "petr@example.com"}}',
        "raw Иванов Иван ivanov@example.com",
        "csv 124;Мария Смирнова;maria@example.com",
        'json {"uid": 43, "first_name": "Anna", "last_name": "Ivanova", "contacts": {"email": "anna@invalid"}}',
        "raw Петр Петров petr@invalid"
    ]

    collection = UserCollection()

    # Парсим и добавляем пользователей
    for record in raw_data:
        if record.startswith('csv'):
            user = CsvUser.from_csv(record)
        elif record.startswith('json'):
            user = JsonUser.from_json(record)
        elif record.startswith('raw'):
            user = RawUser.from_raw(record)
        else:
            user = None
        collection.add_user(user)

    # Обработка команд
    commands = [
        "emails",
        "find name=Иван",
        "invalid"
    ]

    for cmd in commands:
        if cmd == "emails":
            emails = collection.get_all_emails()
            print("Все email-адреса:")
            for email in emails:
                print(email)
            print()
        elif cmd.startswith("find name="):
            pattern = cmd.split("=", 1)[1]
            found = collection.find_by_name(pattern)
            print(f"Пользователи, содержащие '{pattern}':")
            for user in found:
                print(str(user))
            print()
        elif cmd == "invalid":
            invalids = collection.get_invalid_emails()
            print("Некорректные email:")
            for user in invalids:
                print(str(user))
            print()

if __name__ == "__main__":
    main()
