
def formatar_nome(nome):
    return nome.lower().title()
def validar_email(email):
    if "@" in email and email.split("@")[-1] in ["gmail.com", "outlook.com", "yahoo,com", "org", "com", "edu.br", "br"]:
         if "." in email.split("@")[-1]:
            return True
    return False
