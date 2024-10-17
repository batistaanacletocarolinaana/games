import pygame

#tela do game
janela = pygame.display.set_mode([640,480])
pygame.display.set_caption('GAME')

#imagem do fundo e personagem
imagem_fundo = pygame.image.load("imagemnbosque.jpg")
personagem = pygame.image.load("persona-removebg-preview-removebg-preview.png")

#posição do patrick (nome do personagem) e a velocidade
pos_y_personagem = 280
pos_x_personagem = 245
velocidade = 5

loop = True

while loop:
    
    for events in pygame.event.get():
        
        if events.type == pygame.QUIT:
            loop = False
    #movimentos 
    
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        pos_y_personagem -= velocidade
    if teclas[pygame.K_RIGHT]:
        pos_y_personagem += velocidade   
        
    if pos_y_personagem <= -5:
        pos_y_personagem = -5 
    if pos_y_personagem >= 500:
        pos_y_personagem = 500 
    print(pos_y_personagem)
   
    janela.blit(imagem_fundo ,(0,0))
    janela.blit(personagem,(pos_y_personagem,pos_x_personagem))
    pygame.display.update()
