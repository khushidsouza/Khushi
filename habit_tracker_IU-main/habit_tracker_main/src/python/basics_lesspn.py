name = "khushi"  
temperature = "45"
print("Name:", name)           # Outputs: Name: Alice
print("Temperature:", temperature)  # Outputs: Temperature: 36.6
a = [1,2,3]
b = a
c = [1,2,3]
print (a is b)
print (b is c)
print (c is a)

# age = 20
# age = int(input("input your age : "))
# if age < 21:
#     print("You are young.")
# elif age == 21:
#     print("You are old.")
# else:
#     print("You are a fossil.")

def greet() :
    name = input("Input your name :") 
    age = int(input("Input your age :"))
    if age < 21:
        print(f"{name}You are young.")
    elif age == 21:
        print(f"{name}You are old.")
    else:
        print(f"{name}You are a fossil.")

greet()



