import math
import telebot

bot = telebot.TeleBot("6782182630:AAEbWVu_lyBob5IMiVipWNYlWwIkGOHiwG4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-калькулятор. Напиши /calc, чтобы начать.")

@bot.message_handler(commands=['calc'])
def calculator(message):
    bot.reply_to(message, "Выберите операцию:\n"
                          "1. Сложение\n"
                          "2. Вычитание\n"
                          "3. Умножение\n"
                          "4. Деление\n"
                          "5. Квадратный корень числа\n"
                          "6. Возведение в степень\n"
                          "7. Гипотенуза\n"
                          "8. Площадь круга\n"
                          "9. Площадь треугольника по формуле Герона\n")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    if text == '1':
        bot.reply_to(message, "Введите первое число:")
        bot.register_next_step_handler(message, get_num1_for_addition)
    elif text == '2':
        bot.reply_to(message, "Введите уменьшаемое:")
        bot.register_next_step_handler(message, get_minuend_for_subtraction)
    elif text == '3':
        bot.reply_to(message, "Введите первый множитель:")
        bot.register_next_step_handler(message, get_num1_for_multiplication)
    elif text == '4':
        bot.reply_to(message, "Введите делимое:")
        bot.register_next_step_handler(message, get_dividend_for_division)
    elif text == '5':
        bot.reply_to(message, "Введите число:")
        bot.register_next_step_handler(message, get_number_for_square_root)
    elif text == '6':
        bot.reply_to(message, "Введите основание:")
        bot.register_next_step_handler(message, get_base_for_exponentiation)
    elif text == '7':
        bot.reply_to(message, "Введите длину первого катета:")
        bot.register_next_step_handler(message, get_cathetus1_for_hypotenuse)
    elif text == '8':
        bot.reply_to(message, "Выберите вариант расчета:\n"
                              "1. Площадь без буквенного значения pi\n"
                              "2. Площадь с буквенным значением pi (например: 25pi)")
        bot.register_next_step_handler(message, pi)
    elif text == '9':
        bot.reply_to(message, "Введите длину первой стороны:")
        bot.register_next_step_handler(message, get_side1_for_triangle_area)
    else:
        bot.reply_to(message, "Некорректная операция! Попробуйте еще раз.")

# Функции для шагов

def get_num1_for_addition(message):
    num1 = float(message.text)
    bot.reply_to(message, "Введите второе число:")
    bot.register_next_step_handler(message, lambda msg: get_num2_for_addition(msg, num1))

def get_num2_for_addition(message, num1):
    num2 = float(message.text)
    result = num1 + num2
    bot.reply_to(message, f"Сумма: {result}")

def get_minuend_for_subtraction(message):
    minuend = float(message.text)
    bot.reply_to(message, "Введите вычитаемое:")
    bot.register_next_step_handler(message, lambda msg: get_subtrahend_for_subtraction(msg, minuend))

def get_subtrahend_for_subtraction(message, minuend):
    subtrahend = float(message.text)
    result = minuend - subtrahend
    bot.reply_to(message, f"Разность: {result}")

def get_num1_for_multiplication(message):
    num1 = float(message.text)
    bot.reply_to(message, "Введите второй множитель:")
    bot.register_next_step_handler(message, lambda msg: get_num2_for_multiplication(msg, num1))

def get_num2_for_multiplication(message, num1):
    num2 = float(message.text)
    result = num1 * num2
    bot.reply_to(message, f"Произведение: {result}")

def get_dividend_for_division(message):
    dividend = float(message.text)
    bot.reply_to(message, "Введите делитель:")
    bot.register_next_step_handler(message, lambda msg: get_divisor_for_division(msg, dividend))

def get_divisor_for_division(message, dividend):
    divisor = float(message.text)
    if divisor == 0:
        bot.reply_to(message, "На ноль делить нельзя!")
    else:
        result = dividend / divisor
        bot.reply_to(message, f"Частное: {result}")

def get_number_for_square_root(message):
    num = float(message.text)
    if num >= 0:
        result = math.sqrt(num)
        bot.reply_to(message, f"Квадратный корень: {result}")
    else:
        bot.reply_to(message, "Квадратный корень из отрицательного числа не вычисляется!")

def get_base_for_exponentiation(message):
    base = float(message.text)
    bot.reply_to(message, "Введите степень:")
    bot.register_next_step_handler(message, lambda msg: get_exponent_for_exponentiation(msg, base))

def get_exponent_for_exponentiation(message, base):
    exponent = float(message.text)
    result = base ** exponent
    bot.reply_to(message, f"Результат возведения в степень: {result}")

def get_cathetus1_for_hypotenuse(message):
    cathetus1 = float(message.text)
    bot.reply_to(message, "Введите длину второго катета:")
    bot.register_next_step_handler(message, lambda msg: calculate_hypotenuse(msg, cathetus1))

def calculate_hypotenuse(message, cathetus1):
    cathetus2 = float(message.text)
    result = math.sqrt(cathetus1 ** 2 + cathetus2 ** 2)
    bot.reply_to(message, f"Гипотенуза: {result}")

def pi(message):
    text = message.text
    if text == '1':
        bot.reply_to(message, "Введите радиус:")
        bot.register_next_step_handler(message, calculate_circle_area_without_pi)
    elif text == '2':
        bot.reply_to(message, "Введите радиус:")
        bot.register_next_step_handler(message, calculate_circle_area_with_pi)
    else:
        bot.reply_to(message, "Некорректный выбор! Попробуйте еще раз.")

def calculate_circle_area_without_pi(message):
    radius = float(message.text)
    if radius >= 0:
        area = math.pi * radius ** 2
        bot.reply_to(message, f"Площадь: {round(area, 2)}")
    else:
        bot.reply_to(message, "Радиус не может быть меньше нуля!")

def calculate_circle_area_with_pi(message):
    radius = float(message.text)
    if radius >= 0:
        area = radius ** 2
        bot.reply_to(message, f"Площадь: {area}pi")
    else:
        bot.reply_to(message, "Радиус не может быть меньше нуля!")

def get_side1_for_triangle_area(message):
    side1 = float(message.text)
    bot.reply_to(message, "Введите длину второй стороны:")
    bot.register_next_step_handler(message, lambda msg: get_side2_for_triangle_area(msg, side1))

def get_side2_for_triangle_area(message, side1):
    side2 = float(message.text)
    bot.reply_to(message, "Введите длину третьей стороны:")
    bot.register_next_step_handler(message, lambda msg: calculate_triangle_area(msg, side1, side2))

def calculate_triangle_area(message, side1, side2):
    side3 = float(message.text)
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        p = (side1 + side2 + side3) / 2
        area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
        bot.reply_to(message, f"Площадь треугольника: {round(area, 2)}")
    else:
        bot.reply_to(message, "Эти стороны не образуют треугольник!")

# Запускаем бота
bot.polling()