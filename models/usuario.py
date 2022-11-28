import json
from utils import *

class Usuario:

    def __init__(self, nome, telefone, cpf, cep, paswd):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.cep = cep
        self.paswd = paswd

    def cadastrarUsuario(self, usrType='usr'):
        userObject = {
            "nome" : self.nome,
            "telefone" : self.telefone,
            "cpf" : self.cpf,
            "cep" : self.cep,
            "usrtype": usrType,
            "paswd" : hashEncode(self.paswd)
        }

        dbWrite("../data/usuarios.txt", userObject)
        return 'Usuário cadastrado com sucesso'

    def getUser():
        return [loggedUser, loggedUtype] 

    def validarUsuario(login, paswd):
        dbUser = open("../data/usuarios.txt")
        usr = []
        for line in dbUser:
            usr.append(json.loads(line))
        for i in usr:
            if login in i['nome']:
                if hashEncode(paswd) == i["paswd"]:
                    global loggedUser, loggedUtype
                    loggedUser, loggedUtype = login, i['usrtype']
                    return True
            
        return False