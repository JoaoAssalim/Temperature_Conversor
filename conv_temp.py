print('''
Temperature Conversor
[1] - Celcius
[2] - Fahrenheit
''')

def convertFahrenheit(temperature):
    return temperature * 1.8 + 32

def convertCelcius(temperature):
    return (temperature - 32) / 1.8

option = input('-> ')

if option.isdigit():
    option = int(option)
    temperature = input('Enter the temperature (use "." to float numbers): ')
    if temperature.isdigit():
        temperature = float(temperature)

        if option == 1:
            print(convertCelcius(temperature))
        elif option == 2:
            print(convertFahrenheit(temperature))
    else:
        print('This is not a number')
else:
    print('enter a menu option!')