def cesar_shift(s, shift):
    result = ''
    for ch in s:
        if ch.isalpha():
            # Определение базового ASCII для прописных или строчных букв
            base = ord('A') if ch.isupper() else ord('a')
            # Смещение и перенос по алфавиту
            shifted = (ord(ch) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += ch
    return result

def process_commands(initial_str, commands):
    history = [initial_str]
    current_str = initial_str

    for cmd in commands:
        if cmd.startswith('c'):
            # Обработка шифра Цезаря
            try:
                shift_value = int(cmd[1:])
                current_str = cesar_shift(current_str, shift_value)
            except ValueError:
                print(f"Некорректная команда: {cmd}")
                continue
        elif cmd == 'r':
            # Реверс строки
            current_str = current_str[::-1]
        else:
            print(f"Неизвестная команда: {cmd}")
            continue
        history.append(current_str)
    return history

# Ввод данных
initial_input = input("Введите исходную строку: ")
commands_input = input("Введите команды через пробел: ")

commands_list = commands_input.split()

# Обработка
history_steps = process_commands(initial_input, commands_list)

# Вывод истории изменений
for i, step in enumerate(history_steps):
    print(f"Шаг {i}: {step}")
