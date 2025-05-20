def length_conversion(value, from_unit, to_unit):
    length_units = {'inches': 2.54, 'centimeters': 1}
    return value * length_units[from_unit] / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {'pounds': 0.453592, 'kilograms': 1}
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    else:
        return value

def time_conversion(value, from_unit, to_unit):
    time_units = {'seconds': 1, 'minutes': 60, 'hours': 3600}
    return value * time_units[from_unit] / time_units[to_unit]

def unit_converter():
    print("Choose conversion type: ")
    print("1. Length\n2. Weight\n3. Temperature\n4. Time")
    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (inches/centimeters): ").lower()
        to_unit = input("Enter to unit (inches/centimeters): ").lower()
        print(f"Converted value: {length_conversion(value, from_unit, to_unit)} {to_unit}")

    elif choice == 2:
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (pounds/kilograms): ").lower()
        to_unit = input("Enter to unit (pounds/kilograms): ").lower()
        print(f"Converted value: {weight_conversion(value, from_unit, to_unit)} {to_unit}")

    elif choice == 3:
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (celsius/fahrenheit): ").lower()
        to_unit = input("Enter to unit (celsius/fahrenheit): ").lower()
        print(f"Converted value: {temperature_conversion(value, from_unit, to_unit)} {to_unit}")

    elif choice == 4:
        value = float(input("Enter value: "))
        from_unit = input("Enter from unit (seconds/minutes/hours): ").lower()
        to_unit = input("Enter to unit (seconds/minutes/hours): ").lower()
        print(f"Converted value: {time_conversion(value, from_unit, to_unit)} {to_unit}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    unit_converter()