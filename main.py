def sum(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def main():
    print("Ingrese el primer número:")
    a = int(input())
    print("Ingrese el segundo número:")
    b = int(input())
    print("Enter your operation:")
    print("+: sumar")
    print("-: restar")
    print("*: multiplicar")
    print("/: dividir")
    operation = input()
    msg = "el resultado es: "
    if operation == "+":
        print(msg + str(sum(a, b)))
    elif operation == "-":
        print(msg + str(substract(a, b)))
    elif operation == "*":
        print(msg + str(multiply(a, b)))
    elif operation == "/":
        print(msg + str(divide(a, b)))
    else:
        print("Operador seleccionado es inválido")

main()


