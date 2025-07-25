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

