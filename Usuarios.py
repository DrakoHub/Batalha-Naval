print("Olá Boas Vindas Usuario")
UsersList = []

#Loop de Cadastros
while True:
    nome = input("Insira seu Nome:\n")
    idade = int(input("Insira sua Idade:\n"))
    cidade = input("Insira sua Cidade:\n")
    if idade > 150:
        print("Idade Inválidade")
        break
    UserTempList = [nome, idade, cidade]
    UsersList.append(UserTempList)
    AddNew = input("Desejas Adicionar outro cadastro?: \n [s/n] \n")
    if AddNew == "n" or AddNew == "N":
        break
print("Cadastros:")
MedAge = 0
j = 0
for x in UsersList:
    i = 0
    for y in x:
        if i == 0:
            print("Nome:")
        if i == 1:
            print("Idade:")
            j = j+1
            MedAge = MedAge + y
        if i == 2:
            print("Cidade:")
            i=0
        print(y)
        i = i+1
MedAge = MedAge / j
print(f"A Media das Idades foi Igual a: {MedAge}")
