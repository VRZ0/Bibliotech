import json
import pandas as pd
from utils import *

class Livro:

    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor


    def cadastrarLivro(self):
        bookObject = {
            "nome" : self.nome,
            "autor" : self.autor
        }

        dbWrite("../data/livros.txt", bookObject)
        
        return (f'\n{self.nome} cadastrado com sucesso!')
    
    def getLivros():
        dbBook = open("../data/livros.txt")
        books = []
        names = []
        authors = []
        for line in dbBook:
            books.append(json.loads(line))
        
        for i in books:
            names.append(i['nome'])
            authors.append(i['autor'])

        data = {
            "nomes:" : names,
            "autores:" : authors
        }

        return data

        
    def listarLivros():

        df = pd.DataFrame(Livro.getLivros())

        return df