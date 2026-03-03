import pygame
import sys
import random

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Janela')

PRETO = (0, 0, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

def cor_aleatoria(diferente_de=None):
    while True:
        c = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if c != diferente_de:
            return c
#Texto1
texto1_conteudo = "FRANZÃO"
texto1_cor = cor_aleatoria()
texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
texto1_rect = texto1.get_rect(center=(largura//3, altura//2))
#Texto2 
texto2_conteudo = "GOSTOSO"
texto2_cor = cor_aleatoria(diferente_de=texto1_cor)
texto2 = fonte.render(texto2_conteudo, True, texto2_cor)
texto2_rect = texto2.get_rect(center=(2*largura//3, altura//2))

clock = pygame.time.Clock()

def dir_nao_zero():
    return random.choice((-1, 1))

velocidade = 4
v1x = velocidade * dir_nao_zero()
v1y = velocidade * dir_nao_zero()
v2x = velocidade * dir_nao_zero()
v2y = velocidade * dir_nao_zero()

def move_e_quica(rect, vx, vy):
    rect.x += vx
    rect.y += vy
    bateu = False
    if rect.left <= 0:
        rect.left = 0
        vx = abs(vx)
        bateu = True
    elif rect.right >= largura:
        rect.right = largura
        vx = -abs(vx)
        bateu = True
    if rect.top <= 0:
        rect.top = 0
        vy = abs(vy)
        bateu = True
    elif rect.bottom >= altura:
        rect.bottom = altura
        vy = -abs(vy)
        bateu = True
    return vx, vy, bateu


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    v1x, v1y, bateu1 = move_e_quica(texto1_rect, v1x, v1y)
    v2x, v2y, bateu2 = move_e_quica(texto2_rect, v2x, v2y)

    if bateu1:
        texto1_cor = cor_aleatoria(texto1_cor)
        texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
    if bateu2:
        texto2_cor = cor_aleatoria(texto2_cor)
        texto2 = fonte.render(texto2_conteudo, True, texto2_cor)

    if texto1_rect.colliderect(texto2_rect):
        v1x, v1y = -v1x, -v1y
        v2x, v2y = -v2x, -v2y
        texto1_cor = cor_aleatoria(texto1_cor)
        texto2_cor = cor_aleatoria(texto2_cor)
        texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
        texto2 = fonte.render(texto2_conteudo, True, texto2_cor)
        texto1_rect.x += int((v1x > 0) or -1)
        texto2_rect.x += int((v2x > 0) or -1)
        texto1_rect.y += int((v1y > 0) or -1)
        texto2_rect.y += int((v2y > 0) or -1)

    tela.fill(PRETO)
    tela.blit(texto1, texto1_rect)
    tela.blit(texto2, texto2_rect)
    clock.tick(240)
    pygame.display.flip()
   
       
pygame.quit()
sys.exit()



