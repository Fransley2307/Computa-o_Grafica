import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Configuração da janela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Computação Gráfica")

# Cores
PRETO = (0, 0, 0)

# Fonte
tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

# Função para gerar cor aleatória
def cor_aleatoria(diferente_de=None):
    while True:
        cor = (
            random.randint(1, 255),
            random.randint(1, 255),
            random.randint(1, 255)
        )
        if cor != diferente_de:
            return cor

# Textos
texto1_conteudo = "FRANZÃO"
texto2_conteudo = "GOSTOSO"

texto1_cor = cor_aleatoria()
texto2_cor = cor_aleatoria(texto1_cor)

texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
texto2 = fonte.render(texto2_conteudo, True, texto2_cor)

texto1_rect = texto1.get_rect(center=(largura // 3, altura // 2))
texto2_rect = texto2.get_rect(center=(2 * largura // 3, altura // 2))

# Controle de FPS
clock = pygame.time.Clock()

# Direção aleatória
def direcao():
    return random.choice([-1, 1])

# Velocidade aleatória
def velocidade_aleatoria(min_v=2, max_v=6):
    return random.randint(min_v, max_v)

# Velocidades iniciais
v1x = velocidade_aleatoria() * direcao()
v1y = velocidade_aleatoria() * direcao()
v2x = velocidade_aleatoria() * direcao()
v2y = velocidade_aleatoria() * direcao()

# Função de movimento e quique (SEM abs)
def move_e_quica(rect, vx, vy):
    rect.x += vx
    rect.y += vy
    bateu = False

    if rect.left <= 0 or rect.right >= largura:
        vx = -vx
        bateu = True

    if rect.top <= 0 or rect.bottom >= altura:
        vy = -vy
        bateu = True

    return vx, vy, bateu

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento
    v1x, v1y, bateu1 = move_e_quica(texto1_rect, v1x, v1y)
    v2x, v2y, bateu2 = move_e_quica(texto2_rect, v2x, v2y)

    # Muda a cor ao bater na borda
    if bateu1:
        texto1_cor = cor_aleatoria(texto1_cor)
        texto1 = fonte.render(texto1_conteudo, True, texto1_cor)

    if bateu2:
        texto2_cor = cor_aleatoria(texto2_cor)
        texto2 = fonte.render(texto2_conteudo, True, texto2_cor)

    # Colisão entre textos
    if texto1_rect.colliderect(texto2_rect):
        v1x, v1y = -v1x, -v1y
        v2x, v2y = -v2x, -v2y

        texto1_cor = cor_aleatoria(texto1_cor)
        texto2_cor = cor_aleatoria(texto2_cor)

        texto1 = fonte.render(texto1_conteudo, True, texto1_cor)
        texto2 = fonte.render(texto2_conteudo, True, texto2_cor)

    # Desenho
    tela.fill(PRETO)
    tela.blit(texto1, texto1_rect)
    tela.blit(texto2, texto2_rect)
    pygame.display.flip()

    
    clock.tick(240)# limita o fps em 240 

# Finalização
pygame.quit()
sys.exit()
