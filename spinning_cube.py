import pygame
import math

# CONSTANTS
WHITE = (255, 255, 255)
VELOCITY_X = 0.5
VELOCITY_Y = 0.15
VELOCITY_Z = 0.1

# creating a window
WIN_WIDTH = 800
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH))
pygame.display.set_caption("Rotating Cube")

# pygame clock
clock = pygame.time.Clock()
FPS = 60

# cube parameters
cube_x = WIN_WIDTH/2
cube_y = WIN_WIDTH/2
cube_z = 0
cube_size = WIN_WIDTH/4

verticies = [
    #[x, y, z]
    [cube_x - cube_size, cube_y - cube_size, cube_z - cube_size],
    [cube_x + cube_size, cube_y - cube_size, cube_z - cube_size],
    [cube_x + cube_size, cube_y + cube_size, cube_z - cube_size],
    [cube_x - cube_size, cube_y + cube_size, cube_z - cube_size],
    [cube_x - cube_size, cube_y - cube_size, cube_z + cube_size],
    [cube_x + cube_size, cube_y - cube_size, cube_z + cube_size],
    [cube_x + cube_size, cube_y + cube_size, cube_z + cube_size],
    [cube_x - cube_size, cube_y + cube_size, cube_z + cube_size]
]
edges = [  # lists of connected points
    [0, 1], [1, 2], [2, 3], [3, 0],  # back face
    [4, 5], [5, 6], [6, 7], [7, 4],  # front face
    [0, 4], [1, 5], [2, 6], [3, 7]  # connecting sides
]


# rotate along the x axis
def rotate_x():
    angle = VELOCITY_X / FPS * 2
    for vertex in verticies:
        y = vertex[1] - cube_y
        z = vertex[2] - cube_z
        new_y = y * math.cos(angle) - z * math.sin(angle)
        new_z = z * math.cos(angle) + y * math.sin(angle)
        vertex[1] = new_y + cube_y
        vertex[2] = new_z + cube_z


# rotate along the y axis
def rotate_y():
    angle = VELOCITY_Y / FPS * 2
    for vertex in verticies:
        x = vertex[0] - cube_x
        z = vertex[2] - cube_z
        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_z = z * math.cos(angle) + x * math.sin(angle)
        vertex[0] = new_x + cube_x
        vertex[2] = new_z + cube_z


# rotate along the z axis
def rotate_z():
    angle = VELOCITY_Z / FPS * 2
    for vertex in verticies:
        x = vertex[0] - cube_x
        y = vertex[1] - cube_y
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = y * math.cos(angle) + x * math.sin(angle)
        vertex[0] = new_x + cube_x
        vertex[1] = new_y + cube_y


def update():
    WIN.fill((0, 0, 0))

    # rotating the cube
    rotate_x()
    rotate_y()
    rotate_z()

    # drawing the cube
    for edge in edges:
        pygame.draw.line(WIN, WHITE, (verticies[edge[0]][0], verticies[edge[0]][1]),
                         (verticies[edge[1]][0], verticies[edge[1]][1]), 3)

    pygame.display.update()
    clock.tick(FPS)


def main():
    pygame.init()
    run = True
    while run:
        update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()
