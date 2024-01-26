import pygame
import vector as v
import matrix as m
import shape
import math


# Pygame definitions

pygame.init()

window_size = (600,600)

WINDOW = pygame.display.set_mode(window_size)

camera_position = v.Vector3D(0,0,30)

cube = shape.Shape(window_size[0]/2,window_size[1]/2)
triangular_based_prism = shape.Shape(window_size[0]/2,window_size[1]/2)
cube.setVertices([
    v.Vector3D(-20,-20,12), #0
    v.Vector3D(-20,20,12),#1
    v.Vector3D(20,20,12),#2
    v.Vector3D(20,-20,12),#3
    v.Vector3D(-20,-20,10),#4
    v.Vector3D(-20,20,10),#5
    v.Vector3D(20,20,10),#6
    v.Vector3D(20,-20,10)#7
])

cube.setSurfaces( #just defined the connections of a cube
    [[0,1,2,3],
     [0,1,5,4],
     [3,2,6,7],
     [0,3,7,4],
     [1,2,6,5],
     [4,5,6,7]]
)

triangular_based_prism.setVertices([
    v.Vector3D(-100,0,5), #0
    v.Vector3D(100,0,5),  #1
    v.Vector3D(0,100,5),  #2
    v.Vector3D(-100,0,4), #3
    v.Vector3D(100,0,4),  #4
    v.Vector3D(0,100,4),  #5
])

triangular_based_prism.setSurfaces([
    [0,1,2],
    [0,2,5,3],
    [0,1,4,3],
    [1,2,5,4],
    [3,4,5]
])

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
                move_array[0] = 1
            if event.key == pygame.K_d:
                move_array[0] = -1
            if event.key == pygame.K_w:
                move_array[1] = 1
            if event.key == pygame.K_s:
                move_array[1] = -1
            if event.key == pygame.K_z:
                move_array[2] = -1
            if event.key == pygame.K_x:
                move_array[2] = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_array[0] = 0
            if event.key == pygame.K_d:
                move_array[0] = 0
            if event.key == pygame.K_w:
                move_array[1] = 0
            if event.key == pygame.K_s:
                move_array[1] = 0
            if event.key == pygame.K_z:
                move_array[2] = 0
            if event.key == pygame.K_x:
                move_array[2] = 0
    
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
        
        pygame.draw.polygon(WINDOW,colour_array[_],coords,5) # Draws polygon filled in

    for _ in range(len(triangular_based_prism.surfaces)):
        coords = triangular_based_prism.getSurfaceCoordinates((len(triangular_based_prism.surfaces)-1)-_,camera_position) # Gets all 2d coordinates for a surface of shape
        
        pygame.draw.polygon(WINDOW,colour_array[_],coords,0) # Draws polygon filled in
    


    pygame.display.update() # Update screen