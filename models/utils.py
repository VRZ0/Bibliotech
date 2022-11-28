import re
import hashlib
import json

#validations
def nameValidation(nome):

    for i in nome:

        valid = re.match(r'[a-zA-Z]', i)

        while not valid:
            return nameValidation(input('Digite um nome valido: '))

    return nome  

def telValidation(telefone):
    
    padrao = "^[1-9]{2}(?:[2-8]|9[1-9])[0-9]{3}[0-9]{4}$"

    valid = re.search(padrao, telefone)

    while not valid:
            return telValidation(input('Digite um telefone valido: '))

    return telefone  

def cpfValidation(cpf):

    padrao = "^[0-9]{3}[0-9]{3}[0-9]{3}[0-9]{2}$"

    valid = re.search(padrao, cpf)

    #inicio da copia
    if valid:
        valid = 0
        for dig in range(0, 10):
            valid += int(cpf[dig])
            dig += 1
        if int(cpf[0]) == valid / 11:
            return cpfValidation(input('Digite um cpf valido: '))

        # rotina de cálculos do dígito verificador do CPF
        else:
            # verificação do 10º dígito verificador
            soma = 0
            count = 10
            for i in range(0, len(cpf)-2):
                soma = soma + (int(cpf[i])*count)
                i+=1
                count-=1
            dg1 = 11-(soma%11)
            if dg1 >= 10:
                dg1 = 0

            # verificação do 11º dígito verificador
            soma = 0
            count = 10
            for j in range(1, len(cpf)-1):
                soma = soma + (int(cpf[j])*count)
                j+=1
                count-=1
            dg2 = 11-(soma%11)
            if dg2 >= 10:
                dg2 = 0

            # mensagem ao usuário
            if int(cpf[9]) != dg1 or int(cpf[10]) != dg2:
                return cpfValidation(input('Digite um cpf valido: '))
            else:
                return cpf

def cepValidation(cep):

    padrao = "^[0-9]{8}$"

    valid = re.search(padrao, cep)

    while not valid:
        return cepValidation(input('Digite um cep valido: '))
    
    return cep


#passwords
def paswdValidation(paswd):
    return paswd

def hashEncode(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


#JSON
def dbWrite(path, data):
    db = open(path, "a")
    json.dump((data), db)
    db.write('\n')

#sys
import platform
def getSystem():
    so = platform.system()
    if so == 'Windows':
        return 'cls'
    else:
        return 'clear'