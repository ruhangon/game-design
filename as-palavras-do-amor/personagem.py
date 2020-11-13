import random

class Personagem:
    def __init__(self):
        self.frase="oi "

    def incrementa_frase(self, palavra):
        self.frase = self.frase+palavra
        self.frase = self.frase+" " # acrescenta espaço depois da palavra adicionada

    def embaralha_frase(self):
        palavras = self.frase.split()
        random.shuffle(palavras)
        nova_frase=" ".join(palavras)
        self.frase=nova_frase

