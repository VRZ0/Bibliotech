from livro import Livro
from emprestimo import Emprestimo
from usuario import Usuario
from utils import *
import os

clrcmd = getSystem()

class Menu:
    def __init__(self, user):
        self.user = user

    def selectItem(choice):
        os.system(clrcmd) or None
        match choice:
            case '1':
                print('\n=== Seus emprestimos ===\n')
                print(f'\n{Emprestimo.listarEmprestimos(Usuario.getUser()[0])}')
                return Menu.showBanner()

            case '2':
                print('\n=== Faça um emprestimo ===\n')
                print(Livro.listarLivros())

                loanBook = int(input('\nQual livro deseja alugar? '))        
                data = (Livro.getLivros())['nomes:']
                
                emprestimo = Emprestimo(Usuario.getUser()[0], data[loanBook])

                print(emprestimo.fazerEmprestimo())
                return Menu.showBanner()
            
            case '3':
                print('\n=== Nosso Acervo ===\n')
                print(Livro.listarLivros())
                return Menu.showBanner()
            
            case '99':
                print('\n=== Sobre nós ===\n')
                print('A RiseCode é uma empresa que nasceu com o objetivo de transformar a vida das pessoas, trazendo para seus clientes soluções simples e práticas para seus clientes. A empresa, mesmo com poucos anos de existência, já trabalha com o desenvolvimento de I.A, fornece desenvolvimento de software seguro e web Applications para as mais diversas empresas, atua na execução de pentests, e ainda fornece consultoria de segurança.')
                return Menu.showBanner()
            
            case '4':
                if Usuario.getUser()[1] == 'adm':
                    print('\n=== Cadastre novos livros ===\n')
                    nomeLivro = input('Qual livro deseja cadastrar: ')
                    autorLivro = input('Qual o autor do livro: ')
                    livro = Livro(nomeLivro, autorLivro)
                    print(livro.cadastrarLivro())
                    return Menu.showBanner()
            case '5':
                if Usuario.getUser()[1] == 'adm':
                    print('\n=== Cadastrar um novo administrador ===\n')
                    nome = nameValidation(str(input('Digite o nome: ')))
                    telefone = telValidation(input('digite o telefone: '))
                    cpf = cpfValidation(input('Digite o cpf: '))
                    cep = cepValidation(input('Digite o cep: '))
                    senha = paswdValidation(input('Digite a senha: '))
                    user = Usuario(nome, telefone, cpf, cep, senha)

                    print(user.cadastrarUsuario('adm'))
                    return Menu.showBanner()
            
            case '6':
                if Usuario.getUser()[1] == 'adm':
                    print('\n=== Todos os emprestimos ===\n')
                    print(Emprestimo.listarEmprestimos())
                    return Menu.showBanner()
                

    def showBanner():
        color = '\033[32m'
        if Usuario.getUser()[1] == 'usr':
            text = color + '\n=== Menu: ' + Usuario.getUser()[0] + ' ===\n\n[1] Meus Emprestimos\n[2] Realizar Emprestimo\n[3] Listar livros\n[99] Sobre\n[00] Sair\n\n> ' + '\033[0;0m'
            choice = input(text)
            Menu.selectItem(choice)
        else:
            if Usuario.getUser()[1] == 'adm':
                text = color+ '\n=== Menu: '+ Usuario.getUser()[0] + '===\n\n[1] Meus Emprestimos\n[2] Realizar Emprestimo\n[3] Listar livros\n[4] Cadastrar Livro\n[5] Cadastrar administrador\n[6] Listar todos os emprestimos\n[99] Sobre\n[00] Sair\n\n> ' + '\033[0;0m'
                choice = input(text)
                Menu.selectItem(choice)
