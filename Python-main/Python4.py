# job 1
def my_print_hello():
    print(1 + 2)

my_print_hello()

# job 2
name = "d"
def my_print_name():
    print(name)

my_print_name()

def my_print_name(name):
    print(name)

my_print_name("oui-oui")
my_print_name("non-non")

# job 3
def Add(num1, num2):
    print(num1 + num2)

Add(1, 2)
Add(10, 10)

# job 4
def GetHello():
    return "Hello la plateforme"

message = GetHello()
print(message)

# # job 5
def calcule(num1, operator ,num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        operator == "%"
        return num1 % num2
    

print(calcule(10,'+',5))
print(calcule(10,'-',5))
print(calcule(10,'*',5))
print(calcule(10,'/',5))
print(calcule(10,'%',3))

# job 6
def stat(nombre):
    if nombre > 0:
        print(nombre, "est positif")
    elif nombre == 0:
        print(nombre, "est nul")
    elif nombre <- 0:
        print(nombre, "est négatif")

stat(-1)
stat(0)
stat(5)
stat(10)