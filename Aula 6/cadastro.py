
def nomes_extract(linhas):
    nomes = []
    for linha in linhas:
        comeco_tag = "Nome: "
        comeco = linha.find(comeco_tag)
        if comeco != -1:
            inicio_nome = comeco + len(comeco_tag)
            final = linha.find('|', inicio_nome)
            if final != -1:
                nome = linha[inicio_nome:final].strip()
                nomes.append(nome)
    return nomes
    
with open('cadastro.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
        

nomes_extraidos = nomes_extract(linhas)
print("Os nomes extraidos:", nomes_extraidos)
