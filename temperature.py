def show_menu():
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")

    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")

    elif choice == "3":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")