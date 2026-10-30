nota = input("Insira o conceito do aluno com valores de A, B, C, D, ou F: ").upper()
match nota:
    case "A":
        print("Excelente")
    case "B":
        print("Bom")
    case "C":
        print("Regular")
    case "D":
        print("Ruim")
    case "F":
        print("Reprovado")
    case _:
        print("Opção inválida")
    