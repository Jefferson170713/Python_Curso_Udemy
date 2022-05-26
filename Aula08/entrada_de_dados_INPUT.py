"""
    ********************** [J] ***********************
    Nome: Jefferson De Almeida            Eng.Produção
    **************************************************
"""
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = (peso/(altura**2))
print(f"Seu nome é {nome} Sua idade {idade} "
      f"Seu peso {peso:.2f} Kg. Sua Altura {altura:.2f} m "
      f"Seu imc {imc:.2f}")