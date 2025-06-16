def eh_par(numero):
    """Verifica se o número é par."""
    return numero % 2 == 0

def eh_primo(numero):
    """Verifica se o número é primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


print("=== Análise de Dois Números Inteiros ===")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

print("\n--- Operações Matemáticas ---")
print(f"Soma: {num1} + {num2} = {num1 + num2}")
print(f"Subtração: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicação: {num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"Divisão: {num1} / {num2} = {num1 / num2:.2f}")
else:
    print("Divisão: Não é possível dividir por zero.")

print("\n--- Análise dos Números ---")
for i, num in enumerate([num1, num2], start=1):
    print(f"\nNúmero {i}: {num}")
    print("→ Par" if eh_par(num) else "→ Ímpar")
    print("→ Primo" if eh_primo(num) else "→ Não é primo")
