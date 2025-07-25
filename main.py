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

def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



