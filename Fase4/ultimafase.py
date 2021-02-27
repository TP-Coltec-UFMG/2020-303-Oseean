
import pygame          
pygame.init()          

screen = pygame.display.set_mode((800, 600), 0)
fonte = pygame.font.SysFont("Serif", 60)   

PRETO = (0, 0, 0)
CINZA = (176,196,222)
BRANCO = (70,130,180)
AZUL = (70, 70, 220)


# sons
VACA1 = pygame.mixer.Sound("COWS.WAV")
VACA2 = pygame.mixer.Sound("COW_1.WAV")
VACA3 = pygame.mixer.Sound("COW_2.WAV")
VACA4 = pygame.mixer.Sound("COW_3.WAV")
VACA5 = pygame.mixer.Sound("COW.WAV")
som_passar_mouse = pygame.mixer.Sound("som_carta.wav")
teste = pygame.mixer.Sound("LO_SWISS.WAV")
welcome = pygame.mixer.Sound("BemVindoDificil.wav")




class Cenario:
    def __init__(self,v1,p1,b1,a1,v2,p2,b2,a2,s2,m2): 
        self.v1 = v1
        self.p1 = p1
        self.b1 = b1
        self.a1 = a1
        self.v2 = v2
        self.p2 = p2
        self.b2 = b2
        self.a2 = a2
        self.s2 = s2
        self.m2 = m2

        self.escolha1 = None
        self.vitoria = 0

    def pintar_tela(self,tela):
        pygame.draw.rect(tela,CINZA,(50,50,700,500),0)
        self.v1.pintar_carta(screen)
        self.p1.pintar_carta(screen)
        self.b1.pintar_carta(screen)
        self.a1.pintar_carta(screen)
        self.v2.pintar_carta(screen)
        self.p2.pintar_carta(screen)
        self.b2.pintar_carta(screen)
        self.a2.pintar_carta(screen)
        self.s2.pintar_carta(screen)
        self.m2.pintar_carta(screen)


        texto ="DIFICIL"
        posicao = (290, 80)
        antialiasing = True
        cor_do_texto = BRANCO 
        imagem_do_texto = fonte.render(texto, antialiasing, cor_do_texto)
        screen.blit(imagem_do_texto, posicao)


    def calcular_regras(self, eventos):
        # Lista temporaria
        cartas = [
        self.v1,
        self.p1,
        self.b1,
        self.a1,
        self.v2,
        self.p2,
        self.b2,
        self.a2,
        self.s2,
        self.m2,
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
                        if c_pos.collidepoint(pygame.mouse.get_pos()) and c.sumir == 0:
                            if self.escolha1 is None:
                                # salvar escolha 1
                                self.escolha1 = c
                            elif self.escolha1.som == c.som and self.escolha1 != c:
                                # 'c' é a escolha 2
                                teste.play()
                                self.escolha1.sumir = 1
                                c.sumir = 1
                                self.vitoria += 1
                                self.escolha1 = None
                            else:
                                self.escolha1 = None

#class Cartas:
#    def __init__(self,centro_x,centro_y,altura,largura):
#         self.centro_x = centro_x
#         self.centro_y = centro_y
#         self.altura = altura
#         self.largura =  largura
#         self.cor = BRANCO

#     def pintar_carta(self,tela):
#         pygame.draw.rect(tela,self.cor,(self.centro_x,self.centro_y,self.altura,self.largura), 0, 10)


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
        pos = pygame.Rect((self.centro_x, self.centro_y, self.largura, self.altura))
        if pos.collidepoint(pygame.mouse.get_pos()):
            self.cor = AZUL
            if not self.mouse_encima:
                global som_passar_mouse
                som_passar_mouse.play(maxtime=1000)
            # Tocar apenas uma vez
            self.mouse_encima = True
        else:
            self.cor = BRANCO
            self.mouse_encima = False

        for event in eventos:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if pos.collidepoint(pygame.mouse.get_pos()):
                        self.som.play(0, 2000)


if  __name__ == "__main__":

    welcome.play()
    v1 = Cartas(150,180,90,140, VACA1)
    v2 = Cartas(250,180,90,140, VACA2)
    p1 = Cartas(350,180,90,140, VACA3)
    p2 = Cartas(150,350,90,140, VACA4)
    b1 = Cartas(250,350,90,140, VACA5)
    b2 = Cartas(350,350,90,140, VACA1)
    a1 = Cartas(450,180,90,140, VACA2)
    a2 = Cartas(450,350,90,140, VACA3)
    s2 = Cartas(550,180,90,140, VACA4)
    m2 = Cartas(550,350,90,140, VACA5)
    cenario = Cenario(v1, v2, p1, p2, b1, b2, a1, a2, s2, m2)

    while True:
    
        eventos = pygame.event.get()

        for e in eventos:
            if e.type == pygame.QUIT:
                exit()

        cenario.calcular_regras(eventos)
        # v1.calcular_regras(eventos)
        # p1.calcular_regras(eventos)
        # b1.calcular_regras(eventos)
        # v2.calcular_regras(eventos)
        # p2.calcular_regras(eventos)
        # b2.calcular_regras(eventos)

        cenario.pintar_tela(screen)
        # v1.pintar_carta(screen)
        # p1.pintar_carta(screen)
        # b1.pintar_carta(screen)
        # v2.pintar_carta(screen)
        # p2.pintar_carta(screen)
        # b2.pintar_carta(screen)
        pygame.display.update()
    
    
    #    cenario.pintar_tela(screen)
    #    v1.pintar_carta(screen)
    #    p1.pintar_carta(screen)
    #    b1.pintar_carta(screen)
    #    a1.pintar_carta(screen)
    #    v2.pintar_carta(screen)
    #    p2.pintar_carta(screen)
    #    b2.pintar_carta(screen)
    #    a2.pintar_carta(screen)
    #    pygame.display.update()

    #    for e in pygame.event.get(): 
    #        if e.type == pygame.QUIT:
    #            exit()