#!/usr/bin/env python3

#    function adminLogin(username, password) {
#   if ((username === "admin" || username === "ADMIN") && password === "12345") {
#     return "Access granted";
#   } else {
#     return "Access denied";
#   }
# }
def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and (password == "12345"):
        return "Access granted"
    else: 
        return "Access denied"
pass

# // function howsTheWeather(temperature) {
# //   let response;
# //   if (temperature < 40) {
# //     response = "brisk";
# //   } else if (temperature >= 40 && temperature <= 65) {
# //     response = "a little chilly";
# //   } else if (temperature > 85) {
# //     response = "too dang hot";
# //   } else {
# //     response = "perfect";
# //   }
# //   return `It's ${response} out there!`;
# // }

def hows_the_weather(temperature):
    response = ""
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
    return f"It's {response} out there!"
pass

# function fizzbuzz(num) {
#   if (num % 3 === 0 && num % 5 === 0) {
#     return "FizzBuzz";
#   } else if (num % 3 === 0) {
#     return "Fizz";
#   } else if (num % 5 === 0) {
#     return "Buzz";
#   } else {
#     return num;
#   }
# }

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
pass

# function calculator(operation, num1, num2) {
#   switch (operation) {
#     case "+":
#       return num1 + num2;
#     case "-":
#       return num1 - num2;
#     case "*":
#       return num1 * num2;
#     case "/":
#       return num1 / num2;
#     default:
#       console.log("Invalid operation!");
#   }
# }
def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
pass