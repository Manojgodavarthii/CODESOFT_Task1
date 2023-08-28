def calculator():
  number_1 = float(input('Enter the first number: '))
  number_2 = float(input('Enter the second number: '))

  
  operation = input('Select the operation (+, -, *, /): ')

  
  if operation == '+':
    result = number_1 + number_2
  elif operation == '-':
    result = number_1 - number_2
  elif operation == '*':
    result = number_1 * number_2
  elif operation == '/':
    result = number_1 / number_2
  else:
    print('Invalid operation!')

  print('The result is:', result)


if __name__ == '__main__':
  calculator()
