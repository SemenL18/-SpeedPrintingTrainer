import time
import random

def select_mode():
    print("Выберите режим тренажёра:")
    print("1. Слоги")
    print("2. Слова")
    print("3. Текст")
    mode = input("Ваш выбор (1/2/3): ")
    while mode not in ('1', '2', '3'):
        mode = input("Введите 1, 2 или 3: ")
    return mode

syllables = [
    "ла ле ли ло лу",
    "ко ки ка ку ке",
    "ма ме ми мо му",
    "ба бе би бо бу",
]

simple_words = [
    "программа",
    "интеграл",
    "традиция",
    "скорость",
    "молоко",
    "погода",
    "студент",
    "клавиатура",
]

hard_texts = [
    "Сложные символы: @Python#2023!",
    "КОД - это СИЛА.",
    "Работа с текстом: быстро, ЧЁТКО, грамотно.",
    "Обработка строк: trim(x), split(y), join(z).",
    "Умей пользоваться: ( ), { }, [ ], ; : ? !",
]

full_texts = [
    "Скорость печати важна в современном мире.",
    "Программирование требует постоянной практики.",
    "Python -- язык с лаконичным синтаксисом.",
    "Сегодня прекрасная погода для учёбы.",
    "Умение быстро печатать экономит время.",
    "Искусственный интеллект меняет привычную жизнь.",
    "Пиши код чисто и подробно документируй.",
    "Работа с текстом помогает улучшить внимание.",
]

def get_test_text(mode):
    if mode == '1':
        return random.choice(syllables)
    elif mode == '2':
        return random.choice(simple_words)
    else:
        texts = full_texts + hard_texts
        return random.choice(texts)

def main():
    mode = select_mode()
    test_text = get_test_text(mode)
    
    print("\nВаша задача -- точно напечатать следующий текст:")
    print(test_text)
    input("Нажмите Enter, чтобы начать...")

    start_time = time.time()
    user_input = input("\nВаш ввод: ")
    end_time = time.time()
    elapsed = end_time - start_time

    # Подсчёт ошибок
    errors = sum(1 for a, b in zip(test_text, user_input) if a != b) + abs(len(test_text) - len(user_input))
    
    # Подсчет скорости: для режима "слоги" и "слова" - можно считать по пробелам, для текста - символы
    if mode == '1':
        count = len(user_input.split())
        unit = "слогов/мин"
    elif mode == '2':
        count = len(user_input.split())
        unit = "слов/мин"
    else:
        count = len(user_input)
        unit = "символов/мин"
    
    speed = count / elapsed * 60 if elapsed > 0 else 0

    print("\nРезультаты:")
    print(f"Время: {elapsed:.2f} секунд")
    print(f"Ошибки: {errors}")
    print(f"Скорость печати: {speed:.1f} {unit}")

if __name__ == "__main__":
    main()
