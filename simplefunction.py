"""def greet_user(name):
 print("hello " + name)
function =greet_user("sad")""


def rectangle_area(height,width):
    print(width*height)
width = 5
height = 8
rectangle_area(height,width)"


def celsius_to_fahrenheit(celsius):
   print((celsius*9/5)+32)
celsius = 25
celsius_to_fahrenheit(celsius)""

def is_even(n):
 return n % 2 == 0
 print(is_even(10))""



def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = 10
if even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")""


def max_of_two(num1,num2):
 if num1 > num2:
    print("this is bigger",num1)
 else:
    print("this is bigger",num2)
num1 = 78
num2 = 32
max_of_two(num1,num2)""


def is_vowel(char):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if char in vowels:
        return True
    else:
        return False

characters = ['a', 'b', 'E', 'Z']
for char in characters:
    if is_vowel(char):
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is not a vowel.")"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
