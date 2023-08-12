"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num = input("Digite um número inteiro: ")
try:
    numint = int(num)
    if numint % 2 == 0:
     print(f"O número {numint} é um número par!")
    else:
       print(f"O número {numint} é um número ímpar ")

except:
   print("Este não é um número inteiro! ")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input("Qual a hora do dia? ")
horarioint = int(horario)
if horarioint > 0 and horarioint <= 11:
   print("Bom dia!")

elif horarioint > 11 and horarioint <=17:
   print ("Boa tarde!")

elif horarioint >17 and horarioint <23:
   print("Boa noite!")

else:
   print("Poe um horário direito porra!")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu nome: ")

if len(nome) <=4:
    print("Seu nome é muito curto!")

elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal!")

elif len(nome) > 6:
    print("Seu nome é muito grande!")