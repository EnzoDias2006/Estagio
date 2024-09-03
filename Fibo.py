def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def main():
    try:
        num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
        if is_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, informe um número válido.")

if __name__ == "__main__":
    main()
