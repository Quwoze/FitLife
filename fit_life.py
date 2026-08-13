# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30

user_name = input("Привет! Я FitLife, как тебя зовут?\n").title()

while True:
    try:
        user_age = int(input(f"Приятно познакомиться, {user_name}, сколько тебе лет?\n"))

        if user_age < 0:
            print("Возраст не может быть отрицательным. Попробуй ещё раз!")
            continue
        break

    except ValueError:
        print("Похоже, ты ввёл не число. Попробуй ещё раз!")

while True:
    try:
        user_weight = float(input("Какой у тебя вес? (в кг)\n"))

        if user_weight <= 0:
            print("Вес не может быть отрицательным или равным нулю. Попробуй ещё раз!")
            continue
        break

    except ValueError:
        print("Похоже, ты ввёл не число. Попробуй ещё раз!")

while True:
    try:
        user_height = float(input("Какой у тебя рост? (в метрах)\n"))

        if user_height <= 0:
            print("Рост не может быть отрицательным или равным нулю. Попробуй ещё раз!")
            continue
        break

    except ValueError:
        print("Похоже, ты ввёл не число. Попробуй ещё раз!")    


def bmi(weight, height):  #  calc of body mass index
    """Рассчитывает индекс массы тела (ИМТ) и округляет до 1 знака."""
    return round(weight / (height ** 2), 1)

def water_ml(weight):  #  calc of the water norm (in ml)
    """Рассчитывает рекомендуемую норму воды в мл (30 мл на кг веса)."""
    return weight * WATER_PER_KG

b_m_i = bmi(user_weight, user_height)
water_needed = water_ml(user_weight)

print(f"Отчёт о пользователе: {user_name} ({user_age} г.)")
print(f"Твой индекс массы тела: {b_m_i}")
print(f"Рекомендованная норма воды в день: {water_needed} мл, {water_needed / 1000} л. \n")

print(f"Расчёт завершён, {user_name}! Будь здоров!")