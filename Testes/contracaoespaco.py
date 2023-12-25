import math

v = float(input("Digite a velocidade da luz (Ex: 0.5):"))
lrepouso = int(input("Digite o comprimento em repouso:"))

k = math.sqrt(1-(v**2))
lmovimento = k * lrepouso

print(f"O comprimento em movimento é: {lmovimento:.2f} metros")