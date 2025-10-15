number=int(input('Enter a number greater than 0 : '))

while number <= 0:
    print(f'{number} is invalid')
    number=int(input('Enter a number greater than 0 : '))
if number > 0:
    if number % 2 == 0:
        print(f'{number} is an even number')
    else:
        print(f'{number} is an odd number')
else:
    print(f'{number} is invalid')