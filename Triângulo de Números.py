def exibir_triangulo(n):
    for i in range(1, n + 1):
        # Imprime espaços iniciais para alinhar os números
        print(' ' * (n - i), end='')

        # Imprime os números da linha
        for j in range(1, i + 1):
            print(j, end=' ')

        print()  # Nova linha após cada linha do triângulo

# Solicita o número de linhas ao usuário
n = int(input("Digite o número de linhas para o triângulo de números: "))
exibir_triangulo(n)
input()