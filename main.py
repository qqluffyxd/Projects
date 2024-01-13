# actions
plus = '+'
minus = '-'
multiply = '*'
divide = '/'
equals = '='

# user_data
num1 = float(input('Enter first number: '))
action = str(input('Enter action: '))
num2 = float(input('Enter second number: '))

# resources


# Start program
def func1(n):
    if action == '+':
        n = num1 + num2
    elif action == '-':
        n = num1 - num2
    elif action == '*':
        n = num1 * num2
    elif action == '/':
        n = num1 / num2
    print('Result: ', n)


# End, print
func1('')
