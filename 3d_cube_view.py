import pygame
import vector as v
import matrix as m
import shape
import math


# Pygame definitions

pygame.init()

window_size = (600,600)

WINDOW = pygame.display.set_mode(window_size)

camera_position = v.Vector3D(100,100,1)

cube = shape.Shape()
cube.setVertices([
    v.Vector3D(75,75,-1), #0
    v.Vector3D(75,125,-1),#1
    v.Vector3D(125,125,-1),#2
    v.Vector3D(125,75,-1),#3
    v.Vector3D(75,75,-21),#4
    v.Vector3D(75,125,-21),#5
    v.Vector3D(125,125,-21),#6
    v.Vector3D(125,75,-21)#7
])

cube.setSurfaces( #just defined the connections of a cube
    [[0,1,2,3],
     [0,1,5,4],
     [3,2,6,7],
     [0,3,7,4],
     [1,2,6,5],
     [4,5,6,7]]
)

colour_array = ((255,255,0),(255,0,255),(0,255,255),(255,0,0),(0,255,0),(0,0,255))

game_timer = pygame.time.Clock()
ticks_passed = 0
move_array = [0,0,0]

is_running = True
while is_running: # Main pygame loop
    events = pygame.event.get() # Gets all events happening in frame
    for event in events:
        if event.type == pygame.QUIT: # If the exit button is pressed, quit the loop
            is_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                move_array[0] = -1
            if event.key == pygame.K_d:
                move_array[0] = 1
            if event.key == pygame.K_w:
                move_array[1] = -1
            if event.key == pygame.K_s:
                move_array[1] = 1
            if event.key == pygame.K_z:
                camera_position.z-=1
            if event.key == pygame.K_x:
                camera_position.z+=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_array[0] = 0
            if event.key == pygame.K_d:
                move_array[0] = 0
            if event.key == pygame.K_w:
                move_array[1] = 0
            if event.key == pygame.K_s:
                move_array[1] = 0
    
    ticks_passed+=game_timer.tick()
    if ticks_passed>20:
        ticks_passed = 0
        # Movement happens
        camera_position.x +=move_array[0]
        camera_position.y +=move_array[1]
        camera_position.z += move_array[2]


    WINDOW.fill((255,255,255)) # Background colour
    for _ in range(len(cube.surfaces)):
        coords = cube.getSurfaceCoordinates((len(cube.surfaces)-1)-_,camera_position) # Gets all 2d coordinates for a surface of shape
        
        pygame.draw.polygon(WINDOW,colour_array[_],coords,0) # Draws polygon filled in

    
    pygame.display.update() # Update screen