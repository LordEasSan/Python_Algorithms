#!/usr/bin/python3

def basic_calculator(a,b):
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    op = input('Enter operator: ')

    if op == '+':
        print('The addition equals: ', num1 + num2)
    elif op == '-':
        print('The substraction equals: ', num1 - num2)
    elif op == '*':
        print('The multiplication equals: ', num1 * num2)
    elif op == '/':
        print('The division equals: ', abs(num1 / num2))
    else:
        print('Invalid operator')