import pygame
############################initialization###################
pygame.init()
window=pygame.display.set_mode((500,500))
pygame.display.set_caption("snake mania")
############################Character#########################
x=50 #posi
y=50 #posi
width=10#width of character
height=10#h of chrcter
vel=5#velocity of charcter
################################main loop#####################
run=True
while run:
    pygame.time.delay(100)##delay for showing window for checking
    for event in pygame.event.get():#get ongoing events with keyboard and mouses
        if event.type==pygame.QUIT:#exit button on window
            run=False#to  stop mainloop
    keys=pygame.key.get_pressed()#list of events 
    if keys[pygame.K_LEFT]:
        x-=vel#changing the velocity + - rther then shifting
    if keys[pygame.K_RIGHT]:
        x+=vel#
    if keys[pygame.K_UP]:
        y-=vel#
    if keys[pygame.K_DOWN]:
        y+=vel#
    window.fill((0,0,0))#Background colors
    #########################shape##################################
    #module.srawing.shape(base==winddoe,(color r g b ),(posi.posi,width,height))
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()#to  render the objects or surfaces on the main surface
pygame.quit#closing