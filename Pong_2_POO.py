import sys

import pygame

pygame.init()

#Variables iniciales
Black = (0,     0,   0)
White = (255, 255, 255)
screen_size = (800,600)


screen = pygame.display.set_mode(screen_size)#Crea la ventana
clock  = pygame.time.Clock()#Creara los fps en un futuro

class Player():
    def __init__(self):
        self.x_cord  = 0
        self.y_cord  = 0
        self.y_speed = 0
        self.width   = 15 #ancho
        self.heid    = 90 #alto
        self.puntos  = 0

class Pelota():
    def __init__(self):
        self.x       = screen_size[0]/2
        self.y       = screen_size[1]/2
        self.speed_x = 5
        self.speed_y = 5

player1 = Player()
player1.x_cord = 50
player1.y_cord = 300 - 45

player2 = Player()
player2.x_cord = 750 - player2.width
player2.y_cord = 300 - 45

pelota1 = Pelota()


game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over = True
#-------------------------------------------Logica  
        #Jugador 1 movimiento
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.y_speed = -15
            if event.key == pygame.K_s: 
                player1.y_speed = 15
        #Jugador 2 movimiento
        if event.type==pygame.KEYDOWN:
            if event.key ==pygame.K_UP:
                player2.y_speed = -15
            if event.key ==pygame.K_DOWN: 
                player2.y_speed = 15  
            
        #Jugador 1 se detiene 
        if event.type==pygame.KEYUP:
            if event.key ==pygame.K_w:
                player1.y_speed = 0
            if event.key ==pygame.K_s: 
                player1.y_speed = 0
        #Jugador 2 se detiene 
            if event.key ==pygame.K_UP:
                player2.y_speed = 0
            if event.key ==pygame.K_DOWN: 
                player2.y_speed = 0

#Modifica las cordenadas para darle movimient a los jugadores
    player1.y_cord += player1.y_speed
    player2.y_cord += player2.y_speed

#Movimiento pelota
    pelota1.x += pelota1.speed_x
    pelota1.y += pelota1.speed_y

#Rebote de la pelota-Paredes
    if pelota1.y > screen_size[1]-10 or pelota1.y < 10:
        pelota1.speed_y *= -1
    if pelota1.x > screen_size[0]-10 or pelota1.x < 10:
        pelota1.speed_x *= -1

#Revisa si la pelota sale por el lado izquierco
    if pelota1.x<10:
        pelota1.x = 400
        pelota1.y = 300
        pelota1.speed_y*=-1
        player1.puntos +=1
#Revisa si la pelota sale por el lado derecho
    if pelota1.x > 790:
        pelota1.x = 400
        pelota1.y = 300
        pelota1.speed_y*=-1
        player2.puntos +=1


#Limites de los jugadores 

#Limites jugador 1
    if player1.y_cord < 1:
        player1.y_speed = 0
        player1.y_cord  = 1
    
    if player1.y_cord > 515:
        player1.y_speed = 0
        player1.y_cord  = 515

#Limites jugador 2
    if player2.y_cord < 1:
        player2.y_speed = 0
        player2.y_cord  = 1
    if player2.y_cord > 515:
        player2.y_speed = 0
        player2.y_cord  = 515


    screen.fill(Black)
# ----------------------------------------------Zona de dibujo
    jugador1 = pygame.draw.rect(screen, White, (player1.x_cord, player1.y_cord, player1.width, player1.heid)) #300 es la mitad de la pantalla y 45 la mitad del alto de la figura
    jugador2 = pygame.draw.rect(screen, White, (player2.x_cord, player2.y_cord, player2.width, player2.heid))
    pelota   = pygame.draw.circle(screen, White,(pelota1.x, pelota1.y),10)
#---------------------------------------------------------  
#Detectord de colisiones 
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota1.speed_x *= -1
#Puntuaciones
    
    font = pygame.font.SysFont("serif",25)#Tipografia y tamaño
    text = font.render("cambio 3",True, White)#Mensaje en pantalla, True=Calidad de la letra, Color
    screen.blit(text,(0,0))
    pygame.display.flip()

    clock.tick(60)

    
pygame.quit()