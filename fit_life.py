# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30

# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
user_name = input("Привет! Давай знакомиться. Я FitLife, а как тебя зовут?\n").title()
user_age = int(input(f"Приятно познакомиться {user_name}, сколько тебе лет?\n"))
# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
user_weight = float(input("Какой у тебя вес? (в кг)\n"))
user_height = float(input("Какой у тебя рост? (в метрах)\n"))
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
def bmi(): #calc of body mass index
    return round(user_weight / (user_height ** 2), 1)
# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
def water_ml(): #calc of the water norm (in ml)
    return user_weight * WATER_PER_KG
# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f"Отчёт о пользователе: {user_name} ({user_age} г.)")
print(f"Твой индекс массы тела: {bmi()}")
print(f"Рекомендованная норма воды в день: {water_ml()} мл, {water_ml() / 1000} л. \n")

print(f"Расчёт завершен. {user_name} будьте здоровы!")