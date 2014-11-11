import pygame,os,sys,time,math
from pygame.locals import *
screensize = screenh,screenw = 900, 900



pygame.init()
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Car Game")
superpi = math.pi*2
picorrection = 0.01744444444 #do this due to 360 degrees equalling 6.28

environment = True

center = posx,posy = 450,450

steering_angle = 0
steering_rate = 0.01
steering_lock = 0.5

#sideways 70 110 290 250
#upwards 335 25  155 205
rotation1 = 25  * picorrection #Rear Left
rotation2 = 335 * picorrection #Rear Right
rotation3 = 205 * picorrection #Front Left
rotation4 = 155 * picorrection #Front Right


#TODO: rotate the wheels hubs with the corners of the body for deformation purposes
#wheel hubs - on this vehicle, it's fr -5 fl +5 deg -30% total length to get hub points to where the tires will pivot off of
wheelfldeg = 210 * picorrection
wheelfrdeg = 150 * picorrection
wheelrldeg = 330 * picorrection
wheelrrdeg = 30  * picorrection

#wheel config -- here you can change the size IF YOU DARE!
wheelsize = 20

#FRONT WHEELS
wheelpoint1 = 25  * picorrection #Rear Left
wheelpoint2 = 335 * picorrection #Rear Right
wheelpoint3 = 205 * picorrection #Front Left
wheelpoint4 = 155 * picorrection #Front Right

#REAR WHEELS
wheelpointrear1 = 25  * picorrection #Rear Left
wheelpointrear2 = 335 * picorrection #Rear Right
wheelpointrear3 = 205 * picorrection #Front Left
wheelpointrear4 = 155 * picorrection #Front Right


while environment:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	keypress = pygame.key.get_pressed()

	if keypress[K_ESCAPE]:
		sys.exit()
	elif keypress[K_LEFT]:
		if steering_angle < steering_lock:
			steering_angle = steering_angle + steering_rate
			wheelpoint1 = wheelpoint1 + steering_rate
			wheelpoint2 = wheelpoint2 + steering_rate
			wheelpoint3 = wheelpoint3 + steering_rate
			wheelpoint4 = wheelpoint4 + steering_rate
	elif keypress[K_RIGHT]:
		if steering_angle > -steering_lock:
			steering_angle = steering_angle - steering_rate
			wheelpoint1 = wheelpoint1 - steering_rate
			wheelpoint2 = wheelpoint2 - steering_rate
			wheelpoint3 = wheelpoint3 - steering_rate
			wheelpoint4 = wheelpoint4 - steering_rate
	elif steering_angle > 0:
			steering_angle = steering_angle - steering_rate
			wheelpoint1 = wheelpoint1 - steering_rate
			wheelpoint2 = wheelpoint2 - steering_rate
			wheelpoint3 = wheelpoint3 - steering_rate
			wheelpoint4 = wheelpoint4 - steering_rate
	elif steering_angle < 0:
			steering_angle = steering_angle + steering_rate
			wheelpoint1 = wheelpoint1 + steering_rate
			wheelpoint2 = wheelpoint2 + steering_rate
			wheelpoint3 = wheelpoint3 + steering_rate
			wheelpoint4 = wheelpoint4 + steering_rate
	
	if steering_angle > 1:
		steering_angle = 1
	elif steering_angle < -1:
		steering_angle = -1

			
	screen.fill((0,0,0))
	
	#rotate the car entity for testing
	
	rotation1  = rotation1  + 0.001
	rotation2  = rotation2  + 0.001
	rotation3  = rotation3  + 0.001
	rotation4  = rotation4  + 0.001
	
	wheelfldeg = wheelfldeg + 0.001
	wheelfrdeg = wheelfrdeg + 0.001
	wheelrldeg = wheelrldeg + 0.001
	wheelrrdeg  = wheelrrdeg + 0.001

	wheelpoint1 = wheelpoint1 + 0.001
	wheelpoint2 = wheelpoint2 + 0.001
	wheelpoint3 = wheelpoint3 + 0.001
	wheelpoint4 = wheelpoint4 + 0.001
	
	wheelpointrear1 = wheelpointrear1 + 0.001
	wheelpointrear2 = wheelpointrear2 + 0.001
	wheelpointrear3 = wheelpointrear3 + 0.001
	wheelpointrear4 = wheelpointrear4 + 0.001

	#make sure the rotational values do not exceed 6.28
	
	if rotation1    > superpi:
		rotation1   = 0
	if rotation2    > superpi:
		rotation2   = 0
	if rotation3    > superpi:
		rotation3   = 0
	if rotation4    > superpi:
		rotation4   = 0	
	
	if wheelfldeg   > superpi:
		wheelfldeg  = 0
	if wheelfrdeg   > superpi:
		wheelfrdeg  = 0
	if wheelrldeg   > superpi:
		wheelrldeg  = 0
	if wheelrrdeg   > superpi:
		wheelrrdeg  = 0
	if wheelrrdeg   > superpi:
		wheelrrdeg  = 0

		
		
	if wheelpoint1  > superpi:
		wheelpoint1 = 0
	if wheelpoint2  > superpi:
		wheelpoint2 = 0
	if wheelpoint3  > superpi:
		wheelpoint3 = 0
	if wheelpoint4  > superpi:
		wheelpoint4 = 0
		
		
	#the body
	point1 = int(math.sin(rotation1)*100+ posx), int(math.cos(rotation1)*100 + posy)
	point2 = int(math.sin(rotation2)*100+ posx), int(math.cos(rotation2)*100 + posy)
	point3 = int(math.sin(rotation3)*100+ posx), int(math.cos(rotation3)*100 + posy)
	point4 = int(math.sin(rotation4)*100+ posx), int(math.cos(rotation4)*100 + posy)
	
	#to do this set wheels center at hub, then rotate using wheeldeg
	#wheel Hubs
	wheelfl = wheelflx,wheelfly = int(math.sin(wheelfldeg)*70+ posx), int(math.cos(wheelfldeg)*70 + posy)
	wheelfr = wheelfrx,wheelfry = int(math.sin(wheelfrdeg)*70+ posx), int(math.cos(wheelfrdeg)*70 + posy)
	
	wheelrl = wheelrlx,wheelrly = int(math.sin(wheelrldeg)*70+ posx), int(math.cos(wheelrldeg)*70 + posy)
	wheelrr = wheelrrx,wheelrry = int(math.sin(wheelrrdeg)*70+ posx), int(math.cos(wheelrrdeg)*70 + posy)


	#wheelfl
	wheelflpoint1 = int(math.sin(wheelpoint1)*wheelsize+ wheelflx), int(math.cos(wheelpoint1)*wheelsize + wheelfly)
	wheelflpoint2 = int(math.sin(wheelpoint2)*wheelsize+ wheelflx), int(math.cos(wheelpoint2)*wheelsize + wheelfly)
	wheelflpoint3 = int(math.sin(wheelpoint3)*wheelsize+ wheelflx), int(math.cos(wheelpoint3)*wheelsize + wheelfly)
	wheelflpoint4 = int(math.sin(wheelpoint4)*wheelsize+ wheelflx), int(math.cos(wheelpoint4)*wheelsize + wheelfly)
	#wheelfr
	wheelfrpoint1 = int(math.sin(wheelpoint1)*wheelsize+ wheelfrx), int(math.cos(wheelpoint1)*wheelsize + wheelfry)
	wheelfrpoint2 = int(math.sin(wheelpoint2)*wheelsize+ wheelfrx), int(math.cos(wheelpoint2)*wheelsize + wheelfry)
	wheelfrpoint3 = int(math.sin(wheelpoint3)*wheelsize+ wheelfrx), int(math.cos(wheelpoint3)*wheelsize + wheelfry)
	wheelfrpoint4 = int(math.sin(wheelpoint4)*wheelsize+ wheelfrx), int(math.cos(wheelpoint4)*wheelsize + wheelfry)

	#wheelrr
	wheelrrpoint1 = int(math.sin(wheelpointrear1)*wheelsize+ wheelrrx), int(math.cos(wheelpointrear1)*wheelsize + wheelrry)
	wheelrrpoint2 = int(math.sin(wheelpointrear2)*wheelsize+ wheelrrx), int(math.cos(wheelpointrear2)*wheelsize + wheelrry)
	wheelrrpoint3 = int(math.sin(wheelpointrear3)*wheelsize+ wheelrrx), int(math.cos(wheelpointrear3)*wheelsize + wheelrry)
	wheelrrpoint4 = int(math.sin(wheelpointrear4)*wheelsize+ wheelrrx), int(math.cos(wheelpointrear4)*wheelsize + wheelrry)

	#wheelrl
	wheelrlpoint1 = int(math.sin(wheelpointrear1)*wheelsize+ wheelrlx), int(math.cos(wheelpointrear1)*wheelsize + wheelrly)
	wheelrlpoint2 = int(math.sin(wheelpointrear2)*wheelsize+ wheelrlx), int(math.cos(wheelpointrear2)*wheelsize + wheelrly)
	wheelrlpoint3 = int(math.sin(wheelpointrear3)*wheelsize+ wheelrlx), int(math.cos(wheelpointrear3)*wheelsize + wheelrly)
	wheelrlpoint4 = int(math.sin(wheelpointrear4)*wheelsize+ wheelrlx), int(math.cos(wheelpointrear4)*wheelsize + wheelrly)


		
	#draw stuff
	##body
	pygame.draw.polygon(screen, (255,255,255), [point1,point2,point3,point4])
	##wheels
	##tires
	pygame.draw.polygon(screen, (0,0,255), [wheelflpoint1,wheelflpoint2,wheelflpoint3,wheelflpoint4])
	pygame.draw.polygon(screen, (0,0,255), [wheelfrpoint1,wheelfrpoint2,wheelfrpoint3,wheelfrpoint4])
	
	pygame.draw.polygon(screen, (0,0,255), [wheelrrpoint1,wheelrrpoint2,wheelrrpoint3,wheelrrpoint4])
	pygame.draw.polygon(screen, (0,0,255), [wheelrlpoint1,wheelrlpoint2,wheelrlpoint3,wheelrlpoint4])
	###hubs
	pygame.draw.circle(screen, (0,255,0), wheelfl, 3)
	pygame.draw.circle(screen, (0,255,0), wheelfr, 3)
	
	pygame.draw.circle(screen, (0,255,0), wheelrr, 3)
	pygame.draw.circle(screen, (0,255,0), wheelrl, 3)
	##debug
	#pygame.draw.circle(screen, (255,0,0), center, 3)
	#pygame.draw.circle(screen, (255,0,0), point1, 3)
	
	pygame.display.flip()
		
#==========
#Extra Code
#==========
#point1 = (posx-25+(int(math.cos(rotation)*posx-25)),posy-50+(int(math.sin(rotation)*scale)))
#for wheels (posx-25+(int(math.cos(rotation)*scale)),posy+50+(int(math.sin(rotation)*scale)))
	#int(math.cos(rotation)*50+posx) #DO NOT DELETE
