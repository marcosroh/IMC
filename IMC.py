def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

# Dados do aluno
peso_aluno = 70  # kg
altura_aluno = 1.75  # metros

# Dados de outra pessoa
peso_outro = 85  # kg
altura_outro = 1.80  # metros

# Cálculo do IMC
imc_aluno = calcular_imc(peso_aluno, altura_aluno)
imc_outro = calcular_imc(peso_outro, altura_outro)

# Classificação do IMC
classificacao_aluno = classificar_imc(imc_aluno)
classificacao_outro = classificar_imc(imc_outro)

print(f"IMC do aluno: {imc_aluno:.2f} - {classificacao_aluno}")
print(f"IMC de outra pessoa: {imc_outro:.2f} - {classificacao_outro}")
