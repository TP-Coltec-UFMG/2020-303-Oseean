import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont("Serif", 60)

PRETO = (0, 0, 0)
CINZA = (176, 196, 222)
BRANCO = (70, 130, 180)
AZUL = (70, 70, 220)


#sons
galinha = pygame.mixer.Sound("data/CHICKEN.WAV")
cavalo = pygame.mixer.Sound("data/horse.wav")

teste = pygame.mixer.Sound("data/HOTEL_BE.WAV")
som_passar_mouse = pygame.mixer.Sound("data/som_carta.wav")

welcome = pygame.mixer.Sound("data/BemVindoFase1.wav")

class Cenario:
    def __init__(self, g1, c1, g2, c2):
        self.g1 = g1
        self.c1 = c1
        self.g2 = g2
        self.c2 = c2
        self.escolha1 = 0
        self.escolha2 = 0
        self.acerto13 = 0
        self.acerto24 = 0
        self.vitoria = 0

    def pintar_tela(self, tela):
        pygame.draw.rect(tela, CINZA, (50, 50, 700, 500), 0)

        self.g1.pintar_carta(screen)
        self.c1.pintar_carta(screen)
        self.g2.pintar_carta(screen)
        self.c2.pintar_carta(screen)

        texto = "FASE 01"
        posicao = (280, 100)
        antialiasing = True
        cor_do_texto = BRANCO
        imagem_do_texto = fonte.render(texto, antialiasing, cor_do_texto)
        screen.blit(imagem_do_texto, posicao)

    #def VITORIA(self, tela):
        #vitoria.play()

    def processar_eventos_mouse(self, eventos):
        for event in eventos:
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350 and self.acerto13 == 0 and self.acerto13 == 0:
                        galinha.play()

                    elif pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[0] <= 400 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350 and self.acerto24 == 0 and self.acerto24 == 0:
                        cavalo.play()

                    elif pygame.mouse.get_pos()[0] >= 440 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350 and self.acerto13 == 0 and self.acerto13 == 0:
                        galinha.play()

                    elif pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350 and self.acerto24 == 0 and self.acerto24 == 0:
                        cavalo.play()

    def calcular_regras(self, eventos):
            if self.escolha1 == 0:
                if self.escolha2 == 0:
                    for event in eventos:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed()[0]:

                                if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350:
                                    self.escolha1 = 1

                                elif pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[0] <= 400 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350:
                                    self.escolha1 = 2

                                elif pygame.mouse.get_pos()[0] >= 440 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350:
                                    self.escolha1 = 3

                                elif pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350:
                                    self.escolha1 = 4

            elif self.escolha1 != 0:
                for event in eventos:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            if pygame.mouse.get_pos()[0] >= 110 and pygame.mouse.get_pos()[0] <= 250 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350:
                                self.escolha2 = 1

                            elif pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[0] <= 400 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350:
                                self.escolha2 = 2

                            elif pygame.mouse.get_pos()[0] >= 440 and pygame.mouse.get_pos()[0] <= 580 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350:
                                self.escolha2 = 3

                            elif pygame.mouse.get_pos()[0] >= 600 and pygame.mouse.get_pos()[0] <= 740 and pygame.mouse.get_pos()[1] >= 260 and pygame.mouse.get_pos()[1] <= 350:
                                self.escolha2 = 4

            if self.escolha1 != 0 and self.escolha2 != 0:
                if (self.escolha1 == 1 and self.escolha2 == 3) or (self.escolha1 == 3 and self.escolha2 == 1):
                    if self.acerto13 == 0:
                        teste.fadeout(1000)
                        teste.play()
                    self.acerto13 = 1
                    self.g1.sumir = 1
                    self.g2.sumir = 1
                    self.vitoria += 1

                elif (self.escolha1 == 2 and self.escolha2 == 4) or (self.escolha1 == 4 and self.escolha2 == 2):
                    if self.acerto24 == 0:
                        teste.play()
                    self.acerto24 = 1
                    self.c1.sumir = 1
                    self.c2.sumir = 1
                    self.vitoria += 1

                self.escolha1 = 0
                self.escolha2 = 0

                #if self.vitoria == 2:
                 #   self.VITORIA(tela)


class Cartas:
    def __init__(self, centro_x, centro_y, largura, altura):
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.altura = altura
        self.largura = largura
        self.cor = BRANCO
        self.sumir = 0

        welcome.play()

    def pintar_carta(self, tela):
        if self.sumir == 0:
            pygame.draw.rect(tela, self.cor, (self.centro_x, self.centro_y, self.largura, self.altura), 0, 10)
        else:
            pygame.draw.rect(tela, CINZA, (self.centro_x, self.centro_y, self.largura, self.altura), 0, 10)

    def calcular_regras(self):
        pos = pygame.Rect((self.centro_x,self.centro_y,self.altura,self.largura))
        if pos.collidepoint(pygame.mouse.get_pos()):
            self.cor = AZUL
            if not self.mouse_encima and self.sumir == 0:
                global som_passar_mouse
                som_passar_mouse.play(maxtime=1000)
            # Tocar apenas uma vez
            self.mouse_encima = True
        else:
            self.cor = BRANCO
            self.mouse_encima = False

if __name__ == "__main__":
    g1 = Cartas(110, 260, 90, 140)
    c1 = Cartas(270, 260, 90, 140)
    g2 = Cartas(440, 260, 90, 140)
    c2 = Cartas(600, 260, 90, 140)
    cenario = Cenario(g1, c1, g2, c2)


    while True:
        cenario.pintar_tela(screen)
        g1.pintar_carta(screen)
        c1.pintar_carta(screen)
        g2.pintar_carta(screen)
        c2.pintar_carta(screen)
        pygame.display.update()

        eventos = pygame.event.get()
        cenario.processar_eventos_mouse(eventos)
        cenario.calcular_regras(eventos)
        g1.calcular_regras()
        c1.calcular_regras()
        g2.calcular_regras()
        c2.calcular_regras()
