from personagem import Personagem

class Labirinto:
    def __init__(self):
        self.personagem=Personagem()
        self.posicao=0 # inicia no começo do labirinto
        self.local="" # cita a descrição do local onde você está
        self.palavra_encontrada=[False, False, False, False, False, False, False, False, False]

    def retorna_frase_atual(self):
        return self.personagem.frase

    def descobre_descricao_do_local_atual(self):
        if (self.posicao==0):
            self.local="Você está na entrada do parque, nervoso por estar tão próximo do primeiro encontro. Você pode apenas ir para cima aqui"
        if (self.posicao==1):
            self.local="Você caminha um pouco em direção ao norte e então percebe que não é mais possível ir para frente. Há árvores tapando esse caminho. Um caminho plano está disponível, permitindo que você vá para esquerda ou para direita"
        if (self.posicao==2):
            self.local="Seguindo pela esquerda você repara que ainda está muito próximo a entrada do parque. O caminho plano continua a esquerda, você pode seguir por ele ou voltar pela direita. Os outros caminhos estão tapados por bancos. Você encontrou aqui a palavra tudo"
        if (self.posicao==3):
            self.local="Você continua o caminho da esquerda, mas chega em um local sem saídas. Enquanto árvores fecham o norte e o sul, a sua esquerda o parque termina. Você pode voltar pela direita. Foi encontrado aqui a palavra bem?"
        if (self.posicao==4):
            self.local="Aqui o caminho plano segue em direção a direita, mas agora também há a possibilidade de seguir para o norte, uma leve subida abre um novo caminho. Você encontrou aqui a palavra foi"
        if (self.posicao==5):
            self.local="Você chegou ao fim desse caminho próximo a entrada do parque, um amigo seu aparece para conversar um pouco. Parece que você se embaralhou um pouco em relação ao que estava pensando. Aqui você pode voltar pelo caminho da esquerda. As outras direções estão bloqueadas por estátuas"
        if (self.posicao==6):
            self.local="Depois de seguir um pouco em direção ao norte do parque, você percebe que o chão é de grama e permite que você vá por várias direções. Você pode ir para norte, sul, leste ou oeste. Aqui foi encontrada a palavra legal"
        if (self.posicao==7):
            self.local="Ao ir pela esquerda você percebe que aqui existe o começo de uma subida, você olha ao redor e percebe que um escorregador e uma gangorra bloqueiam alguns caminhos. É possível ir para a direita ou seguir subindo, indo para o norte agora"
        if (self.posicao==8):
            self.local="Você segue a subida que leva a direção norte. É perceptível que a gangorra ainda tapa um caminho, além de outras atrações que tapam outros. É possível ir para o sul, ou seguir pela esquerda ssubindo mais"
        if (self.posicao==9):
            self.local="A subida parece estar chegando ao fim, para dar espaço a um novo caminho, quem sabe. É possível ir para o norte novamente, ou seguir pela direita. Aqui foi encontrada a palavra lasanha."
        if (self.posicao==10):
            self.local="A subida chegou ao fim, aqui parece ser um local com pouco espaço, no fim do parque. Ainda assim poderia ser possível seguir para o norte, se não fosse uma lixeira fechando o caminho. Aqui também apareceu um amigo seu para bater um papo. Sua única opção de caminho é voltar pelo sul"
        if (self.posicao==11):
            self.local="Você segue pelo norte e então descobre que não é possível continuar, uma grande atração tapa o caminho por onde você poderia ir. A única possibilidade é voltar para o caminho de baixo. Aqui você encontra a palavra videogame"
        if (self.posicao==12):
            self.local="Indo pela direita você percebe que uma bonita paisagem começa a aparecer, várias árvores estão próximas, mas não chegam a bloquear muitos caminhos. É possível ir para esquerda, para direita ou para o norte"
        if (self.posicao==13):
            self.local="As árvores que formavam uma bonita paisagem agora estão ficando menos frequentes, para dar espaço a uma outra área do parque. Parece que esse caminho leva ao estacionamento do local. Aqui você encontra uma amiga que estava com muita saudade de falar com você. O único caminho é ir para esquerda"
        if (self.posicao==14):
            self.local="Depois de seguir um bom caminho pela parte norte, você percebe que a paisagem mais bonita do parque toma conta do local. Você começa a lembrar perfeitamente do parque, e lembra onde a garota está. Você consegue até ver ela, lá sentada. Para chegar até ela você terá três caminhos, o da esquerda, o da sua frente, ou o da direita. Também é possível voltar para o sul. Aqui foi encontrada a palavra conhecer"
        if (self.posicao==15):
            self.local="O caminho da esquerda permite que você chegue rapidamente até a garota. No meio do caminho você encontra a palavra beijo"
        if (self.posicao==16):
            self.local="Você segue pelo caminho da sua frente, enquanto admira toda a beleza do momento. Nesse caminho, antes de chegar na garota, você encontra a palavra você"
        if (self.posicao==17):
            self.local="Cada vez mais você está perto da garota, só que sem se atentar você encontra um amigo seu que quer trocar uma ideia. Você para um pouco para conversar com ele, mas parece que por causa disso suas ideias se embaralharam. Na sua cabeça isso já aconteceu antes"

    # faz o deslocamento para outra posição próxima do mapa se possível. direcao aceita cima, esquerda, direita ou baixo
    def faz_movimento(self, direcao=""):
        if (self.posicao==0 and direcao=="cima"):
            self.posicao=1
            return 1
        if (self.posicao==0 and direcao=="esquerda" or self.posicao==0 and direcao=="direita" or self.posicao==0 and direcao=="baixo"):
            return -1
        if (self.posicao==1 and direcao=="esquerda"):
            self.posicao=2
            self.encontrou_palavra()
            return 1
        if (self.posicao==1 and direcao=="direita"):
            self.posicao=4
            self.encontrou_palavra()
            return 1
        if (self.posicao==1 and direcao=="cima" or self.posicao==1 and direcao=="baixo"):
            return -1
        if (self.posicao==2 and direcao=="esquerda"):
            self.posicao=3
            self.encontrou_palavra()
            return 1
        if (self.posicao==2 and direcao=="direita"):
            self.posicao=1
            return 1
        if (self.posicao==2 and direcao=="cima" or self.posicao==2 and direcao=="baixo"):
            return -1
        if (self.posicao==3 and direcao=="direita"):
            self.posicao=2
            return 1
        if (self.posicao==3 and direcao=="cima" or self.posicao==3 and direcao=="esquerda" or self.posicao==3 and direcao=="baixo"):
            return -1
        if (self.posicao==4 and direcao=="esquerda"):
            self.posicao=1
            return 1
        if (self.posicao==4 and direcao=="direita"):
            self.posicao=5
            self.personagem.embaralha_frase()
            return 0
        if (self.posicao==4 and direcao=="cima"):
            self.posicao=6
            self.encontrou_palavra()
            return 1
        if (self.posicao==4 and direcao=="baixo"):
            return -1
        if (self.posicao==5 and direcao=="esquerda"):
            self.posicao=4
            return 1
        if (self.posicao==5 and direcao=="cima" or self.posicao==5 and direcao=="baixo" or self.posicao==5 and direcao=="direita"):
            return -1
        if (self.posicao==6 and direcao=="esquerda"):
            self.posicao=7
            return 1
        if (self.posicao==6 and direcao=="cima"):
            self.posicao=11
            self.encontrou_palavra()
            return 1
        if (self.posicao==6 and direcao=="direita"):
            self.posicao=12
            return 1
        if (self.posicao==6 and direcao=="baixo"):
            self.posicao=4
            return 1
        if (self.posicao==7 and direcao=="cima"):
            self.posicao=8
            return 1
        if (self.posicao==7 and direcao=="direita"):
            self.posicao=6
            return 1
        if (self.posicao==7 and direcao=="esquerda" or self.posicao==7 and direcao=="baixo"):
            return -1
        if (self.posicao==8 and direcao=="esquerda"):
            self.posicao=9
            self.encontrou_palavra()
            return 1
        if (self.posicao==8 and direcao=="baixo"):
            self.posicao=7
            return 1
        if (self.posicao==8 and direcao=="cima" or self.posicao==8 and direcao=="direita"):
            return -1
        if (self.posicao==9 and direcao=="cima"):
            self.posicao=10
            self.personagem.embaralha_frase()
            return 0
        if (self.posicao==9 and direcao=="direita"):
            self.posicao=8
            return 1
        if (self.posicao==9 and direcao=="esquerda" or self.posicao==9 and direcao=="baixo"):
            return -1
        if (self.posicao==10 and direcao=="baixo"):
            self.posicao=9
            return 1
        if (self.posicao==10 and direcao=="esquerda" or self.posicao==10 and direcao=="cima" or self.posicao==10 and direcao=="direita"):
            return -1
        if (self.posicao==11 and direcao=="baixo"):
            self.posicao=6
            return 1
        if (self.posicao==11 and direcao=="esquerda" or self.posicao==11 and direcao=="cima" or self.posicao==11 and direcao=="direita"):
            return -1
        if (self.posicao==12 and direcao=="esquerda"):
            self.posicao=6
            return 1
        if (self.posicao==12 and direcao=="cima"):
            self.posicao=14
            self.encontrou_palavra()
            return 1
        if (self.posicao==12 and direcao=="direita"):
            self.posicao=13
            self.personagem.embaralha_frase()
            return 0
        if (self.posicao==12 and direcao=="baixo"):
            return -1
        if (self.posicao==13 and direcao=="esquerda"):
            self.posicao=12
            return 1
        if (self.posicao==13 and direcao=="cima" or self.posicao==13 and direcao=="baixo" or self.posicao==13 and direcao=="direita"):
            return -1
        if (self.posicao==14 and direcao=="baixo"):
            self.posicao=12
            return 1
        if (self.posicao==14 and direcao=="esquerda"):
            self.posicao=15
            self.encontrou_palavra()
            self.posicao=18 # objetivo
            return 1
        if (self.posicao==14 and direcao=="cima"):
            self.posicao=16
            self.encontrou_palavra()
            self.posicao=18 # objetivo
            return 1
        if (self.posicao==14 and direcao=="direita"):
            self.posicao=17
            self.personagem.embaralha_frase()
            self.posicao=18
            return 0

    def encontrou_palavra(self):
        if (self.posicao==2 and self.palavra_encontrada[0]==False):
            self.personagem.incrementa_frase("tudo")
            self.palavra_encontrada[0]=True
        if (self.posicao==3 and self.palavra_encontrada[1]==False):
            self.personagem.incrementa_frase("bem?")
            self.palavra_encontrada[1]=True
        if (self.posicao==4 and self.palavra_encontrada[2]==False):
            self.personagem.incrementa_frase("foi")
            self.palavra_encontrada[2]=True
        if (self.posicao==6 and self.palavra_encontrada[3]==False):
            self.personagem.incrementa_frase("legal")
            self.palavra_encontrada[3]=True
        if (self.posicao==9 and self.palavra_encontrada[4]==False):
            self.personagem.incrementa_frase("lasanha")
            self.palavra_encontrada[4]=True
        if (self.posicao==11 and self.palavra_encontrada[5]==False):
            self.personagem.incrementa_frase("videogame")
            self.palavra_encontrada[5]=True
        if (self.posicao==14 and self.palavra_encontrada[6]==False):
            self.personagem.incrementa_frase("conhecer")
            self.palavra_encontrada[6]=True
        if (self.posicao==15 and self.palavra_encontrada[7]==False):
            self.personagem.incrementa_frase("beijo")
            self.palavra_encontrada[7]=True
        if (self.posicao==16 and self.palavra_encontrada[8]==False):
            self.personagem.incrementa_frase("você")
            self.palavra_encontrada[8]=True

    def chegou_ao_objetivo(self):
        if (self.posicao==18):
            objetivo="Você finalmente chegou ao local onde ela está, você ainda está um pouco nervoso mas lembra da frase que queria falar para ela. Você então respira e fala... \n"
            objetivo = objetivo + self.retorna_frase_atual()
            return objetivo

