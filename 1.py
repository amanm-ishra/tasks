def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

if unit.upper() == 'C':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(str(temperature)+"°C is equal to"+str(converted_temperature)+"°F")
elif unit.upper() == 'F':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(str(temperature)+"°F is equal to"+str(converted_temperature)+"°C")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")