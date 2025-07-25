def average(sum=1, length=1):
    return sum / length

def addition(n=1):
    sum = 0
    positive = 0
    negative = 0
    zeros = 0
    multiple_of_3 = 0
    for i in range(n):
        number = float(input(f'Ingrese el número ({i+1}): '))
        sum += number
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zeros += 0
        if number % 3 == 0:
            multiple_of_3 += 1

    return sum, positive, negative, zeros, multiple_of_3

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

while True:
    print('Opciones:')
    print('1. Sumar, obtener promedio y cuántos son positivos, negativos, ceros y múltiplos de 3.')
    print('2. Calcular área y perímetro de un rectángulo.')
    print('3. Verificar si un número es primo.')
    print('4. Calcular promedio de n calificaciones, cuantas son mayores a 85 y cuantas menores a 60.')
    print('5. Ingresar n números y mostrar el mayor, el menor y cuántos se repiten.')
    print('6. Calculadora de operaciones básicas (suma, resta, multiplicación y división).')
    print('7. Salir del programa.')
    print()

    option = input('Ingrese la opción que desea: ')

    match option:
        case '1':
            n = int(input('Ingrese la cantidad de números que desea sumar: '))
            result = addition(n)
            print()
            print(f'La suma de los números es: {result[0]}')
            print(f'El promedio de los números sumados es: {average(result[0], n)}')
            print(f'La cantidad de positivos es: {result[1]}')
            print(f'La cantidad de negativos es: {result[2]}')
            print(f'La cantidad de ceros es: {result[3]}')
            print(f'La cantidad de múltiplos de 3 es: {result[4]}')
            print()

        case '2':
            base = float(input('Ingrese la base del rectángulo (cm): '))
            height = float(input('Ingrese la altura del rectángulo (cm): '))
            print(f'El area del rectángulo es de: {rectangle_area(base, height)}cm')
            print(f'El perímetro del rectángulo es de {rectangle_perimeter(base, height)} cm')
            print()

        case '3':
            number = int(input('Ingrese un número: '))
            if prime_number(number):
                print(f'{number} es primo.')
            else:
                print(f'{number} no es primo.')
            print()

        case '4':
            n = int(input('Ingrese la cantidad de notas: '))
            results = grades_average(n)
            print(f'El promedio de las notas es: {results[0]}')
            print(f'La cantidad de notas iguales o sobre 85 puntos son: {results[1]}')
            print(f'La cantidad de notas debajo de 60 puntos son: {results[2]}')
            print()

        case '5':
            pass

        case '6':
            pass

        case '7':
            print('Saliendo del programa...')
            break

        case _:
            print('Opción inválida. Intente nuevamente.')
            print()