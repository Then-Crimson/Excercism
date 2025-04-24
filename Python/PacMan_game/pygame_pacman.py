import pygame # type: ignore
import sys

pygame.init()

TILE_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

maze = [
    list("###############"),
    list("#.............#"),
    list("#.#####.###.#"),
    list("#.#.......#.#"),
    list("#.#.#####.#.#"),
    list("#.#.......#.#"),
    list("#.#######.#.#"),
    list("#...........#"),
    list("###############")
]
screen = pygame.display.set_mode((len(maze[0]) * TILE_SIZE, len(maze) * TILE_SIZE))
pygame.display.set_caption("Pac-Man")

pacman_pos = [1, 1]
ghost_pos = [5, 8]
score = 0
font = pygame.font.SysFont(None, 36)

def draw_maze():
    screen.fill(BLACK)
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            x, y = j * TILE_SIZE, i * TILE_SIZE
            if cell == "#":
                pygame.draw.rect(screen, (0, 0, 255), (x, y, TILE_SIZE, TILE_SIZE))
            elif cell == ".":
                pygame.draw.circle(screen, WHITE, (x + TILE_SIZE // 2, y + TILE_SIZE // 2), 5)

    px, py = pacman_pos[1] * TILE_SIZE, pacman_pos[0] * TILE_SIZE
    pygame.draw.circle(screen, (255, 255, 0), (px + TILE_SIZE // 2, py + TILE_SIZE // 2), TILE_SIZE // 2 - 4)

    gx, gy = ghost_pos[1] * TILE_SIZE, ghost_pos[0] * TILE_SIZE
    pygame.draw.circle(screen, (255, 0, 0), (gx + TILE_SIZE // 2, gy + TILE_SIZE // 2), TILE_SIZE // 2 - 4)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

def move_pacman(dx, dy):
    global score
    x, y = pacman_pos
    new_x, new_y = x + dy, y + dx
    if maze[new_x][new_y] != "#":
        if maze[new_x][new_y] == ".":
            score += 10
        pacman_pos[0], pacman_pos[1] = new_x, new_y
        maze[new_x][new_y] = " "

def move_ghost():
    gx, gy = ghost_pos
    px, py = pacman_pos
    dx = 1 if px > gx else -1 if px < gx else 0
    dy = 1 if py > gy else -1 if py < gy else 0

    # Intenta moverse en X, si no puede en Y
    if maze[gx + dx][gy] != "#" and (dx != 0):
        ghost_pos[0] += dx
    elif maze[gx][gy + dy] != "#" and (dy != 0):
        ghost_pos[1] += dy

clock = pygame.time.Clock()
running = True
while running:
    draw_maze()

    if pacman_pos == ghost_pos:
        print("Game Over! El fantasma te atrapó 👻")
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move_pacman(-1, 0)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_pacman(1, 0)
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        move_pacman(0, -1)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move_pacman(0, 1)

    move_ghost()
    clock.tick(5)

pygame.quit()
sys.exit()