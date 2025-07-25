from click import option


def average(sum=1, length=1):
    return sum / length

def addition(n=1):
    sum = 0
    positive = 0
    negative = 0
    multiple_of_3 = 0
    for i in range(n):
        number = float(input(f'Ingrese el número ({i+1}): '))
        sum += number
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        if number % 3 == 0:
            multiple_of_3 += 1

    return sum, positive, negative, multiple_of_3

def rectangle_area(base=1, height=1):
    return base * height

def rectangle_perimeter(base=0, height=0):
    return 2*base + 2*height

def prime_number(num=1):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def grades_average(n=1):
    sum = 0
    over_85 = 0
    risk_zone = 0
    for i in range(n):
        grade = int(input('Ingrese las nota: '))
        sum += grade
        if grade >= 85:
            over_85 += 1
        elif grade < 60:
            risk_zone += 1

    return sum / n, over_85, risk_zone

def max_and_min(n=1):
    numbers = []
    for i in range(n):
        num = int(input('Ingrese el número: '))
        numbers.append(num)

    frequency = {}
    for i in numbers:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    return max(numbers), min(numbers), frequency

def operations(option, num1, num2):
    match option:
        case '1':
            return num1 + num2
        case '2':
            return num1 - num2
        case '3':
            return num1 * num2
        case '4':
            return num1 / num2
        case _:
            return 'Opción invalida'

