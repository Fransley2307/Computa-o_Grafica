import pygame
import sys
import random
#imports das tabelas 

pygame.init()
#Biblioteca

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Janela')
#informa o tamanho da tela 

PRETO = (0, 0, 0)

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

#imforma a cor, uma fonte padrão e o tamnho da fonte.

def cor_aleatoria(diferente_de=None):
    while True:
        c = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        if c != diferente_de:
            return c
#Gera uma cor RGB aleatoriamente diferente da anterior

texto1_conteudo = "FRANZÃO"
texto1_cor = cor_aleatoria()
texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
texto1_rect = texto1.get_rect(center=(largura//3, altura//2))
#Define o texto, coloca com uma cor aleatoria, renderiza o texto cria um retangulo para posicionar a colisão

texto2_conteudo = "GOSTOSO"
texto2_cor = cor_aleatoria(diferente_de=texto1_cor)
texto2 = fonte.render(texto2_conteudo, True, texto2_cor)
texto2_rect = texto2.get_rect(center=(2*largura//3, altura//2))
#mesma coisa do anterior.

clock = pygame.time.Clock()
#controla quantos frame por segundo o jogo esta rodando.


def dir_nao_zero():
    return random.choice((-1, 1))

def velocidade_aleatoria(min_v=2, max_v=6):
    return random.randint(min_v, max_v)

v1x = velocidade_aleatoria() * dir_nao_zero()
v1y = velocidade_aleatoria() * dir_nao_zero()
v2x = velocidade_aleatoria() * dir_nao_zero()
v2y = velocidade_aleatoria() * dir_nao_zero()
#aqui ele sortei posições aleatoria para os textos e a velocidade aleatoria


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
#move o texto, faz ele quicar nas bordas, invertendo as possições quando bate.



rodando = True
while rodando:  #mantem o programa rodando, atualizando as posiçoes.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            #Permite fechar a janela normalmente.

    v1x, v1y, bateu1 = move_e_quica(texto1_rect, v1x, v1y)
    v2x, v2y, bateu2 = move_e_quica(texto2_rect, v2x, v2y)
    # atualiza a posição do texto detectando se bate na borda.

    if bateu1:  #sempre que bate na parede muda a cor 
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
        #detecta colição entre os dois textos inverte a direção e troca a cor

    tela.fill(PRETO)#limpa a tela, desenha o texto e atualzia a tela.
    tela.blit(texto1, texto1_rect)
    tela.blit(texto2, texto2_rect)
    pygame.display.flip()
    clock.tick(240)#limita o fps em 240 
  
         
pygame.quit()
sys.exit()
#fecha o programa corretamente 


