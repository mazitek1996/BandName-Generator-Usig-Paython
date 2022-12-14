# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide(x, y):
#     return x / y
#
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
#
# # Take input from the user
# choice = input("Enter choice(1/2/3/4):")
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if choice == '1':
#     print(num1,"+",num2,"=", add(num1,num2))
#
# elif choice == '2':
#     print(num1,"-",num2,"=", subtract(num1,num2))
#
# elif choice == '3':
#     print(num1,"*",num2,"=", multiply(num1,num2))
#
# elif choice == '4':
#     print(num1,"/",num2,"=", divide(num1,num2))
# else:
#     print("Invalid input")
#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end




print("Good day, This is a Band Name Generator built with python. \n First of all tell us Your")

city_name = input("What is your City Name?.")
pet_name = input("What is your pet's name?.")


print("Your band name should be " + city_name + pet_name)