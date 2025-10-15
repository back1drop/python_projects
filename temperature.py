temperature=round(float(input("Enter temperature: ")),2)
sign=input("Is the temperature in Farenheits or Celsius?Choose between (F or C): ").upper()
if sign == 'F':
    temperature-=273
    print(f"The temperature in celsius is: {temperature} C")
else:
    temperature+=273
    print(f"The temperature in farenheits is: {temperature} F")