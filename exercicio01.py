print("Cálculo de média\n")
nome = input("Insira o nome do aluno: ").title()
nota1 = float(input("Insira a primeira nota: ").replace(",","."))
nota2 = float(input("Insira a segunda nota: ").replace(",","."))
nota3 = float(input("Insira a terceira nota: ").replace(",","."))
media = (nota1 + nota2 + nota3)/3
if media >= 7:
    print((f"Olá, {nome}, sua média foi {media:.2f} e você está aprovado(a) ").replace(".",","))
elif media >=5:
    print((f"Olá, {nome}, sua média foi de {media:.2f} e você está em recuperação").replace(".",","))
else:
    print((f"Olá, {nome}, sua média foi de {media:.2f} e você está rerpovado").replace(".",","))
#outra forma de fazer
#if media >=7:
    #situacao = "Aprovado"
#elif media >=5:
    #situacao = "Recuperação"
#else:
    #"Reprovado"
#print("\nResultado:\n")
#print(f"Nome: ").title()
#print(f"Prova 1: {nota1:.2f}.replace(".",","))
#print(f"Prova 2: {nota2:.2f}.replace(".",","))
#print(f"Prova 3: {nota3:.2f}.replace(".",","))
#print(f"Média: {media:.2f}.replace(".",","))
#print(f"Situção: {situacao.upper()}.replace(".",","))

