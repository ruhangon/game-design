from labirinto import Labirinto
# from openal import al, alc, audio
import lucia
import sys

sys.path.append("../..")

# inicializa lucia
lucia.initialize(audiobackend=lucia.AudioBackend.OPENAL)
lucia.initialize(audiobackend=lucia.AudioBackend.BASS)

parque = Labirinto()

# mostra a janela
teste = lucia.show_window(title="As palavras do amor")

# menu = lucia.ui.Menu()
# menu.add_item_tts("Jogar")
# menu.add_item_tts("Sair do jogo")

# resultado = menu.run("Selecione uma opção")

primeira_fala=True

while True:
    lucia.process_events()

    if (primeira_fala==True):
        parque.descobre_descricao_do_local_atual()
        lucia.output.speak(text=parque.local, interrupt=True)
        primeira_fala=False

    if lucia.key_pressed(lucia.K_SPACE):
        frase_atual=parque.retorna_frase_atual()
        lucia.output.speak(text=frase_atual, interrupt=True)

    if lucia.key_pressed(lucia.K_r):
        lucia.output.speak(text=parque.local, interrupt=True)

    if lucia.key_pressed(lucia.K_h):
        lucia.output.speak(text="As palavras do amor \n\nPressione as setas para se mover \nPressione espaço para saber a frase atual \nCaso você converse com algum amigo, a frase na sua mente irá se embaralhar \nPressione r para repetir o texto do local onde você está \nPressione esc para sair do jogo", interrupt=True)

    if (parque.posicao==18):
        texto_final=parque.chegou_ao_objetivo()
        menu_finalizar = lucia.ui.Menu()
        menu_finalizar.add_item_tts("Finalizar jogo")
        resultado = menu_finalizar.run(texto_final)
        if (resultado=="Finalizar jogo"):
            lucia.quit()

    if lucia.key_pressed(lucia.K_UP):
        n = parque.faz_movimento("cima")
        if (n<0):
            audio_bloqueado = lucia.audio_backend.Sound()
            audio_bloqueado.load("sons/bloqueado.ogg")
            audio_bloqueado.play()
        if (n>0):
            audio_passos = lucia.audio_backend.Sound()
            audio_passos.load("sons/passos.ogg")
            audio_passos.play()
        if (n==0):
            audio_blablabla = lucia.audio_backend.Sound()
            audio_blablabla.load("sons/blablabla.ogg")
            audio_blablabla.play()
        primeira_fala=True

    if lucia.key_pressed(lucia.K_DOWN):
        n = parque.faz_movimento("baixo")
        if (n<0):
            audio_bloqueado = lucia.audio_backend.Sound()
            audio_bloqueado.load("sons/bloqueado.ogg")
            audio_bloqueado.play()
        if (n>0):
            audio_passos = lucia.audio_backend.Sound()
            audio_passos.load("sons/passos.ogg")
            audio_passos.play()
        if (n==0):
            audio_blablabla = lucia.audio_backend.Sound()
            audio_blablabla.load("sons/blablabla.ogg")
            audio_blablabla.play()
        primeira_fala=True

    if lucia.key_pressed(lucia.K_LEFT):
        n = parque.faz_movimento("esquerda")
        if (n<0):
            audio_bloqueado = lucia.audio_backend.Sound()
            audio_bloqueado.load("sons/bloqueado.ogg")
            audio_bloqueado.play()
        if (n>0):
            audio_passos = lucia.audio_backend.Sound()
            audio_passos.load("sons/passos.ogg")
            audio_passos.play()
        if (n==0):
            audio_blablabla = lucia.audio_backend.Sound()
            audio_blablabla.load("sons/blablabla.ogg")
            audio_blablabla.play()
        primeira_fala=True

    if lucia.key_pressed(lucia.K_RIGHT):
        n = parque.faz_movimento("direita")
        if (n<0):
            audio_bloqueado = lucia.audio_backend.Sound()
            audio_bloqueado.load("sons/bloqueado.ogg")
            audio_bloqueado.play()
        if (n>0):
            audio_passos = lucia.audio_backend.Sound()
            audio_passos.load("sons/passos.ogg")
            audio_passos.play()
        if (n==0):
            audio_blablabla = lucia.audio_backend.Sound()
            audio_blablabla.load("sons/blablabla.ogg")
            audio_blablabla.play()
        primeira_fala=True

    if lucia.key_pressed(lucia.K_ESCAPE):
        menu_sair = lucia.ui.Menu()
        menu_sair.add_item_tts("Sim")
        menu_sair.add_item_tts("Não")
        resultado = menu_sair.run("Você deseja sair do jogo")
        if (resultado=="Sim"):
            lucia.quit()

