# Definindo a string de entrada (pode ser substituída por input do usuário)
input_string = input("Digite uma string: ")

# Converte a string para minúsculas para simplificar a contagem de 'a' (ignora maiúsculas/minúsculas)
input_lower = input_string.lower()

# Contagem de ocorrências da letra 'a'
count_a = input_lower.count('a')

# Verifica se a letra 'a' aparece na string e exibe o resultado
if count_a > 0:
    print(f"A letra 'a' aparece {count_a} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")
