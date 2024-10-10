# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(n):
    # Iniciando os dois primeiros termos da sequência
    fib1, fib2 = 0, 1
    
    # Gerar a sequência de Fibonacci até fib2 ser maior ou igual ao número informado
    while fib2 < n:
        fib1, fib2 = fib2, fib1 + fib2
    
    # Verificar se o número informado pertence à sequência
    if n == fib2 or n == 0:
        return True
    else:
        return False

# Solicitar o número de entrada do usuário
num = int(input("Informe um número: "))

# Verificar se o número pertence à sequência de Fibonacci
if pertence_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")