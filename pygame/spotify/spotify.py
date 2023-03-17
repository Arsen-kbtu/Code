import pygame
pygame.init()
songs=["03 novacane.mp3", "Heartless.mp3", "Slide on Me.mp3", "Less than Zero.mp3"]
pics=["nostalgia, ULTRA.jpg", "Live Tour.jpg", "(2) Endless Streaming Art.png", "Live Tour.jpg"]
x=0
W=800
H=600
screen = pygame.display.set_mode((W, H))
screen.fill((255,255,255))
pygame.display.update()

pygame.mixer.music.load(songs[x])
start=False
stop= True
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True       
                if event.type== pygame.KEYDOWN:
                        pressed = pygame.key.get_pressed()
                        if pressed[pygame.K_SPACE]:
                                if stop==True:
                                        if start==False:
                                                pygame.mixer.music.play()
                                                start=True
                                                cov=pygame.image.load(pics[x]).convert()
                                                cover=pygame.transform.scale(cov, (300, 300))
                                                coverr=cover.get_rect(center=(W/2, H/3))
                                                screen.blit(cover, coverr)
                                        else:
                                                pygame.mixer.music.unpause()
                                        stop=False
                                else:
                                        pygame.mixer.music.pause()
                                        stop=True
                        if pressed[pygame.K_LEFT]:
                                if x!=0:
                                        x-=1
                                else:
                                        x=len(songs)-1        
                                cov=pygame.image.load(pics[x]).convert()
                                cover=pygame.transform.scale(cov, (300, 300))
                                coverr=cover.get_rect(center=(W/2, H/3))
                                screen.blit(cover, coverr)
                                pygame.mixer.music.load(songs[x])
                                pygame.mixer.music.play()
                        if pressed[pygame.K_RIGHT]:
                                if x!=len(songs)-1:
                                        x+=1
                                else:
                                        x=0        
                                cov=pygame.image.load(pics[x]).convert()
                                cover=pygame.transform.scale(cov, (300, 300))
                                coverr=cover.get_rect(center=(W/2, H/3))
                                screen.blit(cover, coverr)
                                pygame.mixer.music.load(songs[x])
                                pygame.mixer.music.play()
                pygame.display.update()