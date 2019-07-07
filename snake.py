import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((1000, 800))
done = False
head = [150,70]

s_pos = [[150,70],[120,70],[90,70]]

food = [randint(20,950),randint(20,700)]
l = 0
r = 0
u = 0
d = 0
speed = 60
score = 0
clock = pygame.time.Clock()
color = (255, 0, 0)
color_ = (0, 255, 0)

while not done:

	screen.fill((0, 0, 0))        
	for event in pygame.event.get():
	        if event.type == pygame.QUIT:
                        done = True
         
       
	for position in s_pos:
        	pygame.draw.rect(screen,color,pygame.Rect(position[0],position[1],30,30))
	
        pressed = pygame.key.get_pressed()	
        if pressed[pygame.K_UP]: 
		l = 0
		r = 0
		u = 1
		d = 0
        if pressed[pygame.K_DOWN]:
		l = 0
		r = 0
		u = 0
		d = 1 
        if pressed[pygame.K_LEFT]:
		l = 1
		r = 0
		u = 0
		d = 0
        if pressed[pygame.K_RIGHT]:
		l = 0
		r = 1
		u = 0
		d = 0	

	if pressed[pygame.K_SPACE]:
		done = True
	
	if u == 1 :
		s_pos.insert(0,list(head))
 		s_pos.pop()
		head[1] -= 20	
	
	if d == 1 :
		s_pos.insert(0,list(head))
 		s_pos.pop()
		head[1] += 20	
		
	if l == 1 :
		s_pos.insert(0,list(head))
 		s_pos.pop()
		head[0] -= 20	
	
	if r == 1 :
		s_pos.insert(0,list(head))
 		s_pos.pop()
		head[0] += 20	
	if head[0] > 1000:
		head[0] = 0
	
	if head[1] > 800:
		head[1] = 0
	
	if head[0] < 0:
		head[0] = 1000
		
	if head[1] < 0:
		head[1] = 800

	
	if head[0] < food[0] + 20 and head[0] > food[0] - 20 and head[1] < food[1] + 20 and head[1] > food[1] - 20:
		food[0] = randint(50,900)
		food[1] = randint(50,700)
		speed += 1
		score += 1
		s_pos.insert(0,list(head))
		if u == 1 : head[1] -= 20
		if d == 1 : head[1] += 20
		if l == 1 : head[0] -= 20
		if r == 1 : head[0] += 20
	pygame.draw.rect(screen, color_, pygame.Rect(food[0], food[1], 20, 20))
			
	clock.tick(20)
	pygame.display.flip()
print("your score " + str(score))	
'''	out = s_pos
	out.pop(0)
	for position in out :
		if(position[0] == head[1] and position[1] == head[1]) :
			break			
'''

