import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cylinder():
    base_radius = 1
    top_radius = 1
    height = 2
    slices = 32
    stacks = 32

    # Create a quadric object
    quadric = gluNewQuadric()

    # Draw the body of the cylinder
    gluCylinder(quadric, base_radius, top_radius, height, slices, stacks)

    # Draw the bottom disk
    glPushMatrix()
    gluDisk(quadric, 0, base_radius, slices, stacks)
    glPopMatrix()

    # Draw the top disk
    glPushMatrix()
    glTranslatef(0, 0, height)
    gluDisk(quadric, 0, top_radius, slices, stacks)
    glPopMatrix()

def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Set up the sun light properties
    light_position = [1, 1, 1, 0] # Directional light
    ambient_light = [0.2, 0.2, 0.2, 1.0]
    diffuse_light = [0.7, 0.7, 0.7, 1.0]
    specular_light = [0.9, 0.9, 0.9, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)


    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    setup_lighting()
    glEnable(GL_DEPTH_TEST)

    clock = pygame.time.Clock()
    rotation_x, rotation_y = 0, 0
    mouse_grabbed = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEMOTION and mouse_grabbed:
                dx, dy = event.rel
                rotation_x += dy
                rotation_y += dx
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mouse_grabbed = not mouse_grabbed
                    pygame.mouse.set_visible(not mouse_grabbed)
                    pygame.event.set_grab(mouse_grabbed)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()  # Save the current matrix
        glTranslatef(0, 0, 1)  # Translate to the center of the cylinder
        glRotatef(rotation_x, 1, 0, 0)  # Rotate based on mouse y movement
        glRotatef(rotation_y, 0, 1, 0)  # Rotate based on mouse x movement
        glTranslatef(0, 0, -1)  # Translate back
        draw_cylinder()
        glPopMatrix()  # Restore the matrix

        pygame.display.flip()
        clock.tick(60)  # 60 frames per second

if __name__ == "__main__":
    main()
