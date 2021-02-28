import pygame
import Fase1
import Fase2
import Fase3
import ultimafase
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont("Serif", 60)

PRETO = (0, 0, 0)
CINZA = (176, 196, 222)
BRANCO = (70, 130, 180)
AZUL = (70, 70, 220)

# sons
welcome = pygame.mixer.Sound("PrimeiroAudio.wav")
FASE1 = pygame.mixer.Sound("FASE1.wav")
FASE2 = pygame.mixer.Sound("FASE2.wav")
FASE3= pygame.mixer.Sound("FASE3.wav")
DIFICIL = pygame.mixer.Sound("DIFICIL.wav")
SAIR = pygame.mixer.Sound("sair.wav")



class Cenario:
    def __init__(self, f1, f2, f3, f4d, quit):
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.f4d = f4d
        self.quit = quit
        self.escolha1 = None
        self.vitoria = 0

    def pintar_tela(self, tela):
        pygame.draw.rect(tela, CINZA, (50, 50, 700, 500), 0)
        self.f1.pintar_carta(screen)
        self.f2.pintar_carta(screen)
        self.f3.pintar_carta(screen)
        self.f4d.pintar_carta(screen)
        self.quit.pintar_carta(screen)

        texto = " Ossean"
        posicao = (290, 80)
        antialiasing = True
        cor_do_texto = BRANCO
        imagem_do_texto = fonte.render(texto, antialiasing, cor_do_texto)
        screen.blit(imagem_do_texto, posicao)



    def calcular_regras(self, eventos):
        # Lista temporaria
        cartas = [
            self.f1,
            self.f2,
            self.f3,
            self.f4d,
            self.quit
        ]
        for c in cartas:
            c.calcular_regras(eventos)
        # Eventos
        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    # Se clicou:
                    for c in cartas:
                        c_pos = pygame.Rect((c.centro_x, c.centro_y, c.largura, c.altura))
                        if c_pos.collidepoint(pygame.mouse.get_pos()):
                            if c_pos == (300, 180, 190, 60):
                               Fase1.fase1()
                            elif c_pos == (300, 250, 190, 60):
                               Fase2.fase2()
                            elif c_pos == (300, 320, 190, 60):
                               Fase3.fase3()
                            elif c_pos == (300, 390, 190, 60):
                               ultimafase.fase4()
                            elif c_pos == (300, 460, 190, 60):
                               sys.exit()



class Cartas:
    def __init__(self, centro_x, centro_y, largura, altura, som):
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.altura = altura
        self.largura = largura
        self.cor = BRANCO
        self.sumir = 0
        self.mouse_encima = False
        self.som = som

    def pintar_carta(self, tela):
        if self.sumir == 0:
            pygame.draw.rect(tela, self.cor, (self.centro_x, self.centro_y, self.largura, self.altura), 0, 10)
        else:
            pygame.draw.rect(tela, CINZA, (self.centro_x, self.centro_y, self.largura, self.altura), 0, 10)

    def calcular_regras(self, eventos):
        if self.sumir == 1:
            return
        pos = pygame.Rect(self.centro_x, self.centro_y, self.largura, self.altura)
        mouse = pygame.mouse.get_pos()

        if pos.collidepoint(mouse):
            self.cor = AZUL
            if not self.mouse_encima:
                self.som.play()
            self.mouse_encima = True

        else:
            self.mouse_encima = False
            self.cor = BRANCO



def menu():

    welcome.play()
    f1 = Cartas(300, 180, 190, 60, FASE1)
    f2 = Cartas(300, 250, 190, 60, FASE2)
    f3 = Cartas(300, 320, 190, 60, FASE3)
    f4d = Cartas(300, 390, 190, 60, DIFICIL)
    quit = Cartas(300, 460, 190, 60, SAIR)
    cenario = Cenario(f1, f2, f3, f4d, quit)

    while True:

        eventos = pygame.event.get()

        for e in eventos:
            if e.type == pygame.QUIT:
                exit()

        cenario.calcular_regras(eventos)

        cenario.pintar_tela(screen)

        pygame.display.update()
