import pygame
import pygame_menu
import teste

pygame.init()
screen = pygame.display.set_mode((800, 600), 0)

def fase1():
    welcome = pygame.mixer.Sound("data/BemVindoFase1.wav")
    welcome.play()
    teste.Fase1()
    pass

def fase2():
    welcome = pygame.mixer.Sound("data/BemVindoFase1.wav")
    welcome.play()
    pass

def fase3():
    welcome = pygame.mixer.Sound("data/BemVindoFase1.wav")
    welcome.play()
    pass

def fase4():
    welcome = pygame.mixer.Sound("data/BemVindoFase1.wav")
    welcome.play()
    pass

menu = pygame_menu.Menu(400, 600, 'Bem Vindo',
                       theme=pygame_menu.themes.THEME_BLUE)

#menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('FASE 1', fase1)
menu.add_button('FASE 2', fase2)
menu.add_button('FASE 3', fase3)
menu.add_button('FASE 4', fase4)
menu.add_button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(screen)
