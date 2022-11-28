from usuario import Usuario
from livro import Livro
from datetime import datetime,timedelta
import json
import pandas as pd
from utils import *

class Emprestimo:

    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro        
    
    def listarEmprestimos(usr=''):
        dbLoan = open("../data/emprestimos.txt")
        loans = []
        users = []
        books = []
        dates = []

        for line in dbLoan:
            loans.append(json.loads(line))
        
        if usr != '':
            for i in loans:
                if i['usuario'] == usr:
                    users.append(i['usuario'])
                    books.append(i['livro'])
                    dates.append(i['data'])
        else:
            for i in loans:
                users.append(i['usuario'])
                books.append(i['livro'])
                dates.append(i['data'])

        if books == []:
            return 'Ops... Parece que você não tem nenhuma reserva'
        
        data = {
            "nome:" : users,
            "livro:" : books,
            "devolução" : dates
        }

        df = pd.DataFrame(data)
        
        return df
        
    def fazerEmprestimo(self):
        dbLoan = open("../data/emprestimos.txt")
        loans = []

        for line in dbLoan:
            loans.append(json.loads(line))

        if loans == []:
            prazo = datetime.today().date() + timedelta(days=7)

            loanObject = {
                "usuario" : self.usuario,
                "livro" : self.livro,
                "data" : str(prazo)
            }

            dbWrite("../data/emprestimos.txt", loanObject)

            return (f"\n{self.usuario} curta {self.livro} até dia {prazo}")


        for i in loans:
            if self.livro == i['livro'] and datetime.today().date() <= datetime.strptime(i['data'], '%Y-%m-%d').date():
                return (f"\n{self.usuario}, infelizmente '{self.livro}' já está emprestado até dia {i['data']}")
            else:
                prazo = datetime.today().date() + timedelta(days=7)

                loanObject = {
                    "usuario" : self.usuario,
                    "livro" : self.livro,
                    "data" : str(prazo)
                }

                dbWrite("../data/emprestimos.txt", loanObject)

                return (f"\n{self.usuario}, curta '{self.livro}' até dia {prazo}")
            
        