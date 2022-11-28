from usuario import Usuario
from utils import *
from livro import Livro
from menu import Menu
import re
import pandas as pd
from datetime import datetime
import os

clrcmd = getSystem()
os.system(clrcmd) or None

try:
    logged = False   
    while not logged:    
        print('Bem vindo ao sistema de gerenciamento de biblioteca\n')
        cadastrado = input('Você ja tem uma conta? \n\n[S] Sim\n[N] Não\n\n> ')

        if cadastrado.upper() == 'N':
            os.system(clrcmd) or None
            print('\nRealize um cadastro para continuar:\n')

            nome = nameValidation(str(input('Digite seu nome: ')))
            telefone = telValidation(input('digite seu telefone: '))
            cpf = cpfValidation(input('Digite seu cpf: '))
            cep = cepValidation(input('Digite seu cep: '))
            senha = paswdValidation(input('Digite uma senha: '))
            user = Usuario(nome, telefone, cpf, cep, senha)

            print(user.cadastrarUsuario())
                    
        else:
            if cadastrado.upper() == 'S':
                os.system(clrcmd) or None
                print('\nFaça login para continuar:\n')
                nome = nameValidation(str(input('Digite seu nome: ')))
                senha = paswdValidation(input('Digite uma senha: '))
                while not Usuario.validarUsuario(nome, senha):
                    print('\nUsuario ou senha incorretos!\n')
                    nome = nameValidation(str(input('Digite seu nome: ')))
                    senha = paswdValidation(input('Digite uma senha: '))
                os.system(clrcmd) or None
                logged = True

    menu = Menu('u')     
    Menu.showBanner()
    
except:
    print('Voce cometeu algum erro, por favor tente novamente. Try funcionou')