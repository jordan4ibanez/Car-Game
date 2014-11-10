import pygame,os,sys,time,math
from pygame.locals import *
screensize = screenh,screenw = 900, 900



pygame.init()
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Car Game")
superpi = math.pi*2
picorrection = 0.01744444444

environment = True

center = posx,posy = 450,450

#sideways 70 110 290 250
#upwards 335 25  155 205
rotation2 = 335 * picorrection
rotation1 = 25  * picorrection
rotation4 = 155 * picorrection
rotation3 = 205 * picorrection



#to get value, divide quards by 0.01744444444

while environment == True:
	screen.fill((0,0,0))
	
	#rotate the car body
	rotation1 = rotation1 + 0.001
	rotation2 = rotation2 + 0.001
	rotation3 = rotation3 + 0.001
	rotation4 = rotation4 + 0.001
	
	if rotation1   > superpi:
		rotation1   = 0
	
	if rotation2   > superpi:
		rotation2   = 0
	
	if rotation3   > superpi:
		rotation3   = 0
	if rotation4   > superpi:
		rotation4   = 0

	#point1 = (posx-25+(int(math.cos(rotation)*posx-25)),posy-50+(int(math.sin(rotation)*scale)))
	point1 = int(math.sin(rotation1)*100+ posx), int(math.cos(rotation1)*100 + posy)
	point2 = int(math.sin(rotation2)*100+ posx), int(math.cos(rotation2)*100 + posy)
	point3 = int(math.sin(rotation3)*100+ posx), int(math.cos(rotation3)*100 + posy)
	point4 = int(math.sin(rotation4)*100+ posx), int(math.cos(rotation4)*100 + posy)
	#for wheels (posx-25+(int(math.cos(rotation)*scale)),posy+50+(int(math.sin(rotation)*scale)))
	#int(math.cos(rotation)*50+posx) #DO NOT DELETE
	
	
	pygame.draw.polygon(screen, (255,255,255), [point1,point2,point3,point4])
	pygame.draw.circle(screen, (255,0,0), center, 3)
	pygame.draw.circle(screen, (255,0,0), point1, 3)

	pygame.display.flip()
		



