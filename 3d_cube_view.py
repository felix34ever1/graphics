import pygame
import vector as v
import matrix as m

# Pygame definitions

pygame.init()

window_size = (200,200)

WINDOW = pygame.display.set_mode(window_size)

cube_matrix:list[v.Vector3D] = [v.Vector3D(75,75,0),
                                v.Vector3D(125,75,0),
                                v.Vector3D(125,125,0),
                                v.Vector3D(75,125,0),
                                v.Vector3D(75,75,100),
                                v.Vector3D(125,75,100),
                                v.Vector3D(125,125,100),
                                v.Vector3D(75,125,100)] # A list to hold all points in a cube as vectors
new_mat = m.Matrix(2,3,[1,2,3,4,5,6])

new_mat.display()


is_running = True
while is_running: # Main pygame loop
    events = pygame.event.get() # Gets all events happening in frame
    for event in events:
        if event.type == pygame.QUIT: # If the exit button is pressed, quit the loop
            is_running = False

    WINDOW.fill((255,255,255)) # Background colour

    pygame.display.update() # Update screen