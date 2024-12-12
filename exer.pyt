texto="Olá mundo como está a correr este final de ano."

#1. Contar os Caracteres em uma String
print(len(texto))

#2. Converter String para Maiúsculas
print(texto.upper())

#3. Converter String para Minúsculas
print(texto.lower())

#4. Contar Ocorrências de um Caracter
print(texto.count("e"))

#5. Verificar se uma Palavra está na Frase
print('final' in "final")

#6. Substituir Palavras em uma Frase
print("mundo".replace("mundo", "pessoas"))

#7. Reverter uma String e exibi-la de trás para frente
print(texto[::-1])

#8. Dividir uma Frase em Palavras
print(texto.split())

#9. Capitalizar as Palavras de uma Frase
print(texto.capitalize())

#10. Remover Espaços em Branco no Início e Fim
print(texto.strip())

#11. Verificar o Código do Produto
import re
def verificar_codigo_produto(codigo):
    return bool(re.fullmatch(r"PROD-\d{4}", codigo))
print(verificar_codigo_produto("PROD-1234"))

#12. Separar Letras e Números de uma String
def separar_letras_numeros(placa):
    letras = ''.join([char for char in placa if char.isalpha()])
    numeros = ''.join([char for char in placa if char.isdigit()])
    return letras, numeros
letras, numeros = separar_letras_numeros("ABC-1234")
print(letras)   
print(numeros) 

#13. Imprimir a Senha Escondida no Enigma
def descobrir_senha(enigma):
    return enigma[3:-15:5].upper()
senha = descobrir_senha("Kg8vlk8jIU7D8nNbd0GG4F2aCa4gnb85oÇAcm9aBmc55mnbtBl39Cvbn3")
print(senha)  

#14. Acessar um Caracter Isolado da String 
def acessar_caracter(s, posicao):
    return s[posicao]
print(acessar_caracter("Python", 3)) 

#15. Obter Substring Usando Slicing
def obter_substring(s, inicio, fim):
    return s[inicio:fim]
print(obter_substring("Python", 1, 4))  

#16. Calcular o Perímetro de um Círculo
import math
def calcular_perimetro(raio):
    return 2 * math.pi * raio
print(calcular_perimetro(5))

#17. Calcular sua Idade em Dias
idade=35
print(idade*365)

#18. Converter Metros para Centímetros
metros=28
print(metros*100)

#19. Calcular a Área de um Retângulo
largura=15
altura=10
print(largura*altura)

#20. Programa de Bom Dia
print("Bom dia!")
nome = input("Qual é o seu nome? ")
print(f"É um prazer conhecer você, {nome}!")

#21. História com Parágrafos e "Enter"
print("Era uma vez...", end="")
input()
print("Um aventureiro corajoso.", end="")
input()

#22. Calcular a Raiz Quadrada
numero=float(input("Insira um número:"))
print(numero*numero)

#23. Dobro de um Número
numero=float(input("Digite um número: "))
print(numero*2)

#24. Potência de Dois Valores
a=float(input("Digite o valor de A: "))
b=float(input("Digite o valor de B: "))
print(a**b)

#25. Converter Segundos para Horas, Minutos e Segundos
segundos = 3661
horas, resto = divmod(segundos, 3600)
minutos, segundos = divmod(resto, 60)
print(f"{horas}h {minutos}m {segundos}s")

#26. Área do triângulo
base, altura = 10, 5
print((base * altura) / 2)

#27. Trocar valores
x, y = 10, 45
x, y = y, x
print("x=", x,"y=", y)

#28. Gerar número aleatório
import random
print(random.randint(1, 100))

#29. Converter km para milhas
km=float(input("Insira um número:"))
print(km * 0.621371)

#30. Converter Celsius para Fahrenheit
celsius = float(input("Insira um número:"))
print((celsius * 9/5) + 32)

#31. Tempo de viagem
distancia = float(input("Insira um número:"))
velocidade = float(input("Insira um número:"))
print(distancia / velocidade)

#32. Redução de vida (fumante)
cigarros_por_dia = float(input("Insira um número:"))
anos_fumando = float(input("Insira um número:"))

#33. Dias de vida perdidos
print((cigarros_por_dia * anos_fumando * 365 * 10) / (60 * 24))

#34. Aumento de salário
salario = float(input("Insira um número:"))
percentual = float(input("Insira um número:"))
aumento = salario * (percentual / 100)
novo_salario = salario + aumento
print(aumento, novo_salario)

#35. Horas para dias e horas
horas = float(input("Insira um número:"))
dias, horas_restantes = divmod(horas, 24)
print("Dias=",dias, "Horas restantes=", horas_restantes)

#36. Média de 3 notas
notas = [float(input("Insira um número:")), float(input("Insira um número:")), float(input("Insira um número:"))]
print(sum(notas) / len(notas))

#37,38 Operações com dois números
a, b = float(input("Insira um número:")), float(input("Insira um número:"))
print(a + b, a - b, a * b)

#38,39 Divisão inteira e resto
a, b = float(input("Insira um número:")), float(input("Insira um número:"))
print(a // b, a % b)

#40. Potência
a, b = float(input("Insira um número:")), float(input("Insira um número:"))
print(a ** b)

#41. Seno, cosseno e tangente
angulo = float(input("Insira um número:"))
angulo_rad = math.radians(angulo)
print(math.sin(angulo_rad), math.cos(angulo_rad), math.tan(angulo_rad))

#42. Salário mensal
horas_mes = float(input("Insira um número:"))
valor_hora = float(input("Insira um número:"))
print(horas_mes * valor_hora)

#43. Modo noturno
modo = input("Ativar modo noturno (sim/não)? ").lower()
print("Modo noturno ativado!" if modo == "sim" else "Modo noturno desativado!")

#44. Área e perímetro do quadrado
lado = float(input("Insira um número:"))
print(lado**2, 4 * lado)

#45. Área e perímetro do círculo
raio = float(input("Insira um número:"))
print(math.pi * raio**2, 2 * math.pi * raio)

#46. Perímetro do triângulo
lados = [float(input("Insira um número:")), float(input("Insira um número:")), float(input("Insira um número:"))]
print(sum(lados))

#47. Sucessor de número
numero = float(input("Insira um número:"))
print(numero + 1)

#48. Expressão matemática
print(45 + 15 * 9)

#49. Complexa expressão
print(42 / 30 * (94 + 2) * 6 - 1)

#50. 2a × 3b
a, b = float(input("Insira um número do a:")), float(input("Insira um número do b:"))
print(2 * a * 3 * b)

#51. Soma de três variáveis
x, y, z = 1, 2, 3
print(x + y + z)

#52. Aumento de salário
salario = float(input("Insira um número:"))
percentual = float(input("Insira um número:"))
aumento = salario * (percentual / 100)
novo_salario = salario + aumento
print(aumento, novo_salario)

#53. Preço do carro alugado
dias = float(input("Insira um número:"))
km = float(input("Insira um número:"))
print((60 * dias) + (0.15 * km))