def greet(name):
    return f"Привет {name}"
    
print(greet("deni"))

def square(number):
    return (number**2)

print(square(22))

def max_of_two(num1,num2):
    if num1>num2:return num1
    elif num1 < num2:return num2
    else: return "Числа равны"

num1=int(input("enter first num"))
num2=int(input("enter second num"))