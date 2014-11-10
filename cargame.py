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
rotation1 = 25  * picorrection #Rear Left
rotation2 = 335 * picorrection #Rear Right
rotation4 = 155 * picorrection #Front Right
rotation3 = 205 * picorrection #Front Left

wheelfldeg = 215 * picorrection
wheelfrdeg = 145 * picorrection
wheelrldeg = 0
wheelrrdeg = 0



#to get value, divide quards by 0.01744444444

while environment == True:
	screen.fill((0,0,0))
	
	#rotate the car entity
	rotation1  = rotation1  + 0.001
	rotation2  = rotation2  + 0.001
	rotation3  = rotation3  + 0.001
	rotation4  = rotation4  + 0.001
	wheelfldeg = wheelfldeg + 0.001
	wheelfrdeg = wheelfrdeg + 0.001
	#rotate the wheels with the corners of the body for deformation purposes	
	if rotation1   > superpi:
		rotation1   = 0
	
	if rotation2   > superpi:
		rotation2   = 0
	
	if rotation3   > superpi:
		rotation3   = 0
	if rotation4   > superpi:
		rotation4   = 0
		wheelfl     = 0

	#the body
	point1 = int(math.sin(rotation1)*100+ posx), int(math.cos(rotation1)*100 + posy)
	point2 = int(math.sin(rotation2)*100+ posx), int(math.cos(rotation2)*100 + posy)
	point3 = int(math.sin(rotation3)*100+ posx), int(math.cos(rotation3)*100 + posy)
	point4 = int(math.sin(rotation4)*100+ posx), int(math.cos(rotation4)*100 + posy)
		
	#draw stuff
	pygame.draw.polygon(screen, (255,255,255), [point1,point2,point3,point4])
	pygame.draw.circle(screen, (255,0,0), center, 3)
	pygame.draw.circle(screen, (255,0,0), point1, 3)

	#wheels
	wheelfl = int(math.sin(wheelfldeg)*70+ posx), int(math.cos(wheelfldeg)*70 + posy)
	wheelfr = int(math.sin(wheelfrdeg)*70+ posx), int(math.cos(wheelfrdeg)*70 + posy)
	
	pygame.draw.circle(screen, (0,255,0), wheelfl, 3)
	pygame.draw.circle(screen, (0,255,0), wheelfr, 3)
	

	pygame.display.flip()
		
#==========
#Extra Code
#==========
#point1 = (posx-25+(int(math.cos(rotation)*posx-25)),posy-50+(int(math.sin(rotation)*scale)))
#for wheels (posx-25+(int(math.cos(rotation)*scale)),posy+50+(int(math.sin(rotation)*scale)))
	#int(math.cos(rotation)*50+posx) #DO NOT DELETE
